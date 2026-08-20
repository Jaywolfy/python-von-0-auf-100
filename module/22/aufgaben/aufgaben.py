"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 22 · AUFGABEN — APIs                                      ║
╠══════════════════════════════════════════════════════════════════╣
║  Alle Aufgaben lassen sich MIT den Demo-Daten unten lösen.       ║
║  Wenn du Internet hast: pip install requests und echte Aufrufe!  ║
╚══════════════════════════════════════════════════════════════════╝
"""

# --- Demo-Antworten (simulieren echte APIs) ------------------------
DEMO_BENUTZER = [
    {"id": 1, "name": "Leanne Graham", "username": "Bret",
     "email": "sincere@april.biz",
     "address": {"street": "Kulas Light", "city": "Gwenborough", "zipcode": "92998"},
     "company": {"name": "Romaguera-Crona"}},
    {"id": 2, "name": "Ervin Howell", "username": "Antonette",
     "email": "shanna@melissa.tv",
     "address": {"street": "Victor Plains", "city": "Wisokyburgh", "zipcode": "90566"},
     "company": {"name": "Deckow-Crist"}},
    {"id": 3, "name": "Clementine Bauch", "username": "Samantha",
     "email": "nathan@yesenia.net",
     "address": {"street": "Douglas Extension", "city": "McKenziehaven", "zipcode": "59590"},
     "company": {"name": "Romaguera-Jacobson"}},
]

DEMO_BEITRAEGE = [
    {"userId": 1, "id": 1, "title": "Erster Beitrag", "body": "Text " * 20},
    {"userId": 1, "id": 2, "title": "Zweiter Beitrag", "body": "Text " * 15},
    {"userId": 2, "id": 3, "title": "Dritter Beitrag", "body": "Text " * 30},
    {"userId": 3, "id": 4, "title": "Vierter Beitrag", "body": "Text " * 10},
    {"userId": 1, "id": 5, "title": "Fünfter Beitrag", "body": "Text " * 25},
]

DEMO_KURSE = {"base": "EUR", "date": "2026-07-25",
              "rates": {"USD": 1.0842, "GBP": 0.8531, "CHF": 0.9612,
                        "JPY": 168.44, "PLN": 4.2810, "SEK": 11.234}}

DEMO_WETTER_STAEDTE = {
    "Berlin": {"temp": 24.3, "wind": 12.4, "feuchte": 58},
    "Hamburg": {"temp": 21.8, "wind": 18.9, "feuchte": 72},
    "München": {"temp": 26.7, "wind": 8.1, "feuchte": 45},
    "Köln": {"temp": 23.1, "wind": 14.2, "feuchte": 63},
}


# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - JSON-Antwort auswerten
# ══════════════════════════════════════════════════════════════════
# Gib aus DEMO_BENUTZER aus:
#   a) Alle Namen
#   b) Alle E-Mail-Adressen
#   c) Alle Städte
#   d) Eine formatierte Tabelle: Name | Stadt | Firma

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Verschachtelt zugreifen
# ══════════════════════════════════════════════════════════════════
# Gib für den ersten Benutzer aus:
#   Straße, PLZ, Stadt, Firmenname
# ⚠️ Benutze .get() mit Standardwerten - echte APIs liefern nicht
#    immer alle Felder!

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Daten verknüpfen
# ══════════════════════════════════════════════════════════════════
# Verknüpfe DEMO_BENUTZER und DEMO_BEITRAEGE über userId/id.
# Gib für jeden Benutzer aus:
#   Leanne Graham (3 Beiträge): Erster Beitrag, Zweiter Beitrag, ...

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Robuste Abruf-Funktion
# ══════════════════════════════════════════════════════════════════
# Schreib hole_daten(url, params=None, demo=None), die:
#   - im Offline-Modus die Demo-Daten zurückgibt
#   - sonst requests.get mit timeout=10 benutzt
#   - raise_for_status() aufruft
#   - Timeout, HTTPError, ConnectionError und ValueError abfängt
#   - bei Fehlern None zurückgibt und eine hilfreiche Meldung ausgibt

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Währungsrechner
# ══════════════════════════════════════════════════════════════════
# Schreib rechne_um(betrag, ziel_waehrung, kurse) und gib aus:
#   250 EUR = 271.05 USD
# Gib danach eine Tabelle für alle Währungen aus DEMO_KURSE aus,
# sortiert nach Kurs.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🔴 - Wetter-Dashboard
# ══════════════════════════════════════════════════════════════════
# Baue aus DEMO_WETTER_STAEDTE ein Dashboard:
#
#   ╔══════════════════════════════════════════╗
#   ║          WETTER-ÜBERSICHT ⛅              ║
#   ╠══════════════════════════════════════════╣
#   ║ München    26.7 °C  🔥  ████████████████ ║
#   ║ Berlin     24.3 °C  🌤️  ██████████████   ║
#   ...
#   ╠══════════════════════════════════════════╣
#   ║ Wärmste: München | Kälteste: Hamburg     ║
#   ║ Durchschnitt: 24.0 °C                    ║
#   ╚══════════════════════════════════════════╝
#
# Sortiert nach Temperatur, mit Balken und Emojis.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 🔴 - Statuscodes behandeln
# ══════════════════════════════════════════════════════════════════
# Schreib behandle_status(code), die für jeden Code eine sinnvolle
# Handlungsempfehlung als String zurückgibt:
#   200 -> "OK - weiter"
#   401 -> "API-Key prüfen"
#   429 -> "Rate Limit - 60 Sekunden warten"
#   500 -> "Serverfehler - später erneut versuchen"
#   ... (mindestens 8 Codes)
# Teste mit einer Liste von Codes.

# 👉 Dein Code:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 8 ⭐ BONUS - Zwischenspeicher (Cache)
# ══════════════════════════════════════════════════════════════════
# Schreib eine Funktion hole_mit_cache(url, cache_datei, max_alter_min=60):
#   - existiert die Cache-Datei und ist jünger als max_alter_min:
#     Daten aus der Datei laden (und das melden)
#   - sonst: neu abrufen (bzw. Demo-Daten) und speichern
# 💡 Tipp: pfad.stat().st_mtime und time.time()
# Das spart echte API-Anfragen - und ist gute Etikette. 🤝

# 👉 Dein Code:



print("\n✅ Fertig? Ab zu den Lösungen!")
