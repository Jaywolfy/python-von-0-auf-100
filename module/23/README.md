# 🕷️ Modul 23 — Web-Scraping

> ⏱️ ~4 Stunden · ⬅️ [Modul 22](../22/README.md) · ➡️ [Modul 24](../24/README.md)

---

## 🎯 Lernziele

- [ ] HTML-Struktur verstehen
- [ ] mit BeautifulSoup Elemente finden und auslesen
- [ ] CSS-Selektoren benutzen
- [ ] Tabellen und Listen extrahieren
- [ ] **rechtliche und ethische Grenzen** kennen ⚖️

---

## ⚖️ ZUERST: Die Regeln

> 🚨 **Bevor du irgendetwas scrapest, lies diesen Abschnitt. Wirklich.**

```text
1. 📄 Gibt es eine API?     → dann IMMER die API nutzen, nie scrapen
2. 🤖 robots.txt lesen      → beispiel.de/robots.txt
3. 📜 Nutzungsbedingungen   → viele Seiten verbieten Scraping explizit
4. 🐌 Langsam anfragen      → time.sleep(1-2) zwischen Seiten, Pflicht!
5. 🏷️ User-Agent setzen     → sag ehrlich, wer du bist
6. 🔒 Keine Logins umgehen  → keine Paywalls, keine geschützten Bereiche
7. 👤 Keine personenbezogenen Daten sammeln (DSGVO!)
8. 💾 Ergebnisse cachen     → nicht 100× dieselbe Seite laden
```

**Faustregel:** Wenn du dich fragst, ob es okay ist — frag den Betreiber. Oder lass es. 😊

Zum **Üben** gibt es ausdrücklich dafür gedachte Seiten:
- 📚 [books.toscrape.com](https://books.toscrape.com/)
- 💬 [quotes.toscrape.com](https://quotes.toscrape.com/)

---

## 📖 Die Lektion

### 1. HTML in 2 Minuten

```html
<div class="produkt" id="p1">
    <h2 class="titel">Laptop</h2>
    <span class="preis">899,99 €</span>
    <a href="/details/1">Mehr</a>
</div>
```

```text
<div class="produkt">     ← Tag mit Attribut class
    ▲
    │
  Elemente können ineinander verschachtelt sein.
  class = Gruppe (mehrfach), id = eindeutig (einmalig)
```

💡 **So findest du die richtigen Selektoren:** Im Browser Rechtsklick auf das Element → *„Untersuchen"* → du siehst das HTML. Genau darauf zielst du dann. 🔍

### 2. Installation & Grundgerüst

```bash
pip install requests beautifulsoup4
```

```python
import requests
from bs4 import BeautifulSoup

antwort = requests.get(url, timeout=10,
                       headers={"User-Agent": "Lernprojekt/1.0"})
antwort.raise_for_status()

suppe = BeautifulSoup(antwort.text, "html.parser")
```

### 3. Elemente finden

```python
suppe.find("h1")                          # erstes h1 → Element oder None
suppe.find_all("a")                       # alle a → Liste
suppe.find("div", class_="produkt")       # ⚠️ class_ mit Unterstrich!
suppe.find(id="haupt")
suppe.find_all("p", limit=5)
```

⭐ **CSS-Selektoren** (meist am bequemsten):

```python
suppe.select("div.produkt")               # alle divs mit class produkt
suppe.select_one("#haupt")                # das Element mit id haupt
suppe.select("div.produkt > h2.titel")    # direktes Kind
suppe.select("a[href^='/details']")       # href beginnt mit …
suppe.select("table tr td")               # verschachtelt
```

### 4. Inhalte auslesen

```python
element.text                  # Text inkl. Kindelementen
element.get_text(strip=True)  # ⭐ ohne Leerraum drumherum
element["href"]               # Attribut → KeyError wenn fehlt
element.get("href", "")       # ✅ sicher
element.name                  # Tagname
```

### 5. 🌍 Ein vollständiges Beispiel

```python
produkte = []
for karte in suppe.select("div.produkt"):
    titel_el = karte.select_one("h2.titel")
    preis_el = karte.select_one("span.preis")
    if not (titel_el and preis_el):        # 🛡️ IMMER prüfen!
        continue
    produkte.append({
        "titel": titel_el.get_text(strip=True),
        "preis": preis_el.get_text(strip=True),
        "link": karte.select_one("a").get("href", ""),
    })
```

> 🧠 **Tutor sagt:** Der wichtigste Unterschied zwischen Anfänger- und Profi-Scraping: Profis nehmen an, dass **jedes** Element fehlen kann. Webseiten ändern sich ständig. Prüf immer auf `None`, bevor du zugreifst. 🛡️

### 6. Mehrere Seiten — mit Pause 🐌

```python
import time

alle = []
for seite in range(1, 6):
    antwort = requests.get(f"{basis}/seite-{seite}.html", timeout=10)
    if antwort.status_code != 200:
        break
    alle.extend(extrahiere(antwort.text))
    time.sleep(1.5)          # 🤝 PFLICHT, kein Vorschlag
```

### 7. ⚠️ Wenn Scraping nicht funktioniert

| Symptom | Ursache | Lösung |
|---|---|---|
| Seite ist leer | Inhalt kommt per JavaScript | Playwright/Selenium — oder nach einer API suchen |
| `403 Forbidden` | Bot erkannt | User-Agent setzen; ansonsten: respektieren |
| Zufällige Fehler | Seitenstruktur geändert | Selektoren anpassen, Prüfungen einbauen |
| `429` | zu schnell | längere Pausen |

💡 **Trick:** Öffne im Browser die Netzwerk-Analyse (F12 → Network). Oft lädt die Seite ihre Daten selbst über eine **JSON-API** — die kannst du dann direkt und viel einfacher abfragen. 🎯

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — arbeitet mit **lokalem HTML**, also ohne Internet und ohne fremde Server zu belasten. 📴

---

## 🛠️ Mini-Projekt: Bücher-Scraper 📚

Scrape [books.toscrape.com](https://books.toscrape.com/) (ausdrücklich zum Üben gemacht):

- Titel, Preis, Bewertung, Verfügbarkeit von mindestens 3 Seiten
- `time.sleep(1.5)` zwischen den Seiten
- Ergebnis als CSV **und** JSON speichern (Modul 16)
- Auswertung: Durchschnittspreis, teuerstes Buch, Verteilung der Bewertungen
- Alles in Funktionen + `main()` (Modul 08) und mit Fehlerbehandlung (Modul 13)

---

## 🧠 Selbsttest

1. Was prüfst du, **bevor** du eine Seite scrapest?
2. Wo steht `robots.txt`?
3. Warum `class_` statt `class`?
4. Unterschied `find` / `find_all` / `select`?
5. Was macht `get_text(strip=True)`?
6. Warum `element.get("href")` statt `element["href"]`?
7. Warum `time.sleep()`?
8. Was tun, wenn die Seite per JavaScript lädt?
9. Warum ist eine API besser als Scraping?
10. ✍️ Nenne drei Regeln der Scraping-Etikette.

<details>
<summary>💡 Antworten</summary>

1. Ob es eine API gibt, was `robots.txt` und die Nutzungsbedingungen sagen.
2. Unter `https://domain.de/robots.txt`
3. `class` ist ein reserviertes Python-Schlüsselwort.
4. `find` = erstes Element · `find_all` = alle · `select` = CSS-Selektoren (meist bequemer).
5. Gibt den Text ohne umgebenden Leerraum zurück.
6. `.get()` stürzt nicht ab, wenn das Attribut fehlt.
7. Um den Server nicht zu überlasten und nicht gesperrt zu werden.
8. Playwright/Selenium nutzen — oder besser: nach der zugrunde liegenden JSON-API suchen.
9. Sie ist stabil, erlaubt, schneller und liefert saubere Daten.
10. Langsam anfragen · ehrlicher User-Agent · robots.txt und AGB respektieren.
</details>

---

## 🔄 Wiederholung (Modul 20–22)

1. Was macht `raise_for_status()`?
2. Warum `r"..."` bei Regex?
3. Wo gehören API-Keys hin?
4. Was gehört in `.gitignore`?

---

## 🔗 Vertiefung

- 📖 [BeautifulSoup-Doku](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- 📖 [Automate the Boring Stuff — Kap. 12](https://automatetheboringstuff.com/2e/chapter12/)

**➡️ [Modul 24 — Excel automatisieren](../24/README.md)** 📊
