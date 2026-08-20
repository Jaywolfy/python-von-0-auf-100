"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 21 · MUSTERLÖSUNGEN — Regex                               ║
╚══════════════════════════════════════════════════════════════════╝
"""
import re

TEXT = """
Bestellung BE-2026-4711 vom 15.03.2026
Kunde: Anna Müller, anna.mueller@beispiel.de, Tel. 0151-98765432
Lieferadresse: Bahnhofstr. 7a, 80331 München
Artikel: 3x Laptop (899,99 €), 2x Maus (25,50 €)
Gesamtbetrag: 2.750,97 €
Zahlung per IBAN DE12500105170648489890
Tracking: https://versand.example.com/track/XY123456789DE
Rückfragen an service@beispiel.de oder 089/1234567
Zweite Bestellung BE-2026-4712 vom 02.04.2026, Betrag 149,00 €
"""

print("=" * 62, "\nAUFGABE 1 🟢\n", "=" * 62)

zahlen = re.findall(r"\d+", TEXT)[:10]
gross = re.findall(r"\b[A-ZÄÖÜ][a-zäöüß]+", TEXT)[:8]
plz = re.findall(r"\b\d{5}\b", TEXT)
vier = re.findall(r"\b[A-Za-zÄÖÜäöüß]{4}\b", TEXT)

print(f"  a) Zahlen (erste 10):   {zahlen}")
print(f"  b) Großgeschrieben:     {gross}")
print(f"  c) Postleitzahlen:      {plz}")
print(f"  d) 4-Buchstaben-Wörter: {vier}")


print("\n" + "=" * 62, "\nAUFGABE 2 🟢\n", "=" * 62)

emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", TEXT)
urls = re.findall(r"https?://[^\s]+", TEXT)
print(f"  E-Mails: {emails}")
print(f"  URLs:    {urls}")


print("\n" + "=" * 62, "\nAUFGABE 3 🟡\n", "=" * 62)

betrag_muster = r"(\d{1,3}(?:\.\d{3})*,\d{2})\s*€"
betraege_text = re.findall(betrag_muster, TEXT)


def deutsche_zahl(text):
    """Wandelt '1.234,56' in 1234.56 um."""
    return float(text.replace(".", "").replace(",", "."))


betraege = [deutsche_zahl(b) for b in betraege_text]
print(f"  Gefunden: {betraege_text}")
print(f"  Als Zahl: {betraege}")
print(f"  Summe:    {sum(betraege):,.2f} €")


print("\n" + "=" * 62, "\nAUFGABE 4 🟡\n", "=" * 62)

muster = r"(?P<praefix>[A-Z]{2})-(?P<jahr>\d{4})-(?P<nummer>\d{4})"
for m in re.finditer(muster, TEXT):
    d = m.groupdict()
    print(f"  Bestellung {d['nummer']} aus dem Jahr {d['jahr']} "
          f"(Präfix {d['praefix']})")


print("\n" + "=" * 62, "\nAUFGABE 5 🟡\n", "=" * 62)

umgewandelt = re.sub(r"\b(\d{2})\.(\d{2})\.(\d{4})\b", r"\3-\2-\1", TEXT)
for zeile in umgewandelt.strip().splitlines():
    if "-" in zeile and any(c.isdigit() for c in zeile):
        print(f"  {zeile}")


print("\n" + "=" * 62, "\nAUFGABE 6 🟡\n", "=" * 62)

anonym = TEXT
anonym = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[E-MAIL]", anonym)
anonym = re.sub(r"\b0\d{2,4}[-/]\d{6,8}\b", "[TELEFON]", anonym)
anonym = re.sub(r"\bDE\d{20}\b", "[IBAN]", anonym)

for zeile in anonym.strip().splitlines():
    print(f"  {zeile}")


print("\n" + "=" * 62, "\nAUFGABE 7 🔴\n", "=" * 62)

positionen_muster = r"(\d+)x\s+([A-Za-zÄÖÜäöüß]+)\s+\((\d{1,3}(?:\.\d{3})*,\d{2})\s*€\)"
positionen = []
for menge, artikel, preis in re.findall(positionen_muster, TEXT):
    menge = int(menge)
    preis = deutsche_zahl(preis)
    positionen.append({"menge": menge, "artikel": artikel,
                       "preis": preis, "summe": round(menge * preis, 2)})

print(f"  {'Menge':>6}  {'Artikel':<14}{'Einzeln':>10}{'Summe':>12}")
print("  " + "-" * 44)
for p in positionen:
    print(f"  {p['menge']:>6}  {p['artikel']:<14}{p['preis']:>10.2f}{p['summe']:>12.2f}")
print("  " + "-" * 44)
print(f"  {'GESAMT':<24}{sum(p['summe'] for p in positionen):>18.2f}")


print("\n" + "=" * 62, "\nAUFGABE 8 🔴\n", "=" * 62)


def ist_gueltige_email(text):
    """Grobe Prüfung einer E-Mail-Adresse."""
    return bool(re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.]{2,}", text))


def ist_gueltige_plz(text):
    """Deutsche PLZ: 5 Ziffern, erste nicht 0."""
    return bool(re.fullmatch(r"[1-9]\d{4}", text))


def ist_gueltiges_datum(text):
    """Datum im Format TT.MM.JJJJ (grobe Bereichsprüfung)."""
    return bool(re.fullmatch(r"(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.\d{4}", text))


def ist_starkes_passwort(text):
    """Mindestens 8 Zeichen, Groß, Klein, Ziffer und Sonderzeichen."""
    if len(text) < 8:
        return False
    pruefungen = [r"[a-z]", r"[A-Z]", r"\d", r"[^\w\s]"]
    return all(re.search(p, text) for p in pruefungen)


tests = {
    "ist_gueltige_email": (ist_gueltige_email,
                           ["a@b.de", "max.mustermann@firma.co.uk", "x+y@mail.com"],
                           ["keinat.de", "@firma.de", "max@firma"]),
    "ist_gueltige_plz": (ist_gueltige_plz,
                         ["10115", "80331", "99999"],
                         ["01234", "1234", "123456"]),
    "ist_gueltiges_datum": (ist_gueltiges_datum,
                            ["26.07.2026", "01.01.2000", "31.12.1999"],
                            ["32.07.2026", "26.13.2026", "26.7.2026"]),
    "ist_starkes_passwort": (ist_starkes_passwort,
                             ["Sonne2026!", "Ab3$defgh", "P@ssw0rt1"],
                             ["kurz1!", "keinesonderzeichen1A", "ALLESGROSS1!"]),
}

for name, (funktion, gute, schlechte) in tests.items():
    print(f"\n  {name}:")
    for wert in gute:
        print(f"    ✅ {wert:<26} -> {funktion(wert)}")
    for wert in schlechte:
        print(f"    ❌ {wert:<26} -> {funktion(wert)}")


print("\n" + "=" * 62, "\nAUFGABE 9 ⭐\n", "=" * 62)

MUSTER = {
    "emails":   (r"[\w.+-]+@[\w-]+\.[\w.]+", "📧", "E-Mails"),
    "telefone": (r"\b0\d{2,4}[-/]\d{6,8}\b", "📞", "Telefon"),
    "daten":    (r"\b\d{1,2}\.\d{1,2}\.\d{4}\b", "📅", "Daten"),
    "betraege": (r"\d{1,3}(?:\.\d{3})*,\d{2}\s*€", "💶", "Beträge"),
    "plz":      (r"\b[1-9]\d{4}\b", "🏠", "PLZ"),
    "urls":     (r"https?://[^\s]+", "🔗", "URLs"),
    "ibans":    (r"\bDE\d{20}\b", "🏦", "IBAN"),
    "bestellnr": (r"\b[A-Z]{2}-\d{4}-\d{4}\b", "📄", "Bestell-Nr"),
}


def extrahiere_alles(text):
    """Extrahiert alle bekannten Datentypen aus einem Text."""
    return {schluessel: re.findall(muster, text)
            for schluessel, (muster, _, _) in MUSTER.items()}


def zeige_bericht(daten):
    """Gibt die extrahierten Daten formatiert aus."""
    print("  " + "═" * 58)
    print("     EXTRAHIERTE DATEN")
    print("  " + "═" * 58)
    for schluessel, treffer in daten.items():
        _, symbol, name = MUSTER[schluessel]
        werte = ", ".join(str(t) for t in treffer)
        if len(werte) > 40:
            werte = werte[:37] + "..."
        print(f"  {symbol} {name:<12}{len(treffer):>3}  →  {werte}")
    print("  " + "═" * 58)


zeige_bericht(extrahiere_alles(TEXT))

print("\n🎉 Modul 21 geschafft! Regex ist deine Text-Superkraft. 🔍")
