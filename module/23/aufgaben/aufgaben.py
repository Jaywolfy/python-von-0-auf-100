"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 23 · AUFGABEN — Web-Scraping                              ║
║  Arbeitet mit lokalem HTML - kein Internet nötig. 📴              ║
╚══════════════════════════════════════════════════════════════════╝
"""

HTML = """
<html><body>
<h1>Immobilienangebote</h1>

<div class="angebote">
  <article class="wohnung" data-id="w1">
    <h2 class="titel">3-Zimmer-Wohnung mit Balkon</h2>
    <span class="ort">Berlin-Mitte</span>
    <span class="flaeche">78 m²</span>
    <span class="zimmer">3</span>
    <span class="miete">1.450,00 €</span>
    <span class="etage">4. OG</span>
    <ul class="merkmale">
      <li>Balkon</li><li>Aufzug</li><li>Einbauküche</li>
    </ul>
    <a href="/angebot/w1">Details</a>
  </article>

  <article class="wohnung" data-id="w2">
    <h2 class="titel">Gemütliche Altbauwohnung</h2>
    <span class="ort">Hamburg-Altona</span>
    <span class="flaeche">62 m²</span>
    <span class="zimmer">2</span>
    <span class="miete">980,50 €</span>
    <span class="etage">2. OG</span>
    <ul class="merkmale"><li>Altbau</li><li>Parkett</li></ul>
    <a href="/angebot/w2">Details</a>
  </article>

  <article class="wohnung" data-id="w3">
    <h2 class="titel">Loft im Szeneviertel</h2>
    <span class="ort">Berlin-Kreuzberg</span>
    <span class="flaeche">115 m²</span>
    <span class="zimmer">4</span>
    <span class="miete">2.200,00 €</span>
    <!-- Etage fehlt absichtlich! -->
    <ul class="merkmale"><li>Dachterrasse</li><li>Loft</li><li>Aufzug</li><li>Stellplatz</li></ul>
    <a href="/angebot/w3">Details</a>
  </article>

  <article class="wohnung" data-id="w4">
    <h2 class="titel">Kleines Studio</h2>
    <span class="ort">München-Schwabing</span>
    <span class="flaeche">34 m²</span>
    <span class="zimmer">1</span>
    <span class="miete">890,00 €</span>
    <span class="etage">EG</span>
    <ul class="merkmale"><li>Möbliert</li></ul>
    <a href="/angebot/w4">Details</a>
  </article>
</div>

<table id="statistik">
  <tr><th>Stadt</th><th>Angebote</th><th>Ø Miete</th></tr>
  <tr><td>Berlin</td><td>1247</td><td>1.320 €</td></tr>
  <tr><td>Hamburg</td><td>892</td><td>1.150 €</td></tr>
  <tr><td>München</td><td>1560</td><td>1.780 €</td></tr>
</table>
</body></html>
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Grundlagen
# ══════════════════════════════════════════════════════════════════
# a) Erstelle die "Suppe" mit BeautifulSoup
# b) Gib die h1-Überschrift aus
# c) Gib aus, wie viele Wohnungen es gibt
# d) Gib alle Wohnungstitel aus

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Attribute lesen
# ══════════════════════════════════════════════════════════════════
# Gib für jede Wohnung aus: data-id und den Link (href)

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Strukturiert extrahieren
# ══════════════════════════════════════════════════════════════════
# Baue eine Liste von Dictionaries mit:
#   id, titel, ort, flaeche (int), zimmer (int), miete (float),
#   etage (str oder "unbekannt"!), merkmale (Liste)
# ⚠️ Wohnung w3 hat KEINE Etage - dein Code darf nicht abstürzen!
# Gib eine formatierte Tabelle aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Auswerten
# ══════════════════════════════════════════════════════════════════
# Berechne und gib aus:
#   a) Durchschnittsmiete
#   b) Miete pro m² für jede Wohnung (sortiert)
#   c) Teuerste und günstigste Wohnung
#   d) Alle Wohnungen in Berlin
#   e) Alle Wohnungen mit Aufzug
#   f) Welche Merkmale kommen insgesamt vor? (ohne Duplikate)

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Tabelle auslesen
# ══════════════════════════════════════════════════════════════════
# Lies die Tabelle #statistik aus und gib sie als
# Liste von Dictionaries aus. Berechne die Gesamtzahl der Angebote.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🔴 - CSS-Selektoren
# ══════════════════════════════════════════════════════════════════
# Löse NUR mit select()/select_one() - kein find():
#   a) Alle Wohnungen in Berlin (Tipp: erst alle, dann filtern)
#   b) Alle Links, die mit /angebot beginnen
#   c) Die dritte Wohnung
#   d) Alle Merkmal-Einträge (li) aller Wohnungen
#   e) Die Wohnung mit data-id="w2"

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - Robuster Extraktor
# ══════════════════════════════════════════════════════════════════
# Schreib extrahiere_wohnung(artikel), die aus einem einzelnen
# Article-Element ein Dictionary macht und dabei:
#   - JEDES Feld auf None prüft
#   - fehlende Felder mit sinnvollen Standardwerten füllt
#   - bei kaputten Zahlen nicht abstürzt
# Teste sie mit kaputtem HTML (lösch absichtlich Felder!).

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 ⭐ BONUS - Export
# ══════════════════════════════════════════════════════════════════
# Speichere die extrahierten Wohnungen als CSV UND als JSON
# (Modul 16!). Erzeuge zusätzlich einen Textbericht mit
# Statistiken und Balkendiagramm der Mieten.

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
