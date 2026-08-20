"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 13 · AUFGABEN — Exceptions                                ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Sichere Umwandlung
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion sichere_zahl(text, standard=0), die den Text
# in eine Zahl umwandelt - und bei Fehlern den Standardwert liefert.
# Teste mit: "42", "3.14", "abc", "", None

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Division
# ══════════════════════════════════════════════════════════════════
# Schreib teile_sicher(a, b), die:
#   - das Ergebnis zurückgibt
#   - bei Division durch 0 die Meldung "Division durch Null" ausgibt
#     und None zurückgibt
#   - bei falschen Typen eine passende Meldung ausgibt
# Teste mit (10,2), (10,0), ("10",2)

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Liste robust auswerten
# ══════════════════════════════════════════════════════════════════
daten = ["12", "abc", "45", "", "7", "3.5", None, "99"]
# Summiere alle Werte, die sich in eine ganze Zahl umwandeln lassen.
# Sammle die problematischen Werte in einer Liste und gib am Ende
# einen Bericht aus:
#   ✅ 4 Werte verarbeitet, Summe = 163
#   ⚠️ 4 übersprungen: ['abc', '', '3.5', None]

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Eigene Exception
# ══════════════════════════════════════════════════════════════════
# Definiere eine Exception UngueltigeEmailError.
# Schreib pruefe_email(text), die einen Fehler wirft, wenn:
#   - kein "@" enthalten ist
#   - kein "." nach dem "@" kommt
#   - der Teil vor dem "@" leer ist
# Teste mit 5 verschiedenen Eingaben (gute und schlechte).

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - finally in Aktion
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion verarbeite(daten), die:
#   - try: die Daten verarbeitet (sum())
#   - except: Fehler abfängt
#   - finally: IMMER "Verarbeitung beendet" ausgibt
# Teste mit [1,2,3] und mit [1,"zwei",3].
# Beobachte: finally läuft auch im Fehlerfall!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🔴 - Anti-Muster reparieren
# ══════════════════════════════════════════════════════════════════
# Dieser Code ist schlecht. Schreib ihn richtig und begründe.
#
#   def lade_konfiguration(pfad):
#       try:
#           with open(pfad) as f:
#               zeilen = f.readlines()
#           konfig = {}
#           for z in zeilen:
#               k, v = z.split("=")
#               konfig[k.strip()] = v.strip()
#           return konfig
#       except:
#           return {}
#
# Probleme: (mind. 4 finden!)
# 👉 Deine verbesserte Version:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - Wiederholung bei Fehleingabe
# ══════════════════════════════════════════════════════════════════
# Schreib frage_zahl(prompt, min_wert, max_wert), die so lange fragt,
# bis eine gültige Zahl im Bereich eingegeben wurde.
# Simuliere die Eingaben mit dieser Liste statt input():
eingaben = ["abc", "-5", "999", "42"]
# Erwartete Ausgabe:
#   'abc' -> Bitte eine Zahl eingeben
#   '-5'  -> Muss zwischen 1 und 100 liegen
#   '999' -> Muss zwischen 1 und 100 liegen
#   '42'  -> ✅ Akzeptiert

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 ⭐ BONUS - Robuster Batch-Verarbeiter
# ══════════════════════════════════════════════════════════════════
# Schreib verarbeite_alle(elemente, funktion), die:
#   - jedes Element durch die Funktion schickt
#   - Erfolge sammelt
#   - Fehler mit Element + Fehlermeldung sammelt
#   - ein Ergebnis-Dictionary zurückgibt:
#     {"erfolge": [...], "fehler": [(element, fehlermeldung), ...],
#      "quote": 0.75}
# Teste mit int als Funktion und ["1","2","x","4"]

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
