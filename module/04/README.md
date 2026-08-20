# 🔀 Modul 04 — Bedingungen (if / elif / else)

> ⏱️ ~5 Stunden · ⬅️ [Modul 03](../03/README.md) · ➡️ [Modul 05](../05/README.md)

---

## 🎯 Lernziele

- [ ] mit `if` / `elif` / `else` Entscheidungen treffen
- [ ] Vergleichsoperatoren sicher benutzen
- [ ] `and`, `or`, `not` kombinieren
- [ ] **Einrückung** als Logik verstehen (Pythons Besonderheit!)
- [ ] Truthiness verstehen: was gilt als „wahr"?

---

## 🌍 Warum das wichtig ist

Bis jetzt lief dein Code stur von oben nach unten. Ab jetzt kann er **abzweigen**.

Das ist der Moment, in dem Programme aufhören, Taschenrechner zu sein, und anfangen, **Entscheidungen** zu treffen: „Wenn die Datei ein PDF ist, verschiebe sie in den PDF-Ordner." „Wenn der Wert fehlt, überspringe die Zeile." Jedes Programm, das du je schreiben wirst, steckt voller `if`.

---

## 📖 Die Lektion

### 1. Das einfache `if`

```python
temperatur = 35

if temperatur > 30:
    print("Es ist heiß! 🥵")
    print("Trink genug Wasser.")

print("Das läuft immer.")
```

```text
if temperatur > 30 :
▲       ▲              ▲
│       │              └── Doppelpunkt! Nicht vergessen ⚠️
│       └───────────────── die Bedingung (ergibt True oder False)
└───────────────────────── Schlüsselwort
```

⚠️ **Zwei Dinge, die Anfänger vergessen:**
1. Der **Doppelpunkt** `:` am Ende
2. Die **Einrückung** (4 Leerzeichen) der Folgezeilen

### 2. 🔑 Einrückung IST die Logik

In den meisten Sprachen nutzt man `{ }`. Python nutzt **Einrückung**. Das ist keine Kosmetik — es bestimmt, was zusammengehört.

```python
if temperatur > 30:
    print("A")          # gehört zum if
    print("B")          # gehört zum if
print("C")              # gehört NICHT zum if - läuft immer
```

```text
if bedingung:
│
├─── 4 Leerzeichen ──► gehört dazu
├─── 4 Leerzeichen ──► gehört dazu
│
└─ keine Einrückung ─► gehört NICHT mehr dazu
```

> 🧠 **Tutor sagt:** 90 % der „mein Programm macht was Komisches"-Fälle bei Anfängern sind Einrückungsfehler. Deshalb steht in SETUP.md die Extension **indent-rainbow** — die färbt Einrückungsebenen ein, und du *siehst* die Struktur sofort. 🌈

### 3. `else` und `elif`

```python
alter = 17

if alter >= 18:
    print("Volljährig ✅")
else:
    print("Minderjährig ❌")
```

`elif` = „else if" — für mehrere Fälle:

```python
note = 85

if note >= 90:
    print("Sehr gut 🌟")
elif note >= 80:
    print("Gut 👍")
elif note >= 70:
    print("Befriedigend 🙂")
else:
    print("Nachsitzen 📚")
```

⚠️ **Wichtig:** Python prüft **von oben nach unten** und steigt beim **ersten Treffer aus**. Die Reihenfolge ist entscheidend!

```python
# ❌ FALSCH - alles landet im ersten Zweig
if note >= 70:
    print("Befriedigend")
elif note >= 90:      # wird NIE erreicht, wenn note >= 70
    print("Sehr gut")
```

### 4. Vergleichsoperatoren

| Operator | Bedeutung | Beispiel |
|:---:|---|---|
| `==` | gleich | `x == 5` |
| `!=` | ungleich | `x != 5` |
| `<` `>` | kleiner / größer | `x < 5` |
| `<=` `>=` | kleiner-gleich / größer-gleich | `x <= 5` |
| `in` | enthalten in | `"a" in "hallo"` |
| `not in` | nicht enthalten | `5 not in liste` |

🚨 **Der Klassiker:** `=` ist Zuweisung, `==` ist Vergleich!

```python
if x = 5:     # ❌ SyntaxError
if x == 5:    # ✅
```

💡 **Python kann Vergleiche verketten** (viele Sprachen können das nicht):

```python
if 0 <= note <= 100:      # ✅ elegant
if note >= 0 and note <= 100:    # gleichbedeutend, aber länger
```

### 5. Logische Operatoren

| Operator | Wahr, wenn … | Beispiel |
|---|---|---|
| `and` | **beide** wahr sind | `alter >= 18 and hat_ausweis` |
| `or` | **mindestens eins** wahr ist | `ist_wochenende or ist_feiertag` |
| `not` | das Gegenteil | `not ist_angemeldet` |

```python
alter = 25
fuehrerschein = True

if alter >= 18 and fuehrerschein:
    print("Darf fahren 🚗")

if alter < 6 or alter > 65:
    print("Ermäßigt 🎫")

if not fuehrerschein:
    print("Erst Führerschein machen!")
```

**Wahrheitstabelle:**

| A | B | `A and B` | `A or B` |
|:---:|:---:|:---:|:---:|
| ✅ | ✅ | ✅ | ✅ |
| ✅ | ❌ | ❌ | ✅ |
| ❌ | ✅ | ❌ | ✅ |
| ❌ | ❌ | ❌ | ❌ |

⚠️ **Häufiger Denkfehler:**

```python
if name == "Anna" or "Bernd":     # ❌ funktioniert scheinbar, ist aber falsch!
if name == "Anna" or name == "Bernd":     # ✅
if name in ("Anna", "Bernd"):             # ✅✅ noch besser
```

*Warum falsch?* `"Bernd"` allein ist ein nicht-leerer String → immer `True` → die Bedingung ist **immer** wahr.

### 6. ⭐ Truthiness — was gilt als „wahr"?

Python kann **jeden** Wert als Wahrheitswert deuten:

| Gilt als `False` 🚫 | Gilt als `True` ✅ |
|---|---|
| `False`, `None` | alle anderen Werte |
| `0`, `0.0` | jede Zahl ≠ 0 |
| `""` (leerer String) | jeder nicht-leere String |
| `[]`, `{}`, `()`, `set()` | jede nicht-leere Sammlung |

```python
name = ""

if name:                     # ✅ pythonisch
    print("Name vorhanden")
else:
    print("Kein Name")

# statt: if len(name) > 0:
```

### 7. Verschachteln — und wie man es vermeidet

```python
# 😰 Verschachtelt - schwer lesbar
if angemeldet:
    if guthaben > 0:
        if artikel_verfuegbar:
            print("Kauf möglich")

# 😍 Flach - viel besser
if angemeldet and guthaben > 0 and artikel_verfuegbar:
    print("Kauf möglich")
```

💡 **Guard Clause** — früh aussteigen statt tief verschachteln:

```python
if not angemeldet:
    print("Bitte anmelden")
elif guthaben <= 0:
    print("Guthaben aufladen")
elif not artikel_verfuegbar:
    print("Nicht verfügbar")
else:
    print("Kauf möglich ✅")
```

### 8. Der Ternary-Operator (Kurzform)

```python
status = "warm" if temp > 20 else "kalt"

# entspricht:
if temp > 20:
    status = "warm"
else:
    status = "kalt"
```

Praktisch für einfache Fälle — nicht für komplexe Logik.

---

## ⚠️ Typische Anfängerfehler

| Fehler | Meldung | Fix |
|---|---|---|
| Doppelpunkt vergessen | `SyntaxError` | `if x > 5:` |
| Nicht eingerückt | `IndentationError` | 4 Leerzeichen |
| `=` statt `==` | `SyntaxError` | `==` zum Vergleichen |
| `if x == "a" or "b"` | immer `True` | `x in ("a","b")` |
| `elif`-Reihenfolge falsch | falsches Ergebnis | vom Spezifischsten zum Allgemeinsten |
| `if x == True:` | umständlich | einfach `if x:` |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

| # | Aufgabe | Level |
|:---:|---|:---:|
| 1 | Gerade oder ungerade | 🟢 |
| 2 | Volljährigkeit | 🟢 |
| 3 | Größte von drei Zahlen | 🟢 |
| 4 | Notenrechner | 🟡 |
| 5 | Eintrittspreis nach Alter & Tag | 🟡 |
| 6 | Passwort-Prüfer | 🟡 |
| 7 | Schaltjahr berechnen | 🔴 |
| 8 | Dateityp erkennen & einsortieren | 🔴 |
| 9 ⭐ | Verschachtelten Code entwirren | ⭐ |

---

## 🛠️ Mini-Projekt: Passwort-Prüfer

`passwort_check.py` bewertet ein Passwort:

```text
═══════════════════════════════════
   PASSWORT-PRÜFER 🔐
═══════════════════════════════════
Passwort: Sonne2026!

✅ Mindestens 8 Zeichen
✅ Enthält Großbuchstaben
✅ Enthält Kleinbuchstaben
✅ Enthält Ziffer
✅ Enthält Sonderzeichen
❌ Nicht in der Liste bekannter Passwörter

Stärke: ████████░░  4/5 — STARK 💪
═══════════════════════════════════
```

**Tipps:** `len()` · `any(c.isupper() for c in pw)` (oder zunächst per Hand mit `if`) · `pw in ("passwort", "123456", "qwertz")`

---

## 🧠 Selbsttest

1. Was gehört bei `if` zum Block — woran erkennt Python das?
2. Unterschied zwischen `=` und `==`?
3. Wann läuft der `else`-Zweig?
4. Was ist der Unterschied zwischen mehreren `if` und `if/elif`?
5. Wann ist `and` wahr, wann `or`?
6. Welche Werte gelten als `False`?
7. Warum ist `if x == "a" or "b"` falsch?
8. Was macht `if liste:`?
9. Schreib `if x > 5: y = "groß" else: y = "klein"` als Ternary.
10. ✍️ Erkläre `elif` an einem Alltagsbeispiel.

<details>
<summary>💡 Antworten</summary>

1. Alles, was **eingerückt** unter dem `if` steht (üblicherweise 4 Leerzeichen).
2. `=` weist zu, `==` vergleicht.
3. Wenn keine der Bedingungen davor `True` war.
4. Mehrere `if` werden **alle** geprüft. Bei `if/elif` steigt Python nach dem **ersten Treffer** aus.
5. `and`: beide wahr. `or`: mindestens einer wahr.
6. `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`
7. Weil `"b"` allein als eigener Wahrheitswert ausgewertet wird — und ein nicht-leerer String ist immer `True`.
8. Prüft, ob die Liste **nicht leer** ist.
9. `y = "groß" if x > 5 else "klein"`
10. Z. B.: „Was ziehe ich an? *Wenn* es regnet → Regenjacke. *Sonst wenn* es kalt ist → Mantel. *Sonst wenn* es warm ist → T-Shirt. *Sonst* → Pullover. Sobald ein Fall passt, höre ich auf zu prüfen."
</details>

---

## 🔄 Wiederholung (Modul 01–03)

1. Was gibt `input()` zurück und was musst du oft damit machen?
2. Was ergibt `17 % 5`?
3. Wie gibst du `x` mit 2 Nachkommastellen aus?
4. Was ergibt `"Python"[::-1]`?

---

## 🔗 Vertiefung

- 📖 [Real Python — Conditional Statements](https://realpython.com/python-conditional-statements/)
- 🔍 [Python Tutor](https://pythontutor.com/visualize.html) — verschachteltes `if` Schritt für Schritt ansehen

**➡️ [Modul 05 — Schleifen](../05/README.md)** 🔁
