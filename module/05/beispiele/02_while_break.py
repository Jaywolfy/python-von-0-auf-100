"""
Modul 05 - Beispiel 2: while, break, continue, verschachtelte Schleifen
"""

# ====================================================================
# WHILE
# ====================================================================
zaehler = 0
while zaehler < 5:
    print(f"Durchlauf {zaehler}")
    zaehler += 1              # ⚠️ OHNE diese Zeile: Endlosschleife!

print(f"Fertig. zaehler = {zaehler}\n")


# Countdown
sekunden = 5
while sekunden > 0:
    print(f"{sekunden}...", end=" ")
    sekunden -= 1
print("Start! 🚀\n")

print("-" * 55 + "\n")


# ====================================================================
# BREAK & CONTINUE
# ====================================================================
print("break - Schleife komplett verlassen:")
for zahl in range(100):
    if zahl > 5:
        break
    print(f"  {zahl}", end="")
print("\n  -> abgebrochen bei 6\n")

print("continue - diesen Durchlauf überspringen:")
for zahl in range(10):
    if zahl % 2 != 0:
        continue              # ungerade überspringen
    print(f"  {zahl}", end="")
print("\n  -> nur gerade Zahlen\n")

print("-" * 55 + "\n")


# ====================================================================
# WHILE TRUE + BREAK  (typisches Menü-Muster)
# ====================================================================
befehle = ["hilfe", "status", "unsinn", "ende"]   # simulierte Eingaben
index = 0

while True:
    # In echt: befehl = input("Befehl: ")
    befehl = befehle[index]
    index += 1
    print(f"Eingabe: {befehl}")

    if befehl == "ende":
        print("  Programm wird beendet. 👋")
        break
    elif befehl == "hilfe":
        print("  Verfügbare Befehle: hilfe, status, ende")
    elif befehl == "status":
        print("  Alles läuft. ✅")
    else:
        print("  Unbekannter Befehl. Tippe 'hilfe'.")

print("\n" + "-" * 55 + "\n")


# ====================================================================
# VERSCHACHTELTE SCHLEIFEN
# ====================================================================
print("Rechteck 4x3:")
for zeile in range(3):
    for spalte in range(4):
        print("*", end=" ")
    print()                    # Umbruch nach jeder Zeile

print("\nKleines Einmaleins:")
print("     ", end="")
for s in range(1, 6):
    print(f"{s:>4}", end="")
print("\n" + "-" * 25)

for z in range(1, 6):
    print(f"{z:>3} |", end="")
    for s in range(1, 6):
        print(f"{z * s:>4}", end="")
    print()

print("\nDreieck:")
hoehe = 5
for i in range(1, hoehe + 1):
    print("*" * i)

print("\nPyramide:")
for i in range(1, hoehe + 1):
    leerzeichen = " " * (hoehe - i)
    sterne = "*" * (2 * i - 1)
    print(leerzeichen + sterne)

print("\n" + "-" * 55 + "\n")


# ====================================================================
# FOR ... ELSE
# ====================================================================
zahlen = [1, 3, 5, 7]

for z in zahlen:
    if z % 2 == 0:
        print(f"Gerade Zahl gefunden: {z}")
        break
else:
    print(f"In {zahlen} ist keine gerade Zahl. (else lief, weil kein break kam)")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Bau die Pyramide "auf dem Kopf".
#   2. Erweitere das Einmaleins auf 10x10.
#   3. Baue einen Countdown von 10 mit while.
#   4. Was passiert, wenn du "zaehler += 1" entfernst? (Strg+C hilft! 😄)
# ------------------------------------------------------------------
