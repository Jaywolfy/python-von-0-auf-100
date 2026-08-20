"""
Modul 23 - Beispiel: Web-Scraping mit BeautifulSoup

⚠️ Dieses Beispiel arbeitet mit LOKALEM HTML.
   Kein Internet nötig, kein fremder Server wird belastet. 📴
"""

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ BeautifulSoup fehlt. Installieren mit:")
    print("   pip install beautifulsoup4\n")
    raise SystemExit(0)

# ====================================================================
# UNSERE ÜBUNGS-WEBSEITE (lokal, als String)
# ====================================================================
HTML = """
<!DOCTYPE html>
<html lang="de">
<head><title>Buchladen - Angebote</title></head>
<body>
  <h1 id="haupttitel">Unsere Bücher</h1>
  <p class="hinweis">Alle Preise inkl. MwSt.</p>

  <div class="produktliste">
    <div class="produkt" data-id="1">
      <h2 class="titel">Python für Einsteiger</h2>
      <span class="preis">29,99 €</span>
      <span class="bewertung" data-sterne="5">★★★★★</span>
      <span class="verfuegbar">Auf Lager</span>
      <a href="/buch/1">Details</a>
    </div>
    <div class="produkt" data-id="2">
      <h2 class="titel">Automatisierung mit Skripten</h2>
      <span class="preis">34,50 €</span>
      <span class="bewertung" data-sterne="4">★★★★☆</span>
      <span class="verfuegbar">Auf Lager</span>
      <a href="/buch/2">Details</a>
    </div>
    <div class="produkt" data-id="3">
      <h2 class="titel">Datenanalyse leicht gemacht</h2>
      <span class="preis">45,00 €</span>
      <span class="bewertung" data-sterne="3">★★★☆☆</span>
      <span class="verfuegbar">Vergriffen</span>
      <a href="/buch/3">Details</a>
    </div>
    <div class="produkt" data-id="4">
      <h2 class="titel">Reguläre Ausdrücke</h2>
      <span class="preis">19,90 €</span>
      <!-- Achtung: hier fehlt die Bewertung! -->
      <span class="verfuegbar">Auf Lager</span>
      <a href="/buch/4">Details</a>
    </div>
  </div>

  <table id="filialen">
    <tr><th>Stadt</th><th>Adresse</th><th>Bestand</th></tr>
    <tr><td>Berlin</td><td>Hauptstr. 1</td><td>124</td></tr>
    <tr><td>Hamburg</td><td>Elbweg 7</td><td>89</td></tr>
    <tr><td>München</td><td>Isarplatz 3</td><td>203</td></tr>
  </table>

  <ul class="kategorien">
    <li><a href="/kat/programmierung">Programmierung</a></li>
    <li><a href="/kat/daten">Datenanalyse</a></li>
    <li><a href="/kat/web">Webentwicklung</a></li>
  </ul>
</body>
</html>
"""

suppe = BeautifulSoup(HTML, "html.parser")

# ====================================================================
print("=" * 62, "\n1. EINZELNE ELEMENTE FINDEN\n", "=" * 62)

print(f"  Seitentitel:  {suppe.title.get_text(strip=True)}")
print(f"  find('h1'):   {suppe.find('h1').get_text(strip=True)}")
print(f"  select_one:   {suppe.select_one('#haupttitel').get_text(strip=True)}")
print(f"  class-Suche:  {suppe.find('p', class_='hinweis').get_text(strip=True)}")
print("  💡 class_ mit Unterstrich - 'class' ist ein Python-Schlüsselwort!")

# ====================================================================
print("\n" + "=" * 62, "\n2. ALLE ELEMENTE EINER ART\n", "=" * 62)

titel = suppe.find_all("h2", class_="titel")
print(f"  {len(titel)} Buchtitel gefunden:")
for t in titel:
    print(f"    • {t.get_text(strip=True)}")

links = suppe.select("a")
print(f"\n  {len(links)} Links:")
for a in links:
    print(f"    {a.get_text(strip=True):<22} -> {a.get('href', '')}")

# ====================================================================
print("\n" + "=" * 62, "\n3. ⭐ STRUKTURIERT EXTRAHIEREN (robust!)\n", "=" * 62)


def deutsche_zahl(text):
    """Wandelt '29,99 €' in 29.99 um."""
    zahl = text.replace("€", "").strip().replace(".", "").replace(",", ".")
    return float(zahl)


buecher = []
for karte in suppe.select("div.produkt"):
    titel_el = karte.select_one("h2.titel")
    preis_el = karte.select_one("span.preis")

    # 🛡️ IMMER prüfen - Elemente können fehlen!
    if not (titel_el and preis_el):
        print("  ⚠️  Karte übersprungen (Titel oder Preis fehlt)")
        continue

    bewertung_el = karte.select_one("span.bewertung")
    verfuegbar_el = karte.select_one("span.verfuegbar")

    buecher.append({
        "id": karte.get("data-id", "?"),
        "titel": titel_el.get_text(strip=True),
        "preis": deutsche_zahl(preis_el.get_text(strip=True)),
        # .get() mit Standardwert - Buch 4 hat keine Bewertung!
        "sterne": int(bewertung_el.get("data-sterne", 0)) if bewertung_el else None,
        "verfuegbar": verfuegbar_el.get_text(strip=True) if verfuegbar_el else "?",
        "link": karte.select_one("a").get("href", ""),
    })

print(f"\n  {'Titel':<34}{'Preis':>9}{'Sterne':>8}  Status")
print("  " + "-" * 62)
for b in buecher:
    sterne = "★" * b["sterne"] if b["sterne"] else "—"
    symbol = "✅" if b["verfuegbar"] == "Auf Lager" else "❌"
    print(f"  {b['titel']:<34}{b['preis']:>8.2f}€{sterne:>8}  {symbol} {b['verfuegbar']}")

preise = [b["preis"] for b in buecher]
print("  " + "-" * 62)
print(f"  Durchschnittspreis: {sum(preise) / len(preise):.2f} €")
print(f"  Teuerstes Buch:     {max(buecher, key=lambda b: b['preis'])['titel']}")
print(f"  Auf Lager:          {sum(1 for b in buecher if b['verfuegbar'] == 'Auf Lager')}/{len(buecher)}")

print("""
  💡 Buch 4 hat KEINE Bewertung im HTML - und trotzdem stürzt nichts ab.
     Genau darum geht es beim robusten Scraping. 🛡️
""")

# ====================================================================
print("=" * 62, "\n4. TABELLEN AUSLESEN\n", "=" * 62)

tabelle = suppe.select_one("table#filialen")
zeilen = tabelle.select("tr")

kopf = [th.get_text(strip=True) for th in zeilen[0].select("th")]
daten = []
for zeile in zeilen[1:]:
    zellen = [td.get_text(strip=True) for td in zeile.select("td")]
    daten.append(dict(zip(kopf, zellen)))

print(f"  Spalten: {kopf}")
print(f"\n  {'Stadt':<12}{'Adresse':<16}{'Bestand':>9}")
print("  " + "-" * 37)
for d in daten:
    print(f"  {d['Stadt']:<12}{d['Adresse']:<16}{d['Bestand']:>9}")
gesamt = sum(int(d["Bestand"]) for d in daten)
print("  " + "-" * 37)
print(f"  {'GESAMT':<28}{gesamt:>9}")

# ====================================================================
print("\n" + "=" * 62, "\n5. CSS-SELEKTOREN im Überblick\n", "=" * 62)

beispiele = [
    ("h2", "alle h2-Elemente"),
    ("div.produkt", "divs mit class produkt"),
    ("#haupttitel", "Element mit id haupttitel"),
    ("div.produkt > h2", "h2 als direktes Kind von div.produkt"),
    ("ul.kategorien a", "alle a innerhalb von ul.kategorien"),
    ("a[href^='/buch']", "Links, deren href mit /buch beginnt"),
    ("span.bewertung[data-sterne='5']", "5-Sterne-Bewertungen"),
    ("table#filialen td", "alle Tabellenzellen"),
]

for selektor, erklaerung in beispiele:
    anzahl = len(suppe.select(selektor))
    print(f"  {selektor:<34}{anzahl:>3} Treffer   {erklaerung}")

# ====================================================================
print("\n" + "=" * 62, "\n6. ⚖️ ETIKETTE\n", "=" * 62)
print("""
  So sähe ein ECHTER Abruf aus:

      import requests, time
      from bs4 import BeautifulSoup

      kopfzeilen = {"User-Agent": "Lernprojekt/1.0 (Kontakt: mail@example.de)"}

      for seite in range(1, 4):
          antwort = requests.get(f"{basis}/page-{seite}.html",
                                 headers=kopfzeilen, timeout=10)
          antwort.raise_for_status()
          suppe = BeautifulSoup(antwort.text, "html.parser")
          ...
          time.sleep(1.5)          # 🤝 PFLICHT

  Zum Üben ausdrücklich erlaubt:
      📚 https://books.toscrape.com/
      💬 https://quotes.toscrape.com/
""")
