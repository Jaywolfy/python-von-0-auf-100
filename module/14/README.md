# 🏛️ Modul 14 — OOP Teil 1: Klassen & Objekte

> ⏱️ ~5 Stunden · ⬅️ [Modul 13](../13/README.md) · ➡️ [Modul 15](../15/README.md)

---

## 🎯 Lernziele

- [ ] verstehen, **warum** es Klassen gibt (nicht nur wie)
- [ ] Klassen definieren, Objekte erzeugen
- [ ] `__init__` und `self` begreifen
- [ ] Attribute und Methoden unterscheiden
- [ ] `__str__` für lesbare Ausgabe

---

## 🌍 Warum das wichtig ist

OOP wird oft schlecht erklärt („eine Klasse ist ein Bauplan für ein Auto 🚗") — und Anfänger fragen sich zu Recht: *wozu?*

**Die ehrliche Antwort:** Klassen bündeln **Daten + die Funktionen, die zu diesen Daten gehören**, an einer Stelle.

```python
# ❌ Ohne Klasse: Daten und Funktionen driften auseinander
konto_inhaber = "Anna"
konto_stand = 1000

def einzahlen(stand, betrag):
    return stand + betrag

konto_stand = einzahlen(konto_stand, 500)     # man muss alles mitschleppen

# ✅ Mit Klasse: alles gehört zusammen
konto = Konto("Anna", 1000)
konto.einzahlen(500)
print(konto.stand)
```

Bei **einem** Konto ist der Unterschied klein. Bei 500 Konten mit je 10 Attributen ist es der Unterschied zwischen wartbar und Chaos.

> 🧠 **Tutor sagt:** Du brauchst OOP nicht für jedes Skript. Ein Ordner-Aufräumer kommt gut ohne aus. Aber **du musst es lesen können** — jede Bibliothek, die du je benutzt, ist damit gebaut. 📚

---

## 📖 Die Lektion

### 1. Klasse und Objekt

🏠 **Alltagsbild:** Die **Klasse** ist das Rezept 📄. Ein **Objekt** ist der gebackene Kuchen 🍰. Ein Rezept, beliebig viele Kuchen — jeder mit eigenen Eigenschaften.

```python
class Hund:
    def __init__(self, name, rasse):
        self.name = name
        self.rasse = rasse

    def bellen(self):
        return f"{self.name} sagt Wuff!"


bello = Hund("Bello", "Dackel")      # ein Objekt (Instanz)
rex = Hund("Rex", "Schäferhund")     # noch eines - unabhängig!

print(bello.name)        # Bello
print(rex.bellen())      # Rex sagt Wuff!
```

### 2. ⭐ `self` verstehen

`self` ist der häufigste Stolperstein. In einem Satz:

> **`self` ist „dieses konkrete Objekt hier".**

```python
bello.bellen()
# Python macht daraus intern:
Hund.bellen(bello)          # bello landet in self!
```

Deshalb:
- `self` ist **immer** der erste Parameter jeder Methode
- beim **Aufruf** gibst du ihn **nicht** an
- `self.name` heißt: „der Name **dieses** Objekts"

```python
class Hund:
    def bellen(self):              # ✅ self als erster Parameter
        return f"{self.name} bellt"

    def falsch():                  # ❌ TypeError beim Aufruf
        return "geht nicht"
```

### 3. `__init__` — der Konstruktor

```python
class Konto:
    def __init__(self, inhaber, stand=0):
        self.inhaber = inhaber     # Attribut anlegen
        self.stand = stand
        self.buchungen = []        # jedes Objekt bekommt seine EIGENE Liste
```

`__init__` läuft **automatisch**, wenn du `Konto("Anna")` schreibst. Du rufst es nie selbst auf.

### 4. Methoden

```python
class Konto:
    def __init__(self, inhaber, stand=0):
        self.inhaber = inhaber
        self.stand = stand
        self.buchungen = []

    def einzahlen(self, betrag):
        if betrag <= 0:
            raise ValueError("Betrag muss positiv sein")
        self.stand += betrag
        self.buchungen.append(("Einzahlung", betrag))
        return self.stand

    def abheben(self, betrag):
        if betrag > self.stand:
            raise ValueError(f"Nur {self.stand} € verfügbar")
        self.stand -= betrag
        self.buchungen.append(("Abhebung", -betrag))
        return self.stand

    def kontoauszug(self):
        zeilen = [f"Konto von {self.inhaber}"]
        for art, betrag in self.buchungen:
            zeilen.append(f"  {art:<12} {betrag:>10.2f} €")
        zeilen.append(f"  {'STAND':<12} {self.stand:>10.2f} €")
        return "\n".join(zeilen)
```

### 5. ⭐ `__str__` — lesbare Ausgabe

```python
class Konto:
    ...
    def __str__(self):
        return f"Konto({self.inhaber}: {self.stand:.2f} €)"


print(konto)     # Konto(Anna: 1500.00 €)
# ohne __str__:  <__main__.Konto object at 0x7f8b...>   😐
```

### 6. Klassen- vs. Instanzattribute

```python
class Konto:
    zinssatz = 0.02          # KLASSENATTRIBUT - für alle gleich

    def __init__(self, inhaber):
        self.inhaber = inhaber      # INSTANZATTRIBUT - pro Objekt
```

```python
Konto.zinssatz = 0.03        # ändert es für ALLE Konten
konto.inhaber = "Bernd"      # ändert nur dieses eine
```

🚨 **Falle:** Veränderliche Klassenattribute werden geteilt!

```python
class Kurs:
    teilnehmer = []          # ❌ ALLE Kurse teilen sich diese Liste!

class Kurs:
    def __init__(self):
        self.teilnehmer = [] # ✅ jeder Kurs hat seine eigene
```

### 7. Wann Klasse, wann Funktion? 🤔

| Nimm eine **Funktion**, wenn … | Nimm eine **Klasse**, wenn … |
|---|---|
| eine Aufgabe, rein und raus | Daten + Verhalten gehören zusammen |
| kein Zustand nötig | ein Zustand über die Zeit besteht |
| ein Skript | mehrere Objekte derselben Art |

> 💡 **Warnung vor Übertreibung:** Nicht alles muss eine Klasse sein. Eine Klasse mit nur einer Methode und ohne Zustand ist meistens einfach eine Funktion. 😊

---

## ⚠️ Typische Anfängerfehler

| Fehler | Problem | Fix |
|---|---|---|
| `self` vergessen | `TypeError` | erster Parameter jeder Methode |
| `self.x` vs. `x` | lokale Variable | `self.` nicht vergessen |
| `__init__` selbst aufrufen | unnötig | passiert automatisch |
| Klassenattribut `[]` | wird geteilt | in `__init__` anlegen |
| `print(objekt)` unleserlich | fehlt `__str__` | `__str__` definieren |

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py)

---

## 🛠️ Mini-Projekt: Klasse `Buch` + `Bibliothek`

```python
class Buch:
    """Ein Buch mit Titel, Autor, Jahr, Ausleihstatus."""
    def ausleihen(self): ...
    def zurueckgeben(self): ...
    def __str__(self): ...

class Bibliothek:
    """Verwaltet mehrere Bücher."""
    def hinzufuegen(self, buch): ...
    def suche(self, stichwort): ...
    def verfuegbare(self): ...
    def statistik(self): ...
```

Erzeuge 5 Bücher, leih 2 aus, such nach einem Autor, gib eine Statistik aus.

---

## 🧠 Selbsttest

1. Unterschied Klasse / Objekt?
2. Was ist `self`?
3. Wann läuft `__init__`?
4. Warum steht `self` nicht beim Aufruf?
5. Unterschied Klassen- / Instanzattribut?
6. Warum ist `teilnehmer = []` in der Klasse gefährlich?
7. Was macht `__str__`?
8. Wann Klasse statt Funktion?
9. Wie greifst du in einer Methode auf ein Attribut zu?
10. ✍️ Erkläre Klasse und Objekt mit einem eigenen Bild.

<details>
<summary>💡 Antworten</summary>

1. Klasse = Bauplan, Objekt = konkrete Ausprägung davon.
2. Der Verweis auf das konkrete Objekt, auf dem die Methode aufgerufen wurde.
3. Automatisch beim Erzeugen eines Objekts.
4. Python übergibt das Objekt automatisch als erstes Argument.
5. Klassenattribut gilt für alle Objekte, Instanzattribut nur für eines.
6. Alle Objekte teilen sich dieselbe Liste — Änderungen wirken überall.
7. Legt fest, was `print(objekt)` ausgibt.
8. Wenn Daten und zugehöriges Verhalten dauerhaft zusammengehören.
9. Über `self.attributname`.
10. Z. B.: „Die Klasse ist der Bauplan eines Hauses, jedes gebaute Haus ist ein Objekt — gleicher Grundriss, andere Farbe und andere Bewohner."
</details>

---

## 🔄 Wiederholung (Modul 11–13)

1. Warum `except: pass` vermeiden?
2. Was macht `if __name__ == "__main__":`?
3. Wie durchsuchst du einen Ordner rekursiv nach `.pdf`?
4. Was macht `Counter(...).most_common(3)`?

---

## 🔗 Vertiefung

- 📺 [Corey Schafer — OOP Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) ⭐ die beste OOP-Erklärung auf YouTube
- 📖 [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/)

**➡️ [Modul 15 — OOP Teil 2](../15/README.md)** 🧬
