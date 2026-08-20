"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 18 · MUSTERLÖSUNG — vollständige Testsuite                ║
║                                                                  ║
║  Ausführen:  cd module/18/loesungen  &&  pytest -v               ║
╚══════════════════════════════════════════════════════════════════╝
"""
import pytest
from funktionen import (addiere, durchschnitt, ist_gerade, groesste,
                        ist_palindrom, zaehle_vokale, formatiere_euro,
                        note_zu_text, teile, entferne_duplikate, kuerze_text)


# ══════════════════════════════════════════════════════════════════
# FIXTURES
# ══════════════════════════════════════════════════════════════════
@pytest.fixture
def beispiel_liste():
    """Liefert eine Beispielliste mit Duplikaten."""
    return [3, 1, 4, 1, 5, 9, 2, 6]


# ══════════════════════════════════════════════════════════════════
# addiere
# ══════════════════════════════════════════════════════════════════
def test_addiere_positive():
    assert addiere(2, 3) == 5


def test_addiere_negative():
    assert addiere(-1, -1) == -2


def test_addiere_null():
    assert addiere(0, 0) == 0


def test_addiere_kommazahlen():
    # ⚠️ Floats NIE direkt vergleichen!
    assert abs(addiere(0.1, 0.2) - 0.3) < 1e-9


def test_addiere_strings():
    """Python erlaubt + auch für Strings - dokumentiertes Verhalten."""
    assert addiere("a", "b") == "ab"


# ══════════════════════════════════════════════════════════════════
# ist_gerade
# ══════════════════════════════════════════════════════════════════
@pytest.mark.parametrize("zahl, erwartet", [
    (4, True), (7, False), (0, True), (-2, True), (-3, False),
])
def test_ist_gerade(zahl, erwartet):
    assert ist_gerade(zahl) is erwartet


# ══════════════════════════════════════════════════════════════════
# durchschnitt  (Bug 1: leere Liste)
# ══════════════════════════════════════════════════════════════════
def test_durchschnitt_normalfall():
    assert durchschnitt([2, 4, 6]) == 4


def test_durchschnitt_ein_element():
    assert durchschnitt([5]) == 5


def test_durchschnitt_negative():
    assert durchschnitt([-2, 2]) == 0


def test_durchschnitt_kommazahlen():
    assert abs(durchschnitt([1.5, 2.5]) - 2.0) < 1e-9


def test_durchschnitt_leere_liste_wirft_fehler():
    """🐛 BUG 1: vorher ZeroDivisionError, jetzt klarer ValueError."""
    with pytest.raises(ValueError, match="darf nicht leer"):
        durchschnitt([])


# ══════════════════════════════════════════════════════════════════
# groesste  (Bug 2: nur negative Zahlen)
# ══════════════════════════════════════════════════════════════════
def test_groesste_normalfall():
    assert groesste([3, 7, 2]) == 7


def test_groesste_nur_negative():
    """🐛 BUG 2: alte Version gab 0 zurück, obwohl 0 nicht in der Liste ist."""
    assert groesste([-5, -2, -9]) == -2


def test_groesste_ein_element():
    assert groesste([42]) == 42


def test_groesste_gemischt(beispiel_liste):
    assert groesste(beispiel_liste) == 9


def test_groesste_leer_wirft_fehler():
    with pytest.raises(ValueError):
        groesste([])


# ══════════════════════════════════════════════════════════════════
# ist_palindrom
# ══════════════════════════════════════════════════════════════════
@pytest.mark.parametrize("text, erwartet", [
    ("Otto", True),
    ("Anna", True),
    ("Reliefpfeiler", True),
    ("Ein Esel lese nie", True),
    ("Python", False),
    ("Hallo Welt", False),
    ("a", True),
    ("", True),
    ("Was it a car or a cat I saw?", True),   # mit Satzzeichen
])
def test_ist_palindrom(text, erwartet):
    assert ist_palindrom(text) is erwartet


# ══════════════════════════════════════════════════════════════════
# zaehle_vokale
# ══════════════════════════════════════════════════════════════════
def test_zaehle_vokale_normalfall():
    assert zaehle_vokale("Hallo") == 2


def test_zaehle_vokale_leer():
    assert zaehle_vokale("") == 0


def test_zaehle_vokale_keine_vokale():
    assert zaehle_vokale("rhythm") == 0


def test_zaehle_vokale_grossschreibung():
    assert zaehle_vokale("AEIOU") == 5


def test_zaehle_vokale_umlaute():
    assert zaehle_vokale("Bär Öl Übung") == 4    # ä, ö, ü, u


def test_zaehle_vokale_realer_satz():
    assert zaehle_vokale("Python ist toll") == 3  # o, i, o


# ══════════════════════════════════════════════════════════════════
# formatiere_euro
# ══════════════════════════════════════════════════════════════════
@pytest.mark.parametrize("betrag, erwartet", [
    (0, "0,00 €"),
    (1, "1,00 €"),
    (1234.56, "1.234,56 €"),
    (1000000, "1.000.000,00 €"),
    (-45.5, "-45,50 €"),
    (0.005, "0,01 €"),          # Rundung
])
def test_formatiere_euro(betrag, erwartet):
    assert formatiere_euro(betrag) == erwartet


# ══════════════════════════════════════════════════════════════════
# note_zu_text  (Bug 3: ungültige Note)
# ══════════════════════════════════════════════════════════════════
def test_note_zu_text_gueltig():
    assert note_zu_text(1) == "sehr gut"
    assert note_zu_text(6) == "ungenügend"


@pytest.mark.parametrize("note", [0, 7, -1, 99])
def test_note_zu_text_ungueltig(note):
    """🐛 BUG 3: vorher KeyError, jetzt aussagekräftiger ValueError."""
    with pytest.raises(ValueError, match="Ungültige Note"):
        note_zu_text(note)


# ══════════════════════════════════════════════════════════════════
# teile  (Bug 4: Division durch 0)
# ══════════════════════════════════════════════════════════════════
def test_teile_normalfall():
    assert teile(10, 2) == 5


def test_teile_kommazahl():
    assert abs(teile(1, 3) - 0.3333333333) < 1e-9


def test_teile_durch_null():
    """🐛 BUG 4: vorher ZeroDivisionError, jetzt klarer ValueError."""
    with pytest.raises(ValueError, match="Division durch Null"):
        teile(10, 0)


# ══════════════════════════════════════════════════════════════════
# entferne_duplikate
# ══════════════════════════════════════════════════════════════════
def test_entferne_duplikate(beispiel_liste):
    assert entferne_duplikate(beispiel_liste) == [3, 1, 4, 5, 9, 2, 6]


def test_entferne_duplikate_leer():
    assert entferne_duplikate([]) == []


def test_entferne_duplikate_ohne_duplikate():
    assert entferne_duplikate([1, 2, 3]) == [1, 2, 3]


def test_entferne_duplikate_alle_gleich():
    assert entferne_duplikate([7, 7, 7]) == [7]


def test_entferne_duplikate_reihenfolge_bleibt():
    """Wichtig: die Reihenfolge des ERSTEN Auftretens muss erhalten bleiben."""
    assert entferne_duplikate(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]


# ══════════════════════════════════════════════════════════════════
# kuerze_text  (per TDD entstanden)
# ══════════════════════════════════════════════════════════════════
def test_kuerze_text_kurz_bleibt_unveraendert():
    assert kuerze_text("kurz", 20) == "kurz"


def test_kuerze_text_genau_max_laenge():
    text = "a" * 20
    assert kuerze_text(text, 20) == text


def test_kuerze_text_zu_lang():
    ergebnis = kuerze_text("a" * 50, 20)
    assert len(ergebnis) == 20
    assert ergebnis.endswith("...")


def test_kuerze_text_realer_fall():
    assert kuerze_text("Python ist eine großartige Sprache", 20) == "Python ist eine g..."


def test_kuerze_text_ungueltige_laenge():
    with pytest.raises(ValueError, match="mindestens 4"):
        kuerze_text("text", 3)


# ══════════════════════════════════════════════════════════════════
# Beim direkten Start: Hinweis anzeigen
# ══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("""
    Diese Datei wird mit pytest ausgeführt, nicht direkt:

        pip install pytest
        cd module/18/loesungen
        pytest -v

    Nützliche Optionen:
        pytest -v            ausführlich
        pytest -x            beim ersten Fehler stoppen
        pytest -k palindrom  nur Tests mit "palindrom" im Namen
        pytest --tb=short    kurze Fehlerausgabe
    """)
