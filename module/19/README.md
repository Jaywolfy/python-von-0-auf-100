# 🧼 Modul 19 — Sauberer Code & Type Hints

> ⏱️ ~4 Stunden · ⬅️ [Modul 18](../18/README.md) · ➡️ [Modul 20](../20/README.md)

---

## 🎯 Lernziele

- [ ] PEP 8 — den offiziellen Stilguide anwenden
- [ ] gute Namen vergeben
- [ ] Type Hints schreiben
- [ ] Docstrings, die etwas taugen
- [ ] Ruff einsetzen (Linter + Formatter)
- [ ] Code-Gerüche erkennen und refactoren

---

## 🌍 Warum das wichtig ist

> **Code wird ungefähr 10-mal öfter gelesen als geschrieben.**
> Und der häufigste Leser ist **dein zukünftiges Ich** — ohne jede Erinnerung an heute. 🧠

Sauberer Code ist keine Kosmetik. Er ist der Unterschied zwischen „ich baue das schnell um" und „ich schreibe das lieber neu".

---

## 📖 Die Lektion

### 1. PEP 8 — die wichtigsten Regeln

```python
# ✅ Einrückung: 4 Leerzeichen, nie Tabs
# ✅ Zeilenlänge: max. 79 (PEP 8) bzw. 88 Zeichen (Black/Ruff-Standard)
# ✅ Zwei Leerzeilen zwischen Funktionen auf oberster Ebene
# ✅ Eine Leerzeile zwischen Methoden in einer Klasse

# ✅ Leerzeichen um Operatoren
x = 1 + 2
liste = [1, 2, 3]
def f(a, b=1):        # kein Leerzeichen um = bei Default-Argumenten!
    ...

# ❌
x=1+2
liste = [ 1,2,3 ]
def f(a, b = 1):
```

**Import-Reihenfolge:**

```python
import os                          # 1. Standardbibliothek
import sys

import requests                    # 2. Fremdpakete
from bs4 import BeautifulSoup

from werkzeuge import formatiere   # 3. eigene Module
```

**Namenskonventionen:**

| Was | Stil | Beispiel |
|---|---|---|
| Variable, Funktion | `snake_case` | `anzahl_versuche` |
| Klasse | `PascalCase` | `KontoAuszug` |
| Konstante | `GROSS_MIT_UNTERSTRICH` | `MAX_VERSUCHE = 3` |
| „privat" | führender Unterstrich | `_intern` |

### 2. ⭐ Gute Namen

```python
# ❌
d = {}
def calc(x, y): ...
tmp = get()
flag = True

# ✅
benutzer_nach_id = {}
def berechne_bruttopreis(netto, steuersatz): ...
aktuelle_sitzung = hole_sitzung()
ist_angemeldet = True
```

**Regeln:**
- Bool-Namen mit `ist_`, `hat_`, `kann_`
- Funktionsnamen sind **Verben** (`berechne_`, `lade_`, `pruefe_`)
- Variablennamen sind **Substantive**
- Kein `l`, `I`, `O` (sehen aus wie 1 und 0)
- Lieber lang und klar als kurz und rätselhaft

### 3. Type Hints 🏷️

```python
def berechne_bmi(gewicht_kg: float, groesse_m: float) -> float:
    return gewicht_kg / groesse_m ** 2


def namen_filtern(namen: list[str], mindestlaenge: int = 3) -> list[str]:
    return [n for n in namen if len(n) >= mindestlaenge]


def finde_benutzer(user_id: int) -> dict | None:      # kann None sein
    ...
```

**Häufige Typen:**

```python
list[str]          dict[str, int]        tuple[int, int]
set[str]           str | None            float | int
```

⚠️ **Wichtig:** Python **prüft** Type Hints nicht zur Laufzeit! Sie sind für:
- 👀 dich und andere Menschen (Dokumentation)
- 💡 die IDE (bessere Autovervollständigung & Warnungen)
- 🔍 Prüfwerkzeuge wie `mypy`

### 4. Docstrings, die etwas taugen

```python
def berechne_rabatt(preis: float, prozent: float) -> float:
    """Berechnet den Preis nach Abzug eines Rabatts.

    Args:
        preis: Der ursprüngliche Preis in Euro.
        prozent: Der Rabatt in Prozent (0-100).

    Returns:
        Der reduzierte Preis, gerundet auf 2 Nachkommastellen.

    Raises:
        ValueError: Wenn prozent nicht zwischen 0 und 100 liegt.

    Beispiel:
        >>> berechne_rabatt(100, 20)
        80.0
    """
```

💡 Ein Docstring beschreibt das **Was und Warum**, nicht das **Wie** — das steht im Code.

### 5. 🧹 Ruff — dein automatischer Aufräumdienst

```bash
pip install ruff

ruff check .              # Probleme finden
ruff check --fix .        # automatisch reparieren
ruff format .             # formatieren
```

In VS Code: Ruff-Extension installieren → formatiert bei jedem Speichern. Nie wieder über Leerzeichen nachdenken. 🎉

### 6. 👃 Code-Gerüche (Code Smells)

| Geruch | Warum schlecht | Fix |
|---|---|---|
| 📏 Funktion > 30 Zeilen | macht zu viel | aufteilen |
| 🔢 Magische Zahlen `if x > 86400` | was ist 86400? | `SEKUNDEN_PRO_TAG = 86400` |
| 🌲 4 Ebenen Verschachtelung | unlesbar | Guard Clauses |
| 📋 Copy-Paste-Code | 3× ändern statt 1× | Funktion daraus machen |
| 🏷️ Kommentar erklärt schlechten Namen | Name reparieren! | besserer Name |
| 🎛️ Funktion mit 7 Parametern | zu viel Verantwortung | Objekt/dict übergeben |

### 7. 🌍 Vorher / Nachher

```python
# ❌ VORHER
def p(d, t=0.19):
    r = []
    for i in d:
        if i[1] > 0:
            if i[2] == True:
                s = i[1] * i[3]
                s = s * (1 + t)
                r.append([i[0], s])
    return r


# ✅ NACHHER
MEHRWERTSTEUER = 0.19


def berechne_bruttopreise(
    positionen: list[dict],
    steuersatz: float = MEHRWERTSTEUER,
) -> list[dict]:
    """Berechnet Bruttopreise für alle aktiven Positionen mit Preis > 0.

    Args:
        positionen: Liste mit den Schlüsseln name, preis, aktiv, menge.
        steuersatz: Steuersatz als Dezimalzahl (0.19 = 19 %).

    Returns:
        Liste von dicts mit name und brutto.
    """
    ergebnis = []
    for position in positionen:
        if position["preis"] <= 0 or not position["aktiv"]:
            continue
        netto = position["preis"] * position["menge"]
        ergebnis.append({
            "name": position["name"],
            "brutto": round(netto * (1 + steuersatz), 2),
        })
    return ergebnis
```

**Was ist besser?** Namen sagen, was gemeint ist · Typen sind sichtbar · Guard Clause statt Verschachtelung · magische Zahl benannt · Dictionary statt Index-Rätsel · Docstring erklärt den Zweck.

### 8. ⚖️ Die Balance

> ⚠️ **Nicht übertreiben.** Ein 20-Zeilen-Skript braucht keine Type Hints auf jeder Zeile und keinen 15-zeiligen Docstring.
>
> **Faustregel:** Je länger der Code lebt und je mehr Leute ihn lesen, desto mehr Sorgfalt. Ein Wegwerf-Skript darf hässlich sein. 😊

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — **hässlichen Code aufräumen**

---

## 🛠️ Mini-Projekt: Refactoring-Marathon ♻️

Nimm dein größtes bisheriges Projekt und arbeite diese Liste ab:

- [ ] `ruff check .` — alle Meldungen beheben
- [ ] `ruff format .`
- [ ] Type Hints für alle öffentlichen Funktionen
- [ ] Docstrings für alle Funktionen
- [ ] Keine Funktion länger als 30 Zeilen
- [ ] Keine magischen Zahlen
- [ ] Maximal 3 Einrückungsebenen
- [ ] Alle Tests laufen danach noch grün ✅

**Der wichtigste Punkt:** *Verhalten darf sich nicht ändern.* Deshalb sind Tests (Modul 18) die Voraussetzung fürs Refactoring.

---

## 🧠 Selbsttest

1. Wie viele Leerzeichen Einrückung?
2. Wie heißen Klassen, wie Funktionen?
3. Was macht ein Linter?
4. Wozu Type Hints, wenn Python sie nicht prüft?
5. Was gehört in einen Docstring?
6. Was ist eine magische Zahl?
7. Wie flachst du tiefe Verschachtelung ab?
8. Wann darf Code hässlich sein?
9. Was macht `ruff format`?
10. ✍️ Nenne drei Code-Gerüche und ihre Fixes.

<details>
<summary>💡 Antworten</summary>

1. Vier.
2. Klassen `PascalCase`, Funktionen und Variablen `snake_case`, Konstanten `GROSS`.
3. Er prüft Code auf Stil- und Fehlerprobleme, ohne ihn auszuführen.
4. Für Menschen und IDEs: bessere Lesbarkeit, Autovervollständigung und Frühwarnungen.
5. Was die Funktion tut, ihre Parameter, Rückgabe und mögliche Exceptions.
6. Eine unerklärte Zahl direkt im Code — besser als benannte Konstante.
7. Mit Guard Clauses (früh aussteigen) und ausgelagerten Funktionen.
8. Bei Wegwerf-Skripten, die nur einmal laufen.
9. Formatiert den Code automatisch nach einheitlichem Stil.
10. Z. B.: zu lange Funktion → aufteilen · Copy-Paste → Funktion · magische Zahl → Konstante.
</details>

---

## 🔄 Wiederholung (Modul 16–18)

1. Wozu `newline=""` bei CSV?
2. Wozu eine venv?
3. Wie testest du eine Exception?
4. Was macht `@parametrize`?

---

## 🔗 Vertiefung

- 📖 [PEP 8](https://peps.python.org/pep-0008/) · [Ruff](https://docs.astral.sh/ruff/)
- 📺 [ArjanCodes](https://www.youtube.com/@ArjanCodes) — sauberer Code in Python

**➡️ [Modul 20 — Git & GitHub](../20/README.md)** 🌳
