"""
Modul 25 - Beispiel: Dateien und Ordner automatisieren

🧪 Erzeugt sich einen kompletten Testordner. Deine echten Dateien
   werden NICHT angefasst.
"""
import hashlib
import shutil
from pathlib import Path
from datetime import datetime

BASIS = Path(__file__).parent / "_spielwiese"

# ====================================================================
# TESTUMGEBUNG AUFBAUEN
# ====================================================================
if BASIS.exists():
    shutil.rmtree(BASIS)          # sicher: nur unser eigener Testordner
BASIS.mkdir()

TESTDATEIEN = [
    "urlaub1.jpg", "urlaub2.jpg", "urlaub3.JPG", "portrait.png",
    "rechnung_2026_01.pdf", "rechnung_2026_02.pdf", "vertrag.pdf",
    "notizen.txt", "todo.txt", "budget.xlsx", "kunden.csv",
    "lied.mp3", "clip.mp4", "archiv.zip", "unbekannt.xyz",
]
for name in TESTDATEIEN:
    (BASIS / name).write_text(f"Inhalt von {name}\n", encoding="utf-8")

# Zwei echte Duplikate (gleicher Inhalt, anderer Name)
(BASIS / "kopie_a.txt").write_text("Ich bin doppelt vorhanden.\n", encoding="utf-8")
(BASIS / "kopie_b.txt").write_text("Ich bin doppelt vorhanden.\n", encoding="utf-8")

unter = BASIS / "alt"
unter.mkdir()
(unter / "altes_foto.jpg").write_text("alt\n", encoding="utf-8")
(unter / "altes_dokument.pdf").write_text("alt\n", encoding="utf-8")

print("=" * 62)
print(f"🧪 Testordner angelegt: {BASIS.name}")
print("=" * 62)

# ====================================================================
print("\n1. ORDNER DURCHSUCHEN\n" + "-" * 62)

alle = sorted(p for p in BASIS.rglob("*") if p.is_file())
print(f"  {len(alle)} Dateien gefunden (inkl. Unterordner)")

print("\n  Nur eine Ebene (glob):")
print(f"    {len(list(BASIS.glob('*.pdf')))} PDFs")
print("  Alle Ebenen (rglob):")
print(f"    {len(list(BASIS.rglob('*.pdf')))} PDFs   ← findet auch alt/")

print("\n  Nach Endung gruppiert:")
nach_endung = {}
for p in alle:
    nach_endung.setdefault(p.suffix.lower() or "(ohne)", []).append(p.name)
for endung, dateien in sorted(nach_endung.items()):
    print(f"    {endung:<8}{len(dateien):>3}  {', '.join(dateien[:3])}"
          f"{' …' if len(dateien) > 3 else ''}")

# ====================================================================
print("\n2. 👀 TROCKENLAUF: Ordner sortieren\n" + "-" * 62)

REGELN = {
    "Bilder":    {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Dokumente": {".pdf", ".docx", ".txt", ".odt"},
    "Tabellen":  {".xlsx", ".csv", ".ods"},
    "Musik":     {".mp3", ".wav", ".flac"},
    "Videos":    {".mp4", ".mov", ".mkv"},
    "Archive":   {".zip", ".rar", ".7z"},
}


def ziel_ordner(datei):
    """Bestimmt den Zielordner anhand der Dateiendung."""
    for name, endungen in REGELN.items():
        if datei.suffix.lower() in endungen:
            return name
    return "Sonstiges"


def sortiere(quelle, trockenlauf=True):
    """Sortiert Dateien nach Typ in Unterordner.

    Args:
        quelle: Der zu sortierende Ordner.
        trockenlauf: Wenn True, wird nur angezeigt statt verschoben.

    Returns:
        Ein dict mit der Anzahl je Zielordner.
    """
    statistik = {}
    # ⚠️ list() - sonst iterieren wir über einen Ordner, den wir verändern!
    for datei in sorted(list(quelle.iterdir())):
        if not datei.is_file():
            continue

        name = ziel_ordner(datei)
        ziel = quelle / name / datei.name

        if trockenlauf:
            print(f"    [TEST] {datei.name:<26} → {name}/")
        else:
            ziel.parent.mkdir(exist_ok=True)
            if ziel.exists():                                  # 🛡️
                ziel = ziel.with_stem(f"{ziel.stem}_1")
            datei.rename(ziel)
        statistik[name] = statistik.get(name, 0) + 1
    return statistik


print("  Was WÜRDE passieren:")
statistik = sortiere(BASIS, trockenlauf=True)
print("\n  Zusammenfassung:")
for ordner, anzahl in sorted(statistik.items()):
    print(f"    {ordner:<12}{anzahl:>3} Dateien")

# ====================================================================
print("\n3. ✅ ECHTER LAUF (nur im Testordner!)\n" + "-" * 62)

sortiere(BASIS, trockenlauf=False)
print("  Ergebnis:")
for eintrag in sorted(BASIS.iterdir()):
    if eintrag.is_dir():
        anzahl = len(list(eintrag.glob("*")))
        print(f"    📁 {eintrag.name:<14}{anzahl:>3} Dateien")

# ====================================================================
print("\n4. MASSEN-UMBENENNUNG\n" + "-" * 62)

bilder = BASIS / "Bilder"
if bilder.exists():
    heute = datetime.now().strftime("%Y%m%d")
    for nr, datei in enumerate(sorted(bilder.glob("*")), start=1):
        neu = bilder / f"foto_{heute}_{nr:03d}{datei.suffix.lower()}"
        print(f"    {datei.name:<24} → {neu.name}")
        datei.rename(neu)

# ====================================================================
print("\n5. 🔍 DUPLIKATE FINDEN (per Hash)\n" + "-" * 62)


def datei_hash(pfad, block=65536):
    """Berechnet den SHA-256-Hash einer Datei."""
    h = hashlib.sha256()
    with open(pfad, "rb") as f:
        while stueck := f.read(block):
            h.update(stueck)
    return h.hexdigest()


nach_hash = {}
for datei in BASIS.rglob("*"):
    if datei.is_file():
        nach_hash.setdefault(datei_hash(datei), []).append(datei)

duplikate = {h: pfade for h, pfade in nach_hash.items() if len(pfade) > 1}

if duplikate:
    for h, pfade in duplikate.items():
        print(f"    Hash {h[:12]}… kommt {len(pfade)}x vor:")
        for p in pfade:
            print(f"      • {p.relative_to(BASIS)}")
else:
    print("    Keine Duplikate gefunden")

print("\n  💡 Gleicher Name ≠ gleicher Inhalt. Der Hash vergleicht den INHALT.")

# ====================================================================
print("\n6. 💾 BACKUP ALS ZIP\n" + "-" * 62)

backup_name = BASIS.parent / f"backup_{datetime.now():%Y%m%d_%H%M%S}"
archiv = shutil.make_archive(str(backup_name), "zip", BASIS)
groesse = Path(archiv).stat().st_size
print(f"    ✅ {Path(archiv).name}  ({groesse:,} Bytes)")

# ====================================================================
print("\n7. 📊 ORDNER-STATISTIK\n" + "-" * 62)

gesamt_groesse = 0
anzahl = 0
groesste = None
for datei in BASIS.rglob("*"):
    if datei.is_file():
        groesse = datei.stat().st_size
        gesamt_groesse += groesse
        anzahl += 1
        if groesste is None or groesse > groesste.stat().st_size:
            groesste = datei

print(f"    Dateien gesamt:   {anzahl}")
print(f"    Gesamtgröße:      {gesamt_groesse:,} Bytes")
print(f"    Durchschnitt:     {gesamt_groesse / anzahl:,.0f} Bytes")
print(f"    Größte Datei:     {groesste.name}")
print(f"    Unterordner:      {sum(1 for p in BASIS.rglob('*') if p.is_dir())}")

print(f"""
{'=' * 62}
  🧪 Spielwiese: {BASIS}
     Du darfst den Ordner und das Backup jederzeit löschen.

  🛡️ MERKE: TROCKENLAUF = True ist der Standard.
     Erst nach dem Test auf False setzen. Immer.
{'=' * 62}
""")
