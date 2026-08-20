"""
Modul 00 - Beispiel 3: Kommentare & absichtliche Fehler

Dieses Beispiel ist zum KAPUTTMACHEN gedacht. 💥
"""

# ====================================================================
# TEIL 1: KOMMENTARE
# ====================================================================

# Ein Kommentar beginnt mit # und wird von Python ignoriert.
print("Diese Zeile läuft.")

# print("Diese Zeile läuft NICHT - sie ist auskommentiert.")

print("Und hier geht's weiter.")   # Kommentar am Zeilenende

"""
Ein mehrzeiliger Text in dreifachen Anführungszeichen.
Steht er ganz oben in einer Datei oder Funktion, nennt man ihn
"Docstring" - eine Beschreibung dessen, was der Code tut.
"""

# --- Gute vs. schlechte Kommentare ----------------------------------

# ❌ Schlecht - beschreibt nur, was ohnehin dasteht:
print("Hallo")   # gibt Hallo aus

# ✅ Gut - erklärt das WARUM:
print("=" * 50)  # Trennlinie, damit die Ausgabe lesbar bleibt


# ====================================================================
# TEIL 2: FEHLER PROVOZIEREN 💥
# ====================================================================
# Entferne das # vor EINER Zeile, führe die Datei aus,
# lies die Fehlermeldung, mach das # wieder dran. Dann die nächste.

# print("Hallo)
#   -> SyntaxError: unterminated string literal
#      Übersetzt: "Du hast einen Text angefangen, aber nie beendet."

# prnt("Hallo")
#   -> NameError: name 'prnt' is not defined
#      Übersetzt: "Ich kenne nichts namens 'prnt'." (Tippfehler)

# print(Hallo)
#   -> NameError: name 'Hallo' is not defined
#      Übersetzt: "Ohne Anführungszeichen halte ich Hallo für eine
#                  Variable - und die gibt es nicht."

# Print("Hallo")
#   -> NameError: name 'Print' is not defined
#      Python unterscheidet Groß- und Kleinschreibung!

#     print("Hallo")
#   -> IndentationError: unexpected indent
#      Übersetzt: "Warum ist diese Zeile eingerückt?"

print("\n🎓 Merke: Die LETZTE Zeile einer Fehlermeldung sagt dir, WAS los ist.")
print("   Die Zeile darüber sagt dir, WO es passiert ist.")
