"""
Modul 03 - Beispiel 1: Rechnen in Python
"""

a, b = 17, 5

print(f"a = {a}, b = {b}\n")
print(f"a + b   = {a + b}")
print(f"a - b   = {a - b}")
print(f"a * b   = {a * b}")
print(f"a / b   = {a / b}          ← immer float!")
print(f"a // b  = {a // b}                 ← Ganzzahldivision (abrunden)")
print(f"a %  b  = {a % b}                 ← Rest (Modulo)")
print(f"a ** b  = {a ** b}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# MODULO IN DER PRAXIS  ⭐
# ====================================================================
print("Gerade/ungerade:")
for zahl in (4, 7, 10, 13):
    art = "gerade" if zahl % 2 == 0 else "ungerade"
    print(f"  {zahl:>3} ist {art}")

print("\nSekunden umrechnen:")
sekunden_gesamt = 9385
stunden = sekunden_gesamt // 3600
rest = sekunden_gesamt % 3600
minuten = rest // 60
sekunden = rest % 60
print(f"  {sekunden_gesamt} Sekunden = {stunden}h {minuten}min {sekunden}s")

print("\nZiffern zerlegen (1234):")
n = 1234
print(f"  Einer:     {n % 10}")
print(f"  Zehner:    {n // 10 % 10}")
print(f"  Hunderter: {n // 100 % 10}")
print(f"  Tausender: {n // 1000 % 10}")

print("\nUmlaufen (Wochentage 0-6):")
heute = 5                      # Samstag
print(f"  Heute: {heute}, in 10 Tagen: {(heute + 10) % 7}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# RUNDEN & MATHE
# ====================================================================
import math

print(f"round(3.7)          = {round(3.7)}")
print(f"round(3.14159, 2)   = {round(3.14159, 2)}")
print(f"round(2.5)          = {round(2.5)}   ← Bankers Rounding!")
print(f"round(3.5)          = {round(3.5)}")
print(f"abs(-5)             = {abs(-5)}")
print(f"min(3, 7, 1)        = {min(3, 7, 1)}")
print(f"max(3, 7, 1)        = {max(3, 7, 1)}")
print(f"sum([1, 2, 3, 4])   = {sum([1, 2, 3, 4])}")
print()
print(f"math.sqrt(16)       = {math.sqrt(16)}")
print(f"math.floor(3.9)     = {math.floor(3.9)}   ← immer abrunden")
print(f"math.ceil(3.1)      = {math.ceil(3.1)}   ← immer aufrunden")
print(f"math.pi             = {math.pi:.5f}")

print("\n" + "-" * 55 + "\n")

# ====================================================================
# DIE FLOAT-FALLE 💧
# ====================================================================
print(f"0.1 + 0.2           = {0.1 + 0.2}")
print(f"0.1 + 0.2 == 0.3    = {0.1 + 0.2 == 0.3}   😱")
print()
print("So macht man es richtig:")
print(f"  round(0.1+0.2, 2) == 0.3        -> {round(0.1 + 0.2, 2) == 0.3}")
print(f"  abs((0.1+0.2) - 0.3) < 1e-9     -> {abs((0.1 + 0.2) - 0.3) < 1e-9}")
print()
print("Für Geld: in Cent rechnen (als int) oder das decimal-Modul benutzen.")
preis_cent = 1999          # 19,99 €
print(f"  {preis_cent} Cent = {preis_cent / 100:.2f} €")
