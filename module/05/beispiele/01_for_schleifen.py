"""
Modul 05 - Beispiel 1: for-Schleifen
"""

# ====================================================================
# RANGE
# ====================================================================
print("range(5):        ", end="")
for i in range(5):
    print(i, end=" ")

print("\nrange(2, 6):     ", end="")
for i in range(2, 6):
    print(i, end=" ")

print("\nrange(0, 11, 2): ", end="")
for i in range(0, 11, 2):
    print(i, end=" ")

print("\nrange(10, 0, -1):", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")

print("\n\n" + "-" * 55 + "\n")


# ====================================================================
# ÜBER DINGE ITERIEREN
# ====================================================================
for buchstabe in "Python":
    print(buchstabe, end=" | ")
print("\n")

fruechte = ["Apfel", "Birne", "Kirsche"]
for frucht in fruechte:
    print(f"Ich mag {frucht}")

print()

# Mit Index UND Wert
for i, frucht in enumerate(fruechte):
    print(f"  Index {i}: {frucht}")

print()

# Nummeriert ab 1
for nr, frucht in enumerate(fruechte, start=1):
    print(f"  {nr}. {frucht}")

print("\n" + "-" * 55 + "\n")


# ====================================================================
# DAS AKKUMULATOR-MUSTER ⭐
# ====================================================================
zahlen = [3, 7, 2, 8, 5]

# 1) Summieren
summe = 0                     # Behälter VOR der Schleife!
for zahl in zahlen:
    summe += zahl
print(f"Summe von {zahlen} = {summe}")

# 2) Zählen
wort = "banana"
anzahl_a = 0
for z in wort:
    if z == "a":
        anzahl_a += 1
print(f"'{wort}' enthält {anzahl_a}x den Buchstaben 'a'")

# 3) Sammeln (filtern)
grosse = []
for zahl in zahlen:
    if zahl > 4:
        grosse.append(zahl)
print(f"Zahlen größer als 4: {grosse}")

# 4) Maximum finden
groesste = zahlen[0]
for zahl in zahlen:
    if zahl > groesste:
        groesste = zahl
print(f"Größte Zahl: {groesste}")

# 5) Text aufbauen
initialen = ""
for name in ["Anna", "Bernd", "Clara"]:
    initialen += name[0]
print(f"Initialen: {initialen}")

print("\n" + "-" * 55 + "\n")


# ====================================================================
# HÄUFIGSTER FEHLER: Akkumulator IN der Schleife
# ====================================================================
print("❌ FALSCH:")
for z in [1, 2, 3]:
    falsche_summe = 0        # wird jedes Mal zurückgesetzt!
    falsche_summe += z
print(f"   Ergebnis: {falsche_summe}  (erwartet wäre 6)")

print("✅ RICHTIG:")
richtige_summe = 0
for z in [1, 2, 3]:
    richtige_summe += z
print(f"   Ergebnis: {richtige_summe}")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Summiere alle Zahlen von 1 bis 1000.
#   2. Zähle die Vokale in einem Satz.
#   3. Baue aus ["a","b","c"] den String "a-b-c" mit einer Schleife.
# ------------------------------------------------------------------
