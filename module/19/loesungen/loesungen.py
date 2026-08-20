"""Modul 19 · Musterlösungen — Sauberer Code.

Jede Aufgabe zeigt: Vorher (hässlich) → Nachher (sauber) + Begründung.
"""
from __future__ import annotations

import csv
from pathlib import Path

print("=" * 62, "\nAUFGABE 1 🟢 — Namen & PEP 8\n", "=" * 62)

MEHRWERTSTEUERSATZ = 0.19


def berechne_bruttosumme(
    nettobetraege: list[float],
    steuersatz: float = MEHRWERTSTEUERSATZ,
) -> float:
    """Summiert Nettobeträge und schlägt die Mehrwertsteuer auf.

    Args:
        nettobetraege: Liste von Nettobeträgen in Euro.
        steuersatz: Steuersatz als Dezimalzahl (0.19 = 19 %).

    Returns:
        Die Bruttosumme.
    """
    return sum(nettobetraege) * (1 + steuersatz)


preise_nach_artikel = {"Kaffee": 8.99, "Milch": 1.19}
ist_angemeldet = True
bruttosumme = berechne_bruttosumme([10, 20, 30])

print(f"  Bruttosumme: {bruttosumme:.2f} €")
print("""
  ✅ WAS WURDE BESSER:
     • calc  -> berechne_bruttosumme  (Verb + sagt, was rauskommt)
     • l, t, s, d, f, tmp  -> sprechende Namen
     • sum() statt Handschleife
     • 0.19 als benannte Konstante
     • Leerzeichen nach PEP 8, Docstring, Type Hints
""")


print("=" * 62, "\nAUFGABE 2 🟢 — Type Hints & Docstrings\n", "=" * 62)


def filtere_namen(namen: list[str], mindestlaenge: int = 3) -> list[str]:
    """Gibt nur die Namen zurück, die lang genug sind.

    Args:
        namen: Liste von Namen.
        mindestlaenge: Erforderliche Mindestanzahl an Zeichen.

    Returns:
        Neue Liste mit den passenden Namen.
    """
    return [name for name in namen if len(name) >= mindestlaenge]


def finde_person(personen: list[dict], name: str) -> dict | None:
    """Sucht eine Person anhand ihres Namens.

    Returns:
        Das gefundene dict oder None, wenn niemand passt.
    """
    for person in personen:
        if person["name"] == name:
            return person
    return None


def berechne_statistik(zahlen: list[float]) -> tuple[float, float, float]:
    """Berechnet Minimum, Maximum und Durchschnitt.

    Raises:
        ValueError: Wenn die Liste leer ist.
    """
    if not zahlen:
        raise ValueError("Liste darf nicht leer sein")
    return min(zahlen), max(zahlen), sum(zahlen) / len(zahlen)


print(f"  filtere_namen(['Al','Anna','Bo']) = {filtere_namen(['Al', 'Anna', 'Bo'])}")
print(f"  berechne_statistik([4, 9, 2])     = {berechne_statistik([4, 9, 2])}")
print("  ✅ '| None' macht sofort klar, dass die Funktion auch nichts finden kann.")


print("\n" + "=" * 62, "\nAUFGABE 3 🟡 — Magische Zahlen\n", "=" * 62)

SEKUNDEN_PRO_MINUTE = 60
SEKUNDEN_PRO_STUNDE = 3600
SEKUNDEN_PRO_TAG = 86_400

GROSSKUNDEN_SCHWELLE_EURO = 10_000
GROSSKUNDEN_RABATT = 0.05


def formatiere_dauer(sekunden: int) -> str:
    """Formatiert eine Sekundenzahl als 'Xd Yh Zm Ws'."""
    tage = sekunden // SEKUNDEN_PRO_TAG
    stunden = (sekunden % SEKUNDEN_PRO_TAG) // SEKUNDEN_PRO_STUNDE
    minuten = (sekunden % SEKUNDEN_PRO_STUNDE) // SEKUNDEN_PRO_MINUTE
    rest = sekunden % SEKUNDEN_PRO_MINUTE
    return f"{tage}d {stunden}h {minuten}m {rest}s"


def berechne_bruttopreis(netto: float) -> float:
    """Berechnet den Bruttopreis inkl. Großkundenrabatt ab 10.000 €."""
    brutto = netto * (1 + MEHRWERTSTEUERSATZ)
    if netto > GROSSKUNDEN_SCHWELLE_EURO:
        brutto *= 1 - GROSSKUNDEN_RABATT
    return round(brutto, 2)


print(f"  formatiere_dauer(100000)      = {formatiere_dauer(100_000)}")
print(f"  berechne_bruttopreis(15000)   = {berechne_bruttopreis(15_000):,.2f} €")
print("  ✅ 86400 sagt nichts. SEKUNDEN_PRO_TAG sagt alles.")


print("\n" + "=" * 62, "\nAUFGABE 4 🟡 — Guard Clauses\n", "=" * 62)

MINDESTALTER = 18


def darf_bestellen(benutzer: dict | None) -> bool:
    """Prüft, ob ein Benutzer bestellen darf."""
    if benutzer is None:
        return False
    if not benutzer["aktiv"]:
        return False
    if benutzer["gesperrt"]:
        return False
    if benutzer["guthaben"] <= 0:
        return False
    return benutzer["alter"] >= MINDESTALTER


testfaelle = [
    None,
    {"aktiv": True, "gesperrt": False, "guthaben": 50, "alter": 25},
    {"aktiv": True, "gesperrt": True, "guthaben": 50, "alter": 25},
    {"aktiv": True, "gesperrt": False, "guthaben": 50, "alter": 16},
]
for fall in testfaelle:
    print(f"  {str(fall)[:52]:<54} -> {darf_bestellen(fall)}")
print("  ✅ Von 6 Einrückungsebenen auf 1. Und man liest es von oben nach unten.")


print("\n" + "=" * 62, "\nAUFGABE 5 🟡 — Funktion aufteilen\n", "=" * 62)

VERSANDKOSTEN_EURO = 4.99
VERSANDFREI_AB_EURO = 100
RABATTSTUFEN = ((500, 0.10), (200, 0.05))


def validiere_bestellung(bestellung: dict) -> str | None:
    """Gibt eine Fehlermeldung zurück oder None, wenn alles passt."""
    if not bestellung.get("kunde"):
        return "Kunde fehlt"
    if not bestellung.get("artikel"):
        return "Keine Artikel"
    return None


def berechne_nettosumme(artikel: list[dict]) -> float:
    """Summiert Preis × Menge aller Artikel."""
    return sum(a["preis"] * a["menge"] for a in artikel)


def ermittle_rabatt(summe: float) -> float:
    """Gibt den Rabattsatz für eine Summe zurück."""
    for schwelle, satz in RABATTSTUFEN:
        if summe > schwelle:
            return satz
    return 0.0


def ermittle_versandkosten(summe: float) -> float:
    """Gibt die Versandkosten zurück (ab 100 € kostenlos)."""
    return 0.0 if summe > VERSANDFREI_AB_EURO else VERSANDKOSTEN_EURO


def zeige_bestellung(bestellung: dict, netto: float,
                     versand: float, brutto: float) -> None:
    """Gibt eine Bestellübersicht aus."""
    print(f"    Kunde:   {bestellung['kunde']}")
    print(f"    Artikel: {len(bestellung['artikel'])}")
    print(f"    Netto:   {netto:>8.2f} €")
    print(f"    Versand: {versand:>8.2f} €")
    print(f"    Brutto:  {brutto:>8.2f} €")


def verarbeite_bestellung(bestellung: dict) -> dict:
    """Validiert und berechnet eine Bestellung."""
    fehler = validiere_bestellung(bestellung)
    if fehler:
        return {"fehler": fehler}

    netto = berechne_nettosumme(bestellung["artikel"])
    netto *= 1 - ermittle_rabatt(netto)
    versand = ermittle_versandkosten(netto)
    brutto = round((netto + versand) * (1 + MEHRWERTSTEUERSATZ), 2)

    zeige_bestellung(bestellung, netto, versand, brutto)
    return {"brutto": brutto}


beispiel = {"kunde": "Anna Müller", "artikel": [
    {"preis": 89.99, "menge": 3},
    {"preis": 249.00, "menge": 1},
]}
verarbeite_bestellung(beispiel)
print(f"  Fehlerfall: {verarbeite_bestellung({'kunde': ''})}")
print("  ✅ Jede Funktion macht EINE Sache und ist einzeln testbar.")


print("\n" + "=" * 62, "\nAUFGABE 6 🔴 — Copy-Paste entfernen\n", "=" * 62)


def zeige_kategorie_report(daten: list[dict], kategorie: str,
                           breite: int = 40) -> float:
    """Gibt einen Report für eine Kategorie aus und liefert die Summe."""
    print("  " + "=" * breite)
    print(f"  {kategorie.upper()}")
    print("  " + "=" * breite)

    gesamt = 0.0
    for eintrag in daten:
        if eintrag["kategorie"] != kategorie:
            continue
        print(f"  {eintrag['name']:<20}{eintrag['preis']:>10.2f}")
        gesamt += eintrag["preis"]

    print("  " + "-" * breite)
    print(f"  {'SUMME':<20}{gesamt:>10.2f}")
    return gesamt


sortiment = [
    {"name": "Laptop", "kategorie": "Technik", "preis": 899.99},
    {"name": "Maus", "kategorie": "Technik", "preis": 25.50},
    {"name": "Schreibtisch", "kategorie": "Möbel", "preis": 349.00},
    {"name": "Bürostuhl", "kategorie": "Möbel", "preis": 259.90},
]

for kategorie in ("Technik", "Möbel"):
    zeige_kategorie_report(sortiment, kategorie)
    print()

print("  ✅ Eine Funktion statt zwei. Neue Kategorie = 0 Zeilen neuer Code.")


print("=" * 62, "\nAUFGABE 7 ⭐ — Komplett-Refactoring\n", "=" * 62)

ORDNER = Path(__file__).parent / "_daten19"
ORDNER.mkdir(exist_ok=True)
CSV_DATEI = ORDNER / "artikel.csv"
CSV_DATEI.write_text(
    "id;name;kategorie;preis\n"
    "1;Laptop;Technik;899,99\n"
    "2;Maus;Technik;25,50\n"
    "3;Defekt;Technik;keine_zahl\n"
    "4;Gratis;Technik;0,00\n"
    "5;Monitor;Technik;219,00\n",
    encoding="utf-8")

CSV_TRENNZEICHEN = ";"
SPALTE_PREIS = 3
SPALTE_NAME = 1


def lade_artikel_mit_bruttopreis(pfad: Path | str) -> list[dict]:
    """Liest Artikel aus einer CSV und ergänzt den Bruttopreis.

    Zeilen mit ungültigem oder nicht-positivem Preis werden übersprungen.

    Args:
        pfad: Pfad zur CSV-Datei (Trennzeichen ';', deutsches Zahlenformat).

    Returns:
        Liste von dicts mit den Schlüsseln name, netto und brutto.

    Raises:
        FileNotFoundError: Wenn die Datei nicht existiert.
    """
    artikel: list[dict] = []

    with open(pfad, encoding="utf-8", newline="") as datei:
        leser = csv.reader(datei, delimiter=CSV_TRENNZEICHEN)
        next(leser, None)                       # Kopfzeile überspringen

        for zeile in leser:
            if len(zeile) <= SPALTE_PREIS:
                continue
            try:
                netto = float(zeile[SPALTE_PREIS].replace(",", "."))
            except ValueError:
                continue                        # gezielt: nur Zahlfehler
            if netto <= 0:
                continue

            artikel.append({
                "name": zeile[SPALTE_NAME],
                "netto": netto,
                "brutto": round(netto * (1 + MEHRWERTSTEUERSATZ), 2),
            })

    return artikel


for eintrag in lade_artikel_mit_bruttopreis(CSV_DATEI):
    print(f"  {eintrag['name']:<12}{eintrag['netto']:>10.2f}{eintrag['brutto']:>10.2f}")

print("""
  ✅ WAS WURDE BESSER:
     • go -> lade_artikel_mit_bruttopreis (sagt genau, was passiert)
     • r, x, c, l, p, n, t -> sprechende Schlüssel
     • except: pass -> except ValueError (Tippfehler werden nicht mehr verschluckt)
     • encoding + newline explizit
     • Spaltenindizes und Steuersatz als Konstanten
     • Type Hints + Docstring mit Raises

  🎉 Modul 19 geschafft! Dein Code ist jetzt lesbar - auch in 6 Monaten.
""")
