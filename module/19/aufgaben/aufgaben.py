"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 19 · AUFGABEN — Sauberer Code                             ║
╠══════════════════════════════════════════════════════════════════╣
║  Jeder Block enthält funktionierenden, aber HÄSSLICHEN Code.     ║
║  Deine Aufgabe: aufräumen, ohne das Verhalten zu ändern.         ║
║                                                                  ║
║  Bonus: pip install ruff  &&  ruff check aufgaben.py             ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# AUFGABE 1 🟢 - Namen verbessern
# ══════════════════════════════════════════════════════════════════
# Benenne alles sinnvoll um und formatiere nach PEP 8.
#
#   def calc(l,t=0.19):
#       s=0
#       for i in l:
#           s=s+i
#       return s*(1+t)
#
#   d={"a":1,"b":2}
#   f=True
#   tmp=calc([10,20,30])

# 👉 Deine saubere Version:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 2 🟢 - Type Hints ergänzen
# ══════════════════════════════════════════════════════════════════
# Ergänze Type Hints und Docstrings:
#
#   def filtere(namen, minlaenge=3):
#       return [n for n in namen if len(n) >= minlaenge]
#
#   def finde_person(personen, name):
#       for p in personen:
#           if p["name"] == name:
#               return p
#       return None
#
#   def statistik(zahlen):
#       return min(zahlen), max(zahlen), sum(zahlen)/len(zahlen)

# 👉 Deine Version:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 3 🟡 - Magische Zahlen
# ══════════════════════════════════════════════════════════════════
# Ersetze alle magischen Zahlen durch benannte Konstanten:
#
#   def berechne(sekunden):
#       t = sekunden // 86400
#       h = (sekunden % 86400) // 3600
#       m = (sekunden % 3600) // 60
#       s = sekunden % 60
#       return f"{t}d {h}h {m}m {s}s"
#
#   def preis_mit_steuer(netto):
#       if netto > 10000:
#           return netto * 1.19 * 0.95
#       return netto * 1.19

# 👉 Deine Version:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 4 🟡 - Verschachtelung abflachen
# ══════════════════════════════════════════════════════════════════
# Baue das mit Guard Clauses um (max. 1 Einrückungsebene im Kern):
#
#   def darf_bestellen(benutzer):
#       if benutzer is not None:
#           if benutzer["aktiv"]:
#               if not benutzer["gesperrt"]:
#                   if benutzer["guthaben"] > 0:
#                       if benutzer["alter"] >= 18:
#                           return True
#                       else:
#                           return False
#                   else:
#                       return False
#               else:
#                   return False
#           else:
#               return False
#       else:
#           return False

# 👉 Deine Version:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 5 🟡 - Zu lange Funktion aufteilen
# ══════════════════════════════════════════════════════════════════
# Teile diese Funktion in mindestens 4 kleine Funktionen auf:
#
#   def verarbeite_bestellung(bestellung):
#       # validieren
#       if not bestellung.get("kunde"):
#           return {"fehler": "Kunde fehlt"}
#       if not bestellung.get("artikel"):
#           return {"fehler": "Keine Artikel"}
#       # summe berechnen
#       summe = 0
#       for a in bestellung["artikel"]:
#           summe += a["preis"] * a["menge"]
#       # rabatt
#       if summe > 500:
#           summe = summe * 0.9
#       elif summe > 200:
#           summe = summe * 0.95
#       # versand
#       versand = 0 if summe > 100 else 4.99
#       # steuer
#       brutto = (summe + versand) * 1.19
#       # ausgabe
#       print("Kunde:", bestellung["kunde"])
#       print("Artikel:", len(bestellung["artikel"]))
#       print("Netto:", round(summe, 2))
#       print("Versand:", versand)
#       print("Brutto:", round(brutto, 2))
#       return {"brutto": round(brutto, 2)}

# 👉 Deine Version:



# ══════════════════════════════════════════════════════════════════
# AUFGABE 6 🔴 - Copy-Paste eliminieren
# ══════════════════════════════════════════════════════════════════
#   def report_technik(daten):
#       print("=" * 40); print("TECHNIK"); print("=" * 40)
#       gesamt = 0
#       for d in daten:
#           if d["kategorie"] == "Technik":
#               print(f"{d['name']:<20}{d['preis']:>10.2f}")
#               gesamt += d["preis"]
#       print("-" * 40); print(f"{'SUMME':<20}{gesamt:>10.2f}")
#
#   def report_moebel(daten):
#       print("=" * 40); print("MÖBEL"); print("=" * 40)
#       gesamt = 0
#       for d in daten:
#           if d["kategorie"] == "Möbel":
#               print(f"{d['name']:<20}{d['preis']:>10.2f}")
#               gesamt += d["preis"]
#       print("-" * 40); print(f"{'SUMME':<20}{gesamt:>10.2f}")

# 👉 Deine Version (EINE Funktion):



# ══════════════════════════════════════════════════════════════════
# AUFGABE 7 ⭐ BONUS - Komplett-Refactoring
# ══════════════════════════════════════════════════════════════════
# Räum diesen Code komplett auf: Namen, Typen, Docstrings, Struktur,
# Konstanten, Fehlerbehandlung. Das Verhalten muss gleich bleiben.
#
#   import csv
#   def go(f):
#       r=[]
#       with open(f) as x:
#           c=csv.reader(x,delimiter=";")
#           next(c)
#           for l in c:
#               if len(l)>3:
#                   try:
#                       p=float(l[3].replace(",","."))
#                       if p>0:
#                           r.append({"n":l[0],"p":p,"t":p*1.19})
#                   except:
#                       pass
#       return r

# 👉 Deine Version:



print("✅ Fertig? Vergleiche mit den Lösungen - und lass ruff drüberlaufen!")
