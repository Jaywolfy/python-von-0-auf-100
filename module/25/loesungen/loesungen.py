"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 25 · MUSTERLÖSUNGEN — Dateien & Ordner                    ║
╚══════════════════════════════════════════════════════════════════╝
"""
import hashlib
import shutil
from datetime import datetime, timedelta
from pathlib import Path

LOES = Path(__file__).parent / "_loesung25"
if LOES.exists():
    shutil.rmtree(LOES)
LOES.mkdir()

DATEIEN = [
    "IMG_0001.jpg", "IMG_0002.jpg", "IMG_0003.JPG", "screenshot.png",
    "Rechnung Müller 2026-01.pdf", "Rechnung Schmidt 2026-02.pdf",
    "vertrag final v2.pdf", "Präsentation Q1.pptx",
    "notizen 2026.txt", "TODO.txt", "alte notiz.txt",
    "Budget 2026.xlsx", "kunden export.csv", "umsatz.xlsx",
    "song.mp3", "podcast folge 12.mp3", "urlaubsvideo.mp4",
    "backup.zip", "readme", "daten.json", "skript.py",
]
for name in DATEIEN:
    (LOES / name).write_text(f"Inhalt: {name}\n", encoding="utf-8")
for name in ("bericht.txt", "bericht_kopie.txt", "Bericht (1).txt"):
    (LOES / name).write_text("Gleicher Inhalt hier.\n", encoding="utf-8")
(LOES / "Downloads alt").mkdir()
for name in ("altes_bild.jpg", "altes_dokument.pdf", "altes_lied.mp3"):
    (LOES / "Downloads alt" / name).write_text("alt\n", encoding="utf-8")


print("=" * 62, "\nAUFGABE 1 🟢\n", "=" * 62)

alle_dateien = [p for p in LOES.rglob("*") if p.is_file()]
alle_ordner = [p for p in LOES.rglob("*") if p.is_dir()]

print(f"  a) Dateien:      {len(alle_dateien)}")
print(f"  b) Ordner:       {len(alle_ordner)}")

nach_endung = {}
for p in alle_dateien:
    nach_endung[p.suffix.lower() or "(ohne)"] = nach_endung.get(
        p.suffix.lower() or "(ohne)", 0) + 1
print("  c) Endungen:")
for endung, anzahl in sorted(nach_endung.items(), key=lambda x: -x[1]):
    print(f"       {endung:<10}{anzahl:>3}  {'▪' * anzahl}")

gesamt = sum(p.stat().st_size for p in alle_dateien)
print(f"  d) Gesamtgröße:  {gesamt:,} Bytes")


print("\n" + "=" * 62, "\nAUFGABE 2 🟢\n", "=" * 62)

BILD_ENDUNGEN = {".jpg", ".jpeg", ".png"}
bilder = [p for p in alle_dateien if p.suffix.lower() in BILD_ENDUNGEN]
rechnungen = [p for p in alle_dateien if "rechnung" in p.name.lower()]
ohne_endung = [p for p in alle_dateien if not p.suffix]
mit_leerzeichen = [p for p in alle_dateien if " " in p.name]

print(f"  a) Bilder ({len(bilder)}):          {[p.name for p in bilder]}")
print(f"  b) Rechnungen ({len(rechnungen)}):      {[p.name for p in rechnungen]}")
print(f"  c) Ohne Endung ({len(ohne_endung)}):     {[p.name for p in ohne_endung]}")
print(f"  d) Mit Leerzeichen ({len(mit_leerzeichen)}): {[p.name for p in mit_leerzeichen][:4]} …")


print("\n" + "=" * 62, "\nAUFGABE 3 🟡\n", "=" * 62)

UMLAUTE = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
           "Ä": "Ae", "Ö": "Oe", "Ü": "Ue"}
ERLAUBT = "abcdefghijklmnopqrstuvwxyz0123456789._-"


def sauberer_name(name):
    """Wandelt einen Dateinamen in eine bereinigte Kleinschreibvariante."""
    stamm, punkt, endung = name.rpartition(".")
    if not punkt:
        stamm, endung = name, ""

    for umlaut, ersatz in UMLAUTE.items():
        stamm = stamm.replace(umlaut, ersatz)

    stamm = stamm.lower().replace(" ", "_")
    stamm = "".join(z for z in stamm if z in ERLAUBT)
    while "__" in stamm:
        stamm = stamm.replace("__", "_")
    stamm = stamm.strip("_")

    return f"{stamm}.{endung.lower()}" if endung else stamm


def bereinige_namen(ordner, trockenlauf=True):
    """Bereinigt alle Dateinamen in einem Ordner.

    Args:
        ordner: Der zu bearbeitende Ordner.
        trockenlauf: Wenn True, wird nur angezeigt statt umbenannt.

    Returns:
        Anzahl der geänderten Dateien.
    """
    geaendert = 0
    for datei in sorted(list(ordner.iterdir())):
        if not datei.is_file():
            continue
        neu = sauberer_name(datei.name)
        if neu == datei.name:
            continue

        ziel = datei.with_name(neu)
        if trockenlauf:
            print(f"    [TEST] {datei.name:<32} → {neu}")
        else:
            if ziel.exists():
                ziel = ziel.with_stem(f"{ziel.stem}_1")
            datei.rename(ziel)
        geaendert += 1
    return geaendert


print("  👀 Trockenlauf:")
anzahl = bereinige_namen(LOES, trockenlauf=True)
print(f"\n  {anzahl} Dateien würden umbenannt.")
print("\n  ✅ Echter Lauf:")
bereinige_namen(LOES, trockenlauf=False)
print(f"    Neue Namen: {[p.name for p in sorted(LOES.glob('*'))[:5]]} …")


print("\n" + "=" * 62, "\nAUFGABE 4 🟡\n", "=" * 62)

REGELN = {
    "Bilder":    {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Dokumente": {".pdf", ".docx", ".txt", ".odt", ".pptx"},
    "Tabellen":  {".xlsx", ".csv", ".ods"},
    "Musik":     {".mp3", ".wav", ".flac"},
    "Videos":    {".mp4", ".mov", ".mkv"},
    "Archive":   {".zip", ".rar", ".7z"},
    "Code":      {".py", ".js", ".json", ".html", ".css"},
}


def ziel_ordner(datei):
    """Bestimmt den Zielordner anhand der Dateiendung."""
    for name, endungen in REGELN.items():
        if datei.suffix.lower() in endungen:
            return name
    return "Sonstiges"


def sortiere_nach_typ(ordner, trockenlauf=True):
    """Sortiert Dateien nach Typ in Unterordner.

    Returns:
        Statistik-dict {Zielordner: Anzahl}.
    """
    statistik = {}
    for datei in sorted(list(ordner.iterdir())):
        if not datei.is_file():
            continue

        name = ziel_ordner(datei)
        ziel = ordner / name / datei.name

        if trockenlauf:
            print(f"    [TEST] {datei.name:<32} → {name}/")
        else:
            ziel.parent.mkdir(exist_ok=True)
            if ziel.exists():
                ziel = ziel.with_stem(f"{ziel.stem}_1")
            datei.rename(ziel)
        statistik[name] = statistik.get(name, 0) + 1
    return statistik


print("  👀 Trockenlauf (Auszug):")
stat = sortiere_nach_typ(LOES, trockenlauf=True)
print("\n  Zusammenfassung:")
for name, anzahl in sorted(stat.items(), key=lambda p: -p[1]):
    print(f"    {name:<12}{anzahl:>3}  {'█' * anzahl}")

print("\n  ✅ Echter Lauf:")
sortiere_nach_typ(LOES, trockenlauf=False)
for eintrag in sorted(LOES.iterdir()):
    if eintrag.is_dir():
        print(f"    📁 {eintrag.name:<14}{len(list(eintrag.glob('*'))):>3} Dateien")


print("\n" + "=" * 62, "\nAUFGABE 5 🟡\n", "=" * 62)


def datei_hash(pfad, block=65536):
    """Berechnet den SHA-256-Hash einer Datei."""
    h = hashlib.sha256()
    with open(pfad, "rb") as f:
        while stueck := f.read(block):
            h.update(stueck)
    return h.hexdigest()


def finde_duplikate(ordner):
    """Findet Dateien mit identischem Inhalt.

    Returns:
        dict {hash: [pfade]} - nur Gruppen mit mehr als einer Datei.
    """
    nach_hash = {}
    for datei in ordner.rglob("*"):
        if datei.is_file():
            nach_hash.setdefault(datei_hash(datei), []).append(datei)
    return {h: p for h, p in nach_hash.items() if len(p) > 1}


duplikate = finde_duplikate(LOES)
verschwendet = 0

for h, pfade in duplikate.items():
    groesse = pfade[0].stat().st_size
    verschwendet += groesse * (len(pfade) - 1)
    print(f"  🔁 {len(pfade)} identische Dateien ({groesse} Bytes):")
    for p in pfade:
        print(f"       • {p.relative_to(LOES)}")

print(f"\n  Verschwendeter Speicher: {verschwendet:,} Bytes")
print("  ⚠️ NUR ANGEZEIGT - gelöscht wird nichts. Der Mensch entscheidet. 🛡️")


print("\n" + "=" * 62, "\nAUFGABE 6 🔴\n", "=" * 62)

PAPIERKORB = LOES / "_papierkorb"


def in_papierkorb(datei, papierkorb=PAPIERKORB):
    """Verschiebt eine Datei in den Papierkorb statt sie zu löschen.

    Args:
        datei: Die zu 'löschende' Datei.
        papierkorb: Zielordner.

    Returns:
        Der neue Pfad im Papierkorb.
    """
    datei = Path(datei)
    papierkorb.mkdir(exist_ok=True)

    ziel = papierkorb / datei.name
    if ziel.exists():
        stempel = datetime.now().strftime("%Y%m%d_%H%M%S")
        ziel = papierkorb / f"{datei.stem}_{stempel}{datei.suffix}"

    shutil.move(str(datei), str(ziel))
    return ziel


def papierkorb_leeren(papierkorb=PAPIERKORB, aelter_als_tage=30, trockenlauf=True):
    """Entfernt Dateien, die länger als X Tage im Papierkorb liegen."""
    if not papierkorb.exists():
        return 0

    grenze = datetime.now() - timedelta(days=aelter_als_tage)
    entfernt = 0
    for datei in papierkorb.iterdir():
        aenderung = datetime.fromtimestamp(datei.stat().st_mtime)
        if aenderung < grenze:
            if trockenlauf:
                print(f"    [TEST] würde löschen: {datei.name}")
            else:
                datei.unlink()
            entfernt += 1
    return entfernt


# Ein Duplikat testweise in den Papierkorb schieben
if duplikate:
    erste_gruppe = list(duplikate.values())[0]
    verschoben = in_papierkorb(erste_gruppe[-1])
    print(f"  ✅ '{erste_gruppe[-1].name}' → Papierkorb: {verschoben.name}")

print(f"  Papierkorb enthält: {len(list(PAPIERKORB.glob('*')))} Datei(en)")
print(f"  Zu löschen (>30 Tage): {papierkorb_leeren(trockenlauf=True)}")
print("\n  💡 Das ist die sichere Alternative zu unlink()/os.remove():")
print("     Man kann jederzeit zurückholen, was man versehentlich entfernt hat.")


print("\n" + "=" * 62, "\nAUFGABE 7 🔴\n", "=" * 62)

BACKUP_ORDNER = LOES.parent / "_backups25"
BACKUP_ORDNER.mkdir(exist_ok=True)


def erstelle_backup(quelle, ziel_ordner=BACKUP_ORDNER, behalte=5):
    """Erstellt ein ZIP-Backup und räumt alte Backups auf.

    Args:
        quelle: Der zu sichernde Ordner.
        ziel_ordner: Wohin die Backups kommen.
        behalte: Wie viele Backups aufgehoben werden.

    Returns:
        (Pfad, Größe in Bytes)
    """
    ziel_ordner.mkdir(exist_ok=True)
    stempel = datetime.now().strftime("%Y%m%d_%H%M%S")
    basis = ziel_ordner / f"backup_{stempel}"

    archiv = Path(shutil.make_archive(str(basis), "zip", quelle))

    # Alte Backups entfernen
    vorhandene = sorted(ziel_ordner.glob("backup_*.zip"),
                        key=lambda p: p.stat().st_mtime, reverse=True)
    for alt in vorhandene[behalte:]:
        alt.unlink()
        print(f"    🗑️  Altes Backup entfernt: {alt.name}")

    return archiv, archiv.stat().st_size


archiv, groesse = erstelle_backup(LOES)
print(f"  ✅ {archiv.name}  ({groesse:,} Bytes)")
print(f"  Vorhandene Backups: {len(list(BACKUP_ORDNER.glob('backup_*.zip')))}")


print("\n" + "=" * 62, "\nAUFGABE 8 ⭐\n", "=" * 62)


def raeume_auf(ordner, trockenlauf=True, mit_backup=True):
    """Kompletter Aufräumvorgang mit Bericht.

    Args:
        ordner: Der aufzuräumende Ordner.
        trockenlauf: Wenn True, wird nichts verändert.
        mit_backup: Vorher ein ZIP-Backup anlegen.

    Returns:
        Ein Bericht als dict.
    """
    bericht = {"zeitpunkt": datetime.now().isoformat(timespec="seconds"),
               "ordner": str(ordner), "trockenlauf": trockenlauf}

    if mit_backup and not trockenlauf:
        archiv, groesse = erstelle_backup(ordner)
        bericht["backup"] = f"{archiv.name} ({groesse:,} Bytes)"

    bericht["umbenannt"] = bereinige_namen(ordner, trockenlauf=trockenlauf)
    bericht["sortiert"] = sortiere_nach_typ(ordner, trockenlauf=trockenlauf)

    dupl = finde_duplikate(ordner)
    bericht["duplikatgruppen"] = len(dupl)
    bericht["duplikate"] = [[str(p.relative_to(ordner)) for p in pfade]
                            for pfade in dupl.values()]
    return bericht


TESTORDNER = LOES.parent / "_aufraeumtest"
if TESTORDNER.exists():
    shutil.rmtree(TESTORDNER)
TESTORDNER.mkdir()
for name in ("Foto Eins.JPG", "Notiz Zwei.TXT", "Tabelle Drei.xlsx"):
    (TESTORDNER / name).write_text("test\n", encoding="utf-8")

print("  👀 Trockenlauf:")
ergebnis = raeume_auf(TESTORDNER, trockenlauf=True, mit_backup=False)

print("\n  ✅ Echter Lauf:")
ergebnis = raeume_auf(TESTORDNER, trockenlauf=False, mit_backup=True)

bericht_datei = TESTORDNER / "aufraeum_bericht.txt"
zeilen = ["AUFRÄUM-BERICHT", "=" * 50,
          f"Zeitpunkt:  {ergebnis['zeitpunkt']}",
          f"Ordner:     {ergebnis['ordner']}",
          f"Backup:     {ergebnis.get('backup', 'keins')}",
          f"Umbenannt:  {ergebnis['umbenannt']} Dateien",
          "Sortiert:"]
for name, anzahl in sorted(ergebnis["sortiert"].items()):
    zeilen.append(f"  {name:<14}{anzahl:>3}")
zeilen.append(f"Duplikatgruppen: {ergebnis['duplikatgruppen']}")
bericht_datei.write_text("\n".join(zeilen), encoding="utf-8")

print(f"\n{bericht_datei.read_text(encoding='utf-8')}")

print(f"""
{'=' * 62}
  📁 Alles liegt in: {LOES.parent}

  🛡️ DIE WICHTIGSTE LEHRE DIESES MODULS:
     Jede Funktion, die Dateien verändert, bekommt einen
     trockenlauf-Parameter mit Standardwert True.
     Diese eine Zeile hat schon mehr Daten gerettet als
     jedes Backup-Programm. 😌
{'=' * 62}
""")
