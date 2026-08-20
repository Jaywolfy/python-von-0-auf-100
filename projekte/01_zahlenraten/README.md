# 🎲 Projekt 1 — Zahlenraten-Spiel

> 📍 **Nach Modul 05** · ⏱️ ~4 Stunden · 🎯 Dein erstes komplettes Programm!

---

## 🎬 So soll es aussehen

```text
╔══════════════════════════════════════════╗
║        🎲  ZAHLENRATEN  🎲                ║
╚══════════════════════════════════════════╝

Wähle den Schwierigkeitsgrad:
  [1] Leicht    (1-50,  10 Versuche)
  [2] Mittel    (1-100, 7 Versuche)
  [3] Schwer    (1-1000, 10 Versuche)
> 2

Ich denke an eine Zahl zwischen 1 und 100.
Du hast 7 Versuche. Los geht's!

Versuch 1/7 > 50
  ⬆️  Zu niedrig!

Versuch 2/7 > 75
  ⬇️  Zu hoch!

Versuch 3/7 > 62
  ⬇️  Zu hoch!   🔥 Du bist ganz nah dran!

Versuch 4/7 > 57
  🎉 RICHTIG! Die Zahl war 57.

Du hast 4 Versuche gebraucht. Nicht schlecht! 💪

╔══════════════════════════════════════════╗
║  Spiele gesamt:   3                      ║
║  Gewonnen:        2  (67 %)              ║
║  Bester Versuch:  3 Versuche             ║
╚══════════════════════════════════════════╝

Nochmal? (j/n) > n
Danke fürs Spielen! 👋
```

---

## ✅ Pflichtanforderungen

- [ ] Zufallszahl mit `random.randint()`
- [ ] Nutzer rät per `input()`
- [ ] Rückmeldung „zu hoch" / „zu niedrig" / „richtig"
- [ ] Versuche werden gezählt
- [ ] Nach dem Gewinn: Anzahl der Versuche anzeigen
- [ ] Frage „Nochmal spielen?" — mit `while`-Schleife
- [ ] **Programm stürzt bei Buchstaben-Eingabe NICHT ab**
- [ ] Hübsche Ausgabe mit Rahmen und Emojis

## 🎁 Bonus-Anforderungen

- [ ] Drei Schwierigkeitsgrade
- [ ] Begrenzte Versuchszahl (verlieren möglich!)
- [ ] „Heiß/Kalt"-Hinweis 🔥❄️ bei weniger als 5 Abstand
- [ ] Statistik über alle Spiele der Sitzung
- [ ] Bestenliste (bester Versuch)
- [ ] Umgekehrter Modus: **du** denkst dir eine Zahl aus, der Computer rät (Binärsuche!)
- [ ] Statistik in eine Datei speichern (nach Modul 11)

---

## ✍️ Deine Planung (auf Papier!)

Beantworte **vor dem ersten Code**:

```text
1. Welche Variablen brauche ich?
   (gesuchte_zahl, versuche, max_versuche, …)

2. Welche Schleifen?
   Äußere Schleife = ?
   Innere Schleife  = ?

3. Wie prüfe ich, ob die Eingabe eine Zahl ist?
   (Ohne try/except - das kommt erst in Modul 13!)

4. Was passiert, wenn die Versuche aufgebraucht sind?

5. Wie messe ich "heiß/kalt"?
```

---

## 🪜 Schritt für Schritt

<details>
<summary><b>Schritt 1 — Die kleinste lauffähige Version</b></summary>

```python
import random

zahl = random.randint(1, 100)
tipp = int(input("Rate: "))

if tipp == zahl:
    print("Richtig!")
else:
    print(f"Falsch. Es war {zahl}.")
```

Ein Versuch, keine Schleife. **Läuft es? Dann weiter.** ✅
</details>

<details>
<summary><b>Schritt 2 — Schleife bis richtig</b></summary>

`while True` + `break` bei Treffer. Rückmeldung zu hoch/zu niedrig.
</details>

<details>
<summary><b>Schritt 3 — Versuche zählen</b></summary>

Zähler vor der Schleife (Akkumulator-Muster aus Modul 05!), in der Schleife erhöhen.
</details>

<details>
<summary><b>Schritt 4 — Robuste Eingabe</b></summary>

```python
eingabe = input("Rate: ")
if not eingabe.isdigit():
    print("Bitte eine Zahl eingeben!")
    continue
tipp = int(eingabe)
```

💡 `isdigit()` reicht hier völlig — `try/except` kommt in Modul 13.
</details>

<details>
<summary><b>Schritt 5 — Nochmal spielen</b></summary>

Äußere `while`-Schleife um alles herum. Am Ende `nochmal = input("Nochmal? (j/n) ")`.
</details>

<details>
<summary><b>Schritt 6 — Schwierigkeitsgrade & Statistik</b></summary>

Dictionary mit den Stufen. Statistik-Variablen **außerhalb** beider Schleifen!
</details>

<details>
<summary><b>Schritt 7 — Schön machen 🎨</b></summary>

Rahmen mit `"═" * 42`, Emojis, `.center()`, Trennlinien.
</details>

---

## 💥 Der Härtetest

Probier das aus, bevor du sagst „fertig":

```text
□ Buchstaben eingeben         → keine Absturz?
□ Nichts eingeben (nur Enter) → keine Absturz?
□ Negative Zahl               → sinnvolle Meldung?
□ Zahl außerhalb des Bereichs → Hinweis?
□ Bei "Nochmal?" etwas anderes als j/n → was passiert?
□ 0 oder eine riesige Zahl eingeben
```

---

## 🧠 Reflexion (ins Journal!)

Nach dem Fertigstellen — beantworte schriftlich:

1. Was war schwieriger als gedacht?
2. Wo hast du am längsten gebraucht?
3. Was würdest du beim nächsten Mal anders angehen?
4. Welchen Teil des Codes verstehst du am wenigsten gut?

---

## 🔍 Musterlösung

👉 [`loesung/zahlenraten.py`](loesung/zahlenraten.py)

⛔ **Erst öffnen, wenn dein Spiel läuft!**

---

**➡️ Weiter: [Modul 06 — Listen](../../module/06/README.md)**
