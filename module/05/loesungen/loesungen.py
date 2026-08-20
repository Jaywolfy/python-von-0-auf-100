"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 05 · MUSTERLÖSUNGEN — Schleifen                           ║
║  ⛔ Erst nach eigenem Versuch!                                    ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

for i in range(1, 21):
    print(i, end=" ")
print()

for i in range(20, 0, -1):
    print(i, end=" ")
print()


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

summe = 0
for i in range(1, 101):
    summe += i
print(f"Summe 1 bis 100 = {summe}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)

wort = "Automatisierung"
for nr, buchstabe in enumerate(wort, start=1):
    print(f"{nr:>2}. {buchstabe}")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)

for zahl in range(1, 51):
    if zahl % 3 != 0:
        continue                # nicht durch 3 teilbar -> überspringen
    if zahl % 5 == 0:
        continue                # Vielfaches von 5 -> überspringen
    print(zahl, end=" ")
print()


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

print("     ", end="")
for s in range(1, 11):
    print(f"{s:>5}", end="")
print("\n" + "-" * 57)

for z in range(1, 11):
    print(f"{z:>3} |", end="")
    for s in range(1, 11):
        print(f"{z * s:>5}", end="")
    print()


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)

satz = "Python macht Programmieren einfach und macht Spass"
satz_klein = satz.lower()

for vokal in "aeiou":
    anzahl = 0
    for zeichen in satz_klein:
        if zeichen == vokal:
            anzahl += 1
    balken = "█" * anzahl
    print(f"{vokal}: {anzahl:>2}  {balken}")

# 💡 Kürzer ginge auch: satz_klein.count(vokal)


print("\n" + "=" * 60, "\nAUFGABE 7 🔴 - FizzBuzz\n", "=" * 60)

for zahl in range(1, 51):
    # WICHTIG: die kombinierte Bedingung MUSS zuerst kommen!
    if zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz", end="  ")
    elif zahl % 3 == 0:
        print("Fizz", end="  ")
    elif zahl % 5 == 0:
        print("Buzz", end="  ")
    else:
        print(zahl, end="  ")
print("\n")
print("💡 Stünde 'if zahl % 3 == 0' zuerst, käme bei 15 nur 'Fizz' heraus.")


print("\n" + "=" * 60, "\nAUFGABE 8 🔴 - Muster\n", "=" * 60)

HOEHE = 5      # nur HIER ändern!

print("A) Wachsendes Dreieck:")
for i in range(1, HOEHE + 1):
    print("*" * i)

print("\nB) Schrumpfendes Dreieck:")
for i in range(HOEHE, 0, -1):
    print("*" * i)

print("\nC) Rechtsbündiges Dreieck:")
for i in range(1, HOEHE + 1):
    print(" " * (HOEHE - i) + "*" * i)

print("\nD) Sanduhr / Schmetterling:")
for i in range(1, HOEHE + 1):
    links = "*" * i
    mitte = " " * (2 * (HOEHE - i))
    print(links + mitte + links)


print("\n" + "=" * 60, "\nAUFGABE 9 🔴\n", "=" * 60)

gesucht = 42
versuche = [50, 25, 37, 43, 42]

for nr, versuch in enumerate(versuche, start=1):
    if versuch > gesucht:
        print(f"Versuch {nr}: {versuch} → zu hoch  ⬆️")
    elif versuch < gesucht:
        print(f"Versuch {nr}: {versuch} → zu niedrig ⬇️")
    else:
        print(f"Versuch {nr}: {versuch} → RICHTIG! 🎉")
        print(f"Du hast {nr} Versuche gebraucht.")
        break
else:
    print("Zahl nicht gefunden.")


print("\n" + "=" * 60, "\nAUFGABE 10 ⭐ - Primzahlen\n", "=" * 60)

print("Primzahlen bis 50:")
for zahl in range(2, 51):
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            break               # Teiler gefunden -> keine Primzahl
    else:
        # else gehört zum for: läuft nur, wenn KEIN break kam
        print(zahl, end=" ")
print()

# Schnellere Variante: nur bis zur Wurzel prüfen
print("\nSchnellere Variante (nur bis zur Wurzel prüfen):")
for zahl in range(2, 51):
    ist_prim = True
    teiler = 2
    while teiler * teiler <= zahl:
        if zahl % teiler == 0:
            ist_prim = False
            break
        teiler += 1
    if ist_prim:
        print(zahl, end=" ")
print()

print("\n🎉 Modul 05 geschafft! Jetzt kannst du automatisieren. 🤖")
