"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 03 · MUSTERLÖSUNGEN                                       ║
║  ⛔ Erst nach eigenem Versuch!                                    ║
║  (input() ist hier durch feste Werte ersetzt, damit die Datei    ║
║   ohne Tippen durchläuft. Die kommentierten Zeilen zeigen, wie   ║
║   es mit echter Eingabe aussähe.)                                ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

a, b = 23, 4
print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b}  = {a % b}")
print(f"{a} ** {b} = {a ** b}")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

# name = input("Name: ")
# geburtsjahr = int(input("Geburtsjahr: "))
name = "Anna"
geburtsjahr = 2001

alter = 2026 - geburtsjahr
print(f"Hallo {name}, du wirst dieses Jahr {alter} Jahre alt.")


print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)

# laenge = float(input("Länge: "))
# breite = float(input("Breite: "))
laenge, breite = 4.5, 3.2

flaeche = laenge * breite
umfang = 2 * (laenge + breite)
print(f"Fläche: {flaeche:.2f} m²")
print(f"Umfang: {umfang:.2f} m")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)

sekunden_gesamt = 100000

tage = sekunden_gesamt // 86400          # 86400 = 24 * 60 * 60
rest = sekunden_gesamt % 86400
stunden = rest // 3600
rest = rest % 3600
minuten = rest // 60
sekunden = rest % 60

print(f"{sekunden_gesamt} Sekunden = {tage} Tag(e), {stunden} Stunden, "
      f"{minuten} Minuten, {sekunden} Sekunden")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

# gewicht = float(input("Gewicht in kg: "))
# groesse = float(input("Größe in m: "))
gewicht, groesse = 78.5, 1.83

bmi = gewicht / (groesse ** 2)
print(f"Dein BMI beträgt {bmi:.1f}")


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)

rechnung = 87.60
trinkgeld_satz = 0.15
personen = 4

trinkgeld = rechnung * trinkgeld_satz
gesamt = rechnung + trinkgeld
pro_person = gesamt / personen

print(f"{'Rechnung:':<18}{rechnung:>8.2f} €")
print(f"{'Trinkgeld (15%):':<18}{trinkgeld:>8.2f} €")
print(f"{'-' * 26}")
print(f"{'Gesamt:':<18}{gesamt:>8.2f} €")
print(f"{'Pro Person:':<18}{pro_person:>8.2f} €")


print("\n" + "=" * 60, "\nAUFGABE 7 🔴\n", "=" * 60)

zahl = 58174

einer      = zahl % 10
zehner     = zahl // 10 % 10
hunderter  = zahl // 100 % 10
tausender  = zahl // 1000 % 10
zehntsd    = zahl // 10000 % 10

quersumme = einer + zehner + hunderter + tausender + zehntsd

print(f"Zahl: {zahl}")
print(f"Ziffern: {zehntsd}, {tausender}, {hunderter}, {zehner}, {einer}")
print(f"Quersumme: {zehntsd} + {tausender} + {hunderter} + {zehner} + {einer} = {quersumme}")

# 💡 Mit einer Schleife (Modul 05) geht das für BELIEBIG lange Zahlen:
rest_zahl = zahl
summe = 0
while rest_zahl > 0:
    summe += rest_zahl % 10      # letzte Ziffer abgreifen
    rest_zahl //= 10             # letzte Ziffer abschneiden
print(f"Mit Schleife berechnet: {summe}")


print("\n" + "=" * 60, "\nAUFGABE 8 🔴\n", "=" * 60)

startkapital = 5000
zinssatz = 0.035
jahre = 10

endkapital = startkapital * (1 + zinssatz) ** jahre
gewinn = endkapital - startkapital
gewinn_prozent = gewinn / startkapital

print(f"{'Startkapital:':<20}{startkapital:>12,.2f} €")
print(f"{'Endkapital:':<20}{endkapital:>12,.2f} €")
print(f"{'Gewinn:':<20}{gewinn:>12,.2f} €")
print(f"{'Gewinn in %:':<20}{gewinn_prozent:>12.1%}")


print("\n" + "=" * 60, "\nAUFGABE 9 ⭐\n", "=" * 60)

# celsius = float(input("Temperatur in °C: "))
# km = float(input("Länge in km: "))
celsius, km = 23.5, 5.0

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

meter = km * 1000
meilen = km * 0.621371
fuss = meter * 3.28084

print("═" * 42)
print("   EINHEITEN-UMRECHNER".center(42))
print("═" * 42)
print(f"{celsius:>9.2f} °C  = {fahrenheit:>9.2f} °F")
print(f"{celsius:>9.2f} °C  = {kelvin:>9.2f} K")
print("-" * 42)
print(f"{km:>9.2f} km  = {meter:>9.2f} m")
print(f"{km:>9.2f} km  = {meilen:>9.2f} Meilen")
print(f"{km:>9.2f} km  = {fuss:>9.2f} Fuß")
print("═" * 42)

print("\n🎉 Modul 03 geschafft!")
