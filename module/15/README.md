# 🧬 Modul 15 — OOP Teil 2: Vererbung & Dunder

> ⏱️ ~5 Stunden · ⬅️ [Modul 14](../14/README.md) · ➡️ [Modul 16](../16/README.md)

---

## 🎯 Lernziele

- [ ] Vererbung verstehen und einsetzen
- [ ] Methoden überschreiben, `super()` benutzen
- [ ] die wichtigsten Dunder-Methoden (`__str__`, `__repr__`, `__len__`, `__eq__`)
- [ ] `@dataclass` — die Abkürzung für Datenklassen ⚡
- [ ] **Komposition vs. Vererbung** — wann was?

---

## 🌍 Warum das wichtig ist

Vererbung verhindert Copy-Paste zwischen ähnlichen Klassen. Und `@dataclass` spart dir bei fast jeder Datenklasse 20 Zeilen Tipparbeit.

Aber Vorsicht: Vererbung wird von Anfängern **massiv überbenutzt**. Dieses Modul zeigt dir auch, wann du sie **nicht** brauchst.

---

## 📖 Die Lektion

### 1. Vererbung — Gemeinsames einmal schreiben

```python
class Tier:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def schlafen(self):
        return f"{self.name} schläft 😴"

    def laut(self):
        return "..."


class Hund(Tier):                 # ← erbt von Tier
    def laut(self):               # überschreibt die Methode
        return "Wuff!"


class Katze(Tier):
    def laut(self):
        return "Miau!"


bello = Hund("Bello", 3)
print(bello.schlafen())     # geerbt von Tier ✅
print(bello.laut())         # eigene Version ✅
```

```text
        Tier            ← Basisklasse (Elternklasse)
       /    \
    Hund   Katze        ← abgeleitete Klassen (Kindklassen)
```

🏠 **Alltagsbild:** „Ein Hund **ist ein** Tier." Wenn dieser Satz stimmt, passt Vererbung. Wenn nicht → **keine Vererbung**.

### 2. `super()` — die Elternversion aufrufen

```python
class Hund(Tier):
    def __init__(self, name, alter, rasse):
        super().__init__(name, alter)     # ⭐ Elternteil erledigt name+alter
        self.rasse = rasse                # eigenes Attribut ergänzen

    def steckbrief(self):
        return f"{super().steckbrief()} | Rasse: {self.rasse}"
```

⚠️ `super().__init__(...)` **nicht vergessen** — sonst fehlen die geerbten Attribute.

### 3. `isinstance` — Typ prüfen

```python
isinstance(bello, Hund)      # True
isinstance(bello, Tier)      # True  ← ein Hund IST ein Tier
type(bello) == Tier          # False ← deshalb lieber isinstance
```

### 4. ⭐ Dunder-Methoden

Sie machen deine Objekte „pythonisch" — sie verhalten sich wie eingebaute Typen.

| Methode | Aktiviert | Beispiel |
|---|---|---|
| `__str__` | `print(obj)`, `str(obj)` | lesbar für Menschen |
| `__repr__` | in der Konsole, in Listen | eindeutig für Entwickler |
| `__len__` | `len(obj)` | Anzahl Elemente |
| `__eq__` | `obj1 == obj2` | Gleichheit definieren |
| `__lt__` | `<`, ermöglicht `sorted()` | Sortierreihenfolge |
| `__contains__` | `x in obj` | Enthaltensein |
| `__getitem__` | `obj[0]` | Indexzugriff |
| `__add__` | `obj1 + obj2` | Addition |

```python
class Geld:
    def __init__(self, betrag, waehrung="EUR"):
        self.betrag = betrag
        self.waehrung = waehrung

    def __str__(self):
        return f"{self.betrag:.2f} {self.waehrung}"

    def __repr__(self):
        return f"Geld({self.betrag}, {self.waehrung!r})"

    def __add__(self, andere):
        return Geld(self.betrag + andere.betrag, self.waehrung)

    def __eq__(self, andere):
        return self.betrag == andere.betrag

    def __lt__(self, andere):
        return self.betrag < andere.betrag


a, b = Geld(10), Geld(5)
print(a + b)                 # 15.00 EUR
print(sorted([a, b]))        # [Geld(5, 'EUR'), Geld(10, 'EUR')]
```

💡 **`__str__` vs. `__repr__`:** `__str__` ist für Nutzer („15.00 EUR"), `__repr__` für dich beim Debuggen („Geld(15, 'EUR')"). Hast du nur eine → nimm `__repr__`, sie springt für beide ein.

### 5. ⚡ `@dataclass` — die große Abkürzung

```python
from dataclasses import dataclass, field

@dataclass
class Punkt:
    x: float
    y: float = 0.0

p = Punkt(3, 4)
print(p)              # Punkt(x=3, y=4)     ← __repr__ geschenkt
print(p == Punkt(3, 4))   # True            ← __eq__ geschenkt
```

Das ersetzt ~15 Zeilen Handarbeit. Für Klassen, die vor allem **Daten halten**, ist das die erste Wahl.

```python
@dataclass
class Artikel:
    name: str
    preis: float
    tags: list = field(default_factory=list)     # ⚠️ NICHT tags: list = []

    def gesamtpreis(self, menge):        # eigene Methoden gehen weiter
        return self.preis * menge
```

### 6. 🤔 Komposition statt Vererbung

Das ist die wichtigste Design-Lektion dieses Moduls.

```python
# ❌ Falsch: "Ein Auto IST ein Motor"?  Nein!
class Auto(Motor): ...

# ✅ Richtig: "Ein Auto HAT einen Motor"
class Auto:
    def __init__(self, marke, motor):
        self.marke = marke
        self.motor = motor          # Komposition

    def starten(self):
        return self.motor.starten()
```

```text
IST-EIN  →  Vererbung     (Hund ist ein Tier)
HAT-EIN  →  Komposition   (Auto hat einen Motor)
```

> 🧠 **Tutor sagt:** Im Zweifel **Komposition**. Sie ist flexibler und führt seltener in Sackgassen. Tiefe Vererbungshierarchien (3+ Ebenen) sind fast immer ein Designfehler. 🏗️

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `super().__init__()` vergessen | Attribute fehlen | immer aufrufen |
| Vererbung ohne „ist ein" | falsches Modell | Komposition |
| 4 Ebenen tief vererbt | unverständlich | flach halten |
| `tags: list = []` in dataclass | geteilt! | `field(default_factory=list)` |
| nur `__str__`, kein `__repr__` | Debugging schwer | `__repr__` ergänzen |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

---

## 🛠️ Mini-Projekt: Modelliere dein Hobby ⚽📚🎮

Nimm ein Thema, das dich interessiert, und baue ein kleines Klassenmodell:

| Thema | Beispielklassen |
|---|---|
| ⚽ Fußball | `Spieler`, `Torwart(Spieler)`, `Mannschaft` (Komposition!) |
| 📚 Lesen | `Medium`, `Buch(Medium)`, `Hoerbuch(Medium)`, `Regal` |
| 🎮 Gaming | `Charakter`, `Magier(Charakter)`, `Krieger(Charakter)`, `Inventar` |
| 🎵 Musik | `Track`, `Album`, `Playlist` |

**Anforderungen:** 1 Basisklasse + 2 abgeleitete · mindestens 1 Komposition · `__str__` und `__repr__` · 1 `@dataclass` · eine Auswertung über eine Liste von Objekten

---

## 🧠 Selbsttest

1. Wann ist Vererbung richtig?
2. Was macht `super()`?
3. Was passiert ohne `super().__init__()`?
4. `__str__` vs. `__repr__`?
5. Wozu `__eq__` und `__lt__`?
6. Was schenkt dir `@dataclass`?
7. Warum `field(default_factory=list)`?
8. Vererbung vs. Komposition — Merksatz?
9. Was macht `isinstance(x, Tier)`?
10. ✍️ Nenn ein Beispiel aus deinem Alltag für „ist-ein" und eines für „hat-ein".

<details>
<summary>💡 Antworten</summary>

1. Wenn der Satz „X **ist ein** Y" stimmt und echtes Verhalten geteilt wird.
2. Ruft die Version der Elternklasse auf.
3. Die in der Elternklasse gesetzten Attribute fehlen → `AttributeError`.
4. `__str__` für Menschen, `__repr__` für Entwickler/Debugging.
5. Um `==` und Sortierung für eigene Objekte zu definieren.
6. `__init__`, `__repr__`, `__eq__` automatisch.
7. Weil ein `[]` als Default zwischen allen Instanzen geteilt würde.
8. „Ist-ein → Vererbung, hat-ein → Komposition."
9. Prüft, ob `x` ein `Tier` oder eine davon abgeleitete Klasse ist.
10. Z. B.: „Ein Rennrad ist ein Fahrrad" (Vererbung) · „Ein Fahrrad hat Räder" (Komposition).
</details>

---

## 🔄 Wiederholung (Modul 12–14)

1. Was ist `self`?
2. Warum ist ein Klassenattribut `[]` gefährlich?
3. Warum `except: pass` vermeiden?
4. Was macht `if __name__ == "__main__":`?

---

## 🔗 Vertiefung

- 📺 [Corey Schafer — Inheritance](https://www.youtube.com/watch?v=RSl87lqOXDE)
- 📖 [Real Python — dataclasses](https://realpython.com/python-data-classes/)

**➡️ [Modul 16 — CSV & JSON](../16/README.md)** 🔗
