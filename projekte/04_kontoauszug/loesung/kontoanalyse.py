"""
🏦 Kontoauszug-Analyse - Musterlösung Projekt 4

Liest eine deutsche Bank-CSV, kategorisiert die Buchungen automatisch
und erstellt eine vollständige Auswertung.

Benutzt Modul 00-16: CSV, JSON, datetime, Exceptions, Funktionen.

AUFRUF:
    python kontoanalyse.py
"""
import csv
import json
import random
from datetime import datetime
from pathlib import Path

# ====================================================================
# EINSTELLUNGEN
# ====================================================================
KATEGORIEN = {
    "Wohnen":       (["miete", "hausverwaltung", "stadtwerke", "strom",
                      "gas", "nebenkosten"], "🏠"),
    "Lebensmittel": (["rewe", "edeka", "aldi", "lidl", "penny", "netto",
                      "bäckerei", "supermarkt"], "🛒"),
    "Mobilität":    (["tankstelle", "shell", "aral", "bahn", "bvg", "hvv",
                      "tanken", "ticket"], "🚗"),
    "Freizeit":     (["kino", "restaurant", "bar", "fitness", "sport",
                      "theater", "konzert"], "🎬"),
    "Abos":         (["netflix", "spotify", "prime", "abo", "mobilfunk",
                      "internet"], "📱"),
    "Gesundheit":   (["apotheke", "arzt", "krankenkasse", "praxis"], "💊"),
    "Versicherung": (["versicherung", "allianz", "huk"], "🛡️"),
}
SONSTIGES_SYMBOL = "❓"
BREITE = 56

ORDNER = Path(__file__).parent / "_daten"
ORDNER.mkdir(exist_ok=True)
CSV_DATEI = ORDNER / "kontoauszug_2026.csv"


# ====================================================================
# TESTDATEN ERZEUGEN
# ====================================================================
def erzeuge_testdaten(pfad, anzahl=140):
    """Erzeugt eine realistische Bank-CSV inklusive fehlerhafter Zeilen."""
    random.seed(2026)

    vorlagen = [
        ("Muster GmbH", "Gehalt", 2850.00, 2850.00),
        ("Hausverwaltung Meier", "Miete", -850.00, -850.00),
        ("REWE Markt GmbH", "Kartenzahlung", -25.00, -120.00),
        ("EDEKA Suedwest", "Kartenzahlung", -18.00, -95.00),
        ("Shell Tankstelle", "Tanken", -45.00, -95.00),
        ("Deutsche Bahn AG", "Ticket", -12.00, -89.00),
        ("Netflix International", "Abo", -17.99, -17.99),
        ("Spotify AB", "Abo Premium", -10.99, -10.99),
        ("Stadtwerke Berlin", "Abschlag Strom", -89.00, -89.00),
        ("Fitness First", "Mitgliedsbeitrag", -39.90, -39.90),
        ("Apotheke am Markt", "Kartenzahlung", -12.00, -68.00),
        ("Kino Central", "Kartenzahlung", -14.50, -32.00),
        ("Restaurant Bella", "Kartenzahlung", -28.00, -95.00),
        ("Allianz Versicherung", "Beitrag Hausrat", -24.50, -24.50),
        ("Amazon EU", "Bestellung", -15.00, -180.00),
    ]

    zeilen = []
    for i in range(anzahl):
        empfaenger, zweck, min_b, max_b = random.choice(vorlagen)
        betrag = round(random.uniform(min(min_b, max_b), max(min_b, max_b)), 2)
        monat = random.randint(1, 6)
        tag = random.randint(1, 28)
        betrag_text = f"{abs(betrag):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        if betrag < 0:
            betrag_text = "-" + betrag_text
        zeilen.append(f"{tag:02d}.{monat:02d}.2026;{empfaenger};{zweck};{betrag_text};EUR")

    # Absichtlich fehlerhafte Zeilen
    zeilen.insert(20, "15.02.2026;Kaputt GmbH;Test;keine_zahl;EUR")
    zeilen.insert(55, "unklar;Fehler AG;Test;-50,00;EUR")
    zeilen.insert(90, "10.03.2026;Zu wenig Spalten")

    kopf = "Datum;Empfänger;Verwendungszweck;Betrag;Währung"
    pfad.write_text(kopf + "\n" + "\n".join(zeilen) + "\n", encoding="utf-8")
    return pfad


# ====================================================================
# HILFSFUNKTIONEN
# ====================================================================
def deutsche_zahl(text):
    """Wandelt '1.234,56' in 1234.56 um.

    Raises:
        ValueError: Wenn der Text keine gültige Zahl ist.
    """
    return float(text.strip().replace(".", "").replace(",", "."))


def euro(betrag):
    """Formatiert einen Betrag im deutschen Format."""
    text = f"{abs(betrag):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{'-' if betrag < 0 else ''}{text} €"


def balken(anteil, breite=16):
    """Erzeugt einen Balken für das Terminal-Diagramm."""
    voll = int(anteil * breite)
    return "█" * voll + " " * (breite - voll)


def kopfzeile(text):
    """Gibt eine Überschrift mit Rahmen aus."""
    print("╔" + "═" * BREITE + "╗")
    print("║" + text.center(BREITE) + "║")
    print("╚" + "═" * BREITE + "╝")


def abschnitt(text):
    """Gibt eine Abschnittsüberschrift aus."""
    print(f"\n── {text} " + "─" * max(0, BREITE - len(text) - 4))


# ====================================================================
# EINLESEN
# ====================================================================
def kategorisiere(empfaenger, zweck):
    """Ordnet einer Buchung anhand von Stichwörtern eine Kategorie zu."""
    text = f"{empfaenger} {zweck}".lower()
    for kategorie, (stichwoerter, _) in KATEGORIEN.items():
        if any(wort in text for wort in stichwoerter):
            return kategorie
    return "Sonstiges"


def lade_buchungen(pfad):
    """Liest die CSV robust ein.

    Args:
        pfad: Pfad zur CSV-Datei.

    Returns:
        (buchungen, fehler) - fehler ist eine Liste (zeilennummer, grund).

    Raises:
        FileNotFoundError: Wenn die Datei nicht existiert.
    """
    pfad = Path(pfad)
    if not pfad.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {pfad.absolute()}")

    buchungen = []
    fehler = []

    with open(pfad, encoding="utf-8", newline="") as f:
        leser = csv.DictReader(f, delimiter=";")
        for nr, zeile in enumerate(leser, start=2):
            try:
                betrag = deutsche_zahl(zeile["Betrag"])
                datum = datetime.strptime(zeile["Datum"], "%d.%m.%Y").date()
            except (ValueError, TypeError, AttributeError) as f_:
                fehler.append((nr, f"{zeile.get('Empfänger', '?')}: {f_}"))
                continue

            empfaenger = (zeile.get("Empfänger") or "").strip()
            zweck = (zeile.get("Verwendungszweck") or "").strip()

            buchungen.append({
                "datum": datum,
                "empfaenger": empfaenger,
                "zweck": zweck,
                "betrag": betrag,
                "kategorie": kategorisiere(empfaenger, zweck),
            })

    return buchungen, fehler


# ====================================================================
# AUSWERTUNGEN
# ====================================================================
def auswertung_kategorien(buchungen):
    """Summiert die Ausgaben je Kategorie."""
    summen = {}
    for b in buchungen:
        if b["betrag"] < 0:
            summen[b["kategorie"]] = summen.get(b["kategorie"], 0) + abs(b["betrag"])
    return summen


def auswertung_monate(buchungen):
    """Berechnet Einnahmen, Ausgaben und Saldo je Monat."""
    monate = {}
    for b in buchungen:
        schluessel = b["datum"].strftime("%Y-%m")
        eintrag = monate.setdefault(schluessel, {"ein": 0.0, "aus": 0.0})
        if b["betrag"] > 0:
            eintrag["ein"] += b["betrag"]
        else:
            eintrag["aus"] += abs(b["betrag"])
    for eintrag in monate.values():
        eintrag["saldo"] = eintrag["ein"] - eintrag["aus"]
    return dict(sorted(monate.items()))


def finde_wiederkehrende(buchungen, mindestens=3):
    """Erkennt wiederkehrende Buchungen (Abos, Daueraufträge)."""
    nach_empfaenger = {}
    for b in buchungen:
        if b["betrag"] < 0:
            nach_empfaenger.setdefault(b["empfaenger"], []).append(abs(b["betrag"]))

    wiederkehrend = {}
    for empfaenger, betraege in nach_empfaenger.items():
        if len(betraege) < mindestens:
            continue
        schnitt = sum(betraege) / len(betraege)
        # Alle Beträge nah am Durchschnitt? → wahrscheinlich ein Abo
        if all(abs(b - schnitt) < max(1.0, schnitt * 0.15) for b in betraege):
            wiederkehrend[empfaenger] = {
                "anzahl": len(betraege),
                "durchschnitt": round(schnitt, 2),
                "gesamt": round(sum(betraege), 2),
            }
    return wiederkehrend


def finde_ausreisser(buchungen, faktor=3):
    """Findet ungewöhnlich große Ausgaben."""
    ausgaben = [abs(b["betrag"]) for b in buchungen if b["betrag"] < 0]
    if not ausgaben:
        return []
    schnitt = sum(ausgaben) / len(ausgaben)
    grenze = schnitt * faktor
    return sorted(
        (b for b in buchungen if b["betrag"] < 0 and abs(b["betrag"]) > grenze),
        key=lambda b: b["betrag"],
    )


# ====================================================================
# AUSGABE & EXPORT
# ====================================================================
def zeige_analyse(buchungen, fehler):
    """Gibt die komplette Analyse im Terminal aus."""
    einnahmen = sum(b["betrag"] for b in buchungen if b["betrag"] > 0)
    ausgaben = sum(-b["betrag"] for b in buchungen if b["betrag"] < 0)
    saldo = einnahmen - ausgaben

    von = min(b["datum"] for b in buchungen)
    bis = max(b["datum"] for b in buchungen)

    print(f"\n📄 Datei:     {CSV_DATEI.name}")
    print(f"📊 Buchungen: {len(buchungen)}  "
          f"({von:%d.%m.%Y} – {bis:%d.%m.%Y})")
    if fehler:
        print(f"⚠️  {len(fehler)} Zeilen übersprungen (fehlerhaft)")

    abschnitt("ÜBERBLICK")
    print(f"  {'Einnahmen':<28}{euro(einnahmen):>26}")
    print(f"  {'Ausgaben':<28}{euro(ausgaben):>26}")
    print("  " + "─" * (BREITE - 2))
    print(f"  {'SALDO':<28}{euro(saldo):>26}  {'🟢' if saldo >= 0 else '🔴'}")

    abschnitt("AUSGABEN NACH KATEGORIE")
    kategorien = auswertung_kategorien(buchungen)
    for kategorie, summe in sorted(kategorien.items(), key=lambda p: -p[1]):
        symbol = KATEGORIEN.get(kategorie, (None, SONSTIGES_SYMBOL))[1]
        anteil = summe / ausgaben if ausgaben else 0
        print(f"  {symbol} {kategorie:<14}{euro(summe):>14}  "
              f"{balken(anteil)} {anteil:>4.0%}")

    abschnitt("MONATSVERLAUF")
    monate = auswertung_monate(buchungen)
    groesste = max(abs(m["saldo"]) for m in monate.values()) or 1
    for monat, werte in monate.items():
        name = datetime.strptime(monat, "%Y-%m").strftime("%B")
        laenge = int(abs(werte["saldo"]) / groesste * 18)
        symbol = "🟢" if werte["saldo"] >= 0 else "🔴"
        print(f"  {name:<12}{euro(werte['saldo']):>13}  {symbol} {'█' * laenge}")

    abschnitt("AUFFÄLLIGKEITEN")
    groesste_ausgabe = min(buchungen, key=lambda b: b["betrag"])
    print(f"  🔴 Größte Ausgabe:  {groesste_ausgabe['empfaenger'][:24]} "
          f"({euro(abs(groesste_ausgabe['betrag']))}) am "
          f"{groesste_ausgabe['datum']:%d.%m.}")

    wiederkehrend = finde_wiederkehrende(buchungen)
    abo_summe = sum(w["gesamt"] for w in wiederkehrend.values())
    print(f"  🔁 Wiederkehrend:   {len(wiederkehrend)} erkannt")
    for name, info in sorted(wiederkehrend.items(),
                             key=lambda p: -p[1]["gesamt"])[:4]:
        print(f"     • {name[:26]:<28}{info['anzahl']:>2}x  "
              f"Ø {euro(info['durchschnitt'])}")
    print(f"  💸 Fixkosten ges.:  {euro(abo_summe)}")

    ausreisser = finde_ausreisser(buchungen)
    print(f"  ⚠️  Ausreißer:       {len(ausreisser)} Buchungen > 3× Ø")

    if einnahmen:
        sparquote = saldo / einnahmen
        print(f"  🐖 Sparquote:       {sparquote:>6.1%}")

    if fehler:
        abschnitt("ÜBERSPRUNGENE ZEILEN")
        for nr, grund in fehler[:5]:
            print(f"  Zeile {nr}: {grund[:60]}")

    return {"einnahmen": round(einnahmen, 2), "ausgaben": round(ausgaben, 2),
            "saldo": round(saldo, 2), "kategorien": kategorien,
            "monate": monate, "wiederkehrend": wiederkehrend,
            "ausreisser": len(ausreisser), "fehlerhafte_zeilen": len(fehler)}


def schreibe_export(ergebnis, buchungen):
    """Schreibt Bericht und JSON-Export."""
    bericht = ORDNER / "bericht.txt"
    zeilen = ["KONTOAUSZUG-ANALYSE", "=" * 50,
              f"Erstellt:   {datetime.now():%d.%m.%Y %H:%M}",
              f"Buchungen:  {len(buchungen)}",
              f"Einnahmen:  {euro(ergebnis['einnahmen'])}",
              f"Ausgaben:   {euro(ergebnis['ausgaben'])}",
              f"Saldo:      {euro(ergebnis['saldo'])}", "",
              "AUSGABEN NACH KATEGORIE", "-" * 50]
    for kategorie, summe in sorted(ergebnis["kategorien"].items(),
                                   key=lambda p: -p[1]):
        zeilen.append(f"{kategorie:<16}{euro(summe):>16}")
    bericht.write_text("\n".join(zeilen), encoding="utf-8")

    json_datei = ORDNER / "analyse.json"
    export = {k: v for k, v in ergebnis.items()}
    export["monate"] = {m: {k: round(v, 2) for k, v in werte.items()}
                        for m, werte in ergebnis["monate"].items()}
    json_datei.write_text(json.dumps(export, indent=2, ensure_ascii=False),
                          encoding="utf-8")

    return bericht, json_datei


# ====================================================================
# HAUPTPROGRAMM
# ====================================================================
def main():
    """Hauptprogramm."""
    kopfzeile("🏦  KONTOAUSZUG-ANALYSE  2026")

    if not CSV_DATEI.exists():
        erzeuge_testdaten(CSV_DATEI)
        print(f"\n  ℹ️  Testdatei erzeugt: {CSV_DATEI.name}")

    try:
        buchungen, fehler = lade_buchungen(CSV_DATEI)
    except FileNotFoundError as f:
        print(f"\n  ❌ {f}")
        return 1
    except PermissionError:
        print(f"\n  ❌ Kein Zugriff auf {CSV_DATEI}")
        return 1

    if not buchungen:
        print("\n  📭 Keine gültigen Buchungen gefunden.")
        return 1

    ergebnis = zeige_analyse(buchungen, fehler)
    bericht, json_datei = schreibe_export(ergebnis, buchungen)

    print(f"\n✅ Geschrieben: {bericht.name} + {json_datei.name}")
    print(f"📁 Ordner: {ORDNER}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
