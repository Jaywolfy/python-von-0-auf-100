# 🛡️ Modul 13 — Exceptions (Fehlerbehandlung)

> ⏱️ ~5 Stunden · ⬅️ [Modul 12](../12/README.md) · ➡️ [Modul 14](../14/README.md)

---

## 🎯 Lernziele

- [ ] `try` / `except` / `else` / `finally` einsetzen
- [ ] **spezifische** Exceptions abfangen statt pauschal alles
- [ ] eigene Exceptions definieren
- [ ] `raise` benutzen
- [ ] wissen, wann man Fehler **nicht** abfängt

---

## 🌍 Warum das wichtig ist

Modul 09 war: Fehler **finden**. Dieses Modul ist: Fehler **überleben**.

Ein Skript, das nach 40 von 500 Dateien abstürzt, weil eine kaputt war, ist wertlos. Ein Skript, das die kaputte überspringt, protokolliert und weitermacht, ist ein Werkzeug. 🛠️

---

## 📖 Die Lektion

### 1. Grundform

```python
try:
    zahl = int(input("Zahl: "))
    print(10 / zahl)
except ValueError:
    print("Das war keine Zahl!")
except ZeroDivisionError:
    print("Durch 0 kann man nicht teilen!")
```

```text
try:      ← "versuche das hier"
    ...
except X: ← "falls Fehler X auftritt, mach das"
    ...
```

### 2. Die volle Form

```python
try:
    datei = open("daten.txt", encoding="utf-8")
except FileNotFoundError:
    print("Datei fehlt")          # nur bei diesem Fehler
else:
    print("Hat geklappt!")        # nur wenn KEIN Fehler kam
    datei.close()
finally:
    print("Läuft IMMER")          # aufräumen, egal was passiert
```

| Block | Läuft wann |
|---|---|
| `try` | immer (der Versuch) |
| `except` | nur bei passendem Fehler |
| `else` | nur wenn **kein** Fehler kam |
| `finally` | **immer** — auch bei Absturz oder `return` |

### 3. 🚨 Spezifisch abfangen!

```python
# ❌ SEHR SCHLECHT - verschluckt ALLES, auch deine Tippfehler
try:
    ...
except:
    pass

# ❌ Auch schlecht
except Exception:
    pass

# ✅ GUT
except (ValueError, TypeError) as fehler:
    print(f"Ungültige Eingabe: {fehler}")
```

> 🧠 **Tutor sagt:** `except: pass` ist der gefährlichste Code in Python. Er versteckt Fehler, statt sie zu lösen — und du suchst später stundenlang, warum „nichts passiert". Fang **immer** nur die Fehler ab, die du auch erwartest. 🚫

### 4. Die Fehlermeldung mitnehmen

```python
try:
    int("abc")
except ValueError as fehler:
    print(f"Fehler: {fehler}")           # invalid literal for int()...
    print(f"Typ: {type(fehler).__name__}")   # ValueError
```

### 5. `raise` — selbst Fehler auslösen

```python
def setze_alter(alter):
    if not isinstance(alter, int):
        raise TypeError("Alter muss eine ganze Zahl sein")
    if alter < 0:
        raise ValueError(f"Alter kann nicht negativ sein: {alter}")
    return alter
```

💡 **Wichtig:** Lieber laut abstürzen mit klarer Meldung als still falsche Daten weiterreichen.

### 6. Eigene Exceptions

```python
class ZuWenigGuthabenError(Exception):
    """Wird ausgelöst, wenn das Guthaben nicht reicht."""


def abheben(konto, betrag):
    if betrag > konto:
        raise ZuWenigGuthabenError(f"Nur {konto} € verfügbar, {betrag} € gefordert")
    return konto - betrag


try:
    abheben(50, 100)
except ZuWenigGuthabenError as e:
    print(f"Abbruch: {e}")
```

(Klassen kommen in Modul 14 — hier reicht das Muster.)

### 7. 🌍 Realbeispiel: robuste Verarbeitung

```python
from pathlib import Path

erfolgreiche, fehlerhafte = 0, []

for datei in Path("daten").glob("*.txt"):
    try:
        inhalt = datei.read_text(encoding="utf-8")
        verarbeite(inhalt)
        erfolgreiche += 1
    except UnicodeDecodeError:
        fehlerhafte.append((datei.name, "falsches Encoding"))
    except PermissionError:
        fehlerhafte.append((datei.name, "kein Zugriff"))

print(f"✅ {erfolgreiche} verarbeitet, ❌ {len(fehlerhafte)} übersprungen")
```

**Das ist der Unterschied zwischen Skript und Werkzeug.** ⭐

### 8. Wann NICHT abfangen 🤔

```python
# ❌ Sinnlos - der Fehler ist ein PROGRAMMIERFEHLER, kein Datenproblem
try:
    ergebnis = meine_funktion()
except AttributeError:
    ergebnis = None                # versteckt einen Tippfehler!
```

**Faustregel:**
- Fehler von **außen** (Datei fehlt, Nutzer tippt Mist, Netzwerk weg) → abfangen ✅
- Fehler von **innen** (Tippfehler, falsche Logik) → **nicht** abfangen, reparieren ❌

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `except: pass` | verschluckt alles 💀 | spezifisch abfangen |
| `try` um 50 Zeilen | unklar, was fehlschlug | eng umschließen |
| `except Exception` überall | versteckt Bugs | konkrete Typen |
| Fehlermeldung wegwerfen | keine Info | `as fehler` benutzen |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

---

## 🛠️ Mini-Projekt: Robuster Rechner

`rechner.py`, der **niemals** abstürzt:

- fragt zwei Zahlen und einen Operator ab
- fängt `ValueError` (keine Zahl) und `ZeroDivisionError` ab
- fragt bei Fehleingabe **erneut** (`while True` + `continue`)
- eigene `UngueltigerOperatorError`
- `finally` zeigt am Ende eine Statistik der Rechnungen

**Testkriterium:** Gib absichtlich Unsinn ein. Wenn das Programm abstürzt, ist es noch nicht fertig. 😄

---

## 🧠 Selbsttest

1. Wofür `try`/`except`?
2. Wann läuft `else`, wann `finally`?
3. Warum ist `except: pass` gefährlich?
4. Wie kommst du an die Fehlermeldung?
5. Was macht `raise`?
6. Wie definierst du eine eigene Exception?
7. Wann sollte man **nicht** abfangen?
8. Warum `try`-Blöcke klein halten?
9. Wie fängst du mehrere Typen in einem `except`?
10. ✍️ Erkläre den Unterschied zwischen Debugging (Modul 09) und Exception-Handling.

<details>
<summary>💡 Antworten</summary>

1. Um erwartbare Laufzeitfehler abzufangen, statt das Programm abstürzen zu lassen.
2. `else` nur ohne Fehler, `finally` immer.
3. Es verschluckt **jeden** Fehler — auch Tippfehler in deinem eigenen Code.
4. `except X as fehler:` und dann `print(fehler)`.
5. Löst absichtlich einen Fehler aus.
6. `class MeinFehler(Exception): pass`
7. Bei Programmierfehlern — die soll man beheben, nicht verstecken.
8. Damit klar ist, welche Anweisung fehlgeschlagen ist.
9. `except (ValueError, TypeError) as e:`
10. Z. B.: „Debugging heißt, einen Fehler zu finden und zu beheben. Exception-Handling heißt, mit einem Fehler zu rechnen, der sich nicht vermeiden lässt — und sinnvoll darauf zu reagieren."
</details>

---

## 🔄 Wiederholung (Modul 10–12)

1. Was macht `if __name__ == "__main__":`?
2. Was macht `Counter(...).most_common(3)`?
3. Warum immer `encoding="utf-8"`?
4. Was macht `[x for x in l if x > 0]`?

---

## 🔗 Vertiefung

- 📖 [Real Python — Exceptions](https://realpython.com/python-exceptions/)
- 📖 [Eingebaute Exceptions](https://docs.python.org/3/library/exceptions.html)

**➡️ [Modul 14 — OOP Teil 1](../14/README.md)** 🏛️
