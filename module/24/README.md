# 📊 Modul 24 — Excel automatisieren

> ⏱️ ~5 Stunden · ⬅️ [Modul 23](../23/README.md) · ➡️ [Modul 25](../25/README.md)

---

## 🎯 Lernziele

- [ ] Excel-Dateien mit `openpyxl` lesen und schreiben
- [ ] Zellen formatieren (Farben, Schrift, Rahmen, Breite)
- [ ] Formeln und Diagramme einfügen
- [ ] mehrere Tabellenblätter verwalten
- [ ] pandas-Einstieg für große Datenmengen

---

## 🌍 Warum das wichtig ist

Das hier ist für die meisten Menschen der **größte Zeitgewinn** des ganzen Kurses. 🎉

```text
❌ Von Hand: 40 Excel-Dateien öffnen, Spalte kopieren, in Sammeldatei
             einfügen, Summe bilden, formatieren.  →  3 Stunden, jeden Monat

✅ Mit Python: python monatsbericht.py            →  4 Sekunden
```

Und weil das Skript **immer gleich** arbeitet, macht es keine Copy-Paste-Fehler. 🎯

---

## 📖 Die Lektion

### 1. Installation & Grundbegriffe

```bash
pip install openpyxl
```

```text
📗 Workbook (Arbeitsmappe)  =  die .xlsx-Datei
 └─ 📄 Worksheet (Blatt)     =  ein Tabellenblatt
     └─ 🔲 Cell (Zelle)       =  A1, B2, …
```

⚠️ In openpyxl beginnen Zeilen und Spalten bei **1**, nicht bei 0!

### 2. Lesen

```python
from openpyxl import load_workbook

mappe = load_workbook("daten.xlsx", data_only=True)   # ⭐ data_only!
blatt = mappe.active                     # oder: mappe["Blattname"]

print(blatt["A1"].value)
print(blatt.cell(row=1, column=1).value)
print(blatt.max_row, blatt.max_column)
print(mappe.sheetnames)

for zeile in blatt.iter_rows(min_row=2, values_only=True):
    print(zeile)                          # Tupel je Zeile
```

💡 **`data_only=True`** liefert die **Werte** von Formeln statt der Formeln selbst. Ohne das bekommst du `"=SUM(A1:A10)"` statt `42`.

### 3. Schreiben

```python
from openpyxl import Workbook

mappe = Workbook()
blatt = mappe.active
blatt.title = "Umsatz 2026"

blatt["A1"] = "Produkt"
blatt.cell(row=1, column=2, value="Preis")
blatt.append(["Laptop", 899.99])          # ⭐ ganze Zeile anhängen

mappe.save("bericht.xlsx")                # ⚠️ überschreibt ohne Nachfrage!
```

### 4. 🎨 Formatieren

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

zelle = blatt["A1"]
zelle.font = Font(bold=True, size=14, color="FFFFFF")
zelle.fill = PatternFill("solid", fgColor="4472C4")
zelle.alignment = Alignment(horizontal="center", vertical="center")
zelle.number_format = '#,##0.00 "€"'

duenn = Side(style="thin", color="999999")
zelle.border = Border(left=duenn, right=duenn, top=duenn, bottom=duenn)

blatt.column_dimensions["A"].width = 25
blatt.row_dimensions[1].height = 22
blatt.freeze_panes = "A2"                  # ⭐ Kopfzeile fixieren
```

**Nützliche Zahlenformate:**

| Format | Ergebnis |
|---|---|
| `'#,##0.00 "€"'` | `1.234,56 €` |
| `'0.0%'` | `85,6 %` |
| `'DD.MM.YYYY'` | `26.07.2026` |
| `'#,##0'` | `1.235` |

### 5. Formeln & Diagramme

```python
blatt["D10"] = "=SUM(D2:D9)"              # Excel rechnet beim Öffnen
blatt["E2"] = "=B2*C2"

from openpyxl.chart import BarChart, Reference

diagramm = BarChart()
diagramm.title = "Umsatz pro Monat"
daten = Reference(blatt, min_col=2, min_row=1, max_row=13)
kategorien = Reference(blatt, min_col=1, min_row=2, max_row=13)
diagramm.add_data(daten, titles_from_data=True)
diagramm.set_categories(kategorien)
blatt.add_chart(diagramm, "E2")
```

### 6. Mehrere Blätter

```python
blatt2 = mappe.create_sheet("Auswertung")
mappe["Rohdaten"]
mappe.move_sheet("Auswertung", offset=-1)
del mappe["Altes Blatt"]
```

### 7. 🐼 pandas — ab wann?

```bash
pip install pandas openpyxl
```

```python
import pandas as pd

df = pd.read_excel("daten.xlsx")
print(df.head())
print(df.describe())
print(df.groupby("Kategorie")["Umsatz"].sum())

df[df["Umsatz"] > 1000].to_excel("gross.xlsx", index=False)
```

| Nimm openpyxl | Nimm pandas |
|---|---|
| Formatierung, Farben, Diagramme | Analyse, Gruppierung, Statistik |
| kleine Dateien, feine Kontrolle | große Datenmengen (>10.000 Zeilen) |
| Zellen gezielt bearbeiten | ganze Tabellen umformen |

💡 Man kombiniert beide: mit pandas rechnen, mit openpyxl schön machen. 🎨

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| Index bei 0 begonnen | `IndexError` | Zeilen/Spalten starten bei **1** |
| `data_only` vergessen | Formeltext statt Wert | `data_only=True` |
| Original überschrieben | Daten weg 💀 | unter neuem Namen speichern |
| Datei in Excel offen | `PermissionError` | Excel schließen |
| `save()` vergessen | keine Änderung | am Ende speichern |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — erzeugt sich Testdateien selbst

---

## 🛠️ Mini-Projekt: Monatsbericht-Generator 📈

Siehe [`projekte/06_report/`](../../projekte/06_report/README.md) — das ist Projekt 6.

---

## 🧠 Selbsttest

1. Was ist Workbook, Worksheet, Cell?
2. Bei welchem Index beginnen Zeilen?
3. Wozu `data_only=True`?
4. Wie hängst du eine ganze Zeile an?
5. Wie machst du eine Zelle fett?
6. Was macht `freeze_panes`?
7. Wie schreibst du eine Excel-Formel?
8. Wann pandas statt openpyxl?
9. Was tun bei `PermissionError`?
10. ✍️ Nenne eine Aufgabe aus deinem Alltag, die du damit automatisieren könntest.

<details>
<summary>💡 Antworten</summary>

1. Workbook = Datei, Worksheet = Tabellenblatt, Cell = einzelne Zelle.
2. Bei 1.
3. Damit man die berechneten Werte von Formeln bekommt statt der Formeltexte.
4. `blatt.append([wert1, wert2, ...])`
5. `zelle.font = Font(bold=True)`
6. Fixiert Zeilen/Spalten beim Scrollen (z. B. die Kopfzeile).
7. Als String zuweisen: `blatt["D10"] = "=SUM(D2:D9)"`
8. Bei großen Datenmengen und wenn es um Analyse/Gruppierung geht.
9. Die Datei ist noch in Excel geöffnet — schließen.
10. Z. B. monatliche Auswertungen, Rechnungslisten, Zeiterfassung zusammenführen.
</details>

---

## 🔄 Wiederholung (Modul 21–23)

1. Was macht `re.sub`?
2. Warum `timeout` bei requests?
3. Warum `time.sleep()` beim Scrapen?
4. Was macht `get_text(strip=True)`?

---

## 🔗 Vertiefung

- 📖 [openpyxl-Doku](https://openpyxl.readthedocs.io/)
- 📖 [Automate the Boring Stuff — Kap. 13](https://automatetheboringstuff.com/2e/chapter13/)
- 📖 [pandas — 10 Minuten Einstieg](https://pandas.pydata.org/docs/user_guide/10min.html)

**➡️ [Modul 25 — Dateien, Ordner & PDFs](../25/README.md)** 🤖
