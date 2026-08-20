"""
Modul 08 - Beispiel 2: Vom Skript zum strukturierten Programm

Dieselbe Aufgabe zweimal:
  A) als langes Skript      -> funktioniert, aber unwartbar
  B) mit Funktionen         -> wiederverwendbar, testbar, lesbar
"""

# ====================================================================
# A) DAS LANGE SKRIPT ❌
# ====================================================================
print("=" * 55)
print("VARIANTE A - alles hintereinander")
print("=" * 55)

noten_anna = [2.3, 1.7, 3.0]
summe = 0
for n in noten_anna:
    summe += n
schnitt = summe / len(noten_anna)
print(f"Anna: Durchschnitt {schnitt:.2f}")
if schnitt <= 2.0:
    print("  Bewertung: Sehr gut")
elif schnitt <= 3.0:
    print("  Bewertung: Gut")
else:
    print("  Bewertung: Ausbaufähig")

# Und für Bernd? Alles nochmal kopieren... 😰
noten_bernd = [1.0, 1.3, 1.7]
summe = 0
for n in noten_bernd:
    summe += n
schnitt = summe / len(noten_bernd)
print(f"Bernd: Durchschnitt {schnitt:.2f}")
if schnitt <= 2.0:
    print("  Bewertung: Sehr gut")
elif schnitt <= 3.0:
    print("  Bewertung: Gut")
else:
    print("  Bewertung: Ausbaufähig")


# ====================================================================
# B) MIT FUNKTIONEN ✅
# ====================================================================
print("\n" + "=" * 55)
print("VARIANTE B - in Bausteine zerlegt")
print("=" * 55)


def durchschnitt(werte):
    """Berechnet den Mittelwert einer Zahlenliste."""
    return sum(werte) / len(werte)


def bewerte(schnitt):
    """Wandelt einen Notenschnitt in eine Textbewertung um."""
    if schnitt <= 2.0:
        return "Sehr gut"
    if schnitt <= 3.0:
        return "Gut"
    return "Ausbaufähig"


def zeige_zeugnis(name, noten):
    """Gibt ein formatiertes Zeugnis für eine Person aus."""
    schnitt = durchschnitt(noten)
    print(f"{name:<8} Ø {schnitt:.2f}  →  {bewerte(schnitt)}")


def main():
    """Hauptprogramm."""
    klasse = {
        "Anna":  [2.3, 1.7, 3.0],
        "Bernd": [1.0, 1.3, 1.7],
        "Clara": [3.7, 4.0, 3.3],
        "David": [2.0, 2.3, 1.7],
    }

    for name, noten in klasse.items():
        zeige_zeugnis(name, noten)

    alle_noten = []
    for noten in klasse.values():
        alle_noten.extend(noten)

    print("-" * 40)
    print(f"Klassenschnitt: {durchschnitt(alle_noten):.2f}")


main()

print("""
💡 WAS HAT SICH VERBESSERT?
   • Neue Person hinzufügen = EINE Zeile statt 12
   • bewerte() lässt sich einzeln testen
   • Jede Funktion ist kurz und hat einen klaren Namen
   • Bei einer Änderung an der Bewertung: nur EINE Stelle anfassen
   • main() liest sich wie eine Inhaltsangabe des Programms
""")
