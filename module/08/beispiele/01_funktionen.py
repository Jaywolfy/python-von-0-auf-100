"""
Modul 08 - Beispiel 1: Funktionen von Grund auf
"""

# ====================================================================
# 1. OHNE PARAMETER
# ====================================================================
def begruesse():
    """Gibt eine feste Begrüßung aus."""
    print("Hallo!")
    print("Schön, dass du da bist.\n")


begruesse()          # Definition allein macht nichts - erst der Aufruf!
begruesse()


# ====================================================================
# 2. MIT PARAMETERN
# ====================================================================
def begruesse_person(name, gruss="Hallo"):
    """Begrüßt eine Person mit optionalem Gruß."""
    print(f"{gruss}, {name}!")


begruesse_person("Anna")
begruesse_person("Bernd", "Moin")
begruesse_person(gruss="Servus", name="Clara")     # Reihenfolge egal
print()


# ====================================================================
# 3. ⭐ PRINT vs. RETURN - der wichtigste Unterschied
# ====================================================================
def addiere_print(a, b):
    print(a + b)


def addiere_return(a, b):
    return a + b


print("Mit print:")
x = addiere_print(3, 5)
print(f"  x = {x}     ← None! Man kann damit nicht weiterrechnen.")

print("Mit return:")
y = addiere_return(3, 5)
print(f"  y = {y}        ← der Wert ist da")
print(f"  y * 2 = {y * 2}   ← und damit kann man weiterarbeiten ✅\n")


# ====================================================================
# 4. RETURN BEENDET DIE FUNKTION SOFORT
# ====================================================================
def pruefe_zahl(zahl):
    """Klassifiziert eine Zahl als negativ/null/positiv."""
    if zahl < 0:
        return "negativ"          # ab hier ist die Funktion zu Ende
    if zahl == 0:
        return "null"
    return "positiv"


for z in (-5, 0, 42):
    print(f"  {z:>3} ist {pruefe_zahl(z)}")
print()


# ====================================================================
# 5. MEHRERE RÜCKGABEWERTE
# ====================================================================
def statistik(zahlen):
    """Gibt Minimum, Maximum, Summe und Durchschnitt zurück."""
    return min(zahlen), max(zahlen), sum(zahlen), sum(zahlen) / len(zahlen)


kleinste, groesste, summe, schnitt = statistik([4, 9, 2, 7, 5])
print(f"min={kleinste}  max={groesste}  summe={summe}  Ø={schnitt:.2f}\n")


# ====================================================================
# 6. SCOPE - wo gilt welche Variable?
# ====================================================================
zahl = 10          # global


def aendere_lokal():
    zahl = 99      # eine EIGENE, lokale Variable
    print(f"  In der Funktion: {zahl}")


def lese_global():
    print(f"  Global gelesen:  {zahl}")     # Lesen geht


print("Scope:")
aendere_lokal()
lese_global()
print(f"  Außerhalb:       {zahl}   ← unverändert!\n")


# ====================================================================
# 7. ⚠️ DIE DEFAULT-FALLE
# ====================================================================
def schlecht(item, liste=[]):        # ❌ Default wird geteilt!
    liste.append(item)
    return liste


def gut(item, liste=None):           # ✅
    if liste is None:
        liste = []
    liste.append(item)
    return liste


print("❌ Mit liste=[] als Default:")
print(f"   {schlecht('a')}")
print(f"   {schlecht('b')}   ← 'a' ist noch drin! 😱")

print("✅ Mit liste=None:")
print(f"   {gut('a')}")
print(f"   {gut('b')}   ← wie erwartet\n")


# ====================================================================
# 8. DOCSTRINGS
# ====================================================================
def berechne_bmi(gewicht_kg, groesse_m):
    """Berechnet den Body-Mass-Index.

    Args:
        gewicht_kg: Gewicht in Kilogramm.
        groesse_m: Körpergröße in Metern.

    Returns:
        Der BMI als float, gerundet auf 1 Nachkommastelle.
    """
    return round(gewicht_kg / groesse_m ** 2, 1)


print(f"BMI: {berechne_bmi(78, 1.83)}")
print("\nDocstring über help():")
print(berechne_bmi.__doc__)

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Schreib eine Funktion, die prüft, ob eine Zahl gerade ist.
#   2. Schreib eine Funktion, die eine Liste umdreht (ohne [::-1]).
#   3. Was passiert, wenn du eine Funktion VOR ihrer Definition aufrufst?
# ------------------------------------------------------------------
