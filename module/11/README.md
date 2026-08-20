# 🗂️ Modul 11 — Dateien & Pfade

> ⏱️ ~5 Stunden · ⬅️ [Modul 10](../10/README.md) · ➡️ [Modul 12](../12/README.md)

---

## 🎯 Lernziele

- [ ] Textdateien lesen und schreiben
- [ ] `with open(...)` verstehen und immer benutzen
- [ ] `pathlib` statt String-Pfaden
- [ ] Encoding-Probleme (Umlaute!) vermeiden
- [ ] Ordner durchsuchen und Dateien filtern

---

## 🌍 Warum das wichtig ist

**Hier fängt echte Automatisierung an.** 🤖

Ab jetzt kann dein Programm auf Daten zugreifen, die es nicht selbst erzeugt hat — und Ergebnisse hinterlassen, die den Programmlauf überdauern. Logdateien auswerten, Berichte schreiben, 400 Dateien umbenennen: alles baut auf diesem Modul auf.

> ⚠️ **Achtung:** Ab hier kann dein Code **echte Dateien kaputt machen**. Arbeite in einem Testordner und probier `"w"` (überschreiben) nie an wichtigen Dateien aus. 🛡️

---

## 📖 Die Lektion

### 1. ⭐ Immer `with open(...)`

```python
with open("daten.txt", "r", encoding="utf-8") as datei:
    inhalt = datei.read()
# Datei ist hier automatisch geschlossen ✅
```

```text
with open( "daten.txt" ,  "r" , encoding="utf-8" ) as datei:
              ▲            ▲          ▲
            Pfad         Modus    IMMER angeben!
```

⚠️ **Ohne `with`** musst du selbst `datei.close()` aufrufen — und bei einem Fehler bleibt die Datei offen. **Nimm immer `with`.**

### 2. Die Modi

| Modus | Bedeutung | Vorsicht |
|:---:|---|---|
| `"r"` | lesen (Standard) | Fehler, wenn Datei fehlt |
| `"w"` | schreiben | 🚨 **löscht vorhandenen Inhalt!** |
| `"a"` | anhängen | sicher — hängt hinten an |
| `"x"` | neu erstellen | Fehler, wenn schon vorhanden |

### 3. Lesen — vier Wege

```python
with open("daten.txt", encoding="utf-8") as f:
    inhalt = f.read()              # ganze Datei als ein String

with open("daten.txt", encoding="utf-8") as f:
    zeilen = f.readlines()         # Liste von Zeilen (mit \n!)

with open("daten.txt", encoding="utf-8") as f:
    for zeile in f:                # ⭐ BESTE Variante bei großen Dateien
        print(zeile.strip())       # strip() entfernt das \n

text = Path("daten.txt").read_text(encoding="utf-8")     # Kurzform
```

💡 **`.strip()` nicht vergessen** — jede Zeile endet mit `\n`.

### 4. Schreiben

```python
with open("bericht.txt", "w", encoding="utf-8") as f:
    f.write("Erste Zeile\n")       # \n selbst schreiben!
    f.write("Zweite Zeile\n")
    f.writelines(["a\n", "b\n"])

with open("log.txt", "a", encoding="utf-8") as f:      # anhängen
    f.write("Neuer Eintrag\n")

Path("kurz.txt").write_text("Inhalt", encoding="utf-8")   # Kurzform
```

### 5. 🚨 Encoding — immer `utf-8`

```python
open("datei.txt")                          # ❌ nimmt Systemstandard
open("datei.txt", encoding="utf-8")        # ✅ immer so
```

Ohne Angabe verhält sich dein Skript auf Windows anders als auf Mac — und Umlaute werden zu `ï¿½`. Das ist eine der nervigsten Fehlerquellen überhaupt.

### 6. ⭐ `pathlib` — der moderne Weg mit Pfaden

```python
from pathlib import Path

p = Path("daten") / "2026" / "bericht.txt"     # ⭐ / funktioniert überall!

p.exists()          # gibt es die Datei?
p.is_file()         # Datei?
p.is_dir()          # Ordner?
p.name              # 'bericht.txt'
p.stem              # 'bericht'
p.suffix            # '.txt'
p.parent            # Path('daten/2026')
p.stat().st_size    # Größe in Bytes

Path.cwd()          # aktuelles Arbeitsverzeichnis ⭐ bei FileNotFoundError!
Path.home()         # Home-Verzeichnis
```

❌ **Nicht mehr so:** `"ordner\\datei.txt"` — funktioniert nur auf Windows.
✅ **So:** `Path("ordner") / "datei.txt"` — funktioniert überall.

### 7. Ordner durchsuchen 🔍

```python
ordner = Path("dokumente")

for eintrag in ordner.iterdir():             # nur eine Ebene
    print(eintrag.name)

for pdf in ordner.glob("*.pdf"):             # nur PDFs
    print(pdf.name)

for pdf in ordner.rglob("*.pdf"):            # ⭐ auch alle Unterordner!
    print(pdf)

ordner.mkdir(exist_ok=True)                  # Ordner anlegen
ordner.mkdir(parents=True, exist_ok=True)    # inkl. Zwischenordner
```

🌍 **Genau damit baust du in Modul 25 den Ordner-Aufräumer.**

### 8. Sicher arbeiten 🛡️

```python
pfad = Path("daten.txt")

if pfad.exists():
    inhalt = pfad.read_text(encoding="utf-8")
else:
    print(f"Datei nicht gefunden: {pfad.absolute()}")
```

(Die elegantere Variante mit `try/except` kommt in Modul 13.)

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `open("w")` an wichtiger Datei | Inhalt weg 💀 | erst mit Testdatei üben |
| `encoding` vergessen | Umlaut-Chaos | `encoding="utf-8"` |
| `.strip()` vergessen | `\n` am Zeilenende | `zeile.strip()` |
| `\n` beim Schreiben vergessen | alles in einer Zeile | `f.write(text + "\n")` |
| `FileNotFoundError` | falsches Arbeitsverzeichnis | `print(Path.cwd())` |
| `"C:\neu"` | `\n` = Umbruch! | `Path("C:/neu")` oder `r"C:\neu"` |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — legt eigene Testdateien an, du zerstörst nichts. 😌

---

## 🛠️ Mini-Projekt: Logdatei-Analysator

`log_analyse.py` liest eine Logdatei mit Zeilen wie:

```text
2026-07-20 08:15:32 INFO  Benutzer angemeldet
2026-07-20 08:16:01 ERROR Datenbankverbindung fehlgeschlagen
```

und schreibt einen Bericht:

```text
════════════════════════════════════
   LOG-ANALYSE
════════════════════════════════════
Zeilen gesamt:       1.243
  INFO                 987
  WARNING              203  ⚠️
  ERROR                 53  🔴

Häufigste Fehlermeldung:
  "Datenbankverbindung fehlgeschlagen" (18x)

Aktivster Tag: 2026-07-20 (412 Einträge)
════════════════════════════════════
```

**Anforderungen:** Zeilenweise lesen · Level zählen (Dict) · Bericht in `bericht.txt` schreiben

---

## 🧠 Selbsttest

1. Warum `with open(...)`?
2. Was macht Modus `"w"` mit einer vorhandenen Datei?
3. Wann `"a"` statt `"w"`?
4. Warum immer `encoding="utf-8"`?
5. Wie liest du eine große Datei speicherschonend?
6. Warum `.strip()` bei Zeilen?
7. Was macht `Path("a") / "b"`?
8. Unterschied `glob` / `rglob`?
9. Wie prüfst du dein aktuelles Arbeitsverzeichnis?
10. ✍️ Erkläre, warum `with` besser ist als manuelles `close()`.

<details>
<summary>💡 Antworten</summary>

1. Es schließt die Datei automatisch — auch wenn ein Fehler auftritt.
2. Sie wird **komplett geleert** und neu geschrieben. 🚨
3. Wenn du an vorhandenen Inhalt anhängen willst (z. B. Logdatei).
4. Sonst hängt das Verhalten vom Betriebssystem ab → kaputte Umlaute.
5. `for zeile in datei:` — lädt nicht alles auf einmal in den Speicher.
6. Jede gelesene Zeile enthält am Ende den Zeilenumbruch `\n`.
7. Setzt einen Pfad plattformunabhängig zusammen: `a/b`.
8. `glob` sucht nur in einer Ebene, `rglob` auch in allen Unterordnern.
9. `from pathlib import Path; print(Path.cwd())`
10. Z. B.: „`with` ist wie eine Tür, die sich von selbst schließt — auch wenn du im Raum stolperst. Bei `close()` musst du daran denken, und bei einem Fehler kommst du nie dort an."
</details>

---

## 🔄 Wiederholung (Modul 08–10)

1. Was macht `[x for x in l if x > 0]`?
2. `print` vs. `return`?
3. Wie liest du einen Traceback?
4. Was macht `dict(zip(a, b))`?

---

## 🔗 Vertiefung

- 📖 [Real Python — pathlib](https://realpython.com/python-pathlib/)
- 📖 [Automate the Boring Stuff — Kap. 9](https://automatetheboringstuff.com/2e/chapter9/)

**➡️ [Modul 12 — Module & Standardbibliothek](../12/README.md)** 📚
