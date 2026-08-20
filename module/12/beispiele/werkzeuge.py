"""
Modul 12 - Beispiel: Ein eigenes Modul

Diese Datei kann man IMPORTIEREN (dann läuft nur der obere Teil)
oder DIREKT AUSFÜHREN (dann läuft auch der __main__-Block unten).
"""


def durchschnitt(werte):
    """Berechnet den Mittelwert einer Zahlenliste."""
    if not werte:
        return 0
    return sum(werte) / len(werte)


def formatiere_euro(betrag):
    """Formatiert eine Zahl als deutschen Eurobetrag: 1.234,57 €"""
    text = f"{betrag:,.2f}"
    text = text.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{text} €"


def ist_palindrom(text):
    """Prüft, ob ein Text vorwärts wie rückwärts gelesen gleich ist."""
    sauber = "".join(z for z in text.lower() if z.isalnum())
    return sauber == sauber[::-1]


def fortschrittsbalken(anteil, breite=20):
    """Erzeugt einen Textbalken: anteil zwischen 0.0 und 1.0"""
    gefuellt = int(anteil * breite)
    return "█" * gefuellt + "░" * (breite - gefuellt) + f" {anteil:.0%}"


def trennlinie(zeichen="-", breite=55):
    """Gibt eine Trennlinie zurück."""
    return zeichen * breite


def zeige_tabelle(zeilen, kopf=None, breite=14):
    """Gibt eine Liste von Listen als ausgerichtete Tabelle aus."""
    if kopf:
        print("".join(f"{s:<{breite}}" for s in kopf))
        print(trennlinie("-", breite * len(kopf)))
    for zeile in zeilen:
        print("".join(f"{str(z):<{breite}}" for z in zeile))


# ====================================================================
# Dieser Block läuft NUR bei direktem Start dieser Datei.
# Beim Import (from werkzeuge import ...) wird er übersprungen.
# ====================================================================
if __name__ == "__main__":
    print(trennlinie("="))
    print("SELBSTTEST von werkzeuge.py")
    print(trennlinie("="))

    print(f"durchschnitt([1,2,3,4]) = {durchschnitt([1, 2, 3, 4])}")
    print(f"formatiere_euro(1234.5) = {formatiere_euro(1234.5)}")
    print(f"ist_palindrom('Otto')   = {ist_palindrom('Otto')}")
    print(f"ist_palindrom('Python') = {ist_palindrom('Python')}")
    print(f"fortschrittsbalken(0.7) = {fortschrittsbalken(0.7)}")
    print()
    zeige_tabelle(
        [["Anna", 30, "Berlin"], ["Bernd", 25, "Hamburg"]],
        kopf=["Name", "Alter", "Stadt"],
    )
    print()
    print("💡 Starte stattdessen 01_standardbibliothek.py, um zu sehen,")
    print("   wie dieses Modul importiert wird.")
