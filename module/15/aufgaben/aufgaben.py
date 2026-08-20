"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 15 · AUFGABEN — Vererbung, Dunder, dataclasses            ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Erste Vererbung
# ══════════════════════════════════════════════════════════════════
# Basisklasse Fahrzeug: marke, baujahr, methode beschreibung()
# Abgeleitet: Auto (zusätzlich tueren), Motorrad (zusätzlich hubraum)
# Beide überschreiben beschreibung() und nutzen super().
# Erzeuge je 2 Objekte und gib sie aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - super() vergessen
# ══════════════════════════════════════════════════════════════════
# Was passiert bei diesem Code? Sag es VORHER voraus, dann teste.
#
#   class Basis:
#       def __init__(self, a):
#           self.a = a
#   class Kind(Basis):
#       def __init__(self, a, b):
#           self.b = b          # super() fehlt!
#   k = Kind(1, 2)
#   print(k.a)
#
# Vorhersage:
# 👉 Reparierte Version:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Dunder-Methoden
# ══════════════════════════════════════════════════════════════════
# Klasse Temperatur(celsius) mit:
#   __str__   -> "23.5 °C"
#   __repr__  -> "Temperatur(23.5)"
#   __add__   -> Temperaturen addieren
#   __eq__, __lt__  -> vergleichen und sortieren
#   Methode in_fahrenheit()
# Teste: addieren, vergleichen, eine Liste sortieren.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - dataclass
# ══════════════════════════════════════════════════════════════════
# Schreib eine @dataclass Mitarbeiter mit:
#   name: str, abteilung: str, gehalt: float,
#   skills: list (richtig als default_factory!)
# Methode: gehalt_erhoehen(prozent)
# Erzeuge 4 Mitarbeiter und werte aus:
#   - Durchschnittsgehalt
#   - Wer verdient am meisten?
#   - Alle Skills ohne Duplikate
#   - Mitarbeiter pro Abteilung

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - __len__ und __contains__
# ══════════════════════════════════════════════════════════════════
# Klasse Playlist mit einer Liste von Titeln.
#   hinzufuegen(titel), __len__, __contains__, __getitem__, __str__
#   gesamtdauer() in Minuten (jeder Titel hat eine Dauer in Sekunden)
# Teste len(), "Song" in playlist, playlist[0] und eine for-Schleife.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🔴 - Vererbung oder Komposition?
# ══════════════════════════════════════════════════════════════════
# Entscheide für JEDES Paar: Vererbung oder Komposition? Begründe!
#   a) Quadrat  <-> Rechteck
#   b) Haus     <-> Zimmer
#   c) Manager  <-> Mitarbeiter
#   d) Buch     <-> Seite
#   e) Elektroauto <-> Auto
#   f) Playlist <-> Song
# Implementiere danach ZWEI davon.

# 👉 Deine Antworten + Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 ⭐ BONUS - Formen-Hierarchie
# ══════════════════════════════════════════════════════════════════
# Basisklasse Form mit:
#   - flaeche() und umfang(), die NotImplementedError werfen
#   - __str__, das Name, Fläche und Umfang zeigt
# Abgeleitet: Rechteck, Quadrat(Rechteck!), Kreis, Dreieck
# Erzeuge eine Liste aller Formen, sortiere nach Fläche,
# gib eine Tabelle mit Gesamtfläche aus.

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
