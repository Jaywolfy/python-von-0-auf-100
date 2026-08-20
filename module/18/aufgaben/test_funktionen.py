"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 18 · AUFGABEN — Tests schreiben                           ║
╠══════════════════════════════════════════════════════════════════╣
║  AUSFÜHREN:                                                      ║
║     pip install pytest                                           ║
║     cd module/18/aufgaben                                        ║
║     pytest -v                                                    ║
║                                                                  ║
║  ⚠️ funktionen.py enthält BUGS. Finde sie mit Tests!             ║
╚══════════════════════════════════════════════════════════════════╝
"""
import pytest
from funktionen import (addiere, durchschnitt, ist_gerade, groesste,
                        ist_palindrom, zaehle_vokale, formatiere_euro,
                        note_zu_text, teile, entferne_duplikate)


# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Vorgegebene Tests verstehen
# ══════════════════════════════════════════════════════════════════
def test_addiere_positive():
    assert addiere(2, 3) == 5


def test_addiere_negative():
    assert addiere(-1, -1) == -2


def test_addiere_null():
    assert addiere(0, 0) == 0


# 👉 Ergänze: Test mit Kommazahlen (Vorsicht bei Floats!)


# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - ist_gerade
# ══════════════════════════════════════════════════════════════════
# Schreib 4 Tests: gerade Zahl, ungerade Zahl, 0, negative Zahl

# 👉 Deine Tests:


# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - durchschnitt (findet einen BUG!)
# ══════════════════════════════════════════════════════════════════
# Schreib Tests für:
#   - Normalfall [2,4,6]
#   - ein Element [5]
#   - negative Zahlen
#   - LEERE LISTE  <- was passiert? Ist das gewünscht?
# Danach: repariere funktionen.py so, dass dein Test durchläuft.

# 👉 Deine Tests:


# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - groesste (findet einen BUG!)
# ══════════════════════════════════════════════════════════════════
# Teste besonders: [-5, -2, -9]  -> sollte -2 sein!

# 👉 Deine Tests:


# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - @parametrize
# ══════════════════════════════════════════════════════════════════
# Schreib EINEN parametrisierten Test für ist_palindrom mit
# mindestens 6 Fällen (Palindrome und Nicht-Palindrome).
#
# Vorlage:
#   @pytest.mark.parametrize("text, erwartet", [
#       ("Otto", True),
#       ...
#   ])
#   def test_palindrom(text, erwartet):
#       assert ist_palindrom(text) == erwartet

# 👉 Dein Test:


# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🟡 - Exceptions testen
# ══════════════════════════════════════════════════════════════════
# Teste mit pytest.raises:
#   - teile(10, 0)        -> ZeroDivisionError
#   - note_zu_text(7)     -> KeyError
# Verbessere danach beide Funktionen so, dass sie einen
# AUSSAGEKRÄFTIGEN ValueError werfen - und passe die Tests an.

# 👉 Deine Tests:


# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - Fixture
# ══════════════════════════════════════════════════════════════════
# Schreib eine Fixture "beispiel_liste", die [3, 1, 4, 1, 5, 9, 2, 6]
# zurückgibt, und benutze sie in mindestens 3 Tests
# (groesste, entferne_duplikate, durchschnitt).

# 👉 Deine Fixture + Tests:


# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 🔴 - Vollständige Testabdeckung
# ══════════════════════════════════════════════════════════════════
# Schreib für zaehle_vokale und formatiere_euro je mindestens
# 4 Tests, die alle 5 Fallarten abdecken:
#   Normalfall, Randfall, Grenzwert, Fehlerfall, realer Fall

# 👉 Deine Tests:


# ══════════════════════════════════════════════════════════════════
# AUFGABE 9 ⭐ BONUS - TDD
# ══════════════════════════════════════════════════════════════════
# Schreib ZUERST Tests für eine Funktion, die es noch NICHT gibt:
#
#   kuerze_text(text, max_laenge=20)
#     - kürzt zu langen Text und hängt "..." an
#     - Gesamtlänge inkl. "..." darf max_laenge nicht überschreiten
#     - kurzer Text bleibt unverändert
#     - max_laenge < 4 -> ValueError
#
# Schreib die Tests, lass sie ROT werden, implementiere dann
# die Funktion in funktionen.py, bis alles GRÜN ist. 🔴➡️🟢

# 👉 Deine Tests:
