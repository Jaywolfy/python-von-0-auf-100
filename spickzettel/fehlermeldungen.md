# 🐞 Spickzettel · Fehlermeldungen entschlüsseln

> **Goldene Regel:** Lies den Traceback **von unten nach oben**.
> Die **letzte Zeile** sagt *was* falsch ist. Die Zeile darüber sagt *wo*.

---

## 📖 Einen Traceback lesen

```text
Traceback (most recent call last):
  File "meinskript.py", line 7, in <module>     ← 3️⃣ WO in deiner Datei
    ergebnis = teile(10, 0)
  File "meinskript.py", line 3, in teile        ← 2️⃣ In welcher Funktion
    return a / b
ZeroDivisionError: division by zero             ← 1️⃣ WAS ist passiert (hier zuerst lesen!)
```

**Dein Ablauf:** letzte Zeile lesen → Zeilennummer suchen → dort `print()` einbauen → schauen, was wirklich drinsteht.

---

## 🚨 Die 15 häufigsten Fehler

### `SyntaxError: invalid syntax`
🔍 **Ursache:** Tippfehler in der Grammatik.
✅ **Meistens:** Doppelpunkt `:` vergessen · Klammer nicht geschlossen · `=` statt `==`
```python
if x == 5      # ❌ fehlt :
if x == 5:     # ✅
```
💡 **Tipp:** Schau **auch die Zeile DARÜBER** an — oft ist dort die offene Klammer.

---

### `IndentationError: expected an indented block`
🔍 Nach `:` fehlt die eingerückte Zeile.
```python
if x > 5:
print("hi")        # ❌
if x > 5:
    print("hi")    # ✅ 4 Leerzeichen
```

### `IndentationError: unexpected indent`
🔍 Zu viel eingerückt, oder Tabs & Leerzeichen gemischt.
✅ VS Code: `Strg+Shift+P` → „Convert Indentation to Spaces"

---

### `NameError: name 'xyz' is not defined`
🔍 Variable/Funktion gibt es (noch) nicht.
✅ Tippfehler? Groß-/Kleinschreibung? Erst benutzt, dann definiert? Vergessen zu importieren?
```python
print(Name)     # ❌ NameError
name = "Anna"
print(name)     # ✅
```

---

### `TypeError: can only concatenate str (not "int") to str`
🔍 Text + Zahl geht nicht.
```python
"Alter: " + 30            # ❌
"Alter: " + str(30)       # ✅
f"Alter: {30}"            # ✅ besser
```

### `TypeError: 'int' object is not subscriptable`
🔍 Du benutzt `[...]` auf etwas, das keine Sammlung ist.
```python
zahl = 5
zahl[0]        # ❌
```

### `TypeError: 'str' object does not support item assignment`
🔍 Strings sind unveränderlich.
```python
s = "hallo"; s[0] = "H"    # ❌
s = "H" + s[1:]            # ✅
```

### `TypeError: xyz() missing 1 required positional argument`
🔍 Du hast der Funktion zu wenige Argumente gegeben.
```python
def add(a, b): return a + b
add(5)        # ❌   add(5, 3) ✅
```

---

### `ValueError: invalid literal for int() with base 10: 'abc'`
🔍 Du willst Text in eine Zahl umwandeln, der keine Zahl ist.
```python
int("abc")     # ❌
int("42")      # ✅
```
✅ **Fix im echten Code:**
```python
try:
    zahl = int(eingabe)
except ValueError:
    print("Bitte eine Zahl eingeben!")
```

---

### `IndexError: list index out of range`
🔍 Du greifst auf eine Position zu, die es nicht gibt. **Index beginnt bei 0!**
```python
l = [1, 2, 3]
l[3]        # ❌ gültig sind 0,1,2
l[-1]       # ✅ letztes Element
```

---

### `KeyError: 'stadt'`
🔍 Der Schlüssel existiert nicht im Dictionary.
```python
d = {"name": "Anna"}
d["stadt"]                  # ❌
d.get("stadt", "unbekannt") # ✅ sicher
```

---

### `AttributeError: 'list' object has no attribute 'push'`
🔍 Diese Methode gibt es für diesen Typ nicht.
✅ Falscher Name (`append` statt `push`) oder falscher Typ. Prüfe mit `type(x)`.

---

### `ZeroDivisionError: division by zero`
🔍 Durch 0 geteilt.
```python
if n != 0:
    ergebnis = x / n
```

---

### `ModuleNotFoundError: No module named 'requests'`
🔍 Paket nicht installiert (oder falsche venv aktiv).
```bash
pip install requests
```

---

### `FileNotFoundError: [Errno 2] No such file or directory: 'daten.txt'`
🔍 Datei existiert nicht **relativ zum aktuellen Arbeitsverzeichnis**.
```python
from pathlib import Path
print(Path.cwd())     # wo bin ich gerade?
```
✅ In VS Code: Ordner öffnen, nicht nur die Datei!

---

### `UnicodeDecodeError`
🔍 Encoding-Problem (Umlaute).
```python
open("datei.txt", encoding="utf-8")     # ✅ immer angeben
```

---

### `RecursionError: maximum recursion depth exceeded`
🔍 Funktion ruft sich endlos selbst auf. Abbruchbedingung fehlt.

---

## 🔇 Der stille Killer: gar kein Fehler, aber falsches Ergebnis

Das ist der schwierigste Fall. Vorgehen:

```python
# 1. print() an JEDER wichtigen Stelle
print(f"{variable=}")        # zeigt Name UND Wert!

# 2. Typen prüfen
print(type(x), type(y))

# 3. Code auf pythontutor.com Schritt für Schritt ablaufen lassen
# 4. Debugger: Breakpoint mit F9, dann F5
```

**Klassiker bei falschen Ergebnissen:**
- `input()` liefert immer **String** → `"5" + "3"` ergibt `"53"`, nicht `8`
- `/` gibt float, `//` gibt int
- Einrückung: Code steht versehentlich innerhalb/außerhalb der Schleife
- `=` (zuweisen) statt `==` (vergleichen)
- Floats: `0.1 + 0.2 == 0.30000000000000004` → nie exakt vergleichen!

---

## 🆘 Wenn nichts hilft

1. Fehlermeldung **wörtlich googeln** (aber deine Dateinamen/Variablen rauslassen)
2. Code auf [pythontutor.com](https://pythontutor.com/visualize.html) laufen lassen
3. Der Ente laut erklären 🦆
4. 20 Minuten Pause. Ernsthaft — funktioniert erschreckend oft. ☕
