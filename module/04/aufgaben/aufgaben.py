"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 04 · AUFGABEN — Bedingungen                               ║
║  🟢 Grundlagen  🟡 Anwenden  🔴 Transfer  ⭐ Bonus                ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Gerade oder ungerade
# ══════════════════════════════════════════════════════════════════
zahl = 47
# Gib aus, ob die Zahl gerade oder ungerade ist.
# 💡 Tipp: % aus Modul 03

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Volljährig?
# ══════════════════════════════════════════════════════════════════
alter = 16
# Gib aus:
#   >= 18  ->  "Volljährig"
#   14-17  ->  "Jugendlich"
#   < 14   ->  "Kind"

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟢 - Die größte Zahl
# ══════════════════════════════════════════════════════════════════
a, b, c = 17, 42, 23
# Finde die größte der drei Zahlen und gib sie aus.
# ⚠️ OHNE max() - nur mit if/elif/else!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Notenrechner
# ══════════════════════════════════════════════════════════════════
punkte = 87
# Wandle Punkte (0-100) in eine Schulnote um:
#   >= 92 -> 1    >= 81 -> 2    >= 67 -> 3
#   >= 50 -> 4    >= 30 -> 5    sonst -> 6
# Gib aus:  87 Punkte -> Note 2
# ⚠️ Prüfe auch, ob die Punktzahl überhaupt zwischen 0 und 100 liegt!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Eintrittspreis
# ══════════════════════════════════════════════════════════════════
alter_gast = 25
ist_student = True
ist_dienstag = True
# Preisregeln (Grundpreis 12 €):
#   - unter 6 Jahre:            kostenlos
#   - 6-17 Jahre:               6 €
#   - Studenten:                8 €
#   - ab 65 Jahre:              8 €
#   - dienstags: zusätzlich 2 € Rabatt (nie unter 0 €)
# ⚠️ Reihenfolge überlegen! Was gilt, wenn jemand Student UND 70 ist?
# Gib den Endpreis aus.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - Passwort-Prüfung
# ══════════════════════════════════════════════════════════════════
passwort = "Sonne2026"
# Prüfe und gib für JEDE Regel ✅ oder ❌ aus:
#   - mindestens 8 Zeichen
#   - enthält mindestens eine Ziffer
#   - enthält Groß- UND Kleinbuchstaben
#   - ist nicht "passwort", "123456" oder "qwertz"
# Zähle die erfüllten Regeln und gib am Ende
# "SCHWACH" (0-2), "MITTEL" (3) oder "STARK" (4) aus.
#
# 💡 Für "enthält Ziffer" ohne Schleife:
#    any(z.isdigit() for z in passwort)     <- kommt in Modul 10,
#    du darfst es hier schon benutzen!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - Schaltjahr
# ══════════════════════════════════════════════════════════════════
jahr = 2100
# Ein Jahr ist ein Schaltjahr, wenn:
#   - es durch 4 teilbar ist
#   - ABER NICHT, wenn es durch 100 teilbar ist
#   - AUSSER es ist auch durch 400 teilbar
# Beispiele: 2024 ✅ | 1900 ❌ | 2000 ✅ | 2100 ❌
# Teste deinen Code mit allen vier Jahren!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 🔴 - Datei einsortieren
# ══════════════════════════════════════════════════════════════════
dateiname = "urlaub_2026.JPG"
# Bestimme den Zielordner nach Dateiendung:
#   .jpg .jpeg .png .gif  -> "Bilder"
#   .pdf .docx .txt       -> "Dokumente"
#   .mp3 .wav             -> "Musik"
#   .mp4 .mov             -> "Videos"
#   alles andere          -> "Sonstiges"
# ⚠️ Groß-/Kleinschreibung der Endung muss egal sein!
# Gib aus:  urlaub_2026.JPG  ->  Bilder/

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 9 ⭐ BONUS - Code entwirren
# ══════════════════════════════════════════════════════════════════
# Dieser Code funktioniert, ist aber schwer lesbar.
# Schreib ihn mit Guard Clauses flach - gleiche Logik, bessere Form.
#
#   if benutzer_existiert:
#       if passwort_korrekt:
#           if not gesperrt:
#               if zwei_faktor_ok:
#                   print("Login erfolgreich")
#               else:
#                   print("2FA fehlgeschlagen")
#           else:
#               print("Konto gesperrt")
#       else:
#           print("Falsches Passwort")
#   else:
#       print("Benutzer unbekannt")

benutzer_existiert = True
passwort_korrekt = True
gesperrt = False
zwei_faktor_ok = False

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
