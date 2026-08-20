# 🏦 Projekt 4 — Kontoauszug-Analyse

> 📍 **Nach Modul 16** · ⏱️ ~5 Stunden · 🎯 Echte Daten auswerten

---

## 🎬 So soll es aussehen

```text
╔════════════════════════════════════════════════════════╗
║          🏦  KONTOAUSZUG-ANALYSE  2026                  ║
╚════════════════════════════════════════════════════════╝

📄 Datei:     kontoauszug_2026.csv
📊 Buchungen: 142  (01.01.2026 – 30.06.2026)
⚠️  3 Zeilen übersprungen (fehlerhaft)

── ÜBERBLICK ────────────────────────────────────────────
  Einnahmen                                  17.100,00 €
  Ausgaben                                   14.238,67 €
  ──────────────────────────────────────────────────────
  SALDO                                       2.861,33 €  🟢

── AUSGABEN NACH KATEGORIE ──────────────────────────────
  🏠 Wohnen         5.100,00 €  ████████████████  36 %
  🛒 Lebensmittel   2.847,30 €  █████████         20 %
  🚗 Mobilität      1.923,45 €  ██████            14 %
  🎬 Freizeit       1.402,10 €  ████              10 %
  📱 Abos             894,00 €  ███                6 %
  ❓ Sonstiges      2.071,82 €  ██████            15 %

── MONATSVERLAUF ────────────────────────────────────────
  Januar    +512,40 €  ████████
  Februar   -204,15 €  ███▏
  März      +892,10 €  ██████████████
  ...

── AUFFÄLLIGKEITEN ──────────────────────────────────────
  🔴 Größte Ausgabe:   Miete Q2 (2.550,00 €) am 01.04.
  🔁 Wiederkehrend:    12 Abos/Daueraufträge erkannt
  ⚠️  Ungewöhnlich:     3 Buchungen > 3× Monatsdurchschnitt
  💸 Abos gesamt:      894,00 € (149,00 €/Monat)

✅ Bericht geschrieben: analyse_2026.xlsx + bericht.txt
```

---

## ✅ Pflichtanforderungen

- [ ] CSV mit `csv.DictReader` einlesen (Semikolon, deutsches Zahlenformat!)
- [ ] Beträge korrekt umwandeln (`1.234,56` → `1234.56`)
- [ ] Datumsangaben mit `datetime` verarbeiten
- [ ] Automatische Kategorisierung über Stichwörter
- [ ] Einnahmen/Ausgaben trennen, Saldo berechnen
- [ ] Auswertung nach Kategorie **und** nach Monat
- [ ] **Fehlerhafte Zeilen überspringen** und melden — nie abstürzen
- [ ] Ergebnis als JSON **und** als Textbericht speichern

## 🎁 Bonus

- [ ] Wiederkehrende Buchungen erkennen (gleicher Empfänger + ähnlicher Betrag)
- [ ] Ausreißer finden (> 3× Durchschnitt)
- [ ] Monatsvergleich mit Trendpfeilen ↗️↘️
- [ ] Excel-Export mit Diagramm (nach Modul 24)
- [ ] Kategorien-Regeln aus JSON-Datei laden
- [ ] Sparquote und Hochrechnung aufs Jahr

---

## 📄 Die Testdaten

Die Musterlösung erzeugt sich eine realistische CSV-Datei selbst:

```csv
Datum;Empfänger;Verwendungszweck;Betrag;Währung
05.01.2026;REWE Markt GmbH;Kartenzahlung;-87,45;EUR
01.01.2026;Muster GmbH;Gehalt Januar;2.850,00;EUR
03.01.2026;Hausverwaltung Meier;Miete Januar;-850,00;EUR
```

⚠️ **Typische Tücken echter Bankdaten:**
- Semikolon statt Komma als Trennzeichen
- Komma als Dezimaltrenner, Punkt als Tausendertrenner
- Datum als `TT.MM.JJJJ`
- Leere Felder, Zeilen mit falscher Spaltenzahl
- Encoding manchmal `cp1252` statt UTF-8

---

## 🗂️ Kategorisierung — der Kern

```python
KATEGORIEN = {
    "Wohnen":       ["miete", "hausverwaltung", "stadtwerke", "strom", "gas"],
    "Lebensmittel": ["rewe", "edeka", "aldi", "lidl", "penny", "bäckerei"],
    "Mobilität":    ["tankstelle", "shell", "aral", "bahn", "bvg", "hvv"],
    "Freizeit":     ["kino", "restaurant", "bar", "fitness", "sport"],
    "Abos":         ["netflix", "spotify", "amazon prime", "abo"],
    "Gesundheit":   ["apotheke", "arzt", "krankenkasse"],
}

def kategorisiere(buchung):
    """Ordnet einer Buchung anhand von Stichwörtern eine Kategorie zu."""
    text = f"{buchung['empfaenger']} {buchung['zweck']}".lower()
    for kategorie, stichwoerter in KATEGORIEN.items():
        if any(wort in text for wort in stichwoerter):
            return kategorie
    return "Sonstiges"
```

💡 So funktionieren echte Finanz-Apps im Kern auch — nur mit größeren Wortlisten.

---

## 🦴 Dein Skelett

```python
def lade_buchungen(pfad):
    """Liest die CSV. Gibt (buchungen, fehlerhafte_zeilen) zurück."""

def deutsche_zahl(text):
    """'1.234,56' → 1234.56"""

def kategorisiere(buchung):
    """Ordnet eine Kategorie zu."""

def auswertung_kategorien(buchungen):
    """Summiert die Ausgaben je Kategorie."""

def auswertung_monate(buchungen):
    """Berechnet Einnahmen, Ausgaben und Saldo je Monat."""

def finde_wiederkehrende(buchungen):
    """Erkennt Daueraufträge und Abos."""

def finde_ausreisser(buchungen, faktor=3):
    """Findet ungewöhnlich große Buchungen."""

def schreibe_bericht(ergebnis, pfad):
    """Schreibt den Textbericht."""

def main():
    """Hauptprogramm."""
```

---

## 💥 Der Härtetest

```text
□ Datei existiert nicht
□ Datei ist leer
□ Datei hat nur eine Kopfzeile
□ Zeile mit fehlendem Betrag
□ Betrag als "keine zahl"
□ Datum im falschen Format
□ Zeile mit zu wenigen Spalten
□ Umlaute im Empfängernamen
□ Alle Buchungen sind Einnahmen (Division durch 0 bei Ausgaben-Anteilen!)
```

---

## 🧠 Reflexion

1. Wie viele fehlerhafte Zeilen hat deine CSV — und wie gehst du damit um?
2. Wie gut funktioniert deine automatische Kategorisierung? Was fehlt?
3. Welche Auswertung war für dich am aufschlussreichsten?
4. Wo hättest du mit `try/except` sparsamer sein können?

---

## 🔍 Musterlösung

👉 [`loesung/kontoanalyse.py`](loesung/kontoanalyse.py)

**➡️ Weiter: [Modul 17 — venv & Projektstruktur](../../module/17/README.md)**
