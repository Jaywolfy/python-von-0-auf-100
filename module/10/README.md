# ✨ Modul 10 — Comprehensions & eingebaute Funktionen

> ⏱️ ~5 Stunden · ⬅️ [Modul 09](../09/README.md) · ➡️ [Modul 11](../11/README.md)

---

## 🎯 Lernziele

- [ ] List- und Dict-Comprehensions schreiben
- [ ] `enumerate`, `zip`, `sorted(key=…)` sicher nutzen
- [ ] `sum`, `min`, `max`, `any`, `all` einsetzen
- [ ] `lambda` verstehen (in kleinen Dosen)
- [ ] wissen, **wann** eine Comprehension zu weit geht

---

## 🌍 Warum das wichtig ist

Alles hier geht auch ohne. Aber: **so schreibt man Python.**

Wenn du fremden Code liest — auf Stack Overflow, in Bibliotheken, in Tutorials — wimmelt es von Comprehensions. Ab diesem Modul liest du diesen Code flüssig statt ihn zu entziffern. Und deine eigenen Programme werden deutlich kürzer.

---

## 📖 Die Lektion

### 1. ⭐ List-Comprehensions

```python
# Vorher: 4 Zeilen
quadrate = []
for x in range(5):
    quadrate.append(x ** 2)

# Nachher: 1 Zeile
quadrate = [x ** 2 for x in range(5)]      # [0, 1, 4, 9, 16]
```

**Der Bauplan:**

```text
[  x ** 2   for   x   in   range(5)  ]
     ▲             ▲          ▲
  was rauskommt  Variable   worüber
```

💡 **Lesetrick:** Lies von rechts nach links: *„Für jedes x in range(5) … nimm x²."*

**Mit Filter:**

```python
[x for x in zahlen if x > 0]                # nur positive
[x**2 for x in zahlen if x % 2 == 0]        # Quadrate der geraden
```

**Mit if/else** (Achtung: steht **vorne**!):

```python
[x if x > 0 else 0 for x in zahlen]         # negative durch 0 ersetzen
```

```text
Filter  (nur if):        [ ausdruck  for x in daten  if bedingung ]
Umformen (if/else):      [ a if bed else b  for x in daten ]
```

### 2. Dict- und Set-Comprehensions

```python
{wort: len(wort) for wort in ["Hallo", "Welt"]}     # {'Hallo': 5, 'Welt': 4}
{v: k for k, v in d.items()}                        # Dict umdrehen ⭐
{len(w) for w in woerter}                           # Set: einmalige Längen
```

### 3. ⚠️ Wann NICHT

Comprehensions sind ein Werkzeug, kein Wettbewerb.

```python
# ❌ Zu viel - unlesbar
ergebnis = [y for x in daten if x for y in x.werte if y > 0 and y < 100]

# ✅ Lieber eine normale Schleife
ergebnis = []
for x in daten:
    if not x:
        continue
    for y in x.werte:
        if 0 < y < 100:
            ergebnis.append(y)
```

> 🧠 **Faustregel:** Passt es in eine Zeile und du verstehst es beim einmaligen Lesen → Comprehension. Sonst → Schleife. **Lesbarkeit schlägt Kürze. Immer.**

### 4. `enumerate` — Index + Wert

```python
for i, name in enumerate(namen):
    print(f"{i}: {name}")

for nr, name in enumerate(namen, start=1):
    print(f"{nr}. {name}")
```

❌ **Nicht mehr so:**
```python
for i in range(len(namen)):
    print(namen[i])          # funktioniert, ist aber unpythonisch
```

### 5. `zip` — mehrere Listen parallel 🤐

```python
namen = ["Anna", "Bernd", "Clara"]
alter = [30, 25, 41]

for name, a in zip(namen, alter):
    print(f"{name} ist {a}")

dict(zip(namen, alter))     # {'Anna': 30, 'Bernd': 25, 'Clara': 41} ⭐
```

⚠️ `zip` stoppt bei der **kürzesten** Liste.

### 6. `sorted` mit `key` 🔑

```python
sorted(woerter, key=len)                    # nach Länge
sorted(woerter, key=str.lower)              # alphabetisch, Groß/Klein egal
sorted(personen, key=lambda p: p["alter"])  # nach Dict-Feld
sorted(paare, key=lambda p: p[1], reverse=True)   # nach 2. Element, absteigend
```

`key` bekommt eine **Funktion**, die zu jedem Element den Sortierwert liefert.

### 7. `any` und `all`

```python
any([False, True, False])      # True   ← mindestens einer
all([True, True, False])       # False  ← alle?

# In der Praxis:
any(z.isdigit() for z in passwort)          # enthält eine Ziffer?
all(n <= 4.0 for n in noten)                # alle bestanden?
any(w.endswith(".pdf") for w in dateien)    # ist ein PDF dabei?
```

### 8. `lambda` — die Wegwerf-Funktion

```python
quadrat = lambda x: x ** 2       # ⚠️ so eher nicht

# ✅ So wird lambda benutzt: als Argument
sorted(personen, key=lambda p: p["alter"])
max(woerter, key=lambda w: len(w))
```

> 🧠 **Tutor sagt:** `lambda` niemals einer Variablen zuweisen — dafür gibt es `def`. `lambda` ist nur für Einweg-Funktionen als Argument gedacht.

### 9. Weitere nützliche Builtins

```python
sum(zahlen)                sum(zahlen, start=100)
min(zahlen)  max(zahlen)   min(woerter, key=len)
len(x)       abs(-5)       round(3.14, 1)
reversed(liste)            sorted(liste)
range(5)     list()        set()      dict()
type(x)      isinstance(x, int)
```

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `[x if x>0 for x in l]` | `SyntaxError` | `[x for x in l if x>0]` |
| `sorted(l, key=len())` | Klammern falsch | `key=len` (ohne Aufruf!) |
| `zip` mit Listen ungleicher Länge | stillschweigend gekürzt | Längen prüfen |
| `quadrat = lambda x: …` | schlechter Stil | `def quadrat(x):` |
| verschachtelte Comprehension | unlesbar | normale Schleife |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — inkl. „Schleife → Comprehension"-Umbauten

---

## 🛠️ Mini-Projekt: Refactoring-Runde ♻️

Nimm deine Lösungen aus **Modul 06 und 07** und schreib jede Schleife, die eine Liste aufbaut oder filtert, als Comprehension.

**Regel:** Wenn eine Comprehension unleserlich wird → **stehen lassen**. Notiere im Journal, welche du bewusst nicht umgebaut hast und warum. Das ist eine echte Entwickler-Entscheidung. 🎯

---

## 🧠 Selbsttest

1. Schreib `[x*2 for x in range(3)]` als normale Schleife.
2. Wo steht der Filter, wo das if/else?
3. Was macht `enumerate(liste, start=1)`?
4. Was macht `dict(zip(a, b))`?
5. Wie sortierst du nach Wortlänge?
6. Unterschied `any` / `all`?
7. Wann `lambda`?
8. Wann **keine** Comprehension?
9. Was passiert bei `zip` mit ungleich langen Listen?
10. ✍️ Erkläre eine Comprehension in Worten.

<details>
<summary>💡 Antworten</summary>

1. `r = []` / `for x in range(3): r.append(x*2)`
2. Filter (`if` allein) steht **hinten**, `if/else` steht **vorne** vor dem `for`.
3. Liefert Paare aus Index (ab 1) und Wert.
4. Baut ein Dictionary aus zwei parallelen Listen.
5. `sorted(woerter, key=len)`
6. `any`: mindestens eins wahr. `all`: alle wahr.
7. Als kurzes Funktionsargument, z. B. für `key=`.
8. Bei verschachtelter Logik, mehreren Bedingungen oder wenn man sie nicht in einem Blick versteht.
9. Sie wird auf die Länge der kürzeren gekürzt — ohne Warnung.
10. Z. B.: „Nimm jedes Element aus der Liste, prüfe die Bedingung, forme es um und sammle das Ergebnis in einer neuen Liste."
</details>

---

## 🔄 Wiederholung (Modul 07–09)

1. Wie liest du einen Traceback?
2. `print` vs. `return`?
3. Was macht `d.get("x", 0)`?
4. Warum darf man eine Liste beim Iterieren nicht verändern?

---

## 🔗 Vertiefung

- 📖 [Real Python — List Comprehensions](https://realpython.com/list-comprehension-python/)
- ⌨️ [Codewars 7 kyu](https://www.codewars.com/) — perfekt zum Üben von Comprehensions

**➡️ [Modul 11 — Dateien & Pfade](../11/README.md)** 🗂️
