"""
🗂️ Ordner-Aufräumer - Musterlösung Projekt 3

Sortiert Dateien nach Typ in Unterordner - sicher, mit Trockenlauf,
Duplikatserkennung und vollständiger Fehlerbehandlung.

Benutzt Modul 00-13: pathlib, Dictionaries, Funktionen, Exceptions.

AUFRUF:
    python aufraeumer.py
"""
import hashlib
import shutil
from datetime import datetime
from pathlib import Path

# ====================================================================
# EINSTELLUNGEN
# ====================================================================
REGELN = {
    "Bilder":    ({".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".bmp"}, "📷"),
    "Dokumente": ({".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf", ".pptx"}, "📄"),
    "Tabellen":  ({".xlsx", ".xls", ".csv", ".ods"}, "📊"),
    "Musik":     ({".mp3", ".wav", ".flac", ".m4a", ".ogg"}, "🎵"),
    "Videos":    ({".mp4", ".mov", ".avi", ".mkv", ".webm"}, "🎬"),
    "Archive":   ({".zip", ".rar", ".7z", ".tar", ".gz"}, "📦"),
    "Code":      ({".py", ".js", ".html", ".css", ".json", ".sql"}, "💻"),
}
SONSTIGES = ("Sonstiges", "❓")
BREITE = 54

DEMO_MODUS = True        # 👈 auf False setzen für echte Ordner


# ====================================================================
# AUSGABE-HILFEN
# ====================================================================
def kopfzeile(text):
    """Gibt eine Überschrift mit Rahmen aus."""
    print("╔" + "═" * BREITE + "╗")
    print("║" + text.center(BREITE) + "║")
    print("╚" + "═" * BREITE + "╝")


def abschnitt(text):
    """Gibt eine Abschnittsüberschrift aus."""
    print(f"\n── {text} " + "─" * max(0, BREITE - len(text) - 4))


def lesbar(bytes_anzahl):
    """Formatiert eine Bytezahl lesbar (KB, MB, GB)."""
    for einheit in ("B", "KB", "MB", "GB"):
        if bytes_anzahl < 1024:
            return f"{bytes_anzahl:,.1f} {einheit}"
        bytes_anzahl /= 1024
    return f"{bytes_anzahl:,.1f} TB"


# ====================================================================
# KERNLOGIK
# ====================================================================
def sammle_dateien(ordner, rekursiv=False):
    """Sammelt alle Dateien eines Ordners.

    Args:
        ordner: Der zu durchsuchende Ordner.
        rekursiv: Auch Unterordner durchsuchen?

    Returns:
        Sortierte Liste der gefundenen Dateien.

    Raises:
        FileNotFoundError: Wenn der Ordner nicht existiert.
        NotADirectoryError: Wenn der Pfad kein Ordner ist.
    """
    ordner = Path(ordner)
    if not ordner.exists():
        raise FileNotFoundError(f"Ordner existiert nicht: {ordner.absolute()}")
    if not ordner.is_dir():
        raise NotADirectoryError(f"Kein Ordner: {ordner}")

    muster = "**/*" if rekursiv else "*"
    # ⚠️ list() - wir verändern den Ordner gleich!
    return sorted(p for p in ordner.glob(muster) if p.is_file())


def ziel_kategorie(datei):
    """Bestimmt Kategorie und Symbol einer Datei anhand ihrer Endung."""
    endung = datei.suffix.lower()
    for name, (endungen, symbol) in REGELN.items():
        if endung in endungen:
            return name, symbol
    return SONSTIGES


def eindeutiger_pfad(ziel):
    """Findet einen freien Dateinamen, falls das Ziel schon existiert.

    bericht.pdf → bericht_1.pdf → bericht_2.pdf …
    """
    if not ziel.exists():
        return ziel
    nummer = 1
    while True:
        kandidat = ziel.with_stem(f"{ziel.stem}_{nummer}")
        if not kandidat.exists():
            return kandidat
        nummer += 1


def sortiere(dateien, basis, trockenlauf=True, zeige_max=8):
    """Sortiert Dateien nach Typ in Unterordner.

    Args:
        dateien: Liste der zu sortierenden Dateien.
        basis: Der Basisordner (dort entstehen die Unterordner).
        trockenlauf: Wenn True, wird nichts verändert.
        zeige_max: Wie viele Einzelzeilen angezeigt werden.

    Returns:
        (statistik, fehler) - statistik ist ein dict, fehler eine Liste.
    """
    statistik = {}
    fehler = []

    for nr, datei in enumerate(dateien, start=1):
        kategorie, _ = ziel_kategorie(datei)
        ziel = basis / kategorie / datei.name

        try:
            if trockenlauf:
                if nr <= zeige_max:
                    print(f"  [TEST] {datei.name[:34]:<36} → {kategorie}/")
            else:
                ziel.parent.mkdir(exist_ok=True)
                ziel = eindeutiger_pfad(ziel)      # 🛡️ nie überschreiben
                datei.rename(ziel)

            statistik[kategorie] = statistik.get(kategorie, 0) + 1

        except PermissionError:
            fehler.append((datei.name, "kein Zugriff (Datei geöffnet?)"))
        except FileNotFoundError:
            fehler.append((datei.name, "Datei verschwunden"))
        except OSError as f:
            fehler.append((datei.name, f"Systemfehler: {f}"))

    if trockenlauf and len(dateien) > zeige_max:
        print(f"  ... {len(dateien) - zeige_max} weitere")

    return statistik, fehler


def datei_hash(pfad, block=65536):
    """Berechnet den SHA-256-Hash einer Datei."""
    h = hashlib.sha256()
    with open(pfad, "rb") as f:
        while stueck := f.read(block):
            h.update(stueck)
    return h.hexdigest()


def finde_duplikate(dateien):
    """Findet Dateien mit identischem Inhalt.

    Returns:
        (duplikatgruppen, verschwendete_bytes)
    """
    nach_hash = {}
    for datei in dateien:
        try:
            nach_hash.setdefault(datei_hash(datei), []).append(datei)
        except (PermissionError, OSError):
            continue          # nicht lesbare Dateien überspringen

    gruppen = [pfade for pfade in nach_hash.values() if len(pfade) > 1]
    verschwendet = sum(g[0].stat().st_size * (len(g) - 1) for g in gruppen)
    return gruppen, verschwendet


def erstelle_backup(ordner, behalten=5):
    """Erstellt ein ZIP-Backup und entfernt zu alte Backups."""
    ziel_ordner = Path(ordner).parent / "_backups"
    ziel_ordner.mkdir(exist_ok=True)
    stempel = datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        archiv = Path(shutil.make_archive(
            str(ziel_ordner / f"backup_{stempel}"), "zip", ordner))
    except OSError as fehler:
        print(f"  ⚠️  Backup fehlgeschlagen: {fehler}")
        return None

    alte = sorted(ziel_ordner.glob("backup_*.zip"),
                  key=lambda p: p.stat().st_mtime, reverse=True)
    for alt in alte[behalten:]:
        alt.unlink()

    return archiv


def zeige_statistik(statistik, gesamt):
    """Gibt die Statistik mit Balkendiagramm aus."""
    if not statistik:
        print("  Keine Dateien zum Sortieren gefunden.")
        return

    hoechste = max(statistik.values())
    for kategorie, anzahl in sorted(statistik.items(), key=lambda p: -p[1]):
        symbol = REGELN.get(kategorie, (None, SONSTIGES[1]))[1]
        balken = "█" * int(anzahl / hoechste * 18)
        anteil = anzahl / gesamt
        print(f"  {symbol} {kategorie:<12}{anzahl:>4}  {balken:<18} {anteil:>4.0%}")


# ====================================================================
# TESTUMGEBUNG (nur für die Demo)
# ====================================================================
def baue_testordner():
    """Erzeugt einen Testordner mit Beispieldateien."""
    ordner = Path(__file__).parent / "_testordner"
    if ordner.exists():
        shutil.rmtree(ordner)
    ordner.mkdir()

    dateien = [
        "urlaubsfoto.jpg", "strand.JPG", "sonnenuntergang.png", "screenshot.png",
        "portrait.jpeg", "logo.gif",
        "Rechnung Müller 2026.pdf", "vertrag.pdf", "notizen.txt", "TODO.txt",
        "praesentation.pptx",
        "budget_2026.xlsx", "kunden.csv", "umsatz.xlsx",
        "podcast_folge_42.mp3", "lieblingslied.mp3",
        "urlaubsvideo.mp4", "clip.mov",
        "backup.zip", "archiv.7z",
        "skript.py", "index.html",
        "unbekannt.xyz", "readme",
    ]
    for name in dateien:
        (ordner / name).write_text(f"Inhalt von {name}\n" * 20, encoding="utf-8")

    # Duplikate
    for name in ("bericht.txt", "bericht_kopie.txt", "Bericht (1).txt"):
        (ordner / name).write_text("Identischer Inhalt.\n" * 100, encoding="utf-8")

    return ordner


# ====================================================================
# HAUPTPROGRAMM
# ====================================================================
def main():
    """Hauptprogramm."""
    kopfzeile("🗂️  ORDNER-AUFRÄUMER  v1.0")

    if DEMO_MODUS:
        ordner = baue_testordner()
        print(f"\n  ℹ️  Demo-Modus: Testordner angelegt")
    else:
        eingabe = input("\n  Welchen Ordner aufräumen? > ").strip().strip('"')
        ordner = Path(eingabe).expanduser()

    # --- Einlesen ---------------------------------------------------
    try:
        dateien = sammle_dateien(ordner)
    except (FileNotFoundError, NotADirectoryError) as fehler:
        print(f"\n  ❌ {fehler}")
        return 1
    except PermissionError:
        print(f"\n  ❌ Kein Zugriff auf {ordner}")
        return 1

    gesamt_groesse = sum(d.stat().st_size for d in dateien)
    unterordner = sum(1 for p in ordner.iterdir() if p.is_dir())

    print(f"\n  📁 Ordner:   {ordner}")
    print(f"  🔍 Gefunden: {len(dateien)} Dateien "
          f"({lesbar(gesamt_groesse)}), {unterordner} Unterordner")
    print("  🛡️ Modus:    TROCKENLAUF (nichts wird verändert)")

    if not dateien:
        print("\n  📭 Nichts zu tun. 🎉")
        return 0

    # --- Trockenlauf ------------------------------------------------
    abschnitt("VORSCHAU")
    statistik, _ = sortiere(dateien, ordner, trockenlauf=True)

    abschnitt("ZUSAMMENFASSUNG")
    zeige_statistik(statistik, len(dateien))

    # --- Duplikate --------------------------------------------------
    gruppen, verschwendet = finde_duplikate(dateien)
    if gruppen:
        print(f"\n  🔁 {len(gruppen)} Duplikatgruppe(n) gefunden "
              f"({lesbar(verschwendet)} verschwendet)")
        for gruppe in gruppen[:3]:
            namen = ", ".join(p.name for p in gruppe)
            print(f"     • {namen[:60]}")
        print("     ⚠️  Duplikate werden NICHT automatisch gelöscht.")

    # --- Bestätigung ------------------------------------------------
    print("\n" + "─" * (BREITE + 2))
    if DEMO_MODUS:
        antwort = "j"
        print("  Wirklich ausführen? (j/n) > j   [Demo]")
    else:
        antwort = input("  Das war ein Trockenlauf. Wirklich ausführen? (j/n) > ")

    if antwort.strip().lower() not in ("j", "ja", "y", "yes"):
        print("\n  Abgebrochen - es wurde nichts verändert. 🛡️")
        return 0

    # --- Backup -----------------------------------------------------
    abschnitt("BACKUP")
    archiv = erstelle_backup(ordner)
    if archiv:
        print(f"  💾 {archiv.name}  ({lesbar(archiv.stat().st_size)})")

    # --- Echter Lauf ------------------------------------------------
    abschnitt("SORTIEREN")
    statistik, fehler = sortiere(dateien, ordner, trockenlauf=False)
    zeige_statistik(statistik, len(dateien))

    if fehler:
        print(f"\n  ⚠️  {len(fehler)} Datei(en) übersprungen:")
        for name, grund in fehler[:5]:
            print(f"     • {name}: {grund}")

    # --- Bericht ----------------------------------------------------
    bericht = ordner / "_aufraeum_bericht.txt"
    zeilen = [
        "AUFRÄUM-BERICHT",
        "=" * 50,
        f"Zeitpunkt:  {datetime.now():%d.%m.%Y %H:%M:%S}",
        f"Ordner:     {ordner}",
        f"Dateien:    {len(dateien)}",
        f"Backup:     {archiv.name if archiv else 'keins'}",
        "",
        "Sortiert nach Kategorie:",
    ]
    zeilen += [f"  {k:<14}{a:>4}" for k, a in sorted(statistik.items())]
    zeilen += ["", f"Duplikatgruppen: {len(gruppen)}",
               f"Fehler:          {len(fehler)}"]
    bericht.write_text("\n".join(zeilen), encoding="utf-8")

    print(f"\n  ✅ Fertig! {sum(statistik.values())} Dateien sortiert.")
    print(f"  📄 Bericht: {bericht.name}")
    print(f"\n  📁 Ergebnis in: {ordner}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
