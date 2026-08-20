"""
💰 Haushaltsbuch - Musterlösung Projekt 2

Benutzt Konzepte aus den Modulen 00-08:
Listen, Dictionaries, Funktionen, Schleifen, Bedingungen, f-Strings.

AUFRUF:
    python haushaltsbuch.py
"""

# ====================================================================
# EINSTELLUNGEN
# ====================================================================
KATEGORIEN = ["Miete", "Lebensmittel", "Mobilität", "Freizeit",
              "Gesundheit", "Versicherung", "Sonstiges"]

BREITE = 54
DEMO_MODUS = True        # 👈 auf False setzen für echte Bedienung

DEMO_EINGABEN = ["3", "5", "6", "2", "4", "q"]
_index = 0


def frage(text):
    """Holt eine Eingabe - im Demo-Modus aus einer Liste."""
    global _index
    if DEMO_MODUS:
        antwort = DEMO_EINGABEN[_index] if _index < len(DEMO_EINGABEN) else "q"
        _index += 1
        print(f"{text}{antwort}")
        return antwort
    return input(text)


# ====================================================================
# AUSGABE-HILFEN
# ====================================================================
def euro(betrag):
    """Formatiert einen Betrag im deutschen Format: 1.234,56 €"""
    text = f"{abs(betrag):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    vorzeichen = "-" if betrag < 0 else ""
    return f"{vorzeichen}{text} €"


def balken(anteil, breite=16):
    """Erzeugt einen Balken für das Terminal-Diagramm."""
    return "█" * int(anteil * breite) + " " * (breite - int(anteil * breite))


def kopfzeile(text):
    """Gibt eine Überschrift mit Rahmen aus."""
    print("╔" + "═" * BREITE + "╗")
    print("║" + text.center(BREITE) + "║")
    print("╚" + "═" * BREITE + "╝")


def zeile(text=""):
    """Gibt eine gerahmte Zeile aus."""
    print("║ " + text.ljust(BREITE - 2) + " ║")


# ====================================================================
# EINGABE-HILFEN
# ====================================================================
def frage_zahl(text, min_wert=None):
    """Fragt so lange, bis eine gültige Zahl eingegeben wurde.

    Args:
        text: Der Eingabe-Prompt.
        min_wert: Optionaler Mindestwert.

    Returns:
        Die eingegebene Zahl als float.
    """
    for _ in range(20):          # Sicherheitsgrenze gegen Endlosschleifen
        eingabe = frage(text).strip().replace(",", ".")
        # ohne try/except - reine String-Prüfung (Modul 02/04)
        ohne_punkt = eingabe.replace(".", "", 1).lstrip("-")
        if not ohne_punkt.isdigit():
            print("  ⚠️  Bitte eine Zahl eingeben (z. B. 12.50)")
            continue

        wert = float(eingabe)
        if min_wert is not None and wert < min_wert:
            print(f"  ⚠️  Der Wert muss mindestens {min_wert} sein.")
            continue
        return wert
    return min_wert or 0.0


def frage_kategorie():
    """Lässt den Nutzer eine Kategorie auswählen."""
    print("\n  Kategorie wählen:")
    for nr, kategorie in enumerate(KATEGORIEN, start=1):
        print(f"    [{nr}] {kategorie}")

    for _ in range(20):          # Sicherheitsgrenze gegen Endlosschleifen
        eingabe = frage("  > ").strip()
        if eingabe.isdigit() and 1 <= int(eingabe) <= len(KATEGORIEN):
            return KATEGORIEN[int(eingabe) - 1]
        print(f"  ⚠️  Bitte 1 bis {len(KATEGORIEN)} eingeben.")
    return KATEGORIEN[-1]


# ====================================================================
# BUCHUNGEN
# ====================================================================
def erfasse_buchung(buchungen, ist_einnahme):
    """Erfasst eine neue Buchung und hängt sie an die Liste an.

    Args:
        buchungen: Die Liste aller Buchungen.
        ist_einnahme: True für Einnahme, False für Ausgabe.
    """
    art = "EINNAHME" if ist_einnahme else "AUSGABE"
    print(f"\n── Neue {art} " + "─" * (BREITE - 14 - len(art)))

    betrag = frage_zahl("  Betrag in € > ", min_wert=0.01)
    kategorie = "Einkommen" if ist_einnahme else frage_kategorie()
    beschreibung = frage("  Beschreibung > ").strip() or "(ohne)"
    datum = frage("  Datum (TT.MM.JJJJ) > ").strip() or "ohne Datum"

    buchungen.append({
        "datum": datum,
        "kategorie": kategorie,
        "betrag": betrag if ist_einnahme else -betrag,
        "beschreibung": beschreibung[:28],
    })
    print(f"\n  ✅ {art} über {euro(betrag)} erfasst.")


def zeige_buchungen(buchungen):
    """Gibt alle Buchungen als Tabelle aus."""
    if not buchungen:
        print("\n  📭 Noch keine Buchungen erfasst.")
        return

    print("\n  " + "─" * 66)
    print(f"  {'#':>3}  {'Datum':<12}{'Kategorie':<15}{'Beschreibung':<20}{'Betrag':>12}")
    print("  " + "─" * 66)
    for nr, b in enumerate(buchungen, start=1):
        symbol = "🟢" if b["betrag"] > 0 else "🔴"
        print(f"  {nr:>3}  {b['datum']:<12}{b['kategorie']:<15}"
              f"{b['beschreibung']:<20}{euro(b['betrag']):>12} {symbol}")
    print("  " + "─" * 66)
    print(f"  {'KONTOSTAND':<50}{euro(kontostand(buchungen)):>16}")


def kontostand(buchungen):
    """Berechnet den aktuellen Kontostand."""
    return sum(b["betrag"] for b in buchungen)


def summe_nach_kategorie(buchungen):
    """Gibt ein dict {kategorie: summe} für alle Ausgaben zurück."""
    summen = {}
    for b in buchungen:
        if b["betrag"] < 0:
            summen[b["kategorie"]] = summen.get(b["kategorie"], 0) + abs(b["betrag"])
    return summen


def loesche_buchung(buchungen):
    """Löscht eine Buchung nach Nummer."""
    if not buchungen:
        print("\n  📭 Keine Buchungen vorhanden.")
        return

    zeige_buchungen(buchungen)
    eingabe = frage("\n  Nummer löschen (Enter = abbrechen) > ").strip()
    if not eingabe:
        return
    if not eingabe.isdigit() or not (1 <= int(eingabe) <= len(buchungen)):
        print("  ⚠️  Ungültige Nummer.")
        return

    entfernt = buchungen.pop(int(eingabe) - 1)
    print(f"  🗑️  '{entfernt['beschreibung']}' gelöscht.")


def filtere_nach_kategorie(buchungen):
    """Zeigt nur die Buchungen einer gewählten Kategorie."""
    if not buchungen:
        print("\n  📭 Keine Buchungen vorhanden.")
        return
    kategorie = frage_kategorie()
    gefiltert = [b for b in buchungen if b["kategorie"] == kategorie]
    print(f"\n  {len(gefiltert)} Buchung(en) in '{kategorie}':")
    zeige_buchungen(gefiltert)


# ====================================================================
# AUSWERTUNG
# ====================================================================
def zeige_auswertung(buchungen):
    """Gibt die komplette Auswertung mit Balkendiagramm aus."""
    if not buchungen:
        print("\n  📭 Noch keine Buchungen - keine Auswertung möglich.")
        return          # 🛡️ verhindert Division durch 0!

    einnahmen = sum(b["betrag"] for b in buchungen if b["betrag"] > 0)
    ausgaben = sum(-b["betrag"] for b in buchungen if b["betrag"] < 0)
    saldo = einnahmen - ausgaben

    print()
    print("╔" + "═" * BREITE + "╗")
    print("║" + "AUSWERTUNG".center(BREITE) + "║")
    print("╠" + "═" * BREITE + "╣")
    zeile(f"{'Einnahmen:':<30}{euro(einnahmen):>20}")
    zeile(f"{'Ausgaben:':<30}{euro(ausgaben):>20}")
    zeile("─" * (BREITE - 2))
    zeile(f"{'SALDO:':<30}{euro(saldo):>20}  {'🟢' if saldo >= 0 else '🔴'}")

    nach_kategorie = summe_nach_kategorie(buchungen)
    if nach_kategorie:
        print("╠" + "═" * BREITE + "╣")
        zeile("AUSGABEN NACH KATEGORIE")
        for kategorie, summe in sorted(nach_kategorie.items(), key=lambda p: -p[1]):
            anteil = summe / ausgaben if ausgaben else 0
            zeile(f" {kategorie:<14}{euro(summe):>12}  {balken(anteil)} {anteil:>4.0%}")

    groesste = min(buchungen, key=lambda b: b["betrag"])
    schnitt = sum(abs(b["betrag"]) for b in buchungen) / len(buchungen)

    print("╠" + "═" * BREITE + "╣")
    if groesste["betrag"] < 0:
        zeile(f"Größte Ausgabe: {groesste['beschreibung']} "
              f"({euro(abs(groesste['betrag']))})")
    zeile(f"Ø pro Buchung:  {euro(schnitt)}")
    zeile(f"Buchungen:      {len(buchungen)}")
    print("╚" + "═" * BREITE + "╝")


# ====================================================================
# MENÜ & HAUPTPROGRAMM
# ====================================================================
def zeige_menue():
    """Gibt das Hauptmenü aus."""
    print()
    print("  [1] Einnahme erfassen        [5] Auswertung")
    print("  [2] Ausgabe erfassen         [6] Nach Kategorie filtern")
    print("  [3] Alle Buchungen anzeigen  [7] Buchung löschen")
    print("  [4] Kontostand               [q] Beenden")


def beispieldaten():
    """Erzeugt ein paar Beispielbuchungen für die Demo."""
    return [
        {"datum": "01.01.2026", "kategorie": "Einkommen", "betrag": 2500.00,
         "beschreibung": "Gehalt Januar"},
        {"datum": "03.01.2026", "kategorie": "Miete", "betrag": -850.00,
         "beschreibung": "Miete Januar"},
        {"datum": "05.01.2026", "kategorie": "Lebensmittel", "betrag": -87.45,
         "beschreibung": "Wocheneinkauf"},
        {"datum": "08.01.2026", "kategorie": "Mobilität", "betrag": -49.00,
         "beschreibung": "Monatsticket"},
        {"datum": "12.01.2026", "kategorie": "Freizeit", "betrag": -32.00,
         "beschreibung": "Kino & Essen"},
        {"datum": "15.01.2026", "kategorie": "Lebensmittel", "betrag": -104.20,
         "beschreibung": "Großeinkauf"},
        {"datum": "18.01.2026", "kategorie": "Einkommen", "betrag": 350.00,
         "beschreibung": "Nebenjob"},
        {"datum": "20.01.2026", "kategorie": "Gesundheit", "betrag": -24.99,
         "beschreibung": "Apotheke"},
        {"datum": "22.01.2026", "kategorie": "Mobilität", "betrag": -62.30,
         "beschreibung": "Tanken"},
        {"datum": "25.01.2026", "kategorie": "Sonstiges", "betrag": -45.00,
         "beschreibung": "Geschenk"},
    ]


def main():
    """Hauptprogramm mit Menüschleife."""
    kopfzeile("💰  HAUSHALTSBUCH  💰")

    buchungen = beispieldaten() if DEMO_MODUS else []
    if DEMO_MODUS:
        print(f"\n  ℹ️  Demo-Modus: {len(buchungen)} Beispielbuchungen geladen.")

    aktionen = {
        "1": lambda: erfasse_buchung(buchungen, True),
        "2": lambda: erfasse_buchung(buchungen, False),
        "3": lambda: zeige_buchungen(buchungen),
        "4": lambda: print(f"\n  💶 Kontostand: {euro(kontostand(buchungen))}"),
        "5": lambda: zeige_auswertung(buchungen),
        "6": lambda: filtere_nach_kategorie(buchungen),
        "7": lambda: loesche_buchung(buchungen),
    }

    while True:
        zeige_menue()
        wahl = frage("\n> ").strip().lower()

        if wahl in ("q", "quit", "ende"):
            print(f"\n  Endstand: {euro(kontostand(buchungen))}")
            print("  Bis zum nächsten Mal! 👋\n")
            break

        aktion = aktionen.get(wahl)
        if aktion:
            aktion()
        else:
            print("  ⚠️  Unbekannte Auswahl. Bitte 1-7 oder q.")


if __name__ == "__main__":
    main()
