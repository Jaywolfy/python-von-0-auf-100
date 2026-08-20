# 🔧 Modul 00 — Einstieg: Dein erstes Programm

> ⏱️ **Zeitbedarf:** ~3 Stunden (3 Tage à 1 h)
> 📍 **Voraussetzung:** [SETUP.md](../../SETUP.md) abgeschlossen
> ⬅️ [Übersicht](../../README.md) · ➡️ [Modul 01](../01/README.md)

---

## 🎯 Lernziele

Nach diesem Modul kannst du:

- [ ] erklären, was ein Programm eigentlich ist
- [ ] eine `.py`-Datei anlegen und ausführen
- [ ] mit `print()` Dinge ausgeben
- [ ] Kommentare schreiben
- [ ] deine ersten Fehlermeldungen lesen (und keine Angst davor haben 😌)

---

## 🌍 Warum das wichtig ist

Alles, was du später baust — der Ordner-Aufräumer, das Excel-Skript, das Wetter-Dashboard — besteht am Ende aus genau dem, was du heute lernst: **eine Reihe von Anweisungen in einer Textdatei.**

Es gibt keinen Zaubertrick. Nur viele kleine Anweisungen, sinnvoll zusammengesetzt.

---

## 📖 Die Lektion

### 1. Was ist ein Programm? 🤖

Ein Computer ist unfassbar schnell — und unfassbar dumm. Er tut **exakt** das, was du sagst. Nicht das, was du meinst.

🏠 **Alltagsbild:** Ein Programm ist ein **Kochrezept**.

```text
Rezept:                          Programm:
1. Wasser aufsetzen              1. Datei öffnen
2. Salz hinzufügen               2. Zeilen lesen
3. Nudeln 8 Min kochen           3. Für jede Zeile: prüfen
4. Abgießen                      4. Ergebnis ausgeben
```

Beides ist: **eine Abfolge von Schritten, in einer bestimmten Reihenfolge.**

Der Unterschied: Ein Mensch, der „Wasser aufsetzen" liest, denkt sich Topf, Herd und Wassermenge selbst dazu. Ein Computer nicht. **Du musst alles sagen.**

> 🧠 **Tutor sagt:** Wenn dein Programm etwas Komisches macht, ist der Computer nie „kaputt" oder „zickig". Er hat exakt gemacht, was du geschrieben hast. Die Frage ist nur: was hast du *wirklich* geschrieben? Diese Haltung spart dir hunderte Stunden Frust. 😌

---

### 2. Warum Python? 🐍

Vergleich derselben Aufgabe („gib Hallo Welt aus") in drei Sprachen:

```java
// Java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hallo Welt!");
    }
}
```

```c
/* C */
#include <stdio.h>
int main() {
    printf("Hallo Welt!\n");
    return 0;
}
```

```python
# Python
print("Hallo Welt!")
```

😄 Genau deshalb. Python ist bewusst so gebaut, dass Code **lesbar wie Englisch** ist. Du kämpfst weniger mit der Sprache und mehr mit dem eigentlichen Problem — und das ist der Teil, der dich schlau macht.

**Und es ist keine „Anfängersprache":** Instagram, Spotify, Netflix, die NASA und praktisch die gesamte KI-Welt laufen auf Python.

---

### 3. Deine erste Anweisung: `print()` 🖨️

```python
print("Hallo Welt!")
```

Zerlegt:

```text
print            (   "Hallo Welt!"   )
  ▲                       ▲
  │                       │
Name der             Das Argument —
Funktion             was ausgegeben werden soll.
                     Anführungszeichen = "das ist Text"
```

Die **runden Klammern** bedeuten: *„führe das jetzt aus"*. Ohne Klammern passiert nichts.

```python
print("Hallo")     # ✅ gibt Hallo aus
print "Hallo"      # ❌ SyntaxError (das war Python 2, längst tot)
print              # ❌ macht gar nichts — nur der Name, kein Aufruf
```

#### Mehrere Werte auf einmal

```python
print("Hallo", "Welt", "!")     # Hallo Welt !
```

Python setzt automatisch Leerzeichen dazwischen. Das kannst du ändern:

```python
print("2026", "07", "26", sep="-")     # 2026-07-26
print("kein", "Trenner", sep="")       # keinTrenner
```

#### Ohne Zeilenumbruch

Normalerweise springt `print` danach in die nächste Zeile. Mit `end` steuerst du das:

```python
print("Lade", end="")
print(".", end="")
print(".", end="")
print(".")
# Ausgabe:  Lade...
```

#### Leere Zeile

```python
print()          # gibt eine Leerzeile aus — gut zum Gliedern
```

---

### 4. Kommentare 💬

Alles hinter `#` ignoriert Python komplett. Kommentare sind **Notizen für Menschen**.

```python
# Das hier ist ein Kommentar - Python liest ihn nicht.

print("Hallo")     # Kommentare gehen auch ans Zeilenende

# print("Ich werde nicht ausgeführt")   ← praktisch zum Testen!
```

**Wofür Kommentare gut sind:**

```python
# ❌ Schlecht: beschreibt das Offensichtliche
zaehler = 0        # setze zaehler auf 0

# ✅ Gut: erklärt das WARUM
zaehler = 0        # startet bei 0, weil die Zählung erst ab dem 2. Durchlauf zählt
```

> 💡 **Profi-Trick:** Wenn du beim Programmieren nicht weiterweißt — schreib erst die Schritte als Kommentare, dann füll sie mit Code:
> ```python
> # 1. Nutzer nach Namen fragen
> # 2. Namen in Großbuchstaben umwandeln
> # 3. Begrüßung ausgeben
> ```
> Das ist keine Anfängerkrücke. Erfahrene Entwickler machen das ständig. 🎯

---

### 5. Wie dein Programm abläuft ⬇️

Python liest deine Datei **von oben nach unten, Zeile für Zeile**. Immer.

```python
print("Erste Zeile")
print("Zweite Zeile")
print("Dritte Zeile")
```

```text
Ausgabe:
Erste Zeile
Zweite Zeile
Dritte Zeile
```

Klingt banal — ist aber die Grundlage für alles. Wenn dein Programm später „im falschen Moment" etwas tut, liegt es fast immer daran, dass etwas an der falschen Stelle steht.

---

### 6. Fehler machen! 💥 (ja, absichtlich)

Fehler sind keine Katastrophe, sondern Nachrichten. Provozier sie jetzt bewusst, solange nichts kaputtgehen kann:

```python
print("Hallo)          # ❌ Anführungszeichen fehlt
prnt("Hallo")          # ❌ Tippfehler im Funktionsnamen
print(Hallo)           # ❌ ohne Anführungszeichen = Python sucht eine Variable
```

Führ jede Zeile einzeln aus und **lies die Fehlermeldung**. Du wirst merken: sie sagt dir ziemlich genau, was los ist.

```text
  File "test.py", line 1
    print("Hallo)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

Übersetzt: *„In Zeile 1 hast du einen Text angefangen, aber nie beendet."* 🔍

> 🧠 **Tutor sagt:** Anfänger sehen eine rote Fehlermeldung und erstarren. Profis sehen dieselbe Meldung und denken „ah, ein Hinweis". Der einzige Unterschied ist Gewöhnung. Deshalb: mach jetzt absichtlich Fehler, solange es null Konsequenzen hat.

---

### 7. Groß- und Kleinschreibung zählt! ⚠️

```python
print("ok")     # ✅
Print("ok")     # ❌ NameError: name 'Print' is not defined
PRINT("ok")     # ❌
```

Python unterscheidet strikt. `name`, `Name` und `NAME` sind drei verschiedene Dinge.

---

## ⚠️ Typische Anfängerfehler

| Fehler | Meldung | Fix |
|---|---|---|
| `print("Hallo"` | `SyntaxError` | Klammer schließen |
| `print(Hallo)` | `NameError` | Anführungszeichen um Text |
| `Print("Hallo")` | `NameError` | klein schreiben: `print` |
| `print "Hallo"` | `SyntaxError` | Klammern benutzen |
| Datei heißt `hallo` | läuft nicht | Endung `.py` nicht vergessen |
| Datei nicht gespeichert | alte Ausgabe | `Strg + S` vor dem Ausführen |

---

## ⌨️ Übungen

👉 Öffne [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) und bearbeite sie der Reihe nach.

| # | Aufgabe | Level |
|:---:|---|:---:|
| 1 | Deinen Namen ausgeben | 🟢 |
| 2 | Steckbrief über 4 Zeilen | 🟢 |
| 3 | Mit `sep` ein Datum formatieren | 🟢 |
| 4 | Eine Trennlinie ausgeben | 🟡 |
| 5 | Ein Rechteck aus Sternchen zeichnen | 🟡 |
| 6 | Eine Ladeanimation mit `end=""` | 🟡 |
| 7 | Drei Fehler absichtlich provozieren & erklären | 🔴 |
| 8 ⭐ | Ein ASCII-Bild deiner Wahl | ⭐ |

**Lösungen:** [`loesungen/loesungen.py`](loesungen/loesungen.py) — ⛔ erst nach eigenem Versuch!

---

## 🛠️ Mini-Projekt: Deine Visitenkarte

Erstelle `visitenkarte.py`, die so etwas ausgibt:

```text
╔════════════════════════════════════╗
║                                    ║
║           ANNA SCHMIDT               ║
║      Python-Lernender 🐍           ║
║                                    ║
║   📧  anna@beispiel.de       ║
║   📍  Deutschland                  ║
║   🎯  Ziel: Alles automatisieren   ║
║                                    ║
╚════════════════════════════════════╝
```

**Anforderungen:**
- ✅ Mindestens 8 `print()`-Aufrufe
- ✅ Mindestens ein Kommentar, der erklärt, was der Abschnitt tut
- ✅ Mindestens einmal `sep=` oder `end=` verwenden
- ✅ Der Rahmen muss sauber ausgerichtet sein (das ist fummeliger als es aussieht 😄)

---

## 🧠 Selbsttest

> **Zuklappen. Auf Papier beantworten. Erst dann nachschauen.** Das ist der wichtigste Teil des Moduls.

1. Was macht `print()`?
2. Warum braucht `print` runde Klammern?
3. Was ist der Unterschied zwischen `print("hallo")` und `print(hallo)`?
4. Wie gibst du zwei Werte mit einem Bindestrich getrennt aus?
5. Wie verhinderst du den Zeilenumbruch nach einem `print`?
6. Womit beginnst du einen Kommentar?
7. In welcher Reihenfolge liest Python deine Datei?
8. Was bedeutet `SyntaxError`?
9. Ist `Print("x")` gültig? Warum (nicht)?
10. ✍️ **Erklär-Aufgabe:** Erkläre einem 12-Jährigen in 3 Sätzen, was ein Programm ist.

<details>
<summary>💡 Antworten (erst nach dem eigenen Versuch!)</summary>

1. Gibt Werte im Terminal aus.
2. Die Klammern bedeuten „führe diese Funktion jetzt aus". Ohne sie hast du nur ihren Namen genannt.
3. `"hallo"` ist Text. `hallo` ohne Anführungszeichen wäre ein **Variablenname** — und den kennt Python nicht → `NameError`.
4. `print("a", "b", sep="-")`
5. `print("a", end="")`
6. Mit `#`
7. Von oben nach unten, Zeile für Zeile.
8. Ein Grammatikfehler — Python versteht die Zeile nicht (fehlende Klammer, fehlender Doppelpunkt, …).
9. Nein. Python unterscheidet Groß-/Kleinschreibung; die eingebaute Funktion heißt `print`.
10. Zum Beispiel: „Ein Programm ist eine Liste von Anweisungen für den Computer, so wie ein Kochrezept. Der Computer arbeitet sie von oben nach unten ab. Er macht dabei ganz genau das, was da steht — auch wenn es Unsinn ist."
</details>

---

## 🔄 Wiederholung

Erstes Modul — noch nichts zu wiederholen. 🎉
Ab Modul 01 steht hier immer eine kurze Rückblende. Genau die macht den Unterschied zwischen „hab ich mal gemacht" und „kann ich".

---

## 🔗 Vertiefung (optional)

- 📺 [Python in 100 Sekunden — Fireship](https://www.youtube.com/watch?v=x7X9w_GIm1s) (2 Min, Überblick)
- 📖 [Automate the Boring Stuff — Kapitel 1](https://automatetheboringstuff.com/2e/chapter1/)
- 🎮 [futurecoder.io](https://futurecoder.io/) — interaktiv im Browser

---

## ✅ Modul abgeschlossen?

- [ ] Alle Beispiele **abgetippt** und ausgeführt
- [ ] Aufgaben 1–7 gelöst
- [ ] Mini-Projekt gebaut
- [ ] Selbsttest **ohne Nachschauen** beantwortet
- [ ] Journal-Eintrag geschrieben

**➡️ Weiter zu [Modul 01 — Variablen & Datentypen](../01/README.md)** 📦
