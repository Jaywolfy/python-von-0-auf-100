"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 09 · AUFGABEN — 11 kaputte Programme reparieren 🔧        ║
╠══════════════════════════════════════════════════════════════════╣
║  SO GEHT'S:                                                      ║
║  1. Entferne das # vor EINEM Block                               ║
║  2. Führ die Datei aus, LIES die Fehlermeldung                   ║
║  3. Schreib als Kommentar: Fehlertyp + was er bedeutet           ║
║  4. Repariere den Code                                           ║
║  5. Nächster Block                                               ║
║                                                                  ║
║  ⚠️ Bei Nr. 8-11 gibt es KEINE Fehlermeldung - der Code läuft,   ║
║     liefert aber ein falsches Ergebnis. Die sind am schwersten!  ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# FEHLER 1 🟢
# ══════════════════════════════════════════════════════════════════
# name = "Anna"
# print("Hallo " + name
#
# Fehlertyp:
# Bedeutung:
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 2 🟢
# ══════════════════════════════════════════════════════════════════
# alter = "25"
# print("Nächstes Jahr: " + alter + 1)
#
# Fehlertyp:
# Bedeutung:
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 3 🟢
# ══════════════════════════════════════════════════════════════════
# zahlen = [1, 2, 3]
# print(zahlen[3])
#
# Fehlertyp:
# Bedeutung:
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 4 🟢
# ══════════════════════════════════════════════════════════════════
# person = {"name": "Anna", "alter": 30}
# print(person["stadt"])
#
# Fehlertyp:
# Bedeutung:
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 5 🟡
# ══════════════════════════════════════════════════════════════════
# def gruesse(name):
# print(f"Hallo {name}")
# gruesse("Anna")
#
# Fehlertyp:
# Bedeutung:
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 6 🟡
# ══════════════════════════════════════════════════════════════════
# def addiere(a, b):
#     return a + b
# print(addiere(5))
#
# Fehlertyp:
# Bedeutung:
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 7 🟡
# ══════════════════════════════════════════════════════════════════
# woerter = ["Apfel", "Birne"]
# woerter.push("Kirsche")
#
# Fehlertyp:
# Bedeutung:
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 8 🔴 - LOGIKFEHLER (kein Absturz!)
# ══════════════════════════════════════════════════════════════════
# Diese Funktion soll die Summe berechnen. Ergebnis ist aber falsch.
def summiere(zahlen):
    for z in zahlen:
        summe = 0
        summe += z
    return summe

print("Fehler 8:", summiere([10, 20, 30]), "  (erwartet: 60)")
# Was ist der Fehler?
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 9 🔴 - LOGIKFEHLER
# ══════════════════════════════════════════════════════════════════
# Soll ALLE Elemente ausgeben - eines fehlt.
def zeige_alle(liste):
    for i in range(len(liste) - 1):
        print("  ", liste[i])

print("Fehler 9:")
zeige_alle(["a", "b", "c"])
# Was fehlt?
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 10 🔴 - LOGIKFEHLER
# ══════════════════════════════════════════════════════════════════
# Soll die größte Zahl finden. Bei negativen Zahlen falsch!
def groesste(zahlen):
    maximum = 0
    for z in zahlen:
        if z > maximum:
            maximum = z
    return maximum

print("Fehler 10:", groesste([-5, -2, -9]), "  (erwartet: -2)")
# Was ist der Fehler?
# 👉 Reparierte Version:


# ══════════════════════════════════════════════════════════════════
# FEHLER 11 🔴 - LOGIKFEHLER
# ══════════════════════════════════════════════════════════════════
# Soll alle negativen Zahlen entfernen. Es bleibt eine übrig!
def entferne_negative(zahlen):
    kopie = zahlen.copy()
    for z in kopie:
        if z < 0:
            kopie.remove(z)
    return kopie

print("Fehler 11:", entferne_negative([1, -2, -3, 4]), "  (erwartet: [1, 4])")
# Was ist der Fehler?
# 👉 Reparierte Version:


print("\n✅ Alle 11 repariert? Vergleiche mit den Lösungen!")
