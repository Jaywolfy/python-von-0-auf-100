"""
Modul 00 - Beispiel 2: Was print() alles kann
"""

# --- Mehrere Werte auf einmal ---------------------------------------
print("Hallo", "Welt", "!")
# Python setzt automatisch Leerzeichen dazwischen -> Hallo Welt !

# --- sep: den Trenner selbst bestimmen ------------------------------
print("2026", "07", "26", sep="-")      # 2026-07-26
print("a", "b", "c", sep="")            # abc
print("Zeile1", "Zeile2", sep="\n")     # \n = Zeilenumbruch

print()

# --- end: was NACH der Ausgabe kommt --------------------------------
# Standard ist end="\n" (Zeilenumbruch). Wir überschreiben das:
print("Lade", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" fertig!")           # hier normaler Umbruch

print()

# --- Nützliche Zeichen ----------------------------------------------
print("Tabulator:\tnach dem Tab")   # \t = Tabulator
print("Zeile A\nZeile B")           # \n = neue Zeile
print("Anführungszeichen: \"so\"")  # \" = ein " im Text
print("Backslash: \\")              # \\ = ein einzelner \

print()

# --- Trennlinien: Strings kann man multiplizieren! ------------------
print("-" * 40)
print("=" * 40)
print("* " * 20)

print()

# --- Ein Kästchen zeichnen ------------------------------------------
print("+" + "-" * 28 + "+")
print("|" + " " * 28 + "|")
print("|" + "  Willkommen bei Python! 🐍 ".center(28) + "|")
print("|" + " " * 28 + "|")
print("+" + "-" * 28 + "+")

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Ändere die Breite des Kästchens von 28 auf 40.
#   2. Baue eine Ladeanimation mit 10 Punkten.
#   3. Gib deinen Namen 5 Mal in einer Zeile aus, getrennt durch " | ".
# ------------------------------------------------------------------
