"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 16 · MUSTERLÖSUNGEN — CSV & JSON                          ║
╚══════════════════════════════════════════════════════════════════╝
"""
import csv
import json
from pathlib import Path

LOES = Path(__file__).parent / "_loesung16"
LOES.mkdir(exist_ok=True)

(LOES / "verkaeufe.csv").write_text(
    "datum;produkt;kategorie;menge;einzelpreis\n"
    "2026-01-15;Laptop;Technik;2;899,99\n"
    "2026-01-18;Maus;Technik;10;25,50\n"
    "2026-02-03;Schreibtisch;Möbel;1;349,00\n"
    "2026-02-14;Tastatur;Technik;5;79,00\n"
    "2026-02-28;Bürostuhl;Möbel;3;259,90\n"
    "2026-03-05;Monitor;Technik;4;219,00\n"
    "2026-03-22;Regal;Möbel;2;129,50\n",
    encoding="utf-8")

(LOES / "einstellungen.json").write_text(
    '{"app":"Lagerverwaltung","version":"2.1",'
    '"besitzer":{"name":"Anna","rolle":"Admin"},'
    '"lager":[{"ort":"Halle A","kapazitaet":5000,"belegt":3200},'
    '{"ort":"Halle B","kapazitaet":3000,"belegt":2950}],'
    '"benachrichtigungen":{"email":true,"sms":false}}',
    encoding="utf-8")


print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

with open(LOES / "verkaeufe.csv", encoding="utf-8", newline="") as f:
    for zeile in csv.DictReader(f, delimiter=";"):
        print(f"  {zeile['datum']}  {zeile['produkt']:<14}{zeile['kategorie']:<10}"
              f"{zeile['menge']:>3} x {zeile['einzelpreis']:>9}")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)


def deutsche_zahl(text):
    """Wandelt einen deutsch formatierten Zahlentext in float um."""
    return float(text.strip().replace(".", "").replace(",", "."))


for t in ("899,99", "1.234,56", "25,50", "10"):
    print(f"  deutsche_zahl({t!r:<12}) = {deutsche_zahl(t)}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟡\n", "=" * 60)

verkaeufe = []
with open(LOES / "verkaeufe.csv", encoding="utf-8", newline="") as f:
    for z in csv.DictReader(f, delimiter=";"):
        menge = int(z["menge"])
        preis = deutsche_zahl(z["einzelpreis"])
        verkaeufe.append({
            "datum": z["datum"],
            "produkt": z["produkt"],
            "kategorie": z["kategorie"],
            "menge": menge,
            "einzelpreis": preis,
            "umsatz": round(menge * preis, 2),
        })

gesamt = sum(v["umsatz"] for v in verkaeufe)
print(f"  a) Gesamtumsatz:  {gesamt:,.2f} €")

pro_kategorie = {}
for v in verkaeufe:
    pro_kategorie[v["kategorie"]] = pro_kategorie.get(v["kategorie"], 0) + v["umsatz"]
print("  b) Pro Kategorie:")
for kat, umsatz in sorted(pro_kategorie.items(), key=lambda p: -p[1]):
    anteil = umsatz / gesamt
    print(f"       {kat:<10}{umsatz:>10,.2f} €  {'█' * int(anteil * 25)} {anteil:.0%}")

bestseller = max(verkaeufe, key=lambda v: v["menge"])
teuerstes = max(verkaeufe, key=lambda v: v["einzelpreis"])
print(f"  c) Bestseller:    {bestseller['produkt']} ({bestseller['menge']} Stück)")
print(f"  d) Teuerstes:     {teuerstes['produkt']} ({teuerstes['einzelpreis']:,.2f} €)")
print(f"  e) Stückzahl:     {sum(v['menge'] for v in verkaeufe)}")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)

zusammenfassung = {}
for v in verkaeufe:
    k = v["kategorie"]
    eintrag = zusammenfassung.setdefault(k, {"anzahl": 0, "stueck": 0, "umsatz": 0.0})
    eintrag["anzahl"] += 1
    eintrag["stueck"] += v["menge"]
    eintrag["umsatz"] += v["umsatz"]

ziel = LOES / "umsatz_pro_kategorie.csv"
with open(ziel, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["kategorie", "anzahl_verkaeufe",
                                      "stueckzahl", "umsatz"], delimiter=";")
    w.writeheader()
    for kat, d in sorted(zusammenfassung.items(), key=lambda p: -p[1]["umsatz"]):
        w.writerow({"kategorie": kat, "anzahl_verkaeufe": d["anzahl"],
                    "stueckzahl": d["stueck"], "umsatz": f"{d['umsatz']:.2f}"})

for zeile in ziel.read_text(encoding="utf-8").splitlines():
    print(f"  {zeile}")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

with open(LOES / "einstellungen.json", encoding="utf-8") as f:
    konfig = json.load(f)

print(f"  a) App:        {konfig['app']}")
print(f"  b) Besitzer:   {konfig['besitzer']['name']} ({konfig['besitzer']['rolle']})")
print(f"  c) Lagerorte:  {[l['ort'] for l in konfig['lager']]}")
print("  d) Auslastung:")
for lager in konfig["lager"]:
    quote = lager["belegt"] / lager["kapazitaet"]
    warnung = " ⚠️ fast voll!" if quote > 0.9 else ""
    print(f"       {lager['ort']:<10}{quote:>6.1%}  "
          f"{'█' * int(quote * 20):<20}{warnung}")
print(f"  e) E-Mail aktiv: {konfig['benachrichtigungen']['email']}")


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)

konfig["lager"].append({"ort": "Halle C", "kapazitaet": 4000, "belegt": 100})
konfig["benachrichtigungen"]["sms"] = True
konfig["version"] = "2.2"

neu = LOES / "einstellungen_neu.json"
with open(neu, "w", encoding="utf-8") as f:
    json.dump(konfig, f, indent=2, ensure_ascii=False)

with open(neu, encoding="utf-8") as f:
    kontrolle = json.load(f)

print(f"  Version:      {kontrolle['version']}")
print(f"  Lager:        {len(kontrolle['lager'])} ({[l['ort'] for l in kontrolle['lager']]})")
print(f"  SMS aktiv:    {kontrolle['benachrichtigungen']['sms']}")


print("\n" + "=" * 60, "\nAUFGABE 7 🔴\n", "=" * 60)

nach_kategorie = {}
for v in verkaeufe:
    nach_kategorie.setdefault(v["kategorie"], []).append(v)

ausgabe = {
    "erstellt": "2026-07-26",
    "anzahl_datensaetze": len(verkaeufe),
    "gesamtumsatz": round(gesamt, 2),
    "nach_kategorie": nach_kategorie,
}

ziel_json = LOES / "verkaeufe.json"
with open(ziel_json, "w", encoding="utf-8") as f:
    json.dump(ausgabe, f, indent=2, ensure_ascii=False)

print(f"  ✅ {ziel_json.name} geschrieben")
print("  Auszug:")
for zeile in ziel_json.read_text(encoding="utf-8").splitlines()[:12]:
    print(f"    {zeile}")
print("    ...")


print("\n" + "=" * 60, "\nAUFGABE 8 ⭐\n", "=" * 60)

kaputt = LOES / "kaputt.csv"
kaputt.write_text(
    "datum;produkt;kategorie;menge;einzelpreis\n"
    "2026-01-15;Laptop;Technik;2;899,99\n"
    "2026-01-16;Maus;Technik;;25,50\n"
    "\n"
    "2026-01-17;Kabel;Technik;abc;9,99\n"
    "2026-01-18;Monitor;Technik;3;\n"
    "2026-01-19;Tastatur;Technik;5;79,00\n",
    encoding="utf-8")


def lade_verkaeufe(pfad):
    """Lädt Verkaufsdaten robust - fehlerhafte Zeilen werden gemeldet."""
    gueltig, fehler = [], []

    with open(pfad, encoding="utf-8", newline="") as f:
        for nr, zeile in enumerate(csv.DictReader(f, delimiter=";"), start=2):
            if not any(zeile.values()):
                fehler.append((nr, "leere Zeile"))
                continue
            try:
                menge = int(zeile["menge"])
                preis = deutsche_zahl(zeile["einzelpreis"])
            except (ValueError, TypeError, AttributeError) as f_:
                fehler.append((nr, f"{zeile.get('produkt', '?')}: {f_}"))
                continue

            gueltig.append({**zeile, "menge": menge, "einzelpreis": preis,
                            "umsatz": round(menge * preis, 2)})

    return {"daten": gueltig, "fehler": fehler,
            "quote": len(gueltig) / (len(gueltig) + len(fehler)) if (gueltig or fehler) else 0}


ergebnis = lade_verkaeufe(kaputt)
print(f"  ✅ {len(ergebnis['daten'])} Zeilen geladen "
      f"({ergebnis['quote']:.0%} Erfolgsquote)")
print(f"  ⚠️  {len(ergebnis['fehler'])} Probleme:")
for nr, grund in ergebnis["fehler"]:
    print(f"       Zeile {nr}: {grund}")

print(f"\n💡 Dateien in: {LOES}")
print("🎉 Modul 16 geschafft!")
