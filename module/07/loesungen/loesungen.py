"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 07 · MUSTERLÖSUNGEN                                       ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

auto = {"marke": "VW", "modell": "Golf", "baujahr": 2018,
        "ps": 150, "elektrisch": False}

for k, v in auto.items():
    print(f"  {k:<12} {v}")

auto["baujahr"] = 2020
auto["farbe"] = "blau"
print(f"\nKilometerstand: {auto.get('kilometerstand', 'unbekannt')}")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

telefonbuch = {"Anna": "0151-111", "Bernd": "0160-222", "Clara": "0170-333"}

print(f"Bernd: {telefonbuch['Bernd']}")
telefonbuch["David"] = "0180-444"
del telefonbuch["Anna"]

print("\nTelefonbuch:")
for name in sorted(telefonbuch):
    print(f"  {name:<8} {telefonbuch[name]}")

print(f"\nEmil enthalten: {'Emil' in telefonbuch}")


print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)

koordinate = (52.52, 13.40)
datensatz = ["Anna", 30, "Berlin", "anna@mail.de"]

breite, laenge = koordinate
print(f"Breite: {breite}, Länge: {laenge}")

name, alter, stadt, email = datensatz
print(f"{name}, {alter}, {stadt}, {email}")

erster, *rest = [1, 2, 3, 4, 5]
print(f"erster={erster}, rest={rest}")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)

farben = ["rot","blau","rot","grün","blau","rot","gelb","blau","rot"]

zaehler = {}
for farbe in farben:
    zaehler[farbe] = zaehler.get(farbe, 0) + 1

# sorted mit key: nach dem Wert (Element 1 des Paares), absteigend
for farbe, anzahl in sorted(zaehler.items(), key=lambda paar: paar[1], reverse=True):
    print(f"  {farbe:<8} {anzahl}  {'█' * anzahl}")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

kurs_a = {"Anna", "Bernd", "Clara", "David"}
kurs_b = {"Clara", "David", "Emil", "Frida"}

print(f"a) Alle:          {sorted(kurs_a | kurs_b)}")
print(f"b) In beiden:     {sorted(kurs_a & kurs_b)}")
print(f"c) Nur Kurs A:    {sorted(kurs_a - kurs_b)}")
print(f"d) Nur in einem:  {sorted(kurs_a ^ kurs_b)}")
print(f"e) Anzahl:        {len(kurs_a | kurs_b)}")


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)

laender = {
    "Deutschland": {"hauptstadt": "Berlin", "einwohner": 84.4, "sprachen": ["Deutsch"]},
    "Schweiz":     {"hauptstadt": "Bern",   "einwohner": 8.8,  "sprachen": ["Deutsch","Französisch","Italienisch"]},
    "Kanada":      {"hauptstadt": "Ottawa", "einwohner": 40.1, "sprachen": ["Englisch","Französisch"]},
}

print(f"a) Hauptstadt Schweiz: {laender['Schweiz']['hauptstadt']}")
print(f"b) 2. Sprache Kanada:  {laender['Kanada']['sprachen'][1]}")

print("\nc) Übersicht:")
for land, daten in laender.items():
    anzahl_sprachen = len(daten["sprachen"])
    print(f"   {land:<13}| {daten['hauptstadt']:<8}| {daten['einwohner']:>5} Mio | {anzahl_sprachen} Sprache(n)")

groesstes = ""
max_einwohner = 0
for land, daten in laender.items():
    if daten["einwohner"] > max_einwohner:
        max_einwohner = daten["einwohner"]
        groesstes = land
print(f"\nd) Meiste Einwohner: {groesstes} ({max_einwohner} Mio)")

alle_sprachen = set()
for daten in laender.values():
    alle_sprachen.update(daten["sprachen"])
print(f"e) Alle Sprachen: {sorted(alle_sprachen)}")


print("\n" + "=" * 60, "\nAUFGABE 7 🥗 MIX\n", "=" * 60)

text = """Python ist eine Programmiersprache. Python ist einfach zu lernen.
Viele Menschen lernen Python weil Python vielseitig ist."""

sauber = text.lower().replace(".", "").replace("\n", " ")
woerter = sauber.split()

zaehler = {}
for w in woerter:
    zaehler[w] = zaehler.get(w, 0) + 1

print(f"a) {len(woerter)} Wörter insgesamt")

print("\nc) Top 5:")
top = sorted(zaehler.items(), key=lambda p: p[1], reverse=True)[:5]
for wort, anzahl in top:
    print(f"   {wort:<20} {anzahl}x")

print(f"\nd) Unterschiedliche Wörter: {len(set(woerter))}")

einmalig = []
for wort, anzahl in zaehler.items():
    if anzahl == 1:
        einmalig.append(wort)
print(f"e) Nur einmal ({len(einmalig)}): {sorted(einmalig)}")


print("\n" + "=" * 60, "\nAUFGABE 8 🔴\n", "=" * 60)

preise = {"Apfel": 0.50, "Brot": 2.30, "Milch": 1.10, "Käse": 4.80}
warenkorb = {"Apfel": 6, "Brot": 2, "Käse": 1}

summe = 0
print("RECHNUNG")
print("-" * 34)
for artikel, menge in warenkorb.items():
    einzelpreis = preise[artikel]
    zeilensumme = menge * einzelpreis
    summe += zeilensumme
    print(f"{artikel:<8}{menge:>3} x {einzelpreis:>5.2f} = {zeilensumme:>7.2f}")
print("-" * 34)
print(f"{'SUMME':<21}{summe:>12.2f}")


print("\n" + "=" * 60, "\nAUFGABE 9 🔴\n", "=" * 60)

laenderkuerzel = {"DE": "Deutschland", "FR": "Frankreich", "IT": "Italien"}

umgedreht = {}
for kuerzel, land in laenderkuerzel.items():
    umgedreht[land] = kuerzel

print(f"Original:   {laenderkuerzel}")
print(f"Umgedreht:  {umgedreht}")
print(f"Kurzform (Modul 10): {dict((v, k) for k, v in laenderkuerzel.items())}")


print("\n" + "=" * 60, "\nAUFGABE 10 ⭐\n", "=" * 60)

noten = {
    "Anna":  [2.3, 1.7, 2.0],
    "Bernd": [3.0, 3.3, 2.7],
    "Clara": [1.0, 1.3, 1.7],
    "David": [4.0, 3.7, 2.3],
}

schnitte = {}
print(f"{'Name':<8}{'Noten':<22}{'Ø':>6}")
print("-" * 36)
for name, liste in noten.items():
    schnitt = sum(liste) / len(liste)
    schnitte[name] = schnitt
    notentext = ", ".join(f"{n}" for n in liste)
    print(f"{name:<8}{notentext:<22}{schnitt:>6.2f}")

klassenschnitt = sum(schnitte.values()) / len(schnitte)
bester = min(schnitte, key=schnitte.get)
schlechtester = max(schnitte, key=schnitte.get)

print("-" * 36)
print(f"Klassendurchschnitt: {klassenschnitt:.2f}")
print(f"Bester:              {bester} ({schnitte[bester]:.2f}) 🥇")
print(f"Schwächster:         {schlechtester} ({schnitte[schlechtester]:.2f})")

ueber_schnitt = []
for name, schnitt in schnitte.items():
    if schnitt < klassenschnitt:          # kleinere Note = besser!
        ueber_schnitt.append(name)
print(f"Besser als Schnitt:  {ueber_schnitt}")

print("\n🎉 Modul 07 geschafft!")
