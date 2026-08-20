# 🐞 Modul 09 — Fehler verstehen & Debugging

> ⏱️ ~5 Stunden · ⬅️ [Modul 08](../08/README.md) · ➡️ [Modul 10](../10/README.md)

---

## 🎯 Lernziele

- [ ] einen Traceback lesen wie ein Profi
- [ ] die 12 häufigsten Fehlertypen erkennen
- [ ] den VS-Code-Debugger benutzen (Breakpoints, Step, Watch)
- [ ] mit `print`-Debugging systematisch vorgehen
- [ ] **Logikfehler** finden — die schwierigsten

---

## 🌍 Warum das wichtig ist

Hier ist die Wahrheit, die dir keiner sagt: **Profis verbringen mehr Zeit mit Fehlersuche als mit Schreiben.**

Der Unterschied zwischen Anfänger und Profi ist nicht, dass Profis weniger Fehler machen. Sie finden sie nur **in 2 Minuten statt in 2 Stunden**. Das ist eine erlernbare Fähigkeit — genau die lernst du jetzt.

> 🧠 **Tutor sagt:** Dieses Modul macht dich unabhängig. Ab hier kannst du dir selbst helfen. 💪

---

## 📖 Die Lektion

### 1. Den Traceback lesen 📖

```text
Traceback (most recent call last):
  File "rechner.py", line 12, in <module>       ← 3️⃣ zuletzt lesen
    ergebnis = teile(10, 0)
  File "rechner.py", line 5, in teile           ← 2️⃣ dann hier
    return a / b
ZeroDivisionError: division by zero             ← 1️⃣ ZUERST lesen!
```

**Deine Reihenfolge:**

```text
1. Letzte Zeile   →  WAS ist passiert (Fehlertyp + Beschreibung)
2. Zeile darüber  →  WO genau (Datei + Zeilennummer)
3. Nach oben      →  WIE ist Python dorthin gekommen (Aufrufkette)
```

💡 **Der Weg von unten nach oben ist die Reihenfolge, in der du lesen solltest.** Die unterste Zeile ist immer die wichtigste.

### 2. Die drei Fehlerarten

| Art | Wann | Beispiel | Schwierigkeit |
|---|---|---|:---:|
| **Syntaxfehler** | vor dem Start | Klammer vergessen | 😊 leicht |
| **Laufzeitfehler** | während der Ausführung | `ZeroDivisionError` | 🙂 mittel |
| **Logikfehler** | nie — läuft „erfolgreich" falsch | Durchschnitt zu hoch | 😰 schwer |

### 3. Die häufigsten Fehler auf einen Blick

📄 Vollständige Liste: [`spickzettel/fehlermeldungen.md`](../../spickzettel/fehlermeldungen.md)

| Fehler | Bedeutung | Erste Idee |
|---|---|---|
| `SyntaxError` | Grammatikfehler | Doppelpunkt? Klammer? **Zeile darüber prüfen!** |
| `IndentationError` | Einrückung falsch | 4 Leerzeichen, keine Tabs |
| `NameError` | Name unbekannt | Tippfehler? Vorher definiert? |
| `TypeError` | falscher Typ | `type(x)` ausgeben |
| `ValueError` | richtiger Typ, falscher Wert | `int("abc")` |
| `IndexError` | Index zu groß | Index startet bei 0 |
| `KeyError` | Schlüssel fehlt | `.get()` benutzen |
| `AttributeError` | Methode gibt's nicht | falscher Typ oder Tippfehler |
| `ZeroDivisionError` | durch 0 geteilt | vorher prüfen |
| `ModuleNotFoundError` | Paket fehlt | `pip install …` |
| `FileNotFoundError` | Datei nicht da | Pfad prüfen, `Path.cwd()` |

### 4. 🖨️ `print`-Debugging — richtig gemacht

Nicht verachten! Auch Profis machen das ständig. Aber systematisch:

```python
def berechne(werte):
    print(f"[DEBUG] Eingabe: {werte=}")          # ⭐ = zeigt Name UND Wert
    print(f"[DEBUG] Typ: {type(werte)}")

    summe = 0
    for i, w in enumerate(werte):
        summe += w
        print(f"[DEBUG] Schritt {i}: {w=}, {summe=}")

    print(f"[DEBUG] Ergebnis: {summe}")
    return summe
```

**Die drei Fragen, die du dir stellst:**

```text
1. Kommt der Code hier überhaupt an?   →  print("HIER!")
2. Was steht wirklich in der Variablen? →  print(f"{x=}")
3. Welchen Typ hat sie?                 →  print(type(x))
```

### 5. 🐛 Der VS-Code-Debugger

Der Debugger ist wie eine **Zeitlupe** für dein Programm.

```text
1. Klick links neben eine Zeilennummer  →  🔴 roter Punkt (Breakpoint)
   (oder Cursor in die Zeile + F9)
2. F5 drücken                           →  Programm läuft bis dorthin und HÄLT AN
3. Links im Panel "Variables"           →  ALLE Werte in diesem Moment sehen 👀
4. F10 = nächste Zeile                  →  Schritt für Schritt weiter
   F11 = in die Funktion hinein
   F5  = weiterlaufen bis zum nächsten Breakpoint
```

| Taste | Aktion | Wann |
|:---:|---|---|
| `F9` | Breakpoint setzen | vor dem Start |
| `F5` | Starten / Fortsetzen | ▶️ |
| `F10` | **Step Over** — nächste Zeile | meistens das hier |
| `F11` | **Step Into** — in die Funktion | wenn der Fehler *in* der Funktion sitzt |
| `Shift+F11` | **Step Out** — raus | genug gesehen |
| `Shift+F5` | Stoppen | ⏹️ |

💡 **Watch-Panel:** Eigene Ausdrücke beobachten, z. B. `len(liste)` oder `summe / anzahl`. Zeigt dir live, wie sich Werte entwickeln.

> 🧠 **Tutor sagt:** Investier heute 30 Minuten in den Debugger. Es fühlt sich anfangs umständlich an — aber ab Modul 14 spart es dir jede Woche Stunden. 🕰️

### 6. 🔇 Logikfehler — der stille Killer

Kein Absturz, aber falsche Ergebnisse. Die Strategie:

```text
1. Was ERWARTE ich?           (konkret, mit Zahl!)
2. Was BEKOMME ich?
3. Wo weichen sie zuerst ab?  (print an jeder Zwischenstufe)
4. Was in Schritt X ist anders als gedacht?
```

**Typische Logikfehler:**

```python
# 1) Akkumulator in der Schleife
for x in liste:
    summe = 0        # ❌ jedes Mal zurückgesetzt
    summe += x

# 2) Off-by-one
for i in range(len(liste) - 1):     # ❌ letztes Element fehlt
for i in range(len(liste)):         # ✅

# 3) = statt ==  (bei Zuweisung in Bedingung)
# 4) Einrückung: Code steht versehentlich in/außerhalb der Schleife
# 5) input() nicht umgewandelt: "5" + "3" == "53"
# 6) Float-Vergleich: 0.1 + 0.2 != 0.3
# 7) Liste beim Iterieren verändert
```

### 7. 🩺 Die Debug-Checkliste

```text
□ Fehlermeldung KOMPLETT gelesen? (letzte Zeile zuerst)
□ Zeilennummer angeschaut?
□ print(f"{x=}") vor der Fehlerzeile eingebaut?
□ type() der beteiligten Variablen geprüft?
□ Datei gespeichert? (Strg+S) 😄
□ Fehlermeldung wörtlich gegoogelt?
□ Auf pythontutor.com laufen lassen?
□ Der Ente erklärt? 🦆
□ 20 Minuten Pause gemacht?
```

---

## ⌨️ Übungen

👉 [`aufgaben/aufgaben.py`](aufgaben/aufgaben.py) — **11 kaputte Programme reparieren** 🔧

Das ist das ungewöhnlichste Aufgabenblatt des Kurses: Du schreibst keinen neuen Code, du **reparierst** vorhandenen. Genau das machst du später die meiste Zeit.

---

## 🛠️ Mini-Projekt: Deine alten Projekte debuggen

Nimm eines deiner früheren Projekte und:

1. Bau **absichtlich drei Fehler** ein (einen pro Fehlerart)
2. Lass es einen Tag liegen 😴
3. Repariere es — **nur** mit Traceback und Debugger, ohne dich zu erinnern
4. Notiere im Journal, wie lange du für jeden gebraucht hast

Beim zweiten Mal bist du doppelt so schnell. Das ist messbarer Fortschritt. 📈

---

## 🧠 Selbsttest

1. In welcher Reihenfolge liest du einen Traceback?
2. Welche drei Fehlerarten gibt es?
3. Was bedeutet `TypeError`? `ValueError`?
4. Was macht `print(f"{x=}")`?
5. Wie setzt du einen Breakpoint in VS Code?
6. Unterschied zwischen `F10` und `F11`?
7. Wie findest du einen Logikfehler systematisch?
8. Was ist ein Off-by-one-Fehler?
9. Was tust du bei `ModuleNotFoundError`?
10. ✍️ Beschreibe deinen Ablauf beim Feststecken in 5 Schritten.

<details>
<summary>💡 Antworten</summary>

1. Letzte Zeile zuerst (was), dann die Zeile darüber (wo), dann nach oben (wie).
2. Syntax-, Laufzeit- und Logikfehler.
3. `TypeError`: falscher **Typ**. `ValueError`: richtiger Typ, aber unpassender **Wert**.
4. Gibt Variablennamen **und** Wert aus — ideal zum Debuggen.
5. Links neben die Zeilennummer klicken oder `F9`.
6. `F10` überspringt Funktionsaufrufe, `F11` steigt in sie hinein.
7. Erwartung vs. Realität vergleichen und schrittweise eingrenzen, wo sie zuerst auseinandergehen.
8. Ein Zähl-/Grenzfehler um genau 1 — meist bei `range()` oder Indizes.
9. `pip install <paket>` — oder prüfen, ob die richtige venv aktiv ist.
10. Z. B.: Fehler lesen → googeln → `print` einbauen → Debugger → Pause/Ente.
</details>

---

## 🔄 Wiederholung (Modul 06–08)

1. `print` vs. `return` — Unterschied?
2. Was gibt eine Funktion ohne `return` zurück?
3. Wie durchläufst du ein Dict mit Schlüssel und Wert?
4. Warum ist `def f(liste=[])` gefährlich?

---

## 🔗 Vertiefung

- 📄 [Spickzettel Fehlermeldungen](../../spickzettel/fehlermeldungen.md)
- 📖 [VS Code Python Debugging](https://code.visualstudio.com/docs/python/debugging)
- 🔍 [pythontutor.com](https://pythontutor.com/visualize.html)

**➡️ [Modul 10 — Comprehensions & Builtins](../10/README.md)** ✨
