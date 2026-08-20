"""
Modul 07 - Beispiel 1: Dictionaries
"""

# ====================================================================
# ERSTELLEN & ZUGREIFEN
# ====================================================================
person = {
    "name": "Anna",
    "alter": 30,
    "stadt": "Berlin",
}

print(f"Dictionary: {person}")
print(f'person["name"]:  {person["name"]}')
print(f"len(person):     {len(person)}")

# Sicherer Zugriff
print(f'person.get("telefon"):            {person.get("telefon")}')
print(f'person.get("telefon", "unbek."):  {person.get("telefon", "unbek.")}')
# person["telefon"]  ->  KeyError!

print("\n" + "-" * 55 + "\n")

# ====================================================================
# ÄNDERN & HINZUFÜGEN
# ====================================================================
person["alter"] = 31                    # ändern
person["telefon"] = "0123-456"          # neu
person.update({"job": "Entwicklerin"})  # mehrere

print("Nach Änderungen:")
for k, v in person.items():
    print(f"  {k:<10} {v}")

del person["telefon"]
print(f'\nNach del: {"telefon" in person = }')

print("\n" + "-" * 55 + "\n")

# ====================================================================
# DURCHLAUFEN
# ====================================================================
print("Nur Schlüssel:", list(person.keys()))
print("Nur Werte:    ", list(person.values()))
print("Paare:")
for schluessel, wert in person.items():
    print(f"  {schluessel:<10} = {wert}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# ⭐ ZÄHLEN MIT DICTIONARY - das wichtigste Muster
# ====================================================================
satz = "Python ist einfach und Python ist maechtig"
woerter = satz.lower().split()

haeufigkeit = {}
for wort in woerter:
    haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1

print("Worthäufigkeit:")
for wort, anzahl in sorted(haeufigkeit.items(), key=lambda p: -p[1]):
    print(f"  {wort:<12} {anzahl}  {'█' * anzahl}")

print()

# Buchstaben zählen
buchstaben = {}
for z in "programmierung":
    buchstaben[z] = buchstaben.get(z, 0) + 1
print("Buchstaben in 'programmierung':")
print(f"  {buchstaben}")

# Häufigster Buchstabe
haeufigster = max(buchstaben, key=buchstaben.get)
print(f"  Häufigster: '{haeufigster}' ({buchstaben[haeufigster]}x)")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# VERSCHACHTELT - so sehen echte Daten aus
# ====================================================================
mitarbeiter = {
    "anna": {
        "alter": 30,
        "skills": ["Python", "SQL", "Docker"],
        "adresse": {"stadt": "Berlin", "plz": "10115"},
    },
    "bernd": {
        "alter": 25,
        "skills": ["JavaScript"],
        "adresse": {"stadt": "Hamburg", "plz": "20095"},
    },
}

print("Zugriff Schritt für Schritt:")
print(f'  mitarbeiter["anna"]                     -> dict mit {len(mitarbeiter["anna"])} Feldern')
print(f'  mitarbeiter["anna"]["skills"]           -> {mitarbeiter["anna"]["skills"]}')
print(f'  mitarbeiter["anna"]["skills"][0]        -> {mitarbeiter["anna"]["skills"][0]}')
print(f'  mitarbeiter["anna"]["adresse"]["stadt"] -> {mitarbeiter["anna"]["adresse"]["stadt"]}')

print("\nÜbersicht:")
for name, daten in mitarbeiter.items():
    stadt = daten["adresse"]["stadt"]
    skills = ", ".join(daten["skills"])
    print(f"  {name.capitalize():<8} {daten['alter']} J., {stadt:<10} [{skills}]")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Füge einen dritten Mitarbeiter hinzu.
#   2. Finde alle Mitarbeiter, die Python können.
#   3. Zähle, wie oft jeder Skill insgesamt vorkommt.
# ------------------------------------------------------------------
