"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 08 · MUSTERLÖSUNGEN — Funktionen                          ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)


def quadrat(zahl):
    """Gibt das Quadrat einer Zahl zurück."""
    return zahl ** 2


for z in (3, 7, -4):
    print(f"  quadrat({z}) = {quadrat(z)}")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)


def begruessung(name, sprache="de"):
    """Gibt eine Begrüßung in der gewünschten Sprache zurück."""
    if sprache == "de":
        return f"Hallo {name}!"
    if sprache == "en":
        return f"Hello {name}!"
    if sprache == "fr":
        return f"Bonjour {name}!"
    return f"Hi {name}!"


for s in ("de", "en", "fr", "es"):
    print(f"  {s}: {begruessung('Anna', s)}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)


def verdopple(x):
    """Gibt das Doppelte zurück (statt es nur auszugeben)."""
    return x * 2


print(f"  verdopple(5)             = {verdopple(5)}")
print(f"  verdopple(verdopple(5))  = {verdopple(verdopple(5))}")
print("  💡 Mit print() statt return wäre der zweite Aufruf ein TypeError,")
print("     weil None * 2 nicht geht.")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)


def analysiere(zahlen):
    """Gibt (min, max, summe, durchschnitt) einer Zahlenliste zurück."""
    return min(zahlen), max(zahlen), sum(zahlen), sum(zahlen) / len(zahlen)


kleinste, groesste, gesamt, schnitt = analysiere([4, 9, 2, 7, 5])
print(f"  Minimum:      {kleinste}")
print(f"  Maximum:      {groesste}")
print(f"  Summe:        {gesamt}")
print(f"  Durchschnitt: {schnitt:.2f}")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)


def ist_gerade(zahl):
    """True, wenn die Zahl gerade ist."""
    return zahl % 2 == 0


def filtere_gerade(liste):
    """Gibt eine neue Liste nur mit den geraden Zahlen zurück."""
    ergebnis = []
    for z in liste:
        if ist_gerade(z):
            ergebnis.append(z)
    return ergebnis


def summe_gerade(liste):
    """Summiert alle geraden Zahlen einer Liste."""
    return sum(filtere_gerade(liste))


zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"  Zahlen:        {zahlen}")
print(f"  Gerade:        {filtere_gerade(zahlen)}")
print(f"  Summe gerade:  {summe_gerade(zahlen)}")


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)


def celsius_zu_fahrenheit(c):
    """Rechnet Grad Celsius in Grad Fahrenheit um."""
    return c * 9 / 5 + 32


def fahrenheit_zu_celsius(f):
    """Rechnet Grad Fahrenheit in Grad Celsius um."""
    return (f - 32) * 5 / 9


def celsius_zu_kelvin(c):
    """Rechnet Grad Celsius in Kelvin um."""
    return c + 273.15


print(f"  20 °C = {celsius_zu_fahrenheit(20):.1f} °F")
print(f"  68 °F = {fahrenheit_zu_celsius(68):.1f} °C")
print(f"  20 °C = {celsius_zu_kelvin(20):.2f} K")
print(f"  Hin und zurück: {fahrenheit_zu_celsius(celsius_zu_fahrenheit(20)):.1f} °C ✅")


print("\n" + "=" * 60, "\nAUFGABE 7 🥗 MIX\n", "=" * 60)


def pruefe_passwort(pw):
    """Prüft ein Passwort und gibt ein Ergebnis-Dictionary zurück."""
    ergebnis = {
        "passwort": pw,
        "laenge_ok": len(pw) >= 8,
        "hat_ziffer": any(z.isdigit() for z in pw),
        "hat_gross": any(z.isupper() for z in pw),
        "hat_klein": any(z.islower() for z in pw),
    }
    punkte = sum([ergebnis["laenge_ok"], ergebnis["hat_ziffer"],
                  ergebnis["hat_gross"], ergebnis["hat_klein"]])
    ergebnis["punkte"] = punkte

    if punkte <= 1:
        ergebnis["bewertung"] = "SEHR SCHWACH 🔴"
    elif punkte == 2:
        ergebnis["bewertung"] = "SCHWACH 🟠"
    elif punkte == 3:
        ergebnis["bewertung"] = "MITTEL 🟡"
    else:
        ergebnis["bewertung"] = "STARK 🟢"
    return ergebnis


def zeige_bericht(ergebnis):
    """Gibt ein Prüfergebnis lesbar aus."""
    haken = {True: "✅", False: "❌"}
    print(f"  Passwort: {ergebnis['passwort']}")
    print(f"    {haken[ergebnis['laenge_ok']]} mindestens 8 Zeichen")
    print(f"    {haken[ergebnis['hat_ziffer']]} enthält Ziffer")
    print(f"    {haken[ergebnis['hat_gross']]} enthält Großbuchstaben")
    print(f"    {haken[ergebnis['hat_klein']]} enthält Kleinbuchstaben")
    balken = "█" * ergebnis["punkte"] + "░" * (4 - ergebnis["punkte"])
    print(f"    {balken}  {ergebnis['bewertung']}\n")


for pw in ("abc", "sonnenschein", "Sonne2026"):
    zeige_bericht(pruefe_passwort(pw))


print("=" * 60, "\nAUFGABE 8 🔴 - Scope\n", "=" * 60)

# Vorhersage:
#   f1() -> 20   (eigene lokale Variable x)
#   f2() -> 10   (liest die globale Variable)
#   f3(x) -> 15  (Parameter x=10, lokal +5)
#   x -> 10      (global unverändert!)

x = 10


def f1():
    x = 20
    return x


def f2():
    return x


def f3(x):
    x = x + 5
    return x


print(f"  f1()={f1()}  f2()={f2()}  f3(x)={f3(x)}  x={x}")
print("  💡 f3 verändert nur seine eigene lokale Kopie des Parameters.")


print("\n" + "=" * 60, "\nAUFGABE 9 🔴 - Refactoring\n", "=" * 60)


def zeilensumme(preis, menge):
    """Berechnet den Gesamtpreis einer Position."""
    return preis * menge


def zeige_position(name, preis, menge):
    """Gibt eine Rechnungsposition formatiert aus."""
    summe = zeilensumme(preis, menge)
    print(f"  {name:<12}{menge:>3} x {preis:>8.2f} = {summe:>9.2f}")
    return summe


def berechne_mwst(netto, satz=0.19):
    """Berechnet die Mehrwertsteuer auf einen Nettobetrag."""
    return netto * satz


def main():
    """Erstellt eine komplette Rechnung."""
    produkte = [["Laptop", 899.99, 2], ["Maus", 25.50, 5], ["Tastatur", 79.00, 3]]

    netto = 0
    print("  RECHNUNG")
    print("  " + "-" * 40)
    for name, preis, menge in produkte:
        netto += zeige_position(name, preis, menge)

    mwst = berechne_mwst(netto)
    print("  " + "-" * 40)
    print(f"  {'Netto:':<20}{netto:>18.2f}")
    print(f"  {'MwSt (19 %):':<20}{mwst:>18.2f}")
    print(f"  {'Brutto:':<20}{netto + mwst:>18.2f}")


main()


print("\n" + "=" * 60, "\nAUFGABE 10 ⭐ - Rekursion\n", "=" * 60)


def fakultaet(n):
    """Berechnet n! rekursiv."""
    if n <= 1:              # Abbruchbedingung - ohne sie: RecursionError!
        return 1
    return n * fakultaet(n - 1)


for n in (1, 5, 10):
    print(f"  {n}! = {fakultaet(n)}")

print("""
  💡 So läuft fakultaet(4) ab:
     fakultaet(4) = 4 * fakultaet(3)
                  = 4 * 3 * fakultaet(2)
                  = 4 * 3 * 2 * fakultaet(1)
                  = 4 * 3 * 2 * 1
                  = 24
""")

print("🎉 Modul 08 geschafft! Du baust jetzt Software, keine Skripte mehr.")
