"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 02 · MUSTERLÖSUNGEN — Strings                             ║
║  ⛔ Erst nach eigenem Versuch!                                    ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

vorname = "Anna"
nachname = "Schmidt"
alter = 25
print(f"Hallo {vorname} {nachname}, du bist {alter} Jahre alt!")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

wort = "Programmieren"
print(f"Erstes Zeichen: {wort[0]}")
print(f"Letztes Zeichen: {wort[-1]}")
print(f"Länge: {len(wort)}")
print(f"Die ersten 4 Zeichen: {wort[:4]}")
print(f"Die letzten 4 Zeichen: {wort[-4:]}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)

print("Fledermaus"[::-1])


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)

print(f"{'Kaffee':<20}{12.5:>10.2f}")
print(f"{'Tee':<20}{3.99:>10.2f}")
print(f"{'Kakao':<20}{7.125:>10.2f}")

# Mit Kopfzeile sieht es noch besser aus:
print()
print(f"{'Artikel':<20}{'Preis':>10}")
print("-" * 30)
print(f"{'Kaffee':<20}{12.5:>10.2f}")
print(f"{'Tee':<20}{3.99:>10.2f}")
print(f"{'Kakao':<20}{7.125:>10.2f}")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

zeile = "Müller;Anna;1995;Hamburg"
teile = zeile.split(";")
nachname_p, vorname_p, jahr, stadt = teile     # Unpacking!
print(f"{vorname_p} {nachname_p}, geboren {jahr}, wohnhaft in {stadt}")


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)

voller_name = "anna maria schmidt"

# Schritt für Schritt (gut zum Verstehen):
teile = voller_name.split()                  # ['anna','maria','schmidt']
buchstaben = []
for teil in teile:                           # (for kommt in Modul 05 -
    buchstaben.append(teil[0].upper())       #  hier nur als Vorgeschmack)
initialen = ".".join(buchstaben) + "."
print("Variante 1:", initialen)

# Kompakt (Comprehension - kommt in Modul 10):
initialen2 = ".".join(t[0].upper() for t in voller_name.split()) + "."
print("Variante 2:", initialen2)

# Ganz ohne Schleife, nur mit Index (funktioniert bei genau 3 Teilen):
t = voller_name.split()
print("Variante 3:", f"{t[0][0].upper()}.{t[1][0].upper()}.{t[2][0].upper()}.")


print("\n" + "=" * 60, "\nAUFGABE 7 🔴\n", "=" * 60)


def ist_palindrom(text):
    """Prüft, ob text ein Palindrom ist (Groß/Klein & Leerzeichen egal)."""
    bereinigt = text.lower().replace(" ", "")
    return bereinigt == bereinigt[::-1]


wort_a = "Otto"
wort_b = "Ein Esel lese nie"
wort_c = "Python"

for w in (wort_a, wort_b, wort_c):
    antwort = "JA" if ist_palindrom(w) else "NEIN"
    print(f"{w[:40]:<42} -> {antwort}")

# Ohne Funktion, ganz direkt:
print()
bereinigt = wort_a.lower().replace(" ", "")
print("Direkt-Variante für 'Otto':", bereinigt == bereinigt[::-1])


print("\n" + "=" * 60, "\nAUFGABE 8 🔴\n", "=" * 60)

trenner = "+" + "-" * 12 + "+" + "-" * 12 + "+" + "-" * 5 + "+"

print(trenner)
print(f"|{'Name':^12}|{'Stadt':^12}|{'Alt':^5}|")
print(trenner)
print(f"|{'Anna':<12}|{'Berlin':<12}|{30:>5}|")
print(f"|{'Bernd':<12}|{'Hamburg':<12}|{25:>5}|")
print(f"|{'Clara':<12}|{'München':<12}|{41:>5}|")
print(trenner)


print("\n" + "=" * 60, "\nAUFGABE 9 ⭐\n", "=" * 60)

email = "max.mustermann@beispiel-firma.de"

benutzername, domain = email.split("@")
vorname_e, nachname_e = benutzername.split(".")

print(f"Benutzername: {benutzername}")
print(f"Domain:       {domain}")
print(f"Vorname:      {vorname_e.capitalize()}")
print(f"Nachname:     {nachname_e.capitalize()}")
print(f"Anzeigename:  {vorname_e.capitalize()} {nachname_e.capitalize()}")
print(f"Kürzel:       {vorname_e[0]}{nachname_e}")

print("\n🎉 Modul 02 geschafft! Strings sind dein Werkzeug Nr. 1.")
