"""
Modul 18 - Zu testende Funktionen.

⚠️ ACHTUNG: Einige dieser Funktionen enthalten BUGS!
   Deine Aufgabe: Schreib Tests, die sie finden.
   Erst DANN reparieren.
"""


def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b


def durchschnitt(werte):
    """Berechnet den Mittelwert einer Zahlenliste."""
    return sum(werte) / len(werte)          # 🐛 was bei leerer Liste?


def ist_gerade(zahl):
    """Prüft, ob eine Zahl gerade ist."""
    return zahl % 2 == 0


def groesste(zahlen):
    """Findet die größte Zahl einer Liste."""
    maximum = 0                              # 🐛 was bei nur negativen Zahlen?
    for z in zahlen:
        if z > maximum:
            maximum = z
    return maximum


def ist_palindrom(text):
    """Prüft, ob ein Text ein Palindrom ist."""
    sauber = text.lower().replace(" ", "")
    return sauber == sauber[::-1]


def zaehle_vokale(text):
    """Zählt die Vokale in einem Text."""
    anzahl = 0
    for z in text.lower():
        if z in "aeiou":
            anzahl += 1
    return anzahl


def formatiere_euro(betrag):
    """Formatiert eine Zahl als Eurobetrag: '1.234,56 €'"""
    text = f"{betrag:,.2f}"
    text = text.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{text} €"


def note_zu_text(note):
    """Wandelt eine Schulnote (1-6) in Text um."""
    texte = {1: "sehr gut", 2: "gut", 3: "befriedigend",
             4: "ausreichend", 5: "mangelhaft", 6: "ungenügend"}
    return texte[note]                       # 🐛 was bei ungültiger Note?


def teile(a, b):
    """Teilt a durch b."""
    return a / b                             # 🐛 was bei b = 0?


def entferne_duplikate(liste):
    """Entfernt Duplikate und behält die Reihenfolge."""
    ergebnis = []
    for x in liste:
        if x not in ergebnis:
            ergebnis.append(x)
    return ergebnis
