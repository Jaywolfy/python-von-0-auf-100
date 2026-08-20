# 🔁 Modul 05 — Schleifen

> ⏱️ ~5 Stunden · ⬅️ [Modul 04](../04/README.md) · ➡️ [Modul 06](../06/README.md)

---

## 🎯 Lernziele

- [ ] `for`-Schleifen mit `range()` benutzen
- [ ] über Strings und Listen iterieren
- [ ] `while`-Schleifen schreiben (und keine Endlosschleife bauen 😅)
- [ ] `break` und `continue` einsetzen
- [ ] Schleifen verschachteln
- [ ] den **Akkumulator** kennen — das wichtigste Schleifenmuster

---

## 🌍 Warum das wichtig ist

Das hier ist der Moment, in dem Programmieren **mächtig** wird.

Ohne Schleife: 400 Dateien einzeln umbenennen. Mit Schleife: 3 Zeilen Code, fertig. Der ganze Sinn von Automatisierung — dein Kursziel — steckt in diesem Modul.

> 🧠 **Tutor sagt:** Wenn du dich beim Programmieren jemals dabei ertappst, Code zu kopieren und nur kleine Zahlen zu ändern — **das ist der Ruf nach einer Schleife.** 🔁

---

## 📖 Die Lektion

### 1. `for` mit `range()`

```python
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4      ← startet bei 0, hört VOR 5 auf!
```

```text
for  i  in  range(5) :
 ▲   ▲  ▲      ▲     ▲
 │   │  │      │     └── Doppelpunkt
 │   │  │      └──────── worüber wird gelaufen
 │   │  └─────────────── Schlüsselwort
 │   └────────────────── Laufvariable (Name frei wählbar)
 └────────────────────── Schleife
```

**`range()` in drei Varianten:**

```python
range(5)          # 0 1 2 3 4
range(2, 6)       # 2 3 4 5           (start, stop)
range(0, 10, 2)   # 0 2 4 6 8         (start, stop, schritt)
range(10, 0, -1)  # 10 9 8 … 1        rückwärts
```

### 2. Über Dinge iterieren

```python
for buchstabe in "Python":
    print(buchstabe)

for frucht in ["Apfel", "Birne", "Kirsche"]:
    print(f"Ich mag {frucht}")
```

💡 **Mit Index UND Wert** → `enumerate()`:

```python
for i, frucht in enumerate(["Apfel", "Birne"]):
    print(f"{i}: {frucht}")
# 0: Apfel
# 1: Birne

for i, frucht in enumerate(["Apfel", "Birne"], start=1):
    print(f"{i}. {frucht}")     # 1. Apfel
```

### 3. ⭐ Das Akkumulator-Muster

Das wichtigste Muster überhaupt. Merk es dir als Bild:

```text
1. Vor der Schleife: leeren Behälter anlegen
2. In der Schleife:  etwas hineintun
3. Nach der Schleife: Ergebnis benutzen
```

```python
summe = 0                      # 1. Behälter
for zahl in [3, 7, 2, 8]:
    summe += zahl              # 2. hineintun
print(summe)                   # 3. benutzen → 20
```

Funktioniert für alles:

```python
# Zählen
anzahl_a = 0
for z in "banana":
    if z == "a":
        anzahl_a += 1

# Sammeln
grosse = []
for zahl in [3, 15, 7, 22]:
    if zahl > 10:
        grosse.append(zahl)

# Maximum suchen
groesste = 0
for zahl in [3, 15, 7, 22]:
    if zahl > groesste:
        groesste = zahl

# Text aufbauen
text = ""
for wort in ["Hallo", "Welt"]:
    text += wort + " "
```

### 4. `while` — solange, bis …

`for` benutzt du, wenn du weißt, **wie oft**. `while`, wenn du weißt, **wann Schluss ist**.

```python
zaehler = 0
while zaehler < 5:
    print(zaehler)
    zaehler += 1        # ⚠️ ohne diese Zeile → Endlosschleife!
```

🌍 **Typischer Einsatz — Eingabe wiederholen:**

```python
while True:
    eingabe = input("Befehl (q zum Beenden): ")
    if eingabe == "q":
        break
    print(f"Du hast '{eingabe}' eingegeben")
```

> 🚨 **Endlosschleife erwischt?** `Strg + C` im Terminal. Passiert jedem. Kein Drama.

### 5. `break` und `continue`

```python
# break: raus aus der Schleife
for zahl in range(100):
    if zahl > 5:
        break
    print(zahl)              # 0 1 2 3 4 5

# continue: diesen Durchlauf überspringen
for zahl in range(10):
    if zahl % 2 != 0:
        continue             # ungerade überspringen
    print(zahl)              # 0 2 4 6 8
```

| | Wirkung |
|---|---|
| `break` | Schleife **komplett** verlassen 🛑 |
| `continue` | zum **nächsten Durchlauf** springen ⏭️ |

### 6. Verschachtelte Schleifen

```python
for zeile in range(3):
    for spalte in range(4):
        print("*", end=" ")
    print()          # Zeilenumbruch nach jeder Zeile
```

```text
* * * *
* * * *
* * * *
```

⚠️ Die innere Schleife läuft **komplett durch** bei jedem Durchlauf der äußeren. Bei 3 × 4 sind das 12 Durchläufe.

### 7. `for … else` (selten, aber nützlich)

```python
for zahl in [1, 3, 5]:
    if zahl % 2 == 0:
        print("Gerade Zahl gefunden!")
        break
else:
    print("Keine gerade Zahl dabei.")     # läuft nur ohne break
```

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `while` ohne Änderung | Endlosschleife 🔄 | Zähler erhöhen |
| `range(1,10)` erwartet 10 | endet bei 9 | `range(1, 11)` |
| Akkumulator **in** der Schleife | wird jedes Mal zurückgesetzt | vor die Schleife |
| Liste beim Iterieren ändern | überspringt Elemente | neue Liste bauen |
| Falsche Einrückung | Code läuft im falschen Block | `indent-rainbow` 🌈 |

```python
# ❌ Klassiker: Akkumulator an der falschen Stelle
for z in [1,2,3]:
    summe = 0       # wird JEDES Mal auf 0 gesetzt!
    summe += z
print(summe)        # 3 statt 6

# ✅
summe = 0
for z in [1,2,3]:
    summe += z
```

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

| # | Aufgabe | Level |
|:---:|---|:---:|
| 1 | Von 1 bis 20 zählen | 🟢 |
| 2 | Summe von 1 bis 100 | 🟢 |
| 3 | Buchstaben eines Wortes einzeln | 🟢 |
| 4 | Nur gerade Zahlen (mit `continue`) | 🟡 |
| 5 | Kleines Einmaleins (verschachtelt) | 🟡 |
| 6 | Vokale zählen | 🟡 |
| 7 | FizzBuzz | 🔴 |
| 8 | Pyramide aus Sternchen | 🔴 |
| 9 | Zahlenraten mit `while` | 🔴 |
| 10 ⭐ | Primzahlen bis 50 | ⭐ |

---

## 🛠️ Mini-Projekt: ASCII-Muster-Generator

`muster.py` gibt diese vier Muster aus (Größe über eine Variable steuerbar):

```text
Muster 1        Muster 2        Muster 3        Muster 4
*               *****           *                   *
**              ****             **                **
***             ***               ***             ***
****            **                 ****          ****
*****           *                   *****       *****
```

**Anforderung:** Alle vier mit verschachtelten Schleifen. Höhe nur an **einer** Stelle im Code ändern müssen.

---

## 🧠 Selbsttest

1. Was gibt `range(3)` aus?
2. Wann `for`, wann `while`?
3. Unterschied `break` / `continue`?
4. Warum muss der Akkumulator **vor** die Schleife?
5. Wie iterierst du mit Index und Wert gleichzeitig?
6. Wie erzeugst du `10, 9, 8, …, 1`?
7. Wie oft läuft die innere Schleife bei `for i in range(3): for j in range(5):`?
8. Wie brichst du eine Endlosschleife im Terminal ab?
9. Was macht `for … else`?
10. ✍️ Erkläre den Akkumulator an einem Alltagsbeispiel.

<details>
<summary>💡 Antworten</summary>

1. `0, 1, 2`
2. `for`: bekannte Anzahl / über etwas iterieren. `while`: unbekannte Anzahl, Abbruch durch Bedingung.
3. `break` verlässt die Schleife. `continue` springt zum nächsten Durchlauf.
4. Sonst wird er bei jedem Durchlauf zurückgesetzt.
5. `for i, wert in enumerate(liste):`
6. `range(10, 0, -1)`
7. 15-mal (3 × 5).
8. `Strg + C`
9. Der `else`-Block läuft nur, wenn die Schleife **ohne** `break` zu Ende ging.
10. Z. B.: „Einkaufskorb: Ich starte mit leerem Korb (vor der Schleife), gehe durch alle Regale (Schleife) und lege passende Sachen rein (`append`). Am Ende schaue ich in den Korb."
</details>

---

## 🔄 Wiederholung (Modul 02–04)

1. Was ergibt `"Python"[2:5]`?
2. Was gilt in Python als `False`?
3. Wie prüfst du, ob eine Zahl gerade ist?
4. Was ist der Unterschied zwischen mehreren `if` und `if/elif`?

---

## 🔗 Vertiefung

- 📖 [Real Python — for Loops](https://realpython.com/python-for-loop/)
- 🔍 [Python Tutor](https://pythontutor.com/visualize.html) — **unbedingt** eine verschachtelte Schleife visualisieren!

**➡️ [Modul 06 — Listen](../06/README.md)** 📋
