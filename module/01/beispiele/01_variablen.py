"""
Modul 01 - Beispiel 1: Variablen anlegen und benutzen
"""

# --- Anlegen --------------------------------------------------------
name = "Anna"
alter = 25
groesse = 1.83
lernt_python = True

# --- Benutzen -------------------------------------------------------
print(name)
print("Hallo", name)
print(name, "ist", alter, "Jahre alt.")

print()

# --- Der Unterschied: MIT und OHNE Anführungszeichen ----------------
print(name)      # Anna   <- Inhalt der Variablen
print("name")    # name    <- das Wort selbst

print()

# --- Variablen ändern sich ------------------------------------------
punkte = 0
print("Start:", punkte)

punkte = 10
print("Nach Level 1:", punkte)

punkte = punkte + 5
print("Nach Bonus:", punkte)

punkte += 5          # Kurzform für punkte = punkte + 5
print("Nach Bonus 2:", punkte)

punkte *= 2          # verdoppeln
print("Nach Verdopplung:", punkte)

print()

# --- Mehrere Zuweisungen --------------------------------------------
a, b, c = 1, 2, 3
print("a, b, c =", a, b, c)

x = y = z = 0
print("x, y, z =", x, y, z)

# Tauschen - in vielen Sprachen braucht man dafür eine Hilfsvariable.
# In Python geht es in einer Zeile:
links, rechts = "A", "B"
print("Vorher: ", links, rechts)
links, rechts = rechts, links
print("Nachher:", links, rechts)

# ------------------------------------------------------------------
# 💥 EXPERIMENTIERE!
#   1. Gib eine Variable aus, BEVOR du sie definierst. Welcher Fehler?
#   2. Schreib "Name" statt "name". Welcher Fehler?
#   3. Erstelle 3 eigene Variablen und tausche zwei davon.
# ------------------------------------------------------------------
