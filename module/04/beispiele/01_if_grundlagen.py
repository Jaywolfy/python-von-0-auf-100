"""
Modul 04 - Beispiel 1: if / elif / else
"""

# ====================================================================
# EINFACHES IF
# ====================================================================
temperatur = 35

if temperatur > 30:
    print("Es ist heiß! 🥵")
    print("Trink genug Wasser.")     # gehört auch zum if (eingerückt)

print("Diese Zeile läuft immer.\n")  # nicht eingerückt -> außerhalb


# ====================================================================
# EINRÜCKUNG IST LOGIK - der Unterschied
# ====================================================================
print("--- Variante A ---")
x = 3
if x > 10:
    print("groß")
    print("wirklich groß")     # nur wenn x > 10

print("--- Variante B ---")
if x > 10:
    print("groß")
print("wirklich groß")         # LÄUFT IMMER - nicht eingerückt!

print()


# ====================================================================
# IF / ELSE
# ====================================================================
alter = 17

if alter >= 18:
    print("Volljährig ✅")
else:
    print("Minderjährig ❌")

print()


# ====================================================================
# IF / ELIF / ELSE - Reihenfolge zählt!
# ====================================================================
note = 85

if note >= 90:
    bewertung = "Sehr gut 🌟"
elif note >= 80:
    bewertung = "Gut 👍"
elif note >= 70:
    bewertung = "Befriedigend 🙂"
elif note >= 60:
    bewertung = "Ausreichend 😐"
else:
    bewertung = "Nicht bestanden 📚"

print(f"Note {note} → {bewertung}\n")


# ====================================================================
# MEHRERE IF vs. IF/ELIF - der Unterschied!
# ====================================================================
zahl = 15

print("Mit mehreren if (ALLE werden geprüft):")
if zahl > 5:
    print("  > 5")
if zahl > 10:
    print("  > 10")
if zahl > 20:
    print("  > 20")

print("Mit elif (nur der ERSTE Treffer):")
if zahl > 5:
    print("  > 5")
elif zahl > 10:
    print("  > 10")
elif zahl > 20:
    print("  > 20")

print("\n💡 Beides ist richtig - je nachdem, was du willst!\n")


# ====================================================================
# VERKETTETE VERGLEICHE
# ====================================================================
note2 = 75
if 0 <= note2 <= 100:
    print(f"{note2} ist eine gültige Note")

if not (0 <= note2 <= 100):
    print("Ungültig")

print()


# ====================================================================
# TERNARY - die Kurzform
# ====================================================================
temp = 25
status = "warm" if temp > 20 else "kalt"
print(f"Bei {temp}°C ist es {status}")

# gleichbedeutend mit:
if temp > 20:
    status2 = "warm"
else:
    status2 = "kalt"
print(f"Gleiche Logik, lange Form: {status2}")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Ändere note auf 95, 65, 30 - welcher Zweig läuft?
#   2. Vertausche die elif-Reihenfolge (>= 60 nach oben). Was passiert?
#   3. Entferne einen Doppelpunkt. Welche Fehlermeldung kommt?
#   4. Rück eine Zeile falsch ein. Was passiert?
# ------------------------------------------------------------------
