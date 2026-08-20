"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 11 · MUSTERLÖSUNGEN — Dateien & Pfade                     ║
╚══════════════════════════════════════════════════════════════════╝
"""
from pathlib import Path
from datetime import datetime

UEB = Path(__file__).parent / "_loesung"
UEB.mkdir(exist_ok=True)

(UEB / "einkaufsliste.txt").write_text(
    "Milch\nBrot\nEier\nKäse\nButter\nApfel\n", encoding="utf-8")
(UEB / "noten.csv").write_text(
    "Anna;2.3\nBernd;1.7\nClara;3.0\nDavid;1.3\nEmil;4.0\n", encoding="utf-8")
(UEB / "text.txt").write_text(
    "Python ist eine großartige Sprache.\n"
    "Mit Python kann man Dateien lesen.\n"
    "Python macht Automatisierung einfach.\n", encoding="utf-8")


print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

with open(UEB / "einkaufsliste.txt", encoding="utf-8") as f:
    for nr, zeile in enumerate(f, start=1):
        print(f"  {nr}. {zeile.strip()}")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

ziele = [
    "Python-Grundlagen sicher beherrschen",
    "Meine Ordner automatisch sortieren lassen",
    "Excel-Berichte automatisch erstellen",
    "Ein eigenes Tool auf GitHub veröffentlichen",
    "Nie wieder etwas 100x von Hand machen",
]

with open(UEB / "meine_ziele.txt", "w", encoding="utf-8") as f:
    for ziel in ziele:
        f.write(ziel + "\n")

print("  Geschrieben. Wieder eingelesen:")
for zeile in (UEB / "meine_ziele.txt").read_text(encoding="utf-8").splitlines():
    print(f"    • {zeile}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)

with open(UEB / "einkaufsliste.txt", "a", encoding="utf-8") as f:
    for artikel in ("Kaffee", "Zucker", "Mehl"):
        f.write(artikel + "\n")

print("  Nach dem Anhängen:")
print("   ", (UEB / "einkaufsliste.txt").read_text(encoding="utf-8").split())


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)

text = (UEB / "text.txt").read_text(encoding="utf-8")
zeilen = text.splitlines()
woerter = text.split()

print(f"  a) Zeilen:   {len(zeilen)}")
print(f"  b) Wörter:   {len(woerter)}")
print(f"  c) Zeichen:  {len(text.replace(chr(10), ''))}")
print("  d) Zeilen mit 'Python':")
for z in zeilen:
    if "Python" in z:
        print(f"       {z}")
laengstes = max(woerter, key=len)
print(f"  e) Längstes Wort: {laengstes} ({len(laengstes)})")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

eintraege = []
with open(UEB / "noten.csv", encoding="utf-8") as f:
    for zeile in f:
        zeile = zeile.strip()
        if not zeile:
            continue
        name, note_text = zeile.split(";")
        eintraege.append((name, float(note_text)))

print(f"  {'Name':<10}{'Note':>6}")
print("  " + "-" * 16)
for name, note in eintraege:
    print(f"  {name:<10}{note:>6.1f}")

noten = [n for _, n in eintraege]
bester = min(eintraege, key=lambda e: e[1])
schlechtester = max(eintraege, key=lambda e: e[1])
bestanden = [e for e in eintraege if e[1] <= 4.0]

print("  " + "-" * 16)
print(f"  Durchschnitt:  {sum(noten) / len(noten):.2f}")
print(f"  Bester:        {bester[0]} ({bester[1]})")
print(f"  Schlechtester: {schlechtester[0]} ({schlechtester[1]})")
print(f"  Bestanden:     {len(bestanden)} von {len(eintraege)}")


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)

zeugnis = UEB / "zeugnis.txt"
with open(zeugnis, "w", encoding="utf-8") as f:
    f.write("ZEUGNIS\n")
    f.write("=" * 30 + "\n")
    for name, note in eintraege:
        status = "bestanden" if note <= 4.0 else "nicht bestanden"
        f.write(f"{name:<10} {note:>4.1f}  {status}\n")
    f.write("-" * 30 + "\n")
    f.write(f"Durchschnitt: {sum(noten) / len(noten):.2f}\n")

print(zeugnis.read_text(encoding="utf-8"))


print("=" * 60, "\nAUFGABE 7 🔴\n", "=" * 60)

sortiert = UEB / "sortiert"
for unter in ("Text", "Daten", "Sonstiges"):
    (sortiert / unter).mkdir(parents=True, exist_ok=True)

zuordnung = {".txt": "Text", ".csv": "Daten"}

print(f"  {'Datei':<28}{'Zielordner'}")
print("  " + "-" * 42)
for datei in sorted(UEB.rglob("*")):
    if datei.is_dir():
        continue
    ziel = zuordnung.get(datei.suffix.lower(), "Sonstiges")
    print(f"  {str(datei.relative_to(UEB)):<28}{ziel}")


print("\n" + "=" * 60, "\nAUFGABE 8 🥗 MIX\n", "=" * 60)

text = (UEB / "text.txt").read_text(encoding="utf-8").lower()
for zeichen in ".,;:!?":
    text = text.replace(zeichen, "")

zaehler = {}
for wort in text.split():
    zaehler[wort] = zaehler.get(wort, 0) + 1

statistik = UEB / "wortstatistik.txt"
with open(statistik, "w", encoding="utf-8") as f:
    for wort, anzahl in sorted(zaehler.items(), key=lambda p: (-p[1], p[0])):
        f.write(f"{wort:<20} : {anzahl}\n")

print("  Top 5:")
for zeile in statistik.read_text(encoding="utf-8").splitlines()[:5]:
    print(f"    {zeile}")


print("\n" + "=" * 60, "\nAUFGABE 9 🔴\n", "=" * 60)


def lies_sicher(pfad):
    """Liest eine Datei und gibt None zurück, wenn sie nicht existiert."""
    pfad = Path(pfad)
    if not pfad.exists():
        print(f"  ❌ Datei nicht gefunden: {pfad.absolute()}")
        print(f"     Aktuelles Verzeichnis: {Path.cwd()}")
        return None
    return pfad.read_text(encoding="utf-8")


inhalt = lies_sicher(UEB / "text.txt")
print(f"  ✅ Gelesen: {len(inhalt)} Zeichen")
lies_sicher(UEB / "gibtsnicht.txt")


print("\n" + "=" * 60, "\nAUFGABE 10 ⭐\n", "=" * 60)


def backup(pfad):
    """Legt eine Kopie der Datei mit Zeitstempel im Namen an."""
    pfad = Path(pfad)
    if not pfad.exists():
        print(f"  ❌ {pfad.name} existiert nicht")
        return None

    stempel = datetime.now().strftime("%Y%m%d_%H%M%S")
    ziel = pfad.with_name(f"{pfad.stem}_{stempel}{pfad.suffix}")
    ziel.write_bytes(pfad.read_bytes())      # bytes = funktioniert für alles
    print(f"  ✅ Backup erstellt: {ziel.name}")
    return ziel


backup(UEB / "noten.csv")

print(f"\n💡 Alle Dateien liegen in: {UEB}")
print("🎉 Modul 11 geschafft! Jetzt kannst du echte Daten verarbeiten.")
