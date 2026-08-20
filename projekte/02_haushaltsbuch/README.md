# 💰 Projekt 2 — Haushaltsbuch (CLI)

> 📍 **Nach Modul 08** · ⏱️ ~5 Stunden · 🎯 Dein erstes Programm mit echter Struktur

---

## 🎬 So soll es aussehen

```text
╔════════════════════════════════════════════════════╗
║              💰  HAUSHALTSBUCH  💰                  ║
╚════════════════════════════════════════════════════╝

  [1] Einnahme erfassen        [5] Auswertung
  [2] Ausgabe erfassen         [6] Nach Kategorie filtern
  [3] Alle Buchungen anzeigen  [7] Buchung löschen
  [4] Kontostand               [q] Beenden

> 5

╔════════════════════════════════════════════════════╗
║                   AUSWERTUNG                        ║
╠════════════════════════════════════════════════════╣
║  Einnahmen:                            2.850,00 €  ║
║  Ausgaben:                             1.923,45 €  ║
║  ────────────────────────────────────────────────  ║
║  SALDO:                                  926,55 €  ║
╠════════════════════════════════════════════════════╣
║  AUSGABEN NACH KATEGORIE                            ║
║   Miete         850,00 €  ████████████████  44 %   ║
║   Lebensmittel  412,30 €  ████████          21 %   ║
║   Mobilität     289,15 €  █████             15 %   ║
║   Freizeit      201,00 €  ████              10 %   ║
║   Sonstiges     171,00 €  ███                9 %   ║
╠════════════════════════════════════════════════════╣
║  Größte Ausgabe:  Miete Januar (850,00 €)          ║
║  Ø pro Buchung:   137,39 €                          ║
║  Buchungen:       14                                ║
╚════════════════════════════════════════════════════╝
```

---

## ✅ Pflichtanforderungen

- [ ] Menü in einer `while True`-Schleife
- [ ] Buchungen erfassen: Betrag, Kategorie, Beschreibung, Datum
- [ ] Einnahmen und Ausgaben unterscheiden
- [ ] Alle Buchungen als **saubere Tabelle** anzeigen
- [ ] Kontostand berechnen
- [ ] Auswertung: Summen, Kategorien, Prozentanteile
- [ ] **Mindestens 8 Funktionen** — jede mit Docstring
- [ ] Keine Funktion länger als 25 Zeilen
- [ ] Robuste Eingabeprüfung (keine Abstürze!)
- [ ] Balkendiagramm im Terminal

## 🎁 Bonus

- [ ] Buchungen löschen und bearbeiten
- [ ] Nach Kategorie filtern
- [ ] Nach Zeitraum filtern
- [ ] Monatsvergleich
- [ ] Budget pro Kategorie mit Warnung bei Überschreitung ⚠️
- [ ] Daten speichern/laden (nach Modul 11/16)
- [ ] Wiederkehrende Buchungen

---

## 🗂️ Welche Datenstruktur?

Das ist die wichtigste Entscheidung dieses Projekts. Denk **selbst** darüber nach, bevor du weiterliest.

<details>
<summary>💡 Vergleich der Möglichkeiten (erst nach eigener Überlegung öffnen!)</summary>

```python
# Variante A: Liste von Listen  😐
buchungen = [["2026-01-05", "Miete", -850.0, "Miete Januar"]]
# ❌ Was war nochmal Index 2?

# Variante B: Liste von Dictionaries  ✅ EMPFOHLEN
buchungen = [
    {"datum": "2026-01-05", "kategorie": "Miete",
     "betrag": -850.0, "beschreibung": "Miete Januar"},
]
# ✅ selbsterklärend, leicht erweiterbar, direkt als JSON speicherbar

# Variante C: Zwei getrennte Listen  ❌
einnahmen = [...]
ausgaben = [...]
# ❌ doppelter Code für alles
```

**Trick:** Ausgaben als **negative** Beträge speichern. Dann ist der Kontostand einfach `sum(b["betrag"] for b in buchungen)` — eine Zeile statt einer Fallunterscheidung. 🎯
</details>

---

## 🦴 Dein Skelett

Fang damit an — alle Funktionen leer, dann eine nach der anderen füllen:

```python
"""Haushaltsbuch - Einnahmen und Ausgaben verwalten."""

KATEGORIEN = ["Miete", "Lebensmittel", "Mobilität", "Freizeit",
              "Gesundheit", "Sonstiges"]


def zeige_menue():
    """Gibt das Hauptmenü aus."""

def frage_zahl(text, min_wert=None):
    """Fragt so lange, bis eine gültige Zahl eingegeben wurde."""

def frage_kategorie():
    """Lässt den Nutzer eine Kategorie auswählen."""

def erfasse_buchung(buchungen, ist_einnahme):
    """Erfasst eine neue Buchung und hängt sie an die Liste an."""

def zeige_buchungen(buchungen):
    """Gibt alle Buchungen als Tabelle aus."""

def kontostand(buchungen):
    """Berechnet den aktuellen Kontostand."""

def summe_nach_kategorie(buchungen):
    """Gibt ein dict {kategorie: summe} für Ausgaben zurück."""

def zeige_auswertung(buchungen):
    """Gibt die komplette Auswertung mit Balkendiagramm aus."""

def balken(anteil, breite=16):
    """Erzeugt einen Balken für das Terminal-Diagramm."""

def main():
    """Hauptprogramm mit Menüschleife."""


if __name__ == "__main__":
    main()
```

---

## 💥 Der Härtetest

```text
□ Buchstaben als Betrag eingeben
□ Negative Zahl bei einer Einnahme
□ 0 als Betrag
□ Auswertung aufrufen, BEVOR eine Buchung existiert  ← Klassiker! (Division durch 0)
□ Sehr lange Beschreibung (Tabelle noch ausgerichtet?)
□ Umlaute in der Beschreibung
□ Ungültige Menüauswahl
□ Buchung mit Nummer 99 löschen (existiert nicht)
```

---

## 🧠 Reflexion

1. Warum hast du dich für diese Datenstruktur entschieden?
2. Welche Funktion war am schwersten? Warum?
3. Wo hast du dich beim Schreiben wiederholt — und wie könntest du das zusammenfassen?
4. Wie viele Abstürze hat der Härtetest gefunden?

---

## 🔍 Musterlösung

👉 [`loesung/haushaltsbuch.py`](loesung/haushaltsbuch.py)

**➡️ Weiter: [Modul 09 — Fehler & Debugging](../../module/09/README.md)**
