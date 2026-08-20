"""
Modul 02 - Beispiel 1: f-Strings (die wichtigste Technik!)
"""

name = "Anna"
alter = 30
groesse = 1.7234
kontostand = 1234567.891
anteil = 0.8567

# ====================================================================
# GRUNDLAGEN
# ====================================================================
print(f"{name} ist {alter} Jahre alt.")
print(f"Nächstes Jahr wird {name} {alter + 1}.")       # Rechnen in {} erlaubt
print(f"Groß geschrieben: {name.upper()}")             # Methoden auch
print(f"Der Name hat {len(name)} Buchstaben.")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# ZAHLEN FORMATIEREN
# ====================================================================
print(f"Größe roh:            {groesse}")
print(f"Größe 2 Stellen:      {groesse:.2f}")
print(f"Größe 1 Stelle:       {groesse:.1f}")
print(f"Ohne Nachkomma:       {groesse:.0f}")

print()
print(f"Kontostand:           {kontostand:.2f}")
print(f"Mit Tausendertrenner: {kontostand:,.2f}")
print(f"Als Prozent:          {anteil:.1%}")
print(f"Führende Nullen:      {42:05d}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# AUSRICHTUNG - so baut man Tabellen!
# ====================================================================
print(f"|{'links':<15}|{'rechts':>15}|{'mitte':^15}|")
print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
print(f"|{'Anna':<15}|{'30':>15}|{'Berlin':^15}|")
print(f"|{'Bernd':<15}|{'25':>15}|{'Hamburg':^15}|")

print()
print(f"{'Titel':*^40}")        # mit Füllzeichen zentrieren

print("\n" + "-" * 55 + "\n")

# ====================================================================
# EINE ECHTE TABELLE
# ====================================================================
print(f"{'Artikel':<20}{'Menge':>8}{'Preis':>12}")
print("-" * 40)
print(f"{'Kaffeebohnen':<20}{3:>8}{12.5:>12.2f}")
print(f"{'Milch':<20}{12:>8}{0.99:>12.2f}")
print(f"{'Zucker (1kg)':<20}{1:>8}{2.45:>12.2f}")
print("-" * 40)
print(f"{'SUMME':<20}{'':>8}{3*12.5 + 12*0.99 + 2.45:>12.2f}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# DER DEBUG-TRICK  ⭐
# ====================================================================
x = 42
liste = [1, 2, 3]
print(f"{x=}")              # x=42
print(f"{liste=}")          # liste=[1, 2, 3]
print(f"{len(liste)=}")     # len(liste)=3
print("💡 Das = im f-String zeigt Name UND Wert. Perfekt zum Debuggen!")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Baue eine Tabelle mit deinen 3 Lieblingsfilmen (Titel, Jahr, Note).
#   2. Gib 1/3 mit 5 Nachkommastellen aus.
#   3. Gib 0.075 als Prozentwert mit 2 Nachkommastellen aus.
# ------------------------------------------------------------------
