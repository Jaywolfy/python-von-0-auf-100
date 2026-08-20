"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 23 · MUSTERLÖSUNGEN — Web-Scraping                        ║
╚══════════════════════════════════════════════════════════════════╝
"""
import csv
import json
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ pip install beautifulsoup4")
    raise SystemExit(0)

# Dasselbe HTML wie in der Aufgabendatei
HTML = (Path(__file__).parent.parent / "aufgaben" / "aufgaben.py").read_text(
    encoding="utf-8").split('HTML = """')[1].split('"""')[0]

suppe = BeautifulSoup(HTML, "html.parser")

print("=" * 62, "\nAUFGABE 1 🟢\n", "=" * 62)

print(f"  Überschrift:  {suppe.find('h1').get_text(strip=True)}")
wohnungen = suppe.select("article.wohnung")
print(f"  Anzahl:       {len(wohnungen)}")
print("  Titel:")
for w in wohnungen:
    print(f"    • {w.select_one('h2.titel').get_text(strip=True)}")


print("\n" + "=" * 62, "\nAUFGABE 2 🟢\n", "=" * 62)

for w in wohnungen:
    link = w.select_one("a")
    print(f"  {w.get('data-id', '?'):<5} -> {link.get('href', 'kein Link')}")


print("\n" + "=" * 62, "\nAUFGABE 3 🟡\n", "=" * 62)


def deutsche_zahl(text):
    """'1.450,00 €' -> 1450.0"""
    return float(text.replace("€", "").strip().replace(".", "").replace(",", "."))


def text_von(element, standard=""):
    """Gibt den Text eines Elements zurück - oder den Standardwert."""
    return element.get_text(strip=True) if element else standard


daten = []
for w in wohnungen:
    miete_el = w.select_one("span.miete")
    flaeche_el = w.select_one("span.flaeche")

    daten.append({
        "id": w.get("data-id", "?"),
        "titel": text_von(w.select_one("h2.titel"), "ohne Titel"),
        "ort": text_von(w.select_one("span.ort"), "unbekannt"),
        "flaeche": int(text_von(flaeche_el, "0").replace("m²", "").strip()),
        "zimmer": int(text_von(w.select_one("span.zimmer"), "0")),
        "miete": deutsche_zahl(text_von(miete_el, "0,00")),
        "etage": text_von(w.select_one("span.etage"), "unbekannt"),   # ⭐ w3!
        "merkmale": [li.get_text(strip=True) for li in w.select("ul.merkmale li")],
    })

print(f"  {'Titel':<32}{'Ort':<20}{'m²':>5}{'Zi':>4}{'Miete':>11}  Etage")
print("  " + "-" * 80)
for d in daten:
    print(f"  {d['titel'][:30]:<32}{d['ort']:<20}{d['flaeche']:>5}{d['zimmer']:>4}"
          f"{d['miete']:>10.2f}€  {d['etage']}")
print("\n  💡 Wohnung w3 hat keine Etage im HTML - dank Standardwert kein Absturz ✅")


print("\n" + "=" * 62, "\nAUFGABE 4 🟡\n", "=" * 62)

mieten = [d["miete"] for d in daten]
print(f"  a) Ø Miete:        {sum(mieten) / len(mieten):,.2f} €")

print("  b) Miete pro m²:")
mit_qm = sorted(daten, key=lambda d: d["miete"] / d["flaeche"])
for d in mit_qm:
    pro_qm = d["miete"] / d["flaeche"]
    print(f"       {d['ort']:<22}{pro_qm:>7.2f} €/m²  {'█' * int(pro_qm)}")

teuerste = max(daten, key=lambda d: d["miete"])
guenstigste = min(daten, key=lambda d: d["miete"])
print(f"  c) Teuerste:       {teuerste['titel']} ({teuerste['miete']:,.2f} €)")
print(f"     Günstigste:     {guenstigste['titel']} ({guenstigste['miete']:,.2f} €)")

berlin = [d["titel"] for d in daten if d["ort"].startswith("Berlin")]
print(f"  d) In Berlin:      {berlin}")

mit_aufzug = [d["titel"] for d in daten if "Aufzug" in d["merkmale"]]
print(f"  e) Mit Aufzug:     {mit_aufzug}")

alle_merkmale = sorted({m for d in daten for m in d["merkmale"]})
print(f"  f) Alle Merkmale:  {alle_merkmale}")


print("\n" + "=" * 62, "\nAUFGABE 5 🟡\n", "=" * 62)

tabelle = suppe.select_one("table#statistik")
zeilen = tabelle.select("tr")
kopf = [th.get_text(strip=True) for th in zeilen[0].select("th")]

statistik = []
for zeile in zeilen[1:]:
    zellen = [td.get_text(strip=True) for td in zeile.select("td")]
    statistik.append(dict(zip(kopf, zellen)))

for s in statistik:
    print(f"  {s['Stadt']:<12}{s['Angebote']:>8} Angebote   Ø {s['Ø Miete']}")
gesamt = sum(int(s["Angebote"]) for s in statistik)
print(f"  {'GESAMT':<12}{gesamt:>8} Angebote")


print("\n" + "=" * 62, "\nAUFGABE 6 🔴 - Nur CSS-Selektoren\n", "=" * 62)

a = [w.select_one("h2.titel").get_text(strip=True)
     for w in suppe.select("article.wohnung")
     if suppe and w.select_one("span.ort").get_text(strip=True).startswith("Berlin")]
print(f"  a) Berlin:          {a}")
angebot_links = [x.get("href") for x in suppe.select('a[href^="/angebot"]')]
print(f"  b) /angebot-Links:  {angebot_links}")
print(f"  c) Dritte Wohnung:  {suppe.select('article.wohnung')[2].select_one('h2').get_text(strip=True)}")
print(f"  d) Merkmale gesamt: {len(suppe.select('article.wohnung ul.merkmale li'))}")
w2 = suppe.select_one('article.wohnung[data-id="w2"]')
print(f"  e) w2:              {w2.select_one('h2').get_text(strip=True)}")


print("\n" + "=" * 62, "\nAUFGABE 7 🔴\n", "=" * 62)


def extrahiere_wohnung(artikel):
    """Extrahiert eine Wohnung robust - jedes Feld darf fehlen.

    Args:
        artikel: Ein BeautifulSoup-Element (article.wohnung).

    Returns:
        Ein Dictionary mit allen Feldern und sinnvollen Standardwerten.
    """
    def zahl(selektor, standard=0.0, entferne=""):
        el = artikel.select_one(selektor)
        if el is None:
            return standard
        text = el.get_text(strip=True).replace(entferne, "")
        try:
            return deutsche_zahl(text) if "," in text else float(text.strip() or 0)
        except ValueError:
            return standard

    link = artikel.select_one("a")

    return {
        "id": artikel.get("data-id", "unbekannt"),
        "titel": text_von(artikel.select_one("h2.titel"), "ohne Titel"),
        "ort": text_von(artikel.select_one("span.ort"), "unbekannt"),
        "flaeche": zahl("span.flaeche", 0.0, "m²"),
        "zimmer": zahl("span.zimmer", 0.0),
        "miete": zahl("span.miete", 0.0, "€"),
        "etage": text_von(artikel.select_one("span.etage"), "unbekannt"),
        "merkmale": [li.get_text(strip=True) for li in artikel.select("ul.merkmale li")],
        "link": link.get("href", "") if link else "",
    }


KAPUTT = """<article class="wohnung"><h2 class="titel">Nur ein Titel</h2>
<span class="miete">keine zahl</span></article>"""
kaputte_suppe = BeautifulSoup(KAPUTT, "html.parser")
ergebnis = extrahiere_wohnung(kaputte_suppe.select_one("article"))

print("  Kaputtes HTML (fast alle Felder fehlen):")
for schluessel, wert in ergebnis.items():
    print(f"    {schluessel:<12} {wert!r}")
print("\n  ✅ Kein Absturz - genau so muss ein Scraper gebaut sein. 🛡️")


print("\n" + "=" * 62, "\nAUFGABE 8 ⭐\n", "=" * 62)

AUSGABE = Path(__file__).parent / "_export23"
AUSGABE.mkdir(exist_ok=True)

# CSV
csv_datei = AUSGABE / "wohnungen.csv"
with open(csv_datei, "w", encoding="utf-8", newline="") as f:
    felder = ["id", "titel", "ort", "flaeche", "zimmer", "miete", "etage"]
    schreiber = csv.DictWriter(f, fieldnames=felder, delimiter=";")
    schreiber.writeheader()
    for d in daten:
        schreiber.writerow({k: d[k] for k in felder})

# JSON
json_datei = AUSGABE / "wohnungen.json"
with open(json_datei, "w", encoding="utf-8") as f:
    json.dump({"anzahl": len(daten), "wohnungen": daten}, f,
              indent=2, ensure_ascii=False)

# Bericht
bericht = AUSGABE / "bericht.txt"
zeilen_bericht = ["WOHNUNGSBERICHT", "=" * 50, ""]
hoechste = max(mieten)
for d in sorted(daten, key=lambda d: -d["miete"]):
    balken = "█" * int(d["miete"] / hoechste * 30)
    zeilen_bericht.append(f"{d['ort']:<22}{d['miete']:>10,.2f} €  {balken}")
zeilen_bericht += ["", "-" * 50,
                   f"Durchschnitt: {sum(mieten) / len(mieten):,.2f} €",
                   f"Anzahl:       {len(daten)}"]
bericht.write_text("\n".join(zeilen_bericht), encoding="utf-8")

print(f"  ✅ {csv_datei.name}   ({csv_datei.stat().st_size} Bytes)")
print(f"  ✅ {json_datei.name}  ({json_datei.stat().st_size} Bytes)")
print(f"  ✅ {bericht.name}\n")
print(bericht.read_text(encoding="utf-8"))

print("\n🎉 Modul 23 geschafft! Aber denk an die Etikette. ⚖️")
