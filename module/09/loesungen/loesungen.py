"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 09 · MUSTERLÖSUNGEN — Debugging                           ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60)
print("FEHLER 1-7: LAUFZEIT- UND SYNTAXFEHLER")
print("=" * 60)

# --- FEHLER 1 -------------------------------------------------------
# SyntaxError: '(' was never closed
# Die schließende Klammer von print() fehlt.
name = "Anna"
print("1) Hallo " + name)

# --- FEHLER 2 -------------------------------------------------------
# TypeError: can only concatenate str (not "int") to str
# alter ist ein String. "25" + 1 geht nicht.
alter = "25"
print("2) Nächstes Jahr: " + str(int(alter) + 1))
print(f"   Besser mit f-String: Nächstes Jahr: {int(alter) + 1}")

# --- FEHLER 3 -------------------------------------------------------
# IndexError: list index out of range
# Die Liste hat 3 Elemente -> gültige Indizes sind 0, 1, 2.
zahlen = [1, 2, 3]
print(f"3) Letztes Element: {zahlen[-1]}  (nicht zahlen[3]!)")

# --- FEHLER 4 -------------------------------------------------------
# KeyError: 'stadt'
# Der Schlüssel existiert nicht.
person = {"name": "Anna", "alter": 30}
print(f"4) Stadt: {person.get('stadt', 'unbekannt')}")

# --- FEHLER 5 -------------------------------------------------------
# IndentationError: expected an indented block
# Nach 'def ...:' MUSS der Funktionskörper eingerückt sein.
def gruesse(name):
    print(f"5) Hallo {name}")


gruesse("Anna")

# --- FEHLER 6 -------------------------------------------------------
# TypeError: addiere() missing 1 required positional argument: 'b'
# Die Funktion braucht zwei Argumente.
def addiere(a, b):
    return a + b


print(f"6) addiere(5, 3) = {addiere(5, 3)}")

# --- FEHLER 7 -------------------------------------------------------
# AttributeError: 'list' object has no attribute 'push'
# push() gibt es in JavaScript, in Python heißt es append().
woerter = ["Apfel", "Birne"]
woerter.append("Kirsche")
print(f"7) {woerter}")


print("\n" + "=" * 60)
print("FEHLER 8-11: LOGIKFEHLER (die schwierigen!)")
print("=" * 60)

# --- FEHLER 8 -------------------------------------------------------
# FEHLER: 'summe = 0' steht INNERHALB der Schleife und wird bei jedem
# Durchlauf zurückgesetzt. Der Akkumulator muss VOR die Schleife.
def summiere(zahlen):
    summe = 0                # ✅ vor der Schleife
    for z in zahlen:
        summe += z
    return summe


print(f"8)  summiere([10,20,30]) = {summiere([10, 20, 30])} ✅")

# --- FEHLER 9 -------------------------------------------------------
# FEHLER: Off-by-one. range(len(liste) - 1) lässt das letzte Element aus.
def zeige_alle(liste):
    for element in liste:    # ✅ noch einfacher: direkt iterieren
        print(f"    {element}")


print("9)  Alle Elemente:")
zeige_alle(["a", "b", "c"])

# --- FEHLER 10 ------------------------------------------------------
# FEHLER: maximum startet bei 0. Sind ALLE Zahlen negativ, bleibt 0
# stehen - obwohl 0 gar nicht in der Liste ist.
def groesste(zahlen):
    if not zahlen:
        return None
    maximum = zahlen[0]      # ✅ mit dem ERSTEN Element starten
    for z in zahlen:
        if z > maximum:
            maximum = z
    return maximum


print(f"10) groesste([-5,-2,-9]) = {groesste([-5, -2, -9])} ✅")

# --- FEHLER 11 ------------------------------------------------------
# FEHLER: Man verändert die Liste, WÄHREND man über sie iteriert.
# Nach dem Entfernen von -2 rutscht -3 auf die Position von -2,
# die Schleife ist aber schon weitergegangen -> -3 wird übersprungen.
def entferne_negative(zahlen):
    ergebnis = []            # ✅ neue Liste bauen statt verändern
    for z in zahlen:
        if z >= 0:
            ergebnis.append(z)
    return ergebnis


print(f"11) entferne_negative([1,-2,-3,4]) = {entferne_negative([1, -2, -3, 4])} ✅")
print("    (Mit Comprehension aus Modul 10: [z for z in zahlen if z >= 0])")


print("\n" + "=" * 60)
print("🎓 DIE 5 WICHTIGSTEN LEHREN")
print("=" * 60)
print("""
 1. Akkumulator IMMER vor die Schleife
 2. Bei range(): Grenzen doppelt prüfen (off-by-one)
 3. Startwerte für min/max: erstes Element, nicht 0
 4. Niemals eine Liste verändern, über die du gerade iterierst
 5. input() und Dateiinhalte sind IMMER Strings

 Und die wichtigste Regel überhaupt:
 👉 Wenn das Ergebnis falsch ist, print() an JEDEN Zwischenschritt.
    Der Fehler steckt immer zwischen "hier war es noch richtig"
    und "hier ist es schon falsch".
""")
