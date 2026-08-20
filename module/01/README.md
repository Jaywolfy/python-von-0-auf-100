# 📦 Modul 01 — Variablen & Datentypen

> ⏱️ ~5 Stunden · ⬅️ [Modul 00](../00/README.md) · ➡️ [Modul 02](../02/README.md)

---

## 🎯 Lernziele

- [ ] Werte in Variablen speichern und wiederverwenden
- [ ] die vier Grundtypen unterscheiden: `str`, `int`, `float`, `bool`
- [ ] `type()` benutzen, um Typen zu prüfen
- [ ] gute Variablennamen vergeben
- [ ] verstehen, warum Typen überhaupt wichtig sind

---

## 🌍 Warum das wichtig ist

Ohne Variablen wäre jedes Programm ein Einwegprogramm. Mit Variablen kannst du Werte **merken**, **weiterreichen** und **verändern**.

Jedes echte Programm besteht im Kern daraus: *Daten reinholen → in Variablen ablegen → verarbeiten → ausgeben.* Dein späterer Ordner-Aufräumer speichert Pfade in Variablen. Dein Excel-Skript speichert Zellwerte in Variablen. Immer dasselbe Muster.

---

## 📖 Die Lektion

### 1. Was ist eine Variable? 📦

🏠 **Alltagsbild:** Ein **beschrifteter Karton**. Du legst etwas rein und klebst ein Etikett drauf. Später sagst du nur noch „hol mir, was im Karton *alter* ist".

```python
alter = 25
```

```text
alter    =    25
  ▲      ▲     ▲
  │      │     └── der Wert, der gespeichert wird
  │      └──────── Zuweisungsoperator ("bekommt den Wert")
  └─────────────── der Name (das Etikett auf dem Karton)
```

⚠️ **Wichtig:** Das `=` heißt hier **nicht** „ist gleich" wie in Mathe. Es heißt **„bekommt den Wert"**. Lies es laut so — das verhindert später viel Verwirrung.

```python
zaehler = 0
zaehler = zaehler + 1      # In Mathe unmöglich. In Python: "nimm den alten
                           # Wert, rechne +1, leg das Ergebnis wieder rein."
print(zaehler)             # 1
```

### 2. Variablen benutzen

```python
name = "Anna"
alter = 30

print(name)                    # Anna
print("Hallo", name)           # Hallo Anna
print(name, "ist", alter)      # Anna ist 30
```

⚠️ **Ohne Anführungszeichen = Variable. Mit = Text.**

```python
print(name)      # Anna       ← der Inhalt der Variablen
print("name")    # name       ← das Wort "name"
```

### 3. Variablen ändern sich 🔄

```python
punkte = 0
print(punkte)      # 0

punkte = 10
print(punkte)      # 10        ← alter Wert ist weg

punkte = punkte + 5
print(punkte)      # 15
```

**Kurzschreibweisen** (die wirst du ständig brauchen):

```python
punkte += 5        # punkte = punkte + 5
punkte -= 3        # punkte = punkte - 3
punkte *= 2        # punkte = punkte * 2
punkte /= 4        # punkte = punkte / 4
```

### 4. Die vier Grundtypen 🎨

| Typ | Name | Beispiel | Wofür |
|---|---|---|---|
| `str` | String / Zeichenkette | `"Hallo"`, `'Anna'` | Text |
| `int` | Integer / Ganzzahl | `42`, `-7`, `0` | Zählbares |
| `float` | Fließkommazahl | `3.14`, `-0.5` | Messwerte, Preise |
| `bool` | Boolean / Wahrheitswert | `True`, `False` | Ja/Nein-Zustände |

```python
name    = "Anna"     # str
alter   = 25          # int
groesse = 1.83        # float
lernt   = True        # bool
```

🔍 **Typ prüfen:**

```python
print(type(name))       # <class 'str'>
print(type(alter))      # <class 'int'>
print(type(groesse))    # <class 'float'>
print(type(lernt))      # <class 'bool'>
```

⚠️ **Kommazahlen brauchen einen PUNKT, kein Komma:**

```python
preis = 19.99      # ✅ float
preis = 19,99      # ❌ das ist ein Tupel! (kommt in Modul 07)
```

### 5. `None` — der Nicht-Wert 🕳️

```python
ergebnis = None       # "hier ist noch nichts drin"
print(type(ergebnis)) # <class 'NoneType'>
```

`None` ist nicht `0` und nicht `""`. Es bedeutet: *„absichtlich leer"*. Du brauchst es z. B., wenn ein Wert erst später gesetzt wird.

### 6. Warum Typen zählen ⚠️

Derselbe Operator macht bei verschiedenen Typen verschiedene Dinge:

```python
print(3 + 4)          # 7        Zahlen → addieren
print("3" + "4")      # 34       Strings → aneinanderhängen!
print("3" * 4)        # 3333     String wiederholen
print(3 * 4)          # 12       multiplizieren
print("3" + 4)        # ❌ TypeError
```

> 🧠 **Tutor sagt:** Das ist die **Fehlerquelle Nummer 1** für Anfänger. Besonders bei `input()` — das gibt **immer** einen String zurück, auch wenn du eine Zahl eintippst. Merk dir jetzt schon: bei jedem seltsamen Ergebnis lautet die erste Frage **„welchen Typ hat das eigentlich?"** → `print(type(x))`

### 7. Typen umwandeln 🔄

```python
int("42")        # 42        String → Ganzzahl
int(3.99)        # 3         float → int (schneidet ab, rundet NICHT!)
float("3.14")    # 3.14
float(5)         # 5.0
str(42)          # "42"
bool(0)          # False
bool(1)          # True
bool("")         # False
bool("text")     # True
```

⚠️ **Geht nur, wenn es Sinn ergibt:**

```python
int("abc")       # ❌ ValueError: invalid literal for int()
int("42.5")      # ❌ ValueError  (erst float, dann int!)
int(float("42.5"))   # ✅ 42
```

### 8. Gute Variablennamen 🏷️

**Regeln (erzwungen von Python):**

```python
mein_name = "ok"      # ✅ Buchstaben, Ziffern, Unterstrich
_privat = "ok"        # ✅ darf mit _ beginnen
name2 = "ok"          # ✅ Ziffer erlaubt - nur nicht am Anfang

2name = "x"           # ❌ SyntaxError
mein-name = "x"       # ❌ Bindestrich = Minus!
class = "x"           # ❌ reserviertes Schlüsselwort
mein name = "x"       # ❌ kein Leerzeichen
```

**Stil (Konvention, `snake_case`):**

```python
# ✅ Gut - sagt, was drin ist
anzahl_versuche = 3
benutzer_email = "a@b.de"
ist_angemeldet = True        # bool-Namen gern mit ist_/hat_/kann_

# ❌ Schlecht
a = 3
x1 = "a@b.de"
AnzahlVersuche = 3           # das ist Java-Stil, nicht Python
l = [1, 2]                   # l, I, O sehen aus wie 1 und 0
```

> 💡 **Faustregel:** Wenn du in 3 Monaten den Code liest — verstehst du dann noch, was drin ist? Der Name kostet dich 2 Sekunden Tippen und spart 20 Minuten Rätselraten.

### 9. Mehrere Zuweisungen

```python
a, b, c = 1, 2, 3           # drei auf einmal
x = y = z = 0               # alle drei auf 0
a, b = b, a                 # tauschen! (elegant, sehr pythonisch)
```

---

## ⚠️ Typische Anfängerfehler

| Fehler | Was passiert | Fix |
|---|---|---|
| `preis = 19,99` | wird zum Tupel `(19, 99)` | Punkt statt Komma |
| `print("name")` statt `print(name)` | gibt das Wort aus | Anführungszeichen weg |
| `"3" + 4` | `TypeError` | `int("3") + 4` |
| `int("42.5")` | `ValueError` | `int(float("42.5"))` |
| `Alter` vs. `alter` | `NameError` | Groß-/Kleinschreibung beachten |
| Variable benutzt, bevor sie existiert | `NameError` | Reihenfolge prüfen |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

| # | Aufgabe | Level |
|:---:|---|:---:|
| 1 | Vier Variablen anlegen und ausgeben | 🟢 |
| 2 | Typen mit `type()` prüfen | 🟢 |
| 3 | Punktestand hochzählen | 🟢 |
| 4 | Zwei Variablen tauschen | 🟡 |
| 5 | Typumwandlungen durchführen | 🟡 |
| 6 | Schlechte Variablennamen verbessern | 🟡 |
| 7 | Vorhersagen, was passiert (ohne auszuführen!) | 🔴 |
| 8 ⭐ | Rechnung mit Zwischenvariablen | ⭐ |

---

## 🛠️ Mini-Projekt: Steckbrief-Generator

Erstelle `steckbrief.py`:

- Lege **mindestens 8 Variablen** an (Name, Alter, Größe, Stadt, Hobby, Lieblingszahl, lernt_python, motto)
- Nutze **alle vier Grundtypen** mindestens einmal
- Gib einen hübsch formatierten Steckbrief aus
- Gib am Ende von jeder Variablen den Typ aus
- Ändere danach **drei** Variablen und gib den Steckbrief erneut aus

**Bonus 🎁:** Berechne aus dem Geburtsjahr das Alter, statt es fest einzutippen.

---

## 🧠 Selbsttest

> Zuklappen. Auf Papier. Ohne Nachschauen.

1. Was bedeutet `=` in Python?
2. Nenne die vier Grundtypen mit je einem Beispiel.
3. Was ergibt `"5" + "3"`? Und `5 + 3`?
4. Wie prüfst du den Typ einer Variablen?
5. Was ist der Unterschied zwischen `19.99` und `19,99`?
6. Warum ist `2name = 5` ungültig?
7. Was macht `punkte += 3`?
8. Was ergibt `int(3.99)`? Warum nicht 4?
9. Was ist `None`?
10. ✍️ Erkläre einem Freund in 2 Sätzen, was eine Variable ist.

<details>
<summary>💡 Antworten</summary>

1. „bekommt den Wert" — eine Zuweisung, kein mathematisches Gleichheitszeichen.
2. `str` `"Hallo"` · `int` `42` · `float` `3.14` · `bool` `True`
3. `"53"` (Verkettung) bzw. `8` (Addition).
4. `type(variable)`
5. `19.99` ist ein `float`. `19,99` sind zwei Werte → ein Tupel `(19, 99)`.
6. Variablennamen dürfen nicht mit einer Ziffer beginnen.
7. Erhöht `punkte` um 3 — Kurzform für `punkte = punkte + 3`.
8. `3`. `int()` **schneidet ab**, es rundet nicht. Zum Runden: `round(3.99)` → `4`.
9. Ein eigener Wert für „absichtlich nichts". Nicht `0`, nicht `""`.
10. Z. B.: „Eine Variable ist ein beschrifteter Behälter für einen Wert. Über den Namen komme ich jederzeit an den Wert und kann ihn austauschen."
</details>

---

## 🔄 Wiederholung (Modul 00)

Ohne nachzuschauen:

1. Wie gibst du `"a"` und `"b"` getrennt durch `-` aus?
2. Wie verhinderst du den Zeilenumbruch nach `print`?
3. Was bedeutet `NameError`?

> Alle drei sofort gewusst? 💪 Wenn nicht → 5 Minuten Modul 00 überfliegen. Genau dafür ist dieser Block da.

---

## 🔗 Vertiefung

- 📖 [Real Python — Variables](https://realpython.com/python-variables/)
- 🔍 [Python Tutor: Variablen visualisieren](https://pythontutor.com/visualize.html) — leg 3 Variablen an und klick dich durch!
- 📄 [Spickzettel Grundlagen](../../spickzettel/grundlagen.md)

---

## ✅ Abgeschlossen?

- [ ] Beispiele abgetippt · [ ] Aufgaben 1–7 · [ ] Mini-Projekt · [ ] Selbsttest · [ ] Journal

**➡️ [Modul 02 — Strings](../02/README.md)** 🔤
