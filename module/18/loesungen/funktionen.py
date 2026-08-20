"""Modul 18 - Reparierte Version der Funktionen."""


def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b


def durchschnitt(werte):
    """Berechnet den Mittelwert.

    Raises:
        ValueError: wenn die Liste leer ist.
    """
    if not werte:
        raise ValueError("Liste darf nicht leer sein")
    return sum(werte) / len(werte)


def ist_gerade(zahl):
    """Prüft, ob eine Zahl gerade ist."""
    return zahl % 2 == 0


def groesste(zahlen):
    """Findet die größte Zahl einer Liste.

    Raises:
        ValueError: wenn die Liste leer ist.
    """
    if not zahlen:
        raise ValueError("Liste darf nicht leer sein")
    maximum = zahlen[0]              # ✅ FIX: erstes Element statt 0
    for z in zahlen:
        if z > maximum:
            maximum = z
    return maximum


def ist_palindrom(text):
    """Prüft, ob ein Text ein Palindrom ist (Satzzeichen werden ignoriert)."""
    sauber = "".join(z for z in text.lower() if z.isalnum())
    return sauber == sauber[::-1]


def zaehle_vokale(text):
    """Zählt die Vokale in einem Text (inkl. Umlaute)."""
    return sum(1 for z in text.lower() if z in "aeiouäöü")


def formatiere_euro(betrag):
    """Formatiert eine Zahl als deutschen Eurobetrag."""
    text = f"{betrag:,.2f}"
    text = text.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{text} €"


def note_zu_text(note):
    """Wandelt eine Schulnote (1-6) in Text um.

    Raises:
        ValueError: bei ungültiger Note.
    """
    texte = {1: "sehr gut", 2: "gut", 3: "befriedigend",
             4: "ausreichend", 5: "mangelhaft", 6: "ungenügend"}
    if note not in texte:
        raise ValueError(f"Ungültige Note: {note} (erlaubt: 1-6)")
    return texte[note]


def teile(a, b):
    """Teilt a durch b.

    Raises:
        ValueError: wenn b gleich 0 ist.
    """
    if b == 0:
        raise ValueError("Division durch Null ist nicht erlaubt")
    return a / b


def entferne_duplikate(liste):
    """Entfernt Duplikate und behält die Reihenfolge."""
    ergebnis = []
    for x in liste:
        if x not in ergebnis:
            ergebnis.append(x)
    return ergebnis


def kuerze_text(text, max_laenge=20):
    """Kürzt einen Text auf max_laenge Zeichen inklusive '...'.

    Raises:
        ValueError: wenn max_laenge kleiner als 4 ist.
    """
    if max_laenge < 4:
        raise ValueError("max_laenge muss mindestens 4 sein")
    if len(text) <= max_laenge:
        return text
    return text[:max_laenge - 3] + "..."
