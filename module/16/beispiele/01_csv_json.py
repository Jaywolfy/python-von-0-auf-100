"""
Modul 16 - Beispiel: CSV und JSON
"""
import csv
import json
from pathlib import Path

ORDNER = Path(__file__).parent / "_daten16"
ORDNER.mkdir(exist_ok=True)

# ====================================================================
# TESTDATEN ANLEGEN (deutsches Format mit Semikolon!)
# ====================================================================
csv_datei = ORDNER / "mitarbeiter.csv"
csv_datei.write_text(
    "name;abteilung;gehalt;eintritt\n"
    "Anna Müller;IT;4.800,50;2019-03-01\n"
    "Bernd Schmidt;Marketing;3.900,00;2021-07-15\n"
    "Clara Weiß;IT;5.600,75;2017-01-10\n"
    "David Braun;Vertrieb;4.200,00;2022-11-02\n",
    encoding="utf-8",
)

# ====================================================================
# 1. CSV LESEN - mit reader
# ====================================================================
print("=" * 60, "\n1. csv.reader\n", "=" * 60)

with open(csv_datei, encoding="utf-8", newline="") as f:
    leser = csv.reader(f, delimiter=";")
    kopf = next(leser)
    print(f"  Spalten: {kopf}")
    for zeile in leser:
        print(f"  {zeile}")

# ====================================================================
# 2. ⭐ CSV LESEN - mit DictReader
# ====================================================================
print("\n" + "=" * 60, "\n2. csv.DictReader (besser!)\n", "=" * 60)


def deutsche_zahl(text):
    """Wandelt '4.800,50' in 4800.50 um."""
    return float(text.replace(".", "").replace(",", "."))


mitarbeiter = []
with open(csv_datei, encoding="utf-8", newline="") as f:
    for zeile in csv.DictReader(f, delimiter=";"):
        mitarbeiter.append({
            "name": zeile["name"],
            "abteilung": zeile["abteilung"],
            "gehalt": deutsche_zahl(zeile["gehalt"]),      # str -> float!
            "eintritt": zeile["eintritt"],
        })

print(f"  {'Name':<16}{'Abteilung':<12}{'Gehalt':>12}")
print("  " + "-" * 40)
for m in mitarbeiter:
    print(f"  {m['name']:<16}{m['abteilung']:<12}{m['gehalt']:>12,.2f}")

gehaelter = [m["gehalt"] for m in mitarbeiter]
print("  " + "-" * 40)
print(f"  {'SUMME':<28}{sum(gehaelter):>12,.2f}")
print(f"  {'DURCHSCHNITT':<28}{sum(gehaelter) / len(gehaelter):>12,.2f}")

print("\n  💡 Ohne Umwandlung wären die Gehälter Strings gewesen -")
print("     und '4.800,50' + '3.900,00' hätte '4.800,503.900,00' ergeben!")

# ====================================================================
# 3. CSV SCHREIBEN
# ====================================================================
print("\n" + "=" * 60, "\n3. CSV schreiben\n", "=" * 60)

bericht = ORDNER / "bericht.csv"

# Auswertung pro Abteilung
pro_abteilung = {}
for m in mitarbeiter:
    a = m["abteilung"]
    pro_abteilung.setdefault(a, []).append(m["gehalt"])

with open(bericht, "w", encoding="utf-8", newline="") as f:
    schreiber = csv.DictWriter(
        f, fieldnames=["abteilung", "anzahl", "summe", "durchschnitt"],
        delimiter=";")
    schreiber.writeheader()
    for abteilung, werte in sorted(pro_abteilung.items()):
        schreiber.writerow({
            "abteilung": abteilung,
            "anzahl": len(werte),
            "summe": f"{sum(werte):.2f}",
            "durchschnitt": f"{sum(werte) / len(werte):.2f}",
        })

print(f"  Geschrieben: {bericht.name}")
print("  Inhalt:")
for zeile in bericht.read_text(encoding="utf-8").splitlines():
    print(f"    {zeile}")

# ====================================================================
# 4. JSON
# ====================================================================
print("\n" + "=" * 60, "\n4. JSON\n", "=" * 60)

konfiguration = {
    "projekt": "Python-Kurs",
    "version": "1.0",
    "autor": {"name": "Anna Schmidt", "email": "anna@beispiel.de"},
    "module": 27,
    "aktiv": True,
    "themen": ["Grundlagen", "OOP", "Automatisierung"],
    "einstellungen": {
        "sprache": "de",
        "schwierigkeit": {"start": "einfach", "ende": "fortgeschritten"},
    },
    "notiz": None,
}

json_datei = ORDNER / "konfig.json"

with open(json_datei, "w", encoding="utf-8") as f:
    json.dump(konfiguration, f, indent=2, ensure_ascii=False)

print(f"  Gespeichert: {json_datei.name}")
print("  Datei-Inhalt (Auszug):")
for zeile in json_datei.read_text(encoding="utf-8").splitlines()[:10]:
    print(f"    {zeile}")
print("    ...")

with open(json_datei, encoding="utf-8") as f:
    geladen = json.load(f)

print("\n  Zugriff auf verschachtelte Werte:")
print(f"    ['autor']['name']                          -> {geladen['autor']['name']}")
print(f"    ['themen'][1]                              -> {geladen['themen'][1]}")
print(f"    ['einstellungen']['schwierigkeit']['ende'] -> {geladen['einstellungen']['schwierigkeit']['ende']}")
print(f"    ['notiz'] (JSON null)                      -> {geladen['notiz']}")

# ====================================================================
# 5. json.dumps / loads (Strings statt Dateien)
# ====================================================================
print("\n" + "=" * 60, "\n5. dumps / loads (für APIs wichtig!)\n", "=" * 60)

als_text = json.dumps({"stadt": "München", "temp": 23.5}, ensure_ascii=False)
print(f"  dumps -> {als_text}   (Typ: {type(als_text).__name__})")

zurueck = json.loads(als_text)
print(f"  loads -> {zurueck}   (Typ: {type(zurueck).__name__})")
print(f"  Zugriff: {zurueck['temp']} °C in {zurueck['stadt']}")

print("\n  ⚠️ Ohne ensure_ascii=False:")
print(f"    {json.dumps({'stadt': 'München'})}")

# ====================================================================
# 6. CSV -> JSON umwandeln (typische Aufgabe!)
# ====================================================================
print("\n" + "=" * 60, "\n6. 🌍 CSV nach JSON umwandeln\n", "=" * 60)

umgewandelt = ORDNER / "mitarbeiter.json"
with open(umgewandelt, "w", encoding="utf-8") as f:
    json.dump({"stand": "2026-07-26", "mitarbeiter": mitarbeiter},
              f, indent=2, ensure_ascii=False)

print(f"  {csv_datei.name} -> {umgewandelt.name} ✅")
print(f"  {len(mitarbeiter)} Datensätze umgewandelt")
print(f"\n💡 Alle Dateien liegen in: {ORDNER}")
