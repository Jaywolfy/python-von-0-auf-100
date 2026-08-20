# 📋 Modul 06 — Listen

> ⏱️ ~5 Stunden · ⬅️ [Modul 05](../05/README.md) · ➡️ [Modul 07](../07/README.md)

---

## 🎯 Lernziele

- [ ] Listen erstellen, lesen, ändern
- [ ] die wichtigsten Listen-Methoden (`append`, `remove`, `sort`, …)
- [ ] Listen mit Schleifen kombinieren
- [ ] verschachtelte Listen verstehen
- [ ] die **Kopier-Falle** kennen (sehr wichtig! ⚠️)

---

## 🌍 Warum das wichtig ist

Bisher hattest du **eine** Variable pro Wert. Bei 500 Dateinamen wäre das unmöglich.

Listen sind der Behälter für „viele Dinge derselben Art". Jede Datei, die du später einliest, jede API-Antwort, jede Tabellenzeile — alles landet in Listen.

---

## 📖 Die Lektion

### 1. Listen erstellen

```python
zahlen = [3, 1, 4, 1, 5]
namen = ["Anna", "Bernd", "Clara"]
gemischt = [1, "zwei", 3.0, True]       # erlaubt, aber selten sinnvoll
leer = []
```

🏠 **Alltagsbild:** Eine Liste ist ein **Schuhregal mit nummerierten Fächern**. Fach 0, Fach 1, Fach 2 …

### 2. Zugreifen — Index & Slicing

```text
namen = [ "Anna", "Bernd", "Clara", "David" ]
Index      0        1        2        3
          -4       -3       -2       -1
```

```python
namen[0]       # 'Anna'
namen[-1]      # 'David'    ⭐ letztes Element
namen[1:3]     # ['Bernd', 'Clara']
namen[:2]      # ['Anna', 'Bernd']
namen[::-1]    # umgedreht
len(namen)     # 4
namen[4]       # ❌ IndexError
```

### 3. Ändern — Listen sind *mutable* 🔄

Anders als Strings kann man Listen direkt verändern:

```python
namen[0] = "Anni"        # ✅ geht! (bei Strings wäre das ein Fehler)
```

### 4. Die wichtigsten Methoden 🧰

```python
liste = [3, 1, 4]

liste.append(5)          # [3,1,4,5]      ans Ende  ⭐ meistgenutzt
liste.insert(0, 9)       # [9,3,1,4,5]    an Position
liste.extend([6, 7])     # [9,3,1,4,5,6,7]  mehrere anhängen
liste.remove(1)          # entfernt den WERT 1 (erstes Vorkommen)
x = liste.pop()          # letztes Element entfernen UND zurückgeben
x = liste.pop(0)         # erstes
del liste[0]             # nach Index löschen
liste.clear()            # alles weg
```

⚠️ **`remove(1)` löscht den Wert 1 — `pop(1)` löscht die Position 1!** Verwechselt jeder mal.

**Sortieren:**

```python
liste.sort()                 # ändert die Liste selbst, gibt None zurück
liste.sort(reverse=True)     # absteigend
liste.sort(key=len)          # nach Kriterium (z.B. Wortlänge)

neue = sorted(liste)         # gibt eine NEUE Liste zurück, Original bleibt
liste.reverse()              # umdrehen
```

🚨 **Klassiker:**

```python
liste = liste.sort()     # ❌ liste ist jetzt None!
liste.sort()             # ✅
liste = sorted(liste)    # ✅
```

**Suchen & Zählen:**

```python
3 in liste           # True/False    ⭐ sehr häufig
liste.count(3)       # wie oft
liste.index(3)       # an welcher Position (ValueError wenn nicht da)
sum(liste)           # Summe
min(liste), max(liste)
```

### 5. Listen + Schleifen ⭐

```python
for name in namen:
    print(name)

for i, name in enumerate(namen):
    print(f"{i}: {name}")

# Filtern (Akkumulator-Muster aus Modul 05)
lange_namen = []
for name in namen:
    if len(name) > 4:
        lange_namen.append(name)
```

### 6. ⚠️ Die Kopier-Falle — sehr wichtig!

```python
a = [1, 2, 3]
b = a               # ⚠️ das ist KEINE Kopie!
b.append(4)
print(a)            # [1, 2, 3, 4]   😱 a hat sich auch geändert!
```

🏠 **Warum?** `b = a` klebt nur ein **zweites Etikett auf denselben Karton**. Es gibt weiterhin nur eine Liste.

```text
a ──┐
    ├──► [1, 2, 3, 4]
b ──┘
```

**Richtig kopieren:**

```python
b = a.copy()        # ✅
b = list(a)         # ✅
b = a[:]            # ✅
```

> 🧠 **Tutor sagt:** Diese Falle erwischt **jeden** einmal — und der Fehler ist gemein, weil er keinen Absturz verursacht, sondern nur falsche Daten. Wenn Werte sich „von selbst" ändern: hier nachschauen. Zum Anschauen: [pythontutor.com](https://pythontutor.com/visualize.html) 👀

### 7. Verschachtelte Listen

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

matrix[0]        # [1, 2, 3]
matrix[0][1]     # 2          ← Zeile 0, Spalte 1

for zeile in matrix:
    for wert in zeile:
        print(wert, end=" ")
    print()
```

🌍 Genau so sieht später eine eingelesene Excel- oder CSV-Tabelle aus.

### 8. Praktische Umwandlungen

```python
list("abc")                    # ['a','b','c']
list(range(5))                 # [0,1,2,3,4]
"a,b,c".split(",")             # ['a','b','c']
"-".join(["a","b","c"])        # 'a-b-c'
```

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `liste = liste.sort()` | `None` | `liste.sort()` ohne Zuweisung |
| `b = a` als Kopie gedacht | beide ändern sich | `b = a.copy()` |
| `remove()` vs. `pop()` | Wert vs. Index | genau überlegen |
| beim Iterieren löschen | überspringt Elemente | neue Liste bauen |
| `liste[len(liste)]` | `IndexError` | `liste[-1]` |

```python
# ❌ Beim Iterieren verändern
for x in liste:
    if x < 0:
        liste.remove(x)        # überspringt Elemente!

# ✅
liste = [x for x in liste if x >= 0]        # Comprehension (Modul 10)
# oder:
neue = []
for x in liste:
    if x >= 0:
        neue.append(x)
liste = neue
```

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — 10 Aufgaben inkl. 🥗 Mix-Aufgaben (Strings + Schleifen + Listen)

---

## 🛠️ Mini-Projekt: To-do-Liste im Terminal

`todo.py` mit Menü:

```text
╔══════════════════════════════╗
║      MEINE TO-DOS 📝         ║
╚══════════════════════════════╝
  1. [ ] Einkaufen
  2. [✓] Python lernen
  3. [ ] Wäsche

[a] Hinzufügen  [e] Erledigt  [l] Löschen  [q] Beenden
> _
```

**Anforderungen:** `while True` + `break` · zwei Listen (Aufgaben + Status) oder eine Liste von Listen · Menü mit `if/elif` · Nummerierung ab 1

---

## 🧠 Selbsttest

1. Wie holst du das letzte Element einer Liste?
2. Unterschied `append` / `extend` / `insert`?
3. Was gibt `liste.sort()` zurück?
4. Unterschied `sort()` / `sorted()`?
5. Warum ändert `b = a; b.append(1)` auch `a`?
6. Wie kopierst du eine Liste richtig (3 Wege)?
7. Unterschied `remove(2)` / `pop(2)`?
8. Wie greifst du auf Zeile 1, Spalte 2 einer Matrix zu?
9. Wie prüfst du, ob ein Wert in einer Liste ist?
10. ✍️ Erkläre die Kopier-Falle mit dem Karton-Bild.

<details>
<summary>💡 Antworten</summary>

1. `liste[-1]`
2. `append` hängt **ein** Element an · `extend` hängt **mehrere** an · `insert(i, x)` fügt an Position `i` ein.
3. `None` — es sortiert die Liste **an Ort und Stelle**.
4. `sort()` verändert die Liste, `sorted()` gibt eine neue zurück.
5. Weil `b = a` nur einen zweiten Namen für dieselbe Liste erzeugt.
6. `a.copy()`, `list(a)`, `a[:]`
7. `remove(2)` löscht den **Wert** 2, `pop(2)` das Element an **Index** 2.
8. `matrix[1][2]`
9. `wert in liste`
10. Z. B.: „`b = a` klebt nur ein zweites Etikett auf denselben Karton. Wer über eines der Etiketten etwas hineinlegt, ändert den Inhalt für beide. `a.copy()` baut einen echten zweiten Karton."
</details>

---

## 🔄 Wiederholung (Modul 03–05)

1. Was ergibt `17 // 5` und `17 % 5`?
2. Was macht `continue`?
3. Warum muss der Akkumulator vor die Schleife?
4. Was gilt als `False`?

---

## 🔗 Vertiefung

- 📖 [Real Python — Lists](https://realpython.com/python-lists-tuples/)
- 📄 [Spickzettel Listen & Dicts](../../spickzettel/listen-dicts.md)

**➡️ [Modul 07 — Dicts, Tupel & Sets](../07/README.md)** 🗃️
