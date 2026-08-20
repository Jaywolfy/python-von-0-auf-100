"""
Modul 26 - Beispiel: Ein vollwertiges Kommandozeilen-Werkzeug

So sieht ein fertiges, alltagstaugliches Python-Skript aus.
Alles aus 27 Modulen kommt hier zusammen. 🎉

AUFRUF:
    python 01_werkzeug.py --help
    python 01_werkzeug.py ./_demo
    python 01_werkzeug.py ./_demo --ausfuehren --backup -v
"""
from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
from datetime import datetime
from pathlib import Path

# ====================================================================
# KONSTANTEN & STANDARDKONFIGURATION
# ====================================================================
VERSION = "1.0.0"

STANDARD_KONFIG = {
    "regeln": {
        "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Dokumente": [".pdf", ".docx", ".txt", ".odt"],
        "Tabellen": [".xlsx", ".csv", ".ods"],
        "Musik": [".mp3", ".wav", ".flac"],
        "Videos": [".mp4", ".mov", ".mkv"],
        "Archive": [".zip", ".rar", ".7z"],
        "Code": [".py", ".js", ".json", ".html"],
    },
    "sonstiges_ordner": "Sonstiges",
    "backups_behalten": 5,
}

log = logging.getLogger("aufraeumer")


# ====================================================================
# 1. LOGGING EINRICHTEN
# ====================================================================
def richte_logging_ein(logdatei: Path | None = None, ausfuehrlich: bool = False) -> None:
    """Konfiguriert das Logging für Konsole und optional eine Datei.

    Args:
        logdatei: Pfad zur Logdatei (None = nur Konsole).
        ausfuehrlich: Wenn True, wird auch DEBUG geloggt.
    """
    handler: list[logging.Handler] = [logging.StreamHandler(sys.stdout)]
    if logdatei:
        logdatei.parent.mkdir(parents=True, exist_ok=True)
        handler.append(logging.FileHandler(logdatei, encoding="utf-8"))

    logging.basicConfig(
        level=logging.DEBUG if ausfuehrlich else logging.INFO,
        format="%(asctime)s [%(levelname)-8s] %(message)s",
        datefmt="%H:%M:%S",
        handlers=handler,
        force=True,
    )


# ====================================================================
# 2. KONFIGURATION LADEN
# ====================================================================
def lade_konfig(pfad: Path | None) -> dict:
    """Lädt die Konfiguration und ergänzt fehlende Werte durch Standardwerte."""
    konfig = json.loads(json.dumps(STANDARD_KONFIG))     # tiefe Kopie
    if pfad and pfad.exists():
        try:
            benutzer = json.loads(pfad.read_text(encoding="utf-8"))
            konfig.update(benutzer)
            log.info("Konfiguration geladen: %s", pfad.name)
        except json.JSONDecodeError as fehler:
            log.warning("Konfigurationsdatei fehlerhaft (%s) - nutze Standardwerte", fehler)
    else:
        log.debug("Keine Konfigurationsdatei - nutze Standardwerte")
    return konfig


# ====================================================================
# 3. DIE EIGENTLICHE LOGIK
# ====================================================================
def ziel_fuer(datei: Path, konfig: dict) -> str:
    """Bestimmt den Zielordner einer Datei anhand ihrer Endung."""
    endung = datei.suffix.lower()
    for name, endungen in konfig["regeln"].items():
        if endung in endungen:
            return name
    return konfig["sonstiges_ordner"]


def fortschritt(aktuell: int, gesamt: int, breite: int = 24) -> str:
    """Erzeugt einen Fortschrittsbalken als String."""
    anteil = aktuell / gesamt if gesamt else 1
    gefuellt = int(anteil * breite)
    return f"[{'█' * gefuellt}{'░' * (breite - gefuellt)}] {anteil:>4.0%}"


def erstelle_backup(ordner: Path, behalten: int = 5) -> Path | None:
    """Erstellt ein ZIP-Backup und entfernt zu alte Backups."""
    ziel_ordner = ordner.parent / "_backups"
    ziel_ordner.mkdir(exist_ok=True)
    stempel = datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        archiv = Path(shutil.make_archive(
            str(ziel_ordner / f"backup_{stempel}"), "zip", ordner))
    except OSError as fehler:
        log.error("Backup fehlgeschlagen: %s", fehler)
        return None

    vorhandene = sorted(ziel_ordner.glob("backup_*.zip"),
                        key=lambda p: p.stat().st_mtime, reverse=True)
    for alt in vorhandene[behalten:]:
        alt.unlink()
        log.debug("Altes Backup entfernt: %s", alt.name)

    log.info("Backup erstellt: %s (%s Bytes)", archiv.name, f"{archiv.stat().st_size:,}")
    return archiv


def sortiere(ordner: Path, konfig: dict, ausfuehren: bool = False) -> dict:
    """Sortiert Dateien nach Typ in Unterordner.

    Args:
        ordner: Der zu sortierende Ordner.
        konfig: Konfiguration mit den Sortierregeln.
        ausfuehren: Wenn False (Standard), passiert nur ein Trockenlauf.

    Returns:
        Statistik-dict {Zielordner: Anzahl}.
    """
    dateien = [p for p in sorted(ordner.iterdir()) if p.is_file()]
    if not dateien:
        log.warning("Keine Dateien in %s gefunden", ordner)
        return {}

    log.info("%d Dateien gefunden%s", len(dateien),
             "" if ausfuehren else "  (TROCKENLAUF - es wird nichts verändert)")

    statistik: dict[str, int] = {}
    for nr, datei in enumerate(dateien, start=1):
        name = ziel_fuer(datei, konfig)
        ziel = ordner / name / datei.name

        try:
            if ausfuehren:
                ziel.parent.mkdir(exist_ok=True)
                if ziel.exists():
                    ziel = ziel.with_stem(f"{ziel.stem}_1")
                datei.rename(ziel)
                log.debug("%s → %s/", datei.name, name)
            else:
                log.debug("[TEST] %s → %s/", datei.name, name)

            statistik[name] = statistik.get(name, 0) + 1

        except PermissionError:
            log.error("Kein Zugriff auf %s - übersprungen", datei.name)
        except OSError as fehler:
            log.error("Fehler bei %s: %s", datei.name, fehler)

        print(f"\r  {fortschritt(nr, len(dateien))} {datei.name[:34]:<34}",
              end="", flush=True)

    print()
    return statistik


# ====================================================================
# 4. ARGUMENTE
# ====================================================================
def parse_argumente(argv=None) -> argparse.Namespace:
    """Liest und prüft die Kommandozeilenargumente."""
    parser = argparse.ArgumentParser(
        prog="aufraeumer",
        description="Sortiert Dateien eines Ordners nach Typ in Unterordner.",
        epilog=("Beispiele:\n"
                "  %(prog)s ~/Downloads                 (Trockenlauf)\n"
                "  %(prog)s ~/Downloads --ausfuehren    (wirklich sortieren)\n"
                "  %(prog)s ~/Downloads -a -b -v        (mit Backup, ausführlich)"),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("ordner", type=Path, help="Der aufzuräumende Ordner")
    parser.add_argument("-a", "--ausfuehren", action="store_true",
                        help="Änderungen wirklich durchführen (Standard: Trockenlauf)")
    parser.add_argument("-b", "--backup", action="store_true",
                        help="Vorher ein ZIP-Backup anlegen")
    parser.add_argument("-k", "--konfig", type=Path, default=None,
                        help="Pfad zu einer JSON-Konfigurationsdatei")
    parser.add_argument("-l", "--log", type=Path, default=None,
                        help="Pfad zu einer Logdatei")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Ausführliche Ausgabe (DEBUG-Level)")
    parser.add_argument("--version", action="version",
                        version=f"%(prog)s {VERSION}")
    return parser.parse_args(argv)


# ====================================================================
# 5. HAUPTPROGRAMM
# ====================================================================
def main(argv=None) -> int:
    """Einstiegspunkt. Gibt den Exit-Code zurück (0 = Erfolg)."""
    args = parse_argumente(argv)
    richte_logging_ein(args.log, args.verbose)

    log.info("=" * 54)
    log.info("Ordner-Aufräumer %s", VERSION)
    log.info("=" * 54)

    if not args.ordner.exists():
        log.error("Ordner existiert nicht: %s", args.ordner.absolute())
        return 1
    if not args.ordner.is_dir():
        log.error("Kein Ordner: %s", args.ordner)
        return 1

    konfig = lade_konfig(args.konfig)

    if args.backup and args.ausfuehren:
        erstelle_backup(args.ordner, konfig["backups_behalten"])
    elif args.backup:
        log.info("Backup übersprungen (nur Trockenlauf)")

    try:
        statistik = sortiere(args.ordner, konfig, args.ausfuehren)
    except Exception:
        log.exception("Unerwarteter Fehler beim Sortieren")   # ⭐ mit Traceback
        return 2

    log.info("-" * 54)
    for name, anzahl in sorted(statistik.items(), key=lambda p: -p[1]):
        log.info("  %-14s %3d Dateien  %s", name, anzahl, "█" * anzahl)
    log.info("-" * 54)
    log.info("Fertig: %d Dateien verarbeitet", sum(statistik.values()))

    if not args.ausfuehren:
        log.info("💡 Das war ein Trockenlauf. Mit --ausfuehren wird es echt.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
