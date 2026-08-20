# 🔤 Modul 02 — Strings (Text)

> ⏱️ ~5 Stunden · ⬅️ [Modul 01](../01/README.md) · ➡️ [Modul 03](../03/README.md)

---

## 🎯 Lernziele

- [ ] Strings erstellen, verketten und wiederholen
- [ ] **f-Strings** benutzen (die wichtigste Technik dieses Moduls!)
- [ ] mit Index und Slicing Teile herausschneiden
- [ ] die 15 wichtigsten String-Methoden anwenden
- [ ] verstehen, warum Strings **unveränderlich** sind

---

## 🌍 Warum das wichtig ist

**Fast alles ist Text.** Dateinamen, CSV-Zeilen, JSON-Antworten von APIs, HTML von Webseiten, Nutzereingaben, Logdateien. Wenn du später eine Rechnung aus einer PDF ziehst oder E-Mail-Adressen aus einer Liste filterst — das ist alles String-Verarbeitung.

> 🧠 **Tutor sagt:** Dieses Modul zahlt sich später am stärksten aus. Beherrsch `f-Strings` und `split`/`join`, und du hast 60 % aller Alltagsaufgaben abgedeckt.

---

## 📖 Die Lektion

### 1. Strings erstellen

```python
a = "doppelte Anführungszeichen"
b = 'einfache gehen auch'
c = """Mehrere
Zeilen"""
```

**Wann welche?** Egal — aber praktisch, wenn im Text selbst Anführungszeichen vorkommen:

```python
print("Er sagte 'Hallo'")        # ✅
print('Er sagte "Hallo"')        # ✅
print("Er sagte \"Hallo\"")      # ✅ mit Escape
```

**Escape-Sequenzen** (Sonderzeichen mit `\`):

| Code | Bedeutung |
|---|---|
| `\n` | Zeilenumbruch |
| `\t` | Tabulator |
| `\"` | Anführungszeichen |
| `\\` | ein Backslash |

```python
print("Zeile 1\nZeile 2")
print("Name:\tAnna")
print("Pfad: C:\\Users\\Anna")     # doppelter Backslash!
print(r"Pfad: C:\Users\DEINNAME")      # r = raw string, einfacher!
```

### 2. Verketten & Wiederholen

```python
vorname = "Anna"
nachname = "Schmidt"

print(vorname + " " + nachname)     # Anna Schmidt
print("-" * 30)                     # ------------------------------
```

⚠️ **Nur String + String:**

```python
"Alter: " + 25          # ❌ TypeError
"Alter: " + str(25)     # ✅
```

### 3. ⭐ f-Strings — die moderne Art

Das ist die wichtigste Technik in diesem Modul. Setz ein `f` vor den String und schreib Variablen in `{}`:

```python
name = "Anna"
alter = 30

print(f"{name} ist {alter} Jahre alt.")     # Anna ist 30 Jahre alt.
```

Vergleich der drei Wege:

```python
print("Name: " + name + ", Alter: " + str(alter))   # 😰 mühsam
print("Name: {}, Alter: {}".format(name, alter))    # 😐 alt
print(f"Name: {name}, Alter: {alter}")              # 😍 f-String
```

**In `{}` darf beliebiger Code stehen:**

```python
print(f"Nächstes Jahr: {alter + 1}")
print(f"Groß: {name.upper()}")
print(f"Länge: {len(name)}")
```

#### 🎨 Formatierung — der eigentliche Superkraft-Teil

```python
preis = 1234.5678

f"{preis:.2f}"          # '1234.57'      2 Nachkommastellen
f"{preis:,.2f}"         # '1,234.57'     Tausendertrennzeichen
f"{preis:10.2f}"        # '   1234.57'   Breite 10, rechtsbündig
f"{0.856:.1%}"          # '85.6%'        Prozent

f"{'Anna':<10}|"        # 'Anna      |'  linksbündig
f"{'Anna':>10}|"        # '      Anna|'  rechtsbündig
f"{'Anna':^10}|"        # '   Anna   |'  zentriert
f"{'Anna':*^10}|"       # '***Anna***|'  mit Füllzeichen

f"{42:05d}"             # '00042'        führende Nullen
```

💡 **Debug-Trick** (spart dir später Stunden):

```python
x = 42
print(f"{x=}")          # x=42     ← zeigt Name UND Wert!
```

### 4. Index & Slicing ✂️

```text
 P  y  t  h  o  n
 0  1  2  3  4  5      ← Index von vorn
-6 -5 -4 -3 -2 -1      ← Index von hinten
```

```python
t = "Python"

t[0]        # 'P'      erstes Zeichen
t[5]        # 'n'
t[-1]       # 'n'      letztes Zeichen  ← sehr nützlich!
t[-2]       # 'o'
t[6]        # ❌ IndexError
```

**Slicing** — `[start:stop]`, wobei `stop` **nicht** enthalten ist:

```python
t[0:3]      # 'Pyt'     Index 0, 1, 2
t[:3]       # 'Pyt'     von Anfang
t[3:]       # 'hon'     bis Ende
t[:]        # 'Python'  Kopie
t[-3:]      # 'hon'     letzte 3
t[::2]      # 'Pto'     jedes 2. Zeichen
t[::-1]     # 'nohtyP'  umgedreht! 🔄
```

> 🧠 **Merkhilfe:** Denk dir die Indizes **zwischen** den Buchstaben:
> ```text
>  |P|y|t|h|o|n|
>  0 1 2 3 4 5 6
> ```
> `t[1:4]` schneidet zwischen 1 und 4 → `yth`. Länge = `stop - start`.

### 5. Die wichtigsten Methoden 🧰

```python
s = "  Hallo Welt  "

s.strip()                  # 'Hallo Welt'    Leerzeichen weg ⭐
s.upper()                  # '  HALLO WELT  '
s.lower()                  # '  hallo welt  '
s.title()                  # '  Hallo Welt  '
s.replace("Welt", "Du")    # '  Hallo Du  '
s.count("l")               # 3
s.find("Welt")             # 8  (oder -1, wenn nicht gefunden)
len(s)                     # 14
```

**Prüfungen** (geben `True`/`False`):

```python
"123".isdigit()            # True    nur Ziffern?
"abc".isalpha()            # True    nur Buchstaben?
"a1".isalnum()             # True
"hallo".startswith("ha")   # True
"bild.png".endswith(".png")# True    ← super für Dateifilter!
"lo" in "hallo"            # True    ← einfachste Prüfung
```

### 6. ⭐ `split()` und `join()` — Das Power-Duo

Das brauchst du **ständig** bei echten Daten.

```python
# split: String → Liste
zeile = "Anna,30,Berlin"
teile = zeile.split(",")           # ['Anna', '30', 'Berlin']

satz = "Der Hund bellt laut"
woerter = satz.split()             # ['Der','Hund','bellt','laut']  (an Leerzeichen)

# join: Liste → String
"-".join(["2026", "07", "26"])     # '2026-07-26'
", ".join(["a", "b", "c"])         # 'a, b, c'
"".join(["a", "b"])                # 'ab'
```

🌍 **Realbeispiel:** Genau so liest du später CSV-Dateien Zeile für Zeile.

### 7. ⚠️ Strings sind unveränderlich (immutable)

```python
s = "hallo"
s[0] = "H"          # ❌ TypeError: 'str' object does not support item assignment
```

Methoden ändern den String **nicht** — sie geben einen **neuen** zurück:

```python
s = "hallo"
s.upper()
print(s)            # 'hallo'   ← unverändert! 😱

s = s.upper()       # ✅ Ergebnis zuweisen
print(s)            # 'HALLO'
```

> 🧠 **Tutor sagt:** Das ist die zweithäufigste Anfängerfalle nach dem Typ-Problem. Merksatz: **String-Methoden geben zurück, sie verändern nicht.**

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `s.upper()` ohne Zuweisung | Ergebnis verpufft | `s = s.upper()` |
| `"Alter: " + 25` | `TypeError` | f-String oder `str(25)` |
| `t[len(t)]` | `IndexError` | letztes Zeichen ist `t[-1]` |
| `s[0] = "X"` | `TypeError` | `s = "X" + s[1:]` |
| `"C:\neu"` | `\n` wird Umbruch | `r"C:\neu"` |
| `f"{preis:2f}"` | fehlender Punkt | `f"{preis:.2f}"` |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

| # | Aufgabe | Level |
|:---:|---|:---:|
| 1 | Begrüßung mit f-String | 🟢 |
| 2 | Erstes/letztes Zeichen, Länge | 🟢 |
| 3 | Wort umdrehen | 🟢 |
| 4 | Preise formatiert ausgeben | 🟡 |
| 5 | Datenzeile mit `split` zerlegen | 🟡 |
| 6 | Initialen bilden | 🟡 |
| 7 | Palindrom-Prüfung | 🔴 |
| 8 | Tabelle sauber ausrichten | 🔴 |
| 9 ⭐ | E-Mail-Adresse zerlegen & Nutzername bauen | ⭐ |

---

## 🛠️ Mini-Projekt: Text-Analysator

Erstelle `text_analyse.py` mit einem festen Beispieltext (ein Absatz deiner Wahl) und gib aus:

```text
════════════════════════════════════
       TEXT-ANALYSE
════════════════════════════════════
Zeichen gesamt:        342
Zeichen ohne Leer.:    287
Wörter:                 58
Sätze:                   4
Längstes Wort:      "Programmiersprache"
Ø Wortlänge:           4.9
Häufigster Buchstabe:  'e'
Text rückwärts:     ...
════════════════════════════════════
```

**Anforderungen:** f-Strings für die Ausgabe · `split()` für Wörter · Ausrichtung mit `:<20` · Zahlen mit `:.1f`

---

## 🧠 Selbsttest

1. Wie schreibst du „Anna ist 30" mit einem f-String?
2. Was ergibt `"Python"[1:4]`?
3. Wie drehst du einen String um?
4. Was macht `"a,b,c".split(",")`?
5. Was macht `"-".join(["a","b"])`?
6. Warum ändert `s.upper()` die Variable `s` nicht?
7. Wie gibst du `3.14159` mit 2 Nachkommastellen aus?
8. Wie holst du das letzte Zeichen eines Strings?
9. Wie prüfst du, ob eine Datei auf `.txt` endet?
10. ✍️ Erkläre Slicing in zwei Sätzen mit eigenem Beispiel.

<details>
<summary>💡 Antworten</summary>

1. `f"{name} ist {alter}"`
2. `'yth'` (Index 1, 2, 3 — 4 ist ausgeschlossen)
3. `text[::-1]`
4. Zerlegt in die Liste `['a','b','c']`
5. Ergibt `'a-b'`
6. Strings sind unveränderlich; Methoden geben einen **neuen** String zurück. Man muss ihn zuweisen.
7. `f"{3.14159:.2f}"`
8. `text[-1]`
9. `dateiname.endswith(".txt")`
10. Z. B.: „Slicing schneidet einen Teil heraus: `[start:stop]`, wobei `stop` nicht mehr dazugehört. `'Hallo'[1:3]` ergibt `'al'`."
</details>

---

## 🔄 Wiederholung (Modul 00–01)

1. Was ergibt `type(10 / 2)`?
2. Was macht `punkte += 5`?
3. Wie gibst du zwei Werte mit `|` getrennt aus?
4. Was ist der Unterschied zwischen `int(3.9)` und `round(3.9)`?

---

## 🔗 Vertiefung

- 📖 [Real Python — f-Strings](https://realpython.com/python-f-strings/)
- 📄 [Spickzettel Strings](../../spickzettel/strings.md)
- ⌨️ [Codewars: 8 kyu String-Aufgaben](https://www.codewars.com/kata/search/python?q=&r%5B%5D=-8&tags=Strings)

**➡️ [Modul 03 — Zahlen & Ein-/Ausgabe](../03/README.md)** 🧮
