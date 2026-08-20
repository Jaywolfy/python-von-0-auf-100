"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 12 · AUFGABEN — Module & Standardbibliothek               ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Datum
# ══════════════════════════════════════════════════════════════════
# a) Gib das heutige Datum als "26.07.2026" aus
# b) Gib den heutigen Wochentag aus
# c) Welches Datum ist in 100 Tagen?
# d) Wie viele Tage sind es bis zum 31.12. dieses Jahres?

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Zufall
# ══════════════════════════════════════════════════════════════════
# a) Simuliere 1000 Würfelwürfe und zähle, wie oft jede Zahl kam
# b) Ziehe 6 Lottozahlen aus 1-49 (ohne Wiederholung), sortiert
# c) Mische ein Kartendeck aus ["Herz","Karo","Pik","Kreuz"] x ["7","8","9","10","B","D","K","A"]
#    und gib die ersten 5 Karten aus

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Counter
# ══════════════════════════════════════════════════════════════════
text = """Der schnelle braune Fuchs springt über den faulen Hund
Der Hund schläft weiter Der Fuchs rennt weiter"""
# a) Die 5 häufigsten Wörter (klein geschrieben)
# b) Die 5 häufigsten Buchstaben (ohne Leerzeichen)
# c) Wie viele UNTERSCHIEDLICHE Wörter gibt es?
# d) Welche Wörter kommen genau einmal vor?

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Eigenes Modul
# ══════════════════════════════════════════════════════════════════
# Erstelle im Ordner "aufgaben" eine Datei meine_werkzeuge.py mit:
#   - mindestens 4 nützlichen Funktionen (mit Docstrings!)
#   - einem if __name__ == "__main__"-Block, der alle testet
# Importiere sie danach HIER und benutze sie.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Altersrechner
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion alter_infos(geburtsdatum_text), die für ein
# Datum im Format "15.03.1998" ein Dictionary zurückgibt mit:
#   alter_jahre, alter_tage, wochentag_der_geburt,
#   tage_bis_naechster_geburtstag

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🔴 - Passwortgenerator
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion erzeuge_passwort(laenge=12, sonderzeichen=True),
# die ein zufälliges Passwort erzeugt, das GARANTIERT enthält:
#   mindestens 1 Großbuchstabe, 1 Kleinbuchstabe, 1 Ziffer
#   und (falls gewünscht) 1 Sonderzeichen.
# 💡 Tipp: import string  ->  string.ascii_letters, string.digits
# 💡 Erst die Pflichtzeichen ziehen, dann auffüllen, dann shuffle

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 ⭐ BONUS - Terminplaner
# ══════════════════════════════════════════════════════════════════
termine = [
    ("Zahnarzt",     "05.08.2026"),
    ("Geburtstag",   "12.09.2026"),
    ("Urlaub",       "01.08.2026"),
    ("Steuererklärung", "31.07.2026"),
]
# Gib eine sortierte Übersicht aus:
#   In   5 Tagen  | 31.07.2026 (Fr) | Steuererklärung  ⚠️
#   In   6 Tagen  | 01.08.2026 (Sa) | Urlaub
#   ...
# Termine in weniger als 7 Tagen mit ⚠️ markieren.

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
