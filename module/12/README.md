# 📚 Modul 12 — Module & Standardbibliothek

> ⏱️ ~5 Stunden · ⬅️ [Modul 11](../11/README.md) · ➡️ [Modul 13](../13/README.md)

---

## 🎯 Lernziele

- [ ] Code auf mehrere Dateien aufteilen und importieren
- [ ] `if __name__ == "__main__":` verstehen
- [ ] die wichtigsten Standardmodule kennen: `datetime`, `random`, `math`, `os`, `collections`, `itertools`
- [ ] wissen, wo man in der Doku nachschlägt

---

## 🌍 Warum das wichtig ist

Python kommt mit **„batteries included"** — einer riesigen mitgelieferten Werkzeugkiste. 🧰

Der teuerste Anfängerfehler ist, Dinge selbst zu bauen, die es längst gibt. Ein Datumsvergleich? `datetime`. Häufigkeiten zählen? `Counter`. Alle Kombinationen? `itertools`. Zwei Zeilen statt zwanzig — und ohne Bugs.

---

## 📖 Die Lektion

### 1. Importieren — vier Varianten

```python
import math                      # math.sqrt(16)
import math as m                 # m.sqrt(16)
from math import sqrt, pi        # sqrt(16)        ⭐ meistgenutzt
from math import *               # ❌ nie machen — unklar, woher was kommt
```

### 2. Eigene Module

```text
mein_projekt/
├── werkzeuge.py      ← deine Funktionen
└── haupt.py          ← benutzt sie
```

```python
# werkzeuge.py
def gruesse(name):
    return f"Hallo {name}!"

# haupt.py
from werkzeuge import gruesse
print(gruesse("Anna"))
```

### 3. ⭐ `if __name__ == "__main__":`

```python
# werkzeuge.py
def gruesse(name):
    return f"Hallo {name}!"

if __name__ == "__main__":
    # läuft NUR, wenn diese Datei direkt gestartet wird
    print(gruesse("Test"))       # nicht beim Import!
```

🏠 **Alltagsbild:** Das ist die Zeile, die sagt *„das hier ist mein Selbsttest — führ ihn nur aus, wenn ich der Hauptdarsteller bin, nicht wenn mich jemand nur als Statist einlädt."*

Ohne diese Zeile läuft dein Testcode auch dann, wenn jemand nur eine Funktion importieren will. Das ist Standard in jedem professionellen Python-Projekt.

### 4. 📅 `datetime`

```python
from datetime import datetime, date, timedelta

heute = date.today()                    # 2026-07-26
jetzt = datetime.now()

jetzt.strftime("%d.%m.%Y %H:%M")        # '26.07.2026 14:30'  ⭐ formatieren
datetime.strptime("24.12.2026", "%d.%m.%Y")   # Text → Datum

morgen = heute + timedelta(days=1)
in_zwei_wochen = heute + timedelta(weeks=2)
差 = date(2026, 12, 24) - heute
print(差.days)                          # Tage bis Weihnachten 🎄
```

**Format-Codes:** `%d` Tag · `%m` Monat · `%Y` Jahr (4-stellig) · `%H:%M:%S` Zeit · `%A` Wochentag

### 5. 🎲 `random`

```python
import random

random.randint(1, 6)                   # Würfel (1 bis 6, inklusive!)
random.random()                        # 0.0 bis 1.0
random.choice(["a", "b", "c"])         # ein zufälliges Element
random.sample(liste, 3)                # 3 verschiedene
random.shuffle(liste)                  # mischt die Liste selbst
random.seed(42)                        # reproduzierbar (zum Testen!)
```

### 6. 📦 `collections`

```python
from collections import Counter, defaultdict

Counter("banane")                      # {'a': 3, 'n': 2, 'b': 1, 'e': 1}
Counter(woerter).most_common(3)        # ⭐ Top 3

d = defaultdict(list)                  # kein KeyError mehr
d["neu"].append(1)                     # funktioniert direkt!
```

> 🧠 **Tutor sagt:** `Counter` ersetzt das ganze Zähl-Muster aus Modul 07 durch **eine Zeile**. Genau deshalb lohnt es sich, die Standardbibliothek zu kennen.

### 7. 🔁 `itertools`

```python
from itertools import combinations, permutations, product, chain

list(combinations([1,2,3], 2))    # [(1,2), (1,3), (2,3)]
list(product("ab", [1,2]))        # alle Kombinationen
list(chain([1,2], [3,4]))         # [1,2,3,4]
```

### 8. Weitere nützliche Module

| Modul | Wofür |
|---|---|
| `os`, `sys` | Betriebssystem, Umgebungsvariablen, Programmargumente |
| `pathlib` | Pfade (Modul 11) |
| `json`, `csv` | Datenformate (Modul 16) |
| `re` | Reguläre Ausdrücke (Modul 21) |
| `statistics` | `mean`, `median`, `stdev` |
| `time` | `time.sleep(2)` — warten |
| `textwrap` | Text umbrechen |
| `shutil` | Dateien kopieren/verschieben (Modul 25) |

📖 **Alles nachschlagen:** [docs.python.org/3/library](https://docs.python.org/3/library/)

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `from math import *` | unklare Herkunft | gezielt importieren |
| Datei `random.py` genannt | überdeckt das Modul! | anders benennen 🚨 |
| Testcode ohne `__main__`-Guard | läuft beim Import mit | Guard einbauen |
| Zirkulärer Import | `ImportError` | Struktur überdenken |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

---

## 🛠️ Mini-Projekt: Dein eigenes Werkzeugmodul 🧰

Erstelle `werkzeuge.py` mit deinen nützlichsten Funktionen aus den letzten Modulen:

```python
"""Meine persönliche Werkzeugkiste."""

def durchschnitt(werte): ...
def ist_palindrom(text): ...
def formatiere_euro(betrag): ...
def zeige_tabelle(daten, spalten): ...
def fortschrittsbalken(anteil, breite=20): ...
def trennlinie(zeichen="-", breite=50): ...

if __name__ == "__main__":
    # Selbsttests für alle Funktionen
    ...
```

Dieses Modul benutzt du für den Rest des Kurses. Es wächst mit dir. 🌱

---

## 🧠 Selbsttest

1. Vier Import-Varianten — welche wann?
2. Warum kein `from x import *`?
3. Was macht `if __name__ == "__main__":`?
4. Wie formatierst du ein Datum als `26.07.2026`?
5. Wie berechnest du die Tage bis zu einem Datum?
6. Was macht `Counter(...).most_common(3)`?
7. Was ist `defaultdict(list)` gut?
8. Wie ziehst du 3 verschiedene Zufallselemente?
9. Warum darf eine Datei nicht `random.py` heißen?
10. ✍️ Erkläre den `__main__`-Guard mit einem Bild.

<details>
<summary>💡 Antworten</summary>

1. `import x` (klar), `import x as y` (kurz), `from x import a` (gezielt, am häufigsten), `from x import *` (nie).
2. Man sieht nicht mehr, woher ein Name kommt, und Namen können sich gegenseitig überschreiben.
3. Der Block läuft nur, wenn die Datei **direkt** gestartet wird — nicht beim Import.
4. `d.strftime("%d.%m.%Y")`
5. `(zieldatum - date.today()).days`
6. Gibt die 3 häufigsten Elemente mit Anzahl zurück.
7. Für Schlüssel, die noch nicht existieren — es legt automatisch eine leere Liste an.
8. `random.sample(liste, 3)`
9. Python würde deine Datei statt des Standardmoduls importieren.
10. Z. B.: „Das ist mein Selbsttest — führ ihn nur aus, wenn ich der Hauptdarsteller bin, nicht wenn ich nur eine Nebenrolle spiele."
</details>

---

## 🔄 Wiederholung (Modul 09–11)

1. Warum `with open(...)`?
2. Was macht `Path("a") / "b"`?
3. Was macht `any(...)`?
4. Wie liest du eine große Datei speicherschonend?

---

## 🔗 Vertiefung

- 📖 [Python Standard Library](https://docs.python.org/3/library/)
- 📖 [Real Python — Modules & Packages](https://realpython.com/python-modules-packages/)

**➡️ [Modul 13 — Exceptions](../13/README.md)** 🛡️
