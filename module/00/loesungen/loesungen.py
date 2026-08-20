"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 00 · MUSTERLÖSUNGEN                                       ║
╠══════════════════════════════════════════════════════════════════╣
║  ⛔ STOPP! Hast du wirklich 15 Minuten selbst probiert?          ║
║                                                                  ║
║  Wenn ja: super, vergleiche jetzt.                               ║
║  Wenn nein: Datei schließen, zurück zu den Aufgaben. 😊          ║
║                                                                  ║
║  💡 Deine Lösung sieht anders aus? Das ist völlig okay!          ║
║     In Python führen viele Wege zum Ziel.                        ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60)
print("AUFGABE 1 🟢")
print("=" * 60)

print("Ich heiße Anna.")


print("\n" + "=" * 60)
print("AUFGABE 2 🟢")
print("=" * 60)

print("Name: Anna")
print("Alter: 25")
print("Lieblingsfarbe: Blau")
print("Ich lerne Python, um meinen Alltag zu automatisieren.")


print("\n" + "=" * 60)
print("AUFGABE 3 🟢")
print("=" * 60)

# Wichtig: drei getrennte Werte + sep
print("26", "07", "2026", sep=".")


print("\n" + "=" * 60)
print("AUFGABE 4 🟡")
print("=" * 60)

print("-" * 50)
print("  MEIN PROGRAMM  ")
print("-" * 50)

# Variante mit Zentrierung (schöner):
print("-" * 50)
print("MEIN PROGRAMM".center(50))
print("-" * 50)


print("\n" + "=" * 60)
print("AUFGABE 5 🟡")
print("=" * 60)

# Variante A: vier einzelne prints
print("*" * 10)
print("*" * 10)
print("*" * 10)
print("*" * 10)

# Variante B: eleganter, mit \n als Trenner
print()
print("*" * 10, "*" * 10, "*" * 10, "*" * 10, sep="\n")

# Variante C: ganz kurz (Trick: String mit \n multiplizieren)
print()
print(("*" * 10 + "\n") * 4, end="")


print("\n" + "=" * 60)
print("AUFGABE 6 🟡")
print("=" * 60)

print("Starte Programm", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" OK")


print("\n" + "=" * 60)
print("AUFGABE 7 🔴")
print("=" * 60)

# print("Hallo)
# SyntaxError: unterminated string literal
# -> Ich habe einen Text mit " begonnen, aber nie geschlossen.
#    Python liest bis zum Zeilenende und findet kein Ende des Textes.

# prnt("Hallo")
# NameError: name 'prnt' is not defined
# -> Tippfehler. Python kennt keine Funktion namens 'prnt'.
#    Es schlägt manchmal sogar vor: "Did you mean: 'print'?"

# print(Hallo)
# NameError: name 'Hallo' is not defined
# -> Ohne Anführungszeichen interpretiert Python 'Hallo' als
#    Variablennamen. Eine Variable mit diesem Namen existiert nicht.

print("Alle drei Fehler sind auskommentiert - die Datei läuft durch. ✅")


print("\n" + "=" * 60)
print("AUFGABE 8 ⭐")
print("=" * 60)

print("   /\\_/\\  ")
print("  ( o.o ) ")
print("   > ^ <  ")
print("  Miau! 🐱")

print()
print("     /\\      ")
print("    /  \\     ")
print("   /____\\    ")
print("   |    |    ")
print("   | [] |    ")
print("   |____|    ")
print("  Mein Haus 🏠")


print("\n" + "=" * 60)
print("🎉 Modul 00 geschafft! Weiter zu Modul 01.")
print("=" * 60)
