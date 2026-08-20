"""
Modul 11 - Beispiel 1: Dateien lesen und schreiben

Diese Datei legt sich ihre Testdaten selbst an - sie zerstört nichts. 😌
"""
from pathlib import Path

# Arbeitsordner für dieses Beispiel
ORDNER = Path(__file__).parent / "_testdaten"
ORDNER.mkdir(exist_ok=True)

# ====================================================================
# SCHREIBEN
# ====================================================================
print("=" * 60)
print("SCHREIBEN")
print("=" * 60)

datei = ORDNER / "notizen.txt"

# Modus "w" = schreiben (⚠️ löscht vorhandenen Inhalt!)
with open(datei, "w", encoding="utf-8") as f:
    f.write("Erste Zeile\n")            # \n selbst schreiben!
    f.write("Zweite Zeile mit Umlauten: äöüß\n")
    f.writelines(["Dritte\n", "Vierte\n"])

print(f"Geschrieben nach: {datei.name}")

# Modus "a" = anhängen (sicher)
with open(datei, "a", encoding="utf-8") as f:
    f.write("Angehängte Zeile\n")

print("Zeile angehängt.")

# Kurzform mit pathlib
(ORDNER / "kurz.txt").write_text("Einzeiler ohne with\n", encoding="utf-8")
print("Kurzform geschrieben.")

# ====================================================================
# LESEN - vier Wege
# ====================================================================
print("\n" + "=" * 60)
print("LESEN")
print("=" * 60)

print("\n1) read() - alles als ein String:")
with open(datei, "r", encoding="utf-8") as f:
    inhalt = f.read()
print(f"   {len(inhalt)} Zeichen")
print("   " + inhalt.replace("\n", "\n   ").rstrip())

print("\n2) readlines() - Liste von Zeilen:")
with open(datei, encoding="utf-8") as f:
    zeilen = f.readlines()
print(f"   {zeilen}")
print("   ⚠️ Beachte die \\n am Ende jeder Zeile!")

print("\n3) ⭐ Zeilenweise iterieren (bei großen Dateien immer so):")
with open(datei, encoding="utf-8") as f:
    for nr, zeile in enumerate(f, start=1):
        print(f"   {nr}: {zeile.strip()}")     # strip() entfernt \n

print("\n4) pathlib-Kurzform:")
text = datei.read_text(encoding="utf-8")
print(f"   {len(text.splitlines())} Zeilen gelesen")

# ====================================================================
# PATHLIB
# ====================================================================
print("\n" + "=" * 60)
print("PATHLIB")
print("=" * 60)

p = ORDNER / "notizen.txt"
print(f"  Pfad:            {p}")
print(f"  p.name:          {p.name}")
print(f"  p.stem:          {p.stem}")
print(f"  p.suffix:        {p.suffix}")
print(f"  p.parent.name:   {p.parent.name}")
print(f"  p.exists():      {p.exists()}")
print(f"  p.is_file():     {p.is_file()}")
print(f"  Größe:           {p.stat().st_size} Bytes")
print(f"\n  Aktuelles Arbeitsverzeichnis: {Path.cwd()}")
print("  💡 Bei FileNotFoundError: IMMER als Erstes Path.cwd() prüfen!")

# ====================================================================
# ORDNER DURCHSUCHEN
# ====================================================================
print("\n" + "=" * 60)
print("ORDNER DURCHSUCHEN")
print("=" * 60)

# Ein paar Testdateien anlegen
for name in ("bericht.pdf", "foto.jpg", "daten.csv", "notiz.txt"):
    (ORDNER / name).write_text("test", encoding="utf-8")

unterordner = ORDNER / "archiv"
unterordner.mkdir(exist_ok=True)
(unterordner / "alt.txt").write_text("alt", encoding="utf-8")

print("\niterdir() - eine Ebene:")
for eintrag in sorted(ORDNER.iterdir()):
    art = "📁" if eintrag.is_dir() else "📄"
    print(f"   {art} {eintrag.name}")

print("\nglob('*.txt') - nur txt, eine Ebene:")
for f in sorted(ORDNER.glob("*.txt")):
    print(f"   📄 {f.name}")

print("\nrglob('*.txt') - txt in ALLEN Unterordnern:")
for f in sorted(ORDNER.rglob("*.txt")):
    print(f"   📄 {f.relative_to(ORDNER)}")

# ====================================================================
# 🌍 REALBEISPIEL: Logdatei auswerten
# ====================================================================
print("\n" + "=" * 60)
print("🌍 REALBEISPIEL: Logdatei auswerten")
print("=" * 60)

log = ORDNER / "app.log"
log.write_text(
    "2026-07-20 08:15:32 INFO  Benutzer angemeldet\n"
    "2026-07-20 08:16:01 ERROR Datenbankverbindung fehlgeschlagen\n"
    "2026-07-20 09:02:11 INFO  Bericht erstellt\n"
    "2026-07-21 07:45:00 WARNING Speicher fast voll\n"
    "2026-07-21 07:46:12 ERROR Datenbankverbindung fehlgeschlagen\n"
    "2026-07-21 10:00:00 INFO  Backup abgeschlossen\n",
    encoding="utf-8",
)

level_zaehler = {}
fehlermeldungen = {}
tage = {}

with open(log, encoding="utf-8") as f:
    for zeile in f:
        zeile = zeile.strip()
        if not zeile:
            continue
        teile = zeile.split(maxsplit=3)      # Datum, Zeit, Level, Rest
        datum, _zeit, level, meldung = teile

        level_zaehler[level] = level_zaehler.get(level, 0) + 1
        tage[datum] = tage.get(datum, 0) + 1
        if level == "ERROR":
            fehlermeldungen[meldung] = fehlermeldungen.get(meldung, 0) + 1

symbole = {"INFO": "  ", "WARNING": "⚠️ ", "ERROR": "🔴"}
print("\n  LOG-ANALYSE")
print("  " + "-" * 40)
for level, anzahl in sorted(level_zaehler.items()):
    print(f"  {symbole.get(level, '  ')} {level:<10} {anzahl:>4}")

haeufigster = max(fehlermeldungen, key=fehlermeldungen.get)
aktivster_tag = max(tage, key=tage.get)
print(f"\n  Häufigster Fehler: '{haeufigster}' ({fehlermeldungen[haeufigster]}x)")
print(f"  Aktivster Tag:     {aktivster_tag} ({tage[aktivster_tag]} Einträge)")

# Bericht schreiben
bericht = ORDNER / "bericht.txt"
with open(bericht, "w", encoding="utf-8") as f:
    f.write("LOG-ANALYSE\n")
    f.write("=" * 40 + "\n")
    for level, anzahl in sorted(level_zaehler.items()):
        f.write(f"{level:<10} {anzahl:>4}\n")
print(f"\n  ✅ Bericht geschrieben: {bericht.name}")

print(f"\n💡 Alle Testdateien liegen in: {ORDNER}")
print("   Du darfst den Ordner jederzeit löschen.")
