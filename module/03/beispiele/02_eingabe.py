"""
Modul 03 - Beispiel 2: Eingaben vom Nutzer

⚠️ Diese Datei wartet auf Eingaben. Führ sie im TERMINAL aus.
   Zum Testen ohne Tippen sind unten feste Werte vorbereitet.
"""

# ====================================================================
# DIE WICHTIGSTE REGEL: input() gibt IMMER einen String zurück
# ====================================================================

# So NICHT:
#   alter = input("Alter: ")
#   print(alter + 1)          -> TypeError!

# So RICHTIG:
#   alter = int(input("Alter: "))

DEMO_MODUS = True     # auf False setzen, um echte Eingaben zu machen

if DEMO_MODUS:
    name = "Anna"
    alter_text = "25"
    groesse_text = "1.83"
    print("(Demo-Modus: feste Werte statt Eingaben)\n")
else:
    name = input("Wie heißt du? ")
    alter_text = input("Wie alt bist du? ")
    groesse_text = input("Wie groß bist du (in m)? ")

# --- Der entscheidende Schritt: umwandeln ---------------------------
print(f"alter_text hat den Typ: {type(alter_text)}")

alter = int(alter_text)          # str -> int
groesse = float(groesse_text)    # str -> float

print(f"alter hat jetzt den Typ: {type(alter)}")

print()
print(f"Hallo {name}!")
print(f"In 10 Jahren bist du {alter + 10}.")
print(f"Du bist {groesse * 100:.0f} cm groß.")
print(f"Du wurdest ungefähr {2026 - alter} geboren.")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# EIN KLEINER RECHNER
# ====================================================================
if DEMO_MODUS:
    zahl1, zahl2 = 12.0, 5.0
else:
    zahl1 = float(input("Erste Zahl:  "))
    zahl2 = float(input("Zweite Zahl: "))

print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
print(f"{zahl1} - {zahl2} = {zahl1 - zahl2}")
print(f"{zahl1} * {zahl2} = {zahl1 * zahl2}")
print(f"{zahl1} / {zahl2} = {zahl1 / zahl2:.4f}")
print(f"{zahl1} // {zahl2} = {zahl1 // zahl2}")
print(f"{zahl1} % {zahl2} = {zahl1 % zahl2}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# SCHÖNE AUSGABE
# ====================================================================
preis = 1234.5678

print(f"Roh:              {preis}")
print(f"2 Nachkommast.:   {preis:.2f}")
print(f"Mit Trennern:     {preis:,.2f}")
print(f"Rechtsbündig:     {preis:>15,.2f}")

# Deutsches Format: 1.234,57
deutsch = f"{preis:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(f"Deutsches Format: {deutsch} €")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Setz DEMO_MODUS auf False und gib echte Werte ein.
#   2. Was passiert, wenn du bei "Alter" den Text "abc" eingibst?
#      (ValueError - in Modul 13 lernst du, das abzufangen.)
#   3. Bau einen Rechner, der auch die Potenz ausgibt.
# ------------------------------------------------------------------
