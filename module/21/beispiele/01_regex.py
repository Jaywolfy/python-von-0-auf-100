"""
Modul 21 - Beispiel: Reguläre Ausdrücke

💡 Kopier die Muster nach https://regex101.com (Flavor: Python) -
   dort wird dir jedes Zeichen erklärt.
"""
import re

TEXT = """
Sehr geehrte Damen und Herren,

anbei die Rechnung Nr. RE-2026-0815 vom 26.07.2026.
Rechnungsbetrag: 1.234,56 € (netto 1.037,45 €).
Zahlbar bis 09.08.2026 auf das Konto DE89370400440532013000.

Bei Rückfragen: buchhaltung@beispiel-firma.de oder +49 151 12345678.
Alternativ: max.mustermann@firma.co.uk

Unsere Adresse: Hauptstraße 42, 10115 Berlin
Weitere Infos: https://beispiel-firma.de/rechnungen?id=815

Mit freundlichen Grüßen
"""

zeile = "-" * 62


def zeige(titel, muster, treffer):
    print(f"\n{titel}")
    print(f"  Muster: {muster}")
    print(f"  Treffer ({len(treffer)}): {treffer}")


# ====================================================================
print("=" * 62, "\n1. ZEICHENKLASSEN & QUANTOREN\n", "=" * 62)

zeige("Alle Zahlenfolgen", r"\d+", re.findall(r"\d+", TEXT)[:8])
zeige("Postleitzahl (genau 5 Ziffern, mit Wortgrenzen)",
      r"\b\d{5}\b", re.findall(r"\b\d{5}\b", TEXT))
zeige("Wörter mit Großbuchstaben am Anfang",
      r"\b[A-ZÄÖÜ]\w+", re.findall(r"\b[A-ZÄÖÜ]\w+", TEXT)[:8])

# ====================================================================
print("\n" + "=" * 62, "\n2. PRAKTISCHE MUSTER\n", "=" * 62)

MUSTER = {
    "📧 E-Mail":   r"[\w.+-]+@[\w-]+\.[\w.]+",
    "📅 Datum":    r"\b\d{1,2}\.\d{1,2}\.\d{4}\b",
    "💶 Betrag":   r"\d{1,3}(?:\.\d{3})*,\d{2}\s*€",
    "🏦 IBAN":     r"\bDE\d{20}\b",
    "🔗 URL":      r"https?://[^\s]+",
    "🏠 PLZ":      r"\b\d{5}\b",
    "📄 Rech.-Nr": r"\bRE-\d{4}-\d{4}\b",
    "📞 Telefon":  r"\+\d{2}\s\d{3}\s\d{8}",
}

for name, muster in MUSTER.items():
    treffer = re.findall(muster, TEXT)
    print(f"  {name:<14} {len(treffer)}  →  {treffer}")

# ====================================================================
print("\n" + "=" * 62, "\n3. GRUPPEN\n", "=" * 62)

datum_muster = r"(\d{1,2})\.(\d{1,2})\.(\d{4})"
treffer = re.search(datum_muster, TEXT)

print(f"  group(0) (alles): {treffer.group(0)}")
print(f"  group(1) (Tag):   {treffer.group(1)}")
print(f"  group(2) (Monat): {treffer.group(2)}")
print(f"  group(3) (Jahr):  {treffer.group(3)}")
print(f"  groups():         {treffer.groups()}")

print("\n  Mit BENANNTEN Gruppen (viel lesbarer):")
benannt = r"(?P<tag>\d{1,2})\.(?P<monat>\d{1,2})\.(?P<jahr>\d{4})"
for m in re.finditer(benannt, TEXT):
    d = m.groupdict()
    print(f"    {d}  →  ISO: {d['jahr']}-{d['monat']:0>2}-{d['tag']:0>2}")

# ====================================================================
print("\n" + "=" * 62, "\n4. ERSETZEN mit re.sub\n", "=" * 62)

# Datumsformat umbauen: 26.07.2026 -> 2026-07-26
iso = re.sub(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", r"\3-\2-\1", "26.07.2026")
print(f"  Datum umformatieren:  26.07.2026  →  {iso}")

# Sensible Daten schwärzen
geschwaerzt = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[E-MAIL ENTFERNT]",
                     "Kontakt: anna@firma.de und bernd@firma.de")
print(f"  Anonymisieren:        {geschwaerzt}")

# Mehrfache Leerzeichen normalisieren
normalisiert = re.sub(r"\s+", " ", "zu    viel   Platz")
print(f"  Leerraum normalisieren: {normalisiert!r}")

# Mit einer Funktion als Ersatz
def verdopple(m):
    return str(int(m.group()) * 2)

verdoppelt = re.sub(r"\d+", verdopple, "a1 b2 c3")
print(f"  Zahlen verdoppeln:    {verdoppelt}")

# ====================================================================
print("\n" + "=" * 62, "\n5. GIERIG vs. GENÜGSAM\n", "=" * 62)

html = "<b>fett</b> und <i>kursiv</i>"
print(f"  Text:            {html}")
gierig = re.findall(r"<.+>", html)
genuegsam = re.findall(r"<.+?>", html)
print(f"  r'<.+>'  gierig:  {gierig}")
print(f"  r'<.+?>' genügsam:{genuegsam}")
print("  💡 Das ? nach dem Quantor macht ihn genügsam.")

# ====================================================================
print("\n" + "=" * 62, "\n6. FLAGS\n", "=" * 62)

ohne = re.findall(r"rechnung", TEXT)
mit = re.findall(r"rechnung", TEXT, re.IGNORECASE)
print(f"  ohne IGNORECASE: {ohne}")
print(f"  mit  IGNORECASE: {mit}")

log = "INFO start\nERROR kaputt\nINFO ende\nERROR nochmal"
ohne_ml = re.findall(r"^ERROR.*", log)
mit_ml = re.findall(r"^ERROR.*", log, re.MULTILINE)
print(f"  ^ERROR ohne MULTILINE: {ohne_ml}")
print(f"  ^ERROR mit  MULTILINE: {mit_ml}")

# ====================================================================
print("\n" + "=" * 62, "\n7. 🌍 REALBEISPIEL: Logdatei auswerten\n", "=" * 62)

LOG = """2026-07-20 08:15:32 INFO  [auth] Benutzer anna angemeldet
2026-07-20 08:16:01 ERROR [db] Verbindung fehlgeschlagen nach 30s
2026-07-20 09:02:11 WARN  [api] Antwortzeit 2400ms
2026-07-21 07:45:00 ERROR [db] Verbindung fehlgeschlagen nach 30s
2026-07-21 10:00:00 INFO  [auth] Benutzer bernd angemeldet"""

muster = (r"(?P<datum>\d{4}-\d{2}-\d{2})\s+"
          r"(?P<zeit>\d{2}:\d{2}:\d{2})\s+"
          r"(?P<level>\w+)\s+"
          r"\[(?P<modul>\w+)\]\s+"
          r"(?P<meldung>.+)")

eintraege = [m.groupdict() for m in re.finditer(muster, LOG)]

print(f"  {'Datum':<12}{'Zeit':<10}{'Level':<8}{'Modul':<8}Meldung")
print("  " + "-" * 74)
for e in eintraege:
    symbol = {"ERROR": "🔴", "WARN": "🟡", "INFO": "  "}.get(e["level"], "  ")
    print(f"  {e['datum']:<12}{e['zeit']:<10}{symbol}{e['level']:<6}"
          f"{e['modul']:<8}{e['meldung'][:34]}")

fehler = [e for e in eintraege if e["level"] == "ERROR"]
print(f"\n  {len(fehler)} Fehler gefunden, alle aus Modul "
      f"'{fehler[0]['modul']}' 🔴")

print("""
  💡 Aus 5 unstrukturierten Textzeilen wurden 5 strukturierte Datensätze -
     mit EINEM Muster. Das ist die Superkraft von Regex.
""")
