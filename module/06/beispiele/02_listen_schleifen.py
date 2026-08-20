"""
Modul 06 - Beispiel 2: Listen + Schleifen = echte Datenverarbeitung
"""

noten = [2.3, 1.7, 3.0, 1.3, 2.7, 4.0, 1.0]

# ====================================================================
# DURCHLAUFEN
# ====================================================================
print("Alle Noten:")
for note in noten:
    print(f"  {note}")

print("\nMit Nummerierung:")
for nr, note in enumerate(noten, start=1):
    print(f"  Prüfung {nr}: {note}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# AUSWERTEN (Akkumulator-Muster)
# ====================================================================
summe = 0
for note in noten:
    summe += note
durchschnitt = summe / len(noten)

beste = noten[0]
schlechteste = noten[0]
for note in noten:
    if note < beste:
        beste = note
    if note > schlechteste:
        schlechteste = note

bestanden = []
durchgefallen = []
for note in noten:
    if note <= 4.0:
        bestanden.append(note)
    else:
        durchgefallen.append(note)

print(f"Anzahl Noten:   {len(noten)}")
print(f"Durchschnitt:   {durchschnitt:.2f}")
print(f"Beste Note:     {beste}")
print(f"Schlechteste:   {schlechteste}")
print(f"Bestanden:      {len(bestanden)}")
print(f"Sortiert:       {sorted(noten)}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# BALKENDIAGRAMM AUS EINER LISTE
# ====================================================================
verkaeufe = [12, 45, 23, 8, 37]
monate = ["Jan", "Feb", "Mär", "Apr", "Mai"]

print("Verkäufe pro Monat:")
for monat, anzahl in zip(monate, verkaeufe):      # zip kommt in Modul 10
    balken = "█" * anzahl
    print(f"  {monat} {anzahl:>3} {balken}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# VERSCHACHTELTE LISTEN (Tabellen)
# ====================================================================
tabelle = [
    ["Name",  "Stadt",   "Alter"],
    ["Anna",  "Berlin",  "30"],
    ["Bernd", "Hamburg", "25"],
    ["Clara", "München", "41"],
]

print("Tabelle:")
for zeile in tabelle:
    for zelle in zeile:
        print(f"{zelle:<10}", end="")
    print()

print()
print(f"tabelle[1]    = {tabelle[1]}")
print(f"tabelle[1][0] = {tabelle[1][0]}      ← Zeile 1, Spalte 0")

# Nur eine Spalte herausziehen
staedte = []
for zeile in tabelle[1:]:          # Kopfzeile überspringen
    staedte.append(zeile[1])
print(f"Alle Städte:  {staedte}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# ⚠️ NICHT beim Iterieren verändern!
# ====================================================================
zahlen = [1, -2, 3, -4, -5, 6]

print(f"Original: {zahlen}")

# ❌ So NICHT:
kaputt = zahlen.copy()
for z in kaputt:
    if z < 0:
        kaputt.remove(z)
print(f"❌ Beim Iterieren entfernt: {kaputt}   ← -5 ist noch da!")

# ✅ So:
sauber = []
for z in zahlen:
    if z >= 0:
        sauber.append(z)
print(f"✅ Neue Liste gebaut:       {sauber}")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Berechne den Median der Noten (sortieren, mittleres Element).
#   2. Finde die 3 besten Noten.
#   3. Baue eine Tabelle mit deinen Lieblingsfilmen und werte sie aus.
# ------------------------------------------------------------------
