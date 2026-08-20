# 📈 Projekt 6 — Report-Generator

> 📍 **Nach Modul 24** · ⏱️ ~6 Stunden · 🎯 Das Projekt, das dir echte Arbeitszeit spart

---

## 🎬 Die Aufgabe

Du bekommst **12 Rohdaten-Dateien** (eine pro Monat) und sollst daraus einen fertigen Monatsbericht bauen:

```text
📥 EINGABE                          📤 AUSGABE
   daten/                              berichte/
   ├── umsatz_2026_01.csv              ├── jahresbericht_2026.xlsx
   ├── umsatz_2026_02.csv     ───►     │    ├── Blatt "Übersicht" (+ Diagramm)
   ├── ...                             │    ├── Blatt "Nach Kategorie"
   └── umsatz_2026_12.csv              │    ├── Blatt "Nach Monat"
                                       │    └── Blatt "Rohdaten"
                                       └── zusammenfassung.txt
```

**Von Hand:** ~3 Stunden. **Mit deinem Skript:** ~2 Sekunden. Jeden Monat. 🎉

---

## 🎬 So soll die Konsolenausgabe aussehen

```text
╔══════════════════════════════════════════════════════╗
║           📈  REPORT-GENERATOR  2026                  ║
╚══════════════════════════════════════════════════════╝

📂 Eingelesen:  12 Dateien, 1.847 Datensätze
⚠️  Übersprungen: 6 fehlerhafte Zeilen

── JAHRESÜBERSICHT ────────────────────────────────────
  Gesamtumsatz                              487.293,45 €
  Bestes Quartal        Q4                  142.881,20 €
  Bester Monat          November             52.104,90 €
  Ø pro Monat                                40.607,79 €
  Artikel verkauft                              12.483

── UMSATZ NACH KATEGORIE ──────────────────────────────
  Technik        241.882,10 €  ████████████████  50 %
  Möbel          148.220,45 €  █████████         30 %
  Bürobedarf      97.190,90 €  ██████            20 %

── MONATSVERLAUF ──────────────────────────────────────
  Jan  32.104 €  ██████████
  Feb  28.910 €  █████████
  ...
  Nov  52.105 €  ████████████████  🏆
  Dez  47.221 €  ███████████████

✅ jahresbericht_2026.xlsx  (4 Blätter, 2 Diagramme)
✅ zusammenfassung.txt
⏱️  Laufzeit: 1,8 Sekunden
```

---

## ✅ Pflichtanforderungen

- [ ] Alle CSV-Dateien eines Ordners automatisch einlesen (`glob`)
- [ ] Fehlerhafte Zeilen überspringen und zählen
- [ ] Auswertung nach **Monat**, **Kategorie** und **Produkt**
- [ ] Excel-Datei mit **mindestens 3 Blättern** erzeugen
- [ ] Formatierung: Kopfzeilen farbig, Euroformat, Spaltenbreiten, fixierte Kopfzeile
- [ ] Mindestens **ein Diagramm** einbetten
- [ ] Textzusammenfassung schreiben
- [ ] Konsolenausgabe mit Balkendiagramm
- [ ] Vollständige Fehlerbehandlung

## 🎁 Bonus

- [ ] Vergleich zum Vorjahr mit Trendpfeilen ↗️↘️
- [ ] Bedingte Formatierung (grün = über Ziel, rot = darunter)
- [ ] Top-10-Produkte-Blatt
- [ ] Zwei Diagrammtypen (Balken **und** Linie)
- [ ] `argparse` für Eingabe-/Ausgabeordner (Modul 26)
- [ ] Automatisch jeden Monatsersten ausführen ⏰
- [ ] PDF-Export der Zusammenfassung

---

## 🦴 Dein Skelett

```python
def finde_dateien(ordner, muster="umsatz_*.csv"):
    """Findet alle passenden Rohdaten-Dateien."""

def lade_datei(pfad):
    """Liest eine CSV. Gibt (datensaetze, fehler) zurück."""

def lade_alle(ordner):
    """Liest alle Dateien ein und fasst sie zusammen."""

def auswertung_monate(daten):
    """Umsatz je Monat."""

def auswertung_kategorien(daten):
    """Umsatz je Kategorie."""

def top_produkte(daten, anzahl=10):
    """Die umsatzstärksten Produkte."""

def erzeuge_excel(auswertungen, daten, pfad):
    """Baut die formatierte Excel-Datei mit Diagrammen."""

def schreibe_zusammenfassung(auswertungen, pfad):
    """Schreibt den Textbericht."""

def zeige_konsole(auswertungen):
    """Gibt die Auswertung im Terminal aus."""

def main():
    """Hauptprogramm."""
```

---

## 🎨 Excel-Formatierung — die Bausteine

```python
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.utils import get_column_letter

def formatiere_kopfzeile(blatt, farbe="4472C4"):
    """Formatiert die erste Zeile als Kopfzeile."""
    for zelle in blatt[1]:
        if zelle.value is not None:
            zelle.font = Font(bold=True, color="FFFFFF")
            zelle.fill = PatternFill("solid", fgColor=farbe)
            zelle.alignment = Alignment(horizontal="center")
    blatt.row_dimensions[1].height = 22
    blatt.freeze_panes = "A2"

def breite_anpassen(blatt, zusatz=4):
    """Passt alle Spaltenbreiten an den Inhalt an."""
    for spalte in range(1, blatt.max_column + 1):
        laengste = max(len(str(blatt.cell(row=r, column=spalte).value or ""))
                       for r in range(1, blatt.max_row + 1))
        blatt.column_dimensions[get_column_letter(spalte)].width = laengste + zusatz
```

💡 Diese beiden Funktionen brauchst du in **jedem** Excel-Projekt. Ab in dein Werkzeugmodul! 🧰

---

## 💥 Der Härtetest

```text
□ Eingabeordner ist leer
□ Eingabeordner existiert nicht
□ Eine CSV hat andere Spalten als die anderen
□ Eine CSV ist komplett leer
□ Excel-Datei ist gerade geöffnet → PermissionError!
□ Umlaute in Produktnamen
□ Ein Monat fehlt ganz (Lücke im Diagramm?)
□ Alle Umsätze sind 0 (Division durch 0!)
```

---

## 🧠 Reflexion

1. Wie lange hätte dieser Bericht von Hand gedauert? Wie lange braucht dein Skript?
2. Welche zwei Funktionen kannst du in **jedes** künftige Excel-Projekt übernehmen?
3. Was müsstest du ändern, wenn nächstes Jahr eine Spalte dazukommt?
4. Wäre pandas hier einfacher gewesen? Wo ja, wo nein?

---

## 🔍 Musterlösung

👉 [`loesung/report.py`](loesung/report.py) — erzeugt sich die 12 Rohdaten-Dateien selbst

**➡️ Weiter: [Modul 25 — Dateien & PDFs](../../module/25/README.md)**
