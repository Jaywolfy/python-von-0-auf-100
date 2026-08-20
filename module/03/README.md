# 🧮 Modul 03 — Zahlen & Ein-/Ausgabe

> ⏱️ ~5 Stunden · ⬅️ [Modul 02](../02/README.md) · ➡️ [Modul 04](../04/README.md)

---

## 🎯 Lernziele

- [ ] alle Rechenoperatoren sicher benutzen — inklusive `//` und `%`
- [ ] mit `input()` Eingaben vom Nutzer holen
- [ ] verstehen, warum `input()` **immer** einen String liefert
- [ ] Zahlen sauber runden und formatieren
- [ ] die Float-Falle kennen (`0.1 + 0.2 != 0.3`)

---

## 🌍 Warum das wichtig ist

Ab jetzt sind deine Programme **interaktiv**. Sie reden mit dir. Und `%` (Modulo) — der Operator, den alle unterschätzen — ist später der Schlüssel für „jede 3. Zeile", „gerade Zahlen", „Zeit in Stunden und Minuten" und dutzende Alltagsprobleme.

---

## 📖 Die Lektion

### 1. Die Rechenoperatoren

| Operator | Bedeutung | Beispiel | Ergebnis |
|:---:|---|---|---|
| `+` | Addition | `7 + 3` | `10` |
| `-` | Subtraktion | `7 - 3` | `4` |
| `*` | Multiplikation | `7 * 3` | `21` |
| `/` | Division | `7 / 3` | `2.333…` ⚠️ immer float! |
| `//` | Ganzzahldivision | `7 // 3` | `2` |
| `%` | Rest (Modulo) | `7 % 3` | `1` |
| `**` | Potenz | `7 ** 3` | `343` |

⚠️ **`/` liefert immer einen float — auch wenn es aufgeht:**

```python
print(10 / 2)          # 5.0    ← nicht 5!
print(type(10 / 2))    # <class 'float'>
print(10 // 2)         # 5      ← int
```

### 2. ⭐ Modulo `%` verstehen

`%` gibt den **Rest** einer Division zurück.

```text
17 : 5 = 3 Rest 2
        ▲       ▲
     17 // 5    17 % 5
```

**Warum das so nützlich ist:**

```python
# Gerade oder ungerade?
zahl % 2 == 0          # True = gerade

# Ist zahl durch 3 teilbar?
zahl % 3 == 0

# Sekunden in Minuten:Sekunden umrechnen
sekunden = 197
minuten = sekunden // 60     # 3
rest     = sekunden % 60     # 17     →  3:17

# Letzte Ziffer einer Zahl
1234 % 10                    # 4

# Immer im Bereich 0-6 bleiben (Wochentage)
(heute + 10) % 7
```

> 🧠 **Tutor sagt:** Wenn du später denkst „ich brauche jedes n-te Element" oder „das soll umlaufen wie eine Uhr" — dann ist die Antwort fast immer `%`. Lern ihn jetzt richtig.

### 3. Rundung & Mathe-Funktionen

```python
round(3.7)             # 4
round(3.14159, 2)      # 3.14
round(2.5)             # 2  ⚠️ kaufmännisch? Nein! (siehe unten)
abs(-5)                # 5
min(3, 7, 1)           # 1
max(3, 7, 1)           # 7
sum([1, 2, 3])         # 6
pow(2, 10)             # 1024   (= 2 ** 10)
```

⚠️ **Bankers Rounding:** Python rundet `.5` zur **nächsten geraden Zahl** (`round(2.5)` → `2`, `round(3.5)` → `4`). Das ist ein statistischer Standard, kein Bug. Für Geldbeträge nutzt man später `decimal`.

**Mehr Mathe? → `math` importieren:**

```python
import math

math.sqrt(16)          # 4.0     Wurzel
math.floor(3.9)        # 3       abrunden
math.ceil(3.1)         # 4       aufrunden
math.pi                # 3.14159…
```

### 4. 💧 Die Float-Falle

```python
print(0.1 + 0.2)                # 0.30000000000000004  😱
print(0.1 + 0.2 == 0.3)         # False
```

Kein Bug! Computer speichern Kommazahlen binär, und `0.1` ist binär eine unendliche Zahl — wie `1/3` im Dezimalsystem. Es wird gerundet.

**Wie du damit umgehst:**

```python
round(0.1 + 0.2, 2) == 0.3           # ✅ True
abs((0.1 + 0.2) - 0.3) < 1e-9        # ✅ Profi-Variante
```

💰 **Für Geld:** Später `from decimal import Decimal` — oder in **Cent als `int`** rechnen. Merk dir das schon mal.

### 5. `input()` — mit dem Nutzer sprechen 💬

```python
name = input("Wie heißt du? ")
print(f"Hallo {name}!")
```

Das Programm **hält an** und wartet auf Enter.

### 6. ⚠️ `input()` gibt IMMER einen String

Das ist **die** klassische Falle:

```python
alter = input("Alter: ")      # Nutzer tippt 25
print(alter + 1)              # ❌ TypeError!
print(type(alter))            # <class 'str'>   ← es ist Text!
```

**Richtig:**

```python
alter = int(input("Alter: "))        # ✅ direkt umwandeln
groesse = float(input("Größe: "))    # ✅ für Kommazahlen
```

⚠️ Tippt der Nutzer `abc`, gibt es einen `ValueError`. Wie man den abfängt, kommt in Modul 13 — bis dahin gehen wir davon aus, dass sinnvolle Werte eingegeben werden.

### 7. Ausgabe schön formatieren

```python
preis = 1234.5678

print(f"Preis: {preis:.2f} €")           # Preis: 1234.57 €
print(f"Preis: {preis:>12,.2f} €")       # Preis:     1,234.57 €
```

🇩🇪 **Deutsches Zahlenformat** (Punkt als Tausender, Komma als Dezimaltrenner):

```python
formatiert = f"{preis:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(formatiert)      # 1.234,57
```

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `input()` + Zahl | `TypeError` | `int(input(...))` |
| `10 / 3` erwartet `3` | gibt `3.33` | `10 // 3` |
| `0.1 + 0.2 == 0.3` | `False` | `round(...)` vergleichen |
| `int("3.5")` | `ValueError` | `int(float("3.5"))` |
| Division durch 0 | `ZeroDivisionError` | vorher prüfen |
| `5 % 0` | `ZeroDivisionError` | vorher prüfen |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

| # | Aufgabe | Level |
|:---:|---|:---:|
| 1 | Alle 7 Operatoren ausgeben | 🟢 |
| 2 | Name & Alter abfragen | 🟢 |
| 3 | Rechteck: Fläche & Umfang | 🟢 |
| 4 | Sekunden → h:min:s | 🟡 |
| 5 | BMI-Rechner | 🟡 |
| 6 | Trinkgeld-Rechner mit Aufteilung | 🟡 |
| 7 | Zahl in Einzelziffern zerlegen (nur Mathe!) | 🔴 |
| 8 | Kredit-Zinsrechner | 🔴 |
| 9 ⭐ | Einheiten-Umrechner (Temperatur & Länge) | ⭐ |

---

## 🛠️ Mini-Projekt: Einheiten-Umrechner

`umrechner.py` fragt Werte ab und gibt eine formatierte Umrechnungstabelle aus:

```text
════════════════════════════════════════
   EINHEITEN-UMRECHNER
════════════════════════════════════════
Temperatur eingeben (°C): 23.5

   23.50 °C  =    74.30 °F
   23.50 °C  =   296.65 K

Länge eingeben (km): 5
    5.00 km  =  5000.00 m
    5.00 km  =     3.11 Meilen
    5.00 km  = 16404.20 Fuß
════════════════════════════════════════
```

**Formeln:** `°F = °C * 9/5 + 32` · `K = °C + 273.15` · `Meilen = km * 0.621371` · `Fuß = m * 3.28084`

---

## 🧠 Selbsttest

1. Was ergibt `7 // 2` und `7 % 2`?
2. Welchen Typ hat `10 / 5`?
3. Wozu benutzt man `%` typischerweise?
4. Welchen Typ gibt `input()` zurück?
5. Wie liest du eine Zahl vom Nutzer ein?
6. Warum ist `0.1 + 0.2 == 0.3` falsch?
7. Wie rundest du auf 2 Nachkommastellen?
8. Was ergibt `2 ** 10`?
9. Wie prüfst du, ob eine Zahl gerade ist?
10. ✍️ Erkläre `%` an einem Alltagsbeispiel.

<details>
<summary>💡 Antworten</summary>

1. `3` und `1`
2. `float` — `/` gibt immer float.
3. Teilbarkeit prüfen, Rest berechnen, „jedes n-te", umlaufende Werte (Uhrzeit, Wochentage).
4. Immer `str`.
5. `zahl = int(input("..."))`
6. Kommazahlen werden binär gespeichert und dabei gerundet; kleine Ungenauigkeiten summieren sich.
7. `round(x, 2)` oder `f"{x:.2f}"` (Letzteres nur für die Anzeige!).
8. `1024`
9. `zahl % 2 == 0`
10. Z. B.: „Ich habe 17 Bonbons und verteile sie an 5 Kinder. Jedes bekommt 3 (`17 // 5`), 2 bleiben übrig (`17 % 5`)."
</details>

---

## 🔄 Wiederholung (Modul 01–02)

1. Wie gibst du `3.14159` mit 2 Nachkommastellen aus?
2. Was macht `"a,b,c".split(",")`?
3. Was ergibt `"5" * 3`?
4. Warum ändert `s.strip()` die Variable `s` nicht?

---

## 🔗 Vertiefung

- 📖 [Real Python — Numbers](https://realpython.com/python-numbers/)
- 🔍 [Warum 0.1 + 0.2 ≠ 0.3](https://docs.python.org/3/tutorial/floatingpoint.html)

**➡️ [Modul 04 — Bedingungen](../04/README.md)** 🔀
