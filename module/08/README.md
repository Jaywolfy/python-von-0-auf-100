# ⚙️ Modul 08 — Funktionen

> ⏱️ ~5 Stunden · ⬅️ [Modul 07](../07/README.md) · ➡️ [Modul 09](../09/README.md)

---

## 🎯 Lernziele

- [ ] eigene Funktionen mit `def` schreiben
- [ ] Parameter und Argumente unterscheiden
- [ ] `return` richtig einsetzen (und den Unterschied zu `print` verstehen!)
- [ ] Default- und Keyword-Argumente nutzen
- [ ] Scope verstehen: wo gilt welche Variable?
- [ ] Docstrings schreiben

---

## 🌍 Warum das wichtig ist

Bis jetzt waren deine Programme ein langer Zettel von oben nach unten. Ab jetzt baust du **Bausteine**.

Funktionen sind der Schritt von „ich schreibe Skripte" zu „ich baue Software". Alles Weitere im Kurs — Klassen, Tests, Module — setzt darauf auf.

> 🧠 **Tutor sagt:** Wenn du Modul 08 nur halb verstehst, wird Modul 14 (Klassen) unmöglich. Nimm dir hier lieber einen Tag mehr. 🐢

---

## 📖 Die Lektion

### 1. Die erste eigene Funktion

```python
def begruesse():
    print("Hallo!")
    print("Schön, dass du da bist.")

begruesse()        # Aufruf - erst hier passiert etwas!
begruesse()        # nochmal - beliebig oft
```

```text
def  begruesse (  ) :
 ▲       ▲      ▲  ▲
 │       │      │  └── Doppelpunkt
 │       │      └───── Parameterliste (hier leer)
 │       └──────────── Name der Funktion
 └──────────────────── "definiere"
```

⚠️ **Definieren ≠ Ausführen.** `def` legt die Funktion nur an. Ohne den Aufruf `begruesse()` passiert gar nichts.

### 2. Parameter — Werte hineingeben

```python
def begruesse(name):
    print(f"Hallo {name}!")

begruesse("Anna")       # Hallo Anna!
begruesse("Bernd")      # Hallo Bernd!
```

| Begriff | Was | Wo |
|---|---|---|
| **Parameter** | `name` | in der Definition |
| **Argument** | `"Anna"` | beim Aufruf |

Mehrere Parameter:

```python
def addiere(a, b):
    print(a + b)

addiere(3, 5)           # Reihenfolge zählt!
```

### 3. ⭐ `return` — das Herzstück

Das ist der wichtigste Abschnitt des Moduls.

```python
def addiere(a, b):
    return a + b            # gibt das Ergebnis ZURÜCK

ergebnis = addiere(3, 5)    # ergebnis = 8
print(ergebnis * 2)         # 16   ← damit kann man weiterrechnen!
```

**`print` vs. `return` — der Unterschied, den alle verwechseln:**

```python
def mit_print(a, b):
    print(a + b)            # zeigt es an

def mit_return(a, b):
    return a + b            # gibt es zurück

x = mit_print(3, 5)         # zeigt 8 an, aber x ist None!
y = mit_return(3, 5)        # zeigt nichts, aber y ist 8 ✅
```

🏠 **Alltagsbild:**
- `print` = der Koch **ruft** „das Essen ist fertig!" → du hast nichts in der Hand
- `return` = der Koch **reicht dir den Teller** → du kannst weiterarbeiten

> 🧠 **Faustregel:** Funktionen, die etwas **berechnen**, benutzen `return`. Nur Funktionen, deren Zweck die Anzeige ist, benutzen `print`. Das trennt sauber und macht deinen Code testbar. ✅

**Weitere Punkte zu `return`:**

```python
def pruefe(zahl):
    if zahl < 0:
        return "negativ"     # ⚡ Funktion endet SOFORT hier
    return "positiv"         # nur erreichbar, wenn zahl >= 0

def mehrere():
    return 1, 2, 3           # gibt ein Tupel zurück
a, b, c = mehrere()

def ohne_return():
    pass
print(ohne_return())         # None  ← ohne return kommt None zurück
```

### 4. Default-Werte & Keyword-Argumente

```python
def begruesse(name, gruss="Hallo"):
    return f"{gruss}, {name}!"

begruesse("Anna")                    # 'Hallo, Anna!'
begruesse("Anna", "Moin")            # 'Moin, Anna!'
begruesse(gruss="Servus", name="Anna")   # Reihenfolge egal!
```

⚠️ Parameter **mit** Default müssen **hinter** denen ohne stehen:

```python
def f(a=1, b):     # ❌ SyntaxError
def f(b, a=1):     # ✅
```

🚨 **Die berüchtigte Falle — niemals veränderliche Defaults:**

```python
def hinzufuegen(item, liste=[]):     # ❌ die Liste wird GETEILT!
    liste.append(item)
    return liste

print(hinzufuegen("a"))    # ['a']
print(hinzufuegen("b"))    # ['a', 'b']   😱 nicht ['b']!

def hinzufuegen(item, liste=None):   # ✅ richtig
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

### 5. Scope — wo gilt welche Variable? 🔍

```python
zahl = 10                # global

def test():
    zahl = 99            # LOKAL - eine eigene, neue Variable
    print(zahl)          # 99

test()
print(zahl)              # 10   ← global unverändert!
```

**Die Regel:**
- Innen kann man **außen lesen**
- Innen kann man außen **nicht überschreiben** (dafür bräuchte man `global` — vermeide das!)

```python
def gut(werte):          # ✅ Daten reingeben, Ergebnis zurückgeben
    return sum(werte)

zaehler = 0
def schlecht():          # ❌ verändert heimlich Globales
    global zaehler
    zaehler += 1
```

### 6. Docstrings 📝

```python
def berechne_bmi(gewicht_kg, groesse_m):
    """Berechnet den Body-Mass-Index.

    Args:
        gewicht_kg: Gewicht in Kilogramm
        groesse_m: Größe in Metern

    Returns:
        Der BMI als float.
    """
    return gewicht_kg / groesse_m ** 2

help(berechne_bmi)       # zeigt den Docstring an
```

💡 In VS Code siehst du den Docstring als Tooltip, wenn du die Funktion aufrufst. Sehr praktisch.

### 7. 🌍 Realbeispiel: Alten Code umbauen

```python
# ❌ Vorher: alles hintereinander, nichts wiederverwendbar
noten = [2.3, 1.7, 3.0]
schnitt = sum(noten) / len(noten)
print(f"Durchschnitt: {schnitt:.2f}")
if schnitt <= 2.0:
    print("Sehr gut")

# ✅ Nachher: Bausteine
def durchschnitt(werte):
    """Berechnet den Mittelwert einer Zahlenliste."""
    return sum(werte) / len(werte)

def bewerte(schnitt):
    """Wandelt einen Notenschnitt in eine Textbewertung um."""
    if schnitt <= 2.0:
        return "Sehr gut"
    elif schnitt <= 3.0:
        return "Gut"
    return "Ausbaufähig"

def zeige_zeugnis(name, noten):
    """Gibt ein formatiertes Zeugnis aus."""
    schnitt = durchschnitt(noten)
    print(f"{name}: {schnitt:.2f} — {bewerte(schnitt)}")

zeige_zeugnis("Anna", [2.3, 1.7, 3.0])
zeige_zeugnis("Bernd", [1.0, 1.3, 1.7])     # ← jetzt beliebig oft!
```

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `print` statt `return` | Ergebnis ist `None` | `return` benutzen |
| Funktion definiert, nie aufgerufen | nichts passiert | `funktion()` |
| Klammern vergessen: `funktion` | gibt das Funktionsobjekt | `funktion()` |
| `liste=[]` als Default | wird zwischen Aufrufen geteilt | `liste=None` |
| Global ändern wollen | funktioniert nicht | Wert **zurückgeben** |
| Funktion nach dem Aufruf definiert | `NameError` | `def` zuerst |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — 10 Aufgaben inkl. 🥗 Mix

---

## 🛠️ Mini-Projekt: Alte Projekte refactoren ♻️

Nimm dein **Haushaltsbuch** oder deinen **Text-Analysator** aus früheren Modulen und zerlege ihn in Funktionen.

**Ziel:**
- keine Funktion länger als 20 Zeilen
- jede Funktion macht **genau eine** Sache
- jede hat einen Docstring
- ganz unten steht nur noch:

```python
def main():
    daten = lade_daten()
    ergebnis = werte_aus(daten)
    zeige_bericht(ergebnis)

main()
```

Das ist echtes Software-Design — und du wirst merken, wie viel klarer der Code wird.

---

## 🧠 Selbsttest

1. Unterschied zwischen Definition und Aufruf?
2. Unterschied Parameter / Argument?
3. `print` vs. `return` — was ist der Unterschied?
4. Was gibt eine Funktion ohne `return` zurück?
5. Was passiert nach einem `return` im Funktionskörper?
6. Wie gibst du mehrere Werte zurück?
7. Warum ist `def f(liste=[])` gefährlich?
8. Kann eine Funktion globale Variablen ändern?
9. Wozu ein Docstring?
10. ✍️ Erkläre `return` mit einem Alltagsbild.

<details>
<summary>💡 Antworten</summary>

1. `def` legt die Funktion an, der Aufruf `f()` führt sie aus.
2. Parameter = Platzhalter in der Definition. Argument = konkreter Wert beim Aufruf.
3. `print` zeigt an, `return` gibt einen Wert an den Aufrufer zurück, mit dem man weiterarbeiten kann.
4. `None`
5. Die Funktion endet sofort; nachfolgender Code wird nicht mehr ausgeführt.
6. `return a, b, c` — kommt als Tupel zurück, entpackbar mit `x, y, z = f()`.
7. Der Default wird **einmal** erzeugt und zwischen allen Aufrufen geteilt.
8. Nur mit `global` — aber das gilt als schlechter Stil. Besser: Wert zurückgeben.
9. Er dokumentiert, was die Funktion tut; `help()` und die IDE zeigen ihn an.
10. Z. B.: „`print` ist, wenn der Koch ruft, dass das Essen fertig ist. `return` ist, wenn er dir den Teller in die Hand drückt."
</details>

---

## 🔄 Wiederholung (Modul 05–07)

1. Was macht `d.get("x", 0)`?
2. Wie kopierst du eine Liste richtig?
3. Was ist der Akkumulator und wo steht er?
4. Wie durchläufst du ein Dict mit Schlüssel und Wert?

---

## 🔗 Vertiefung

- 📖 [Real Python — Defining Functions](https://realpython.com/defining-your-own-python-function/)
- 📺 [Corey Schafer — Functions](https://www.youtube.com/watch?v=9Os0o3wzS_I)

**➡️ [Modul 09 — Fehler & Debugging](../09/README.md)** 🐞
