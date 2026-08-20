"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 06 · MUSTERLÖSUNGEN — Listen                              ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

einkaufsliste = ["Milch", "Brot", "Eier"]
einkaufsliste.append("Käse")
einkaufsliste.insert(0, "Butter")
einkaufsliste.remove("Brot")
print(f"Liste: {einkaufsliste}")
print(f"Länge: {len(einkaufsliste)}")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

temperaturen = [18, 22, 25, 19, 31, 28, 17]
print(f"Anzahl:       {len(temperaturen)}")
print(f"Summe:        {sum(temperaturen)}")
print(f"Durchschnitt: {sum(temperaturen) / len(temperaturen):.1f} °C")
print(f"Minimum:      {min(temperaturen)} °C")
print(f"Maximum:      {max(temperaturen)} °C")
print(f"Sortiert:     {sorted(temperaturen)}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)

tiere = ["Hund", "Katze", "Maus", "Katze", "Vogel"]
print(f'"Maus" enthalten:  {"Maus" in tiere}')
print(f'"Katze" kommt vor: {tiere.count("Katze")}x')
print(f'"Vogel" an Index:  {tiere.index("Vogel")}')


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)

zahlen = [12, -5, 33, 0, -18, 7, 45, -2]
positive, negative, null = [], [], []

for z in zahlen:
    if z > 0:
        positive.append(z)
    elif z < 0:
        negative.append(z)
    else:
        null.append(z)

print(f"Positiv: {positive}")
print(f"Negativ: {negative}")
print(f"Null:    {null}")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

mit_duplikaten = [1, 3, 3, 5, 1, 7, 5, 9, 3]
ohne_duplikate = []

for z in mit_duplikaten:
    if z not in ohne_duplikate:      # nur aufnehmen, wenn noch nicht drin
        ohne_duplikate.append(z)

print(f"Mit:  {mit_duplikaten}")
print(f"Ohne: {ohne_duplikate}")
print(f"(Mit set() ginge es kürzer, aber ohne Reihenfolge: {sorted(set(mit_duplikaten))})")


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)

woerter = ["Banane", "kiwi", "Apfel", "Zitrone", "erdbeere"]
print(f"Original:            {woerter}")
print(f"Alphabetisch:        {sorted(woerter, key=str.lower)}")
print(f"Nach Länge:          {sorted(woerter, key=len)}")
print(f"Nach Länge absteig.: {sorted(woerter, key=len, reverse=True)}")


print("\n" + "=" * 60, "\nAUFGABE 7 🥗 MIX\n", "=" * 60)

satz = "Python ist eine wunderbare und sehr vielseitige Programmiersprache"
woerter_liste = satz.split()

print(f"a) Wörter ({len(woerter_liste)}): {woerter_liste}")

laengstes = woerter_liste[0]
for w in woerter_liste:
    if len(w) > len(laengstes):
        laengstes = w
print(f"b) Längstes Wort: {laengstes} ({len(laengstes)} Buchstaben)")

lang = []
for w in woerter_liste:
    if len(w) > 5:
        lang.append(w)
print(f"c) Länger als 5:  {lang}")

gross = []
for w in woerter_liste:
    gross.append(w.upper())
print(f"d) Groß sortiert: {sorted(gross)}")

gesamtlaenge = 0
for w in woerter_liste:
    gesamtlaenge += len(w)
print(f"e) Ø Wortlänge:   {gesamtlaenge / len(woerter_liste):.2f}")


print("\n" + "=" * 60, "\nAUFGABE 8 🔴 - Kopier-Falle\n", "=" * 60)

# Vorhersage:
#   a = [1, 2, 3, 4]   -> b ist DERSELBE Karton wie a, append(4) trifft beide
#   b = [1, 2, 3, 4]
#   c = [1, 2, 3, 5]   -> c ist eine echte Kopie (VOR dem append(4)!)

a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
c.append(5)
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print("\n💡 a und b zeigen auf dieselbe Liste. c wurde kopiert, bevor 4 kam.")


print("\n" + "=" * 60, "\nAUFGABE 9 🔴 - Matrix\n", "=" * 60)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("a) Matrix:")
for zeile in matrix:
    for zahl in zeile:
        print(f"{zahl:>4}", end="")
    print()

gesamt = 0
for zeile in matrix:
    for zahl in zeile:
        gesamt += zahl
print(f"\nb) Gesamtsumme: {gesamt}")

print("c) Zeilensummen:")
for nr, zeile in enumerate(matrix):
    print(f"   Zeile {nr}: {sum(zeile)}")

diagonale = []
for i in range(len(matrix)):
    diagonale.append(matrix[i][i])
print(f"d) Diagonale: {diagonale}")


print("\n" + "=" * 60, "\nAUFGABE 10 ⭐\n", "=" * 60)

schueler = ["Anna", "Bernd", "Clara", "David"]
noten = [2.3, 1.7, 3.0, 1.3]

# Paare bauen: [note, name] - so sortiert Python automatisch nach Note
paare = []
for i in range(len(schueler)):
    paare.append([noten[i], schueler[i]])

paare.sort()      # sortiert nach dem ersten Element (der Note)

medaillen = ["🥇", "🥈", "🥉"]

print("RANGLISTE")
print("-" * 30)
for platz, paar in enumerate(paare, start=1):
    note, name = paar
    symbol = medaillen[platz - 1] if platz <= 3 else "  "
    print(f"{symbol} {platz}. {name:<10} {note}")

print("-" * 30)
print(f"Durchschnitt: {sum(noten) / len(noten):.2f}")

print("\n🎉 Modul 06 geschafft!")
