"""
Modul 12 - Beispiel: Die Standardbibliothek + eigenes Modul importieren
"""
import math
import random
from datetime import datetime, date, timedelta
from collections import Counter, defaultdict
from itertools import combinations, product
import statistics

# Eigenes Modul importieren - der __main__-Block dort läuft NICHT mit!
from werkzeuge import formatiere_euro, fortschrittsbalken, trennlinie

print(trennlinie("="))
print("EIGENES MODUL IMPORTIERT")
print(trennlinie("="))
print(f"  {formatiere_euro(1234567.891)}")
print(f"  {fortschrittsbalken(0.42)}")
print("  💡 Der Selbsttest aus werkzeuge.py lief NICHT mit. Genau so soll es sein.")

# ====================================================================
print("\n" + trennlinie("=") + "\n📅 DATETIME\n" + trennlinie("="))

heute = date.today()
jetzt = datetime.now()

print(f"  Heute:              {heute}")
print(f"  Deutsch formatiert: {heute.strftime('%d.%m.%Y')}")
print(f"  Mit Wochentag:      {heute.strftime('%A, %d. %B %Y')}")
print(f"  Uhrzeit:            {jetzt.strftime('%H:%M:%S')}")

print(f"\n  Morgen:             {heute + timedelta(days=1)}")
print(f"  In 2 Wochen:        {heute + timedelta(weeks=2)}")
print(f"  Vor 30 Tagen:       {heute - timedelta(days=30)}")

weihnachten = date(heute.year, 12, 24)
if weihnachten < heute:
    weihnachten = date(heute.year + 1, 12, 24)
print(f"\n  Tage bis Weihnachten: {(weihnachten - heute).days} 🎄")

geburtstag = datetime.strptime("15.03.1998", "%d.%m.%Y").date()
alter_tage = (heute - geburtstag).days
print(f"  Text -> Datum: {geburtstag}, das sind {alter_tage:,} Tage")

# ====================================================================
print("\n" + trennlinie("=") + "\n🎲 RANDOM\n" + trennlinie("="))

random.seed(42)      # damit die Ausgabe reproduzierbar ist
print(f"  Würfelwurf:        {random.randint(1, 6)}")
print(f"  5 Würfe:           {[random.randint(1, 6) for _ in range(5)]}")
print(f"  Zufallszahl 0-1:   {random.random():.4f}")
print(f"  Zufälliges Element:{random.choice(['Kopf', 'Zahl'])}")
print(f"  3 aus 10 (ohne Wdh.): {random.sample(range(1, 11), 3)}")

karten = ["Ass", "König", "Dame", "Bube"]
random.shuffle(karten)
print(f"  Gemischt:          {karten}")

# ====================================================================
print("\n" + trennlinie("=") + "\n📦 COLLECTIONS\n" + trennlinie("="))

satz = "Python ist toll und Python ist einfach und Python ist schnell"
woerter = satz.lower().split()

zaehler = Counter(woerter)
print(f"  Counter:           {dict(zaehler)}")
print(f"  Top 3:             {zaehler.most_common(3)}")
print(f"  Buchstaben:        {Counter('banane').most_common()}")
print("  💡 Das ersetzt das ganze Zähl-Muster aus Modul 07 durch EINE Zeile!")

gruppen = defaultdict(list)
for wort in set(woerter):
    gruppen[len(wort)].append(wort)
print(f"\n  Nach Länge gruppiert:")
for laenge in sorted(gruppen):
    print(f"    {laenge} Buchstaben: {sorted(gruppen[laenge])}")

# ====================================================================
print("\n" + trennlinie("=") + "\n🔁 ITERTOOLS\n" + trennlinie("="))

print(f"  combinations([1,2,3], 2): {list(combinations([1, 2, 3], 2))}")
print(f"  product('ab', [1,2]):     {list(product('ab', [1, 2]))}")

# ====================================================================
print("\n" + trennlinie("=") + "\n🧮 MATH & STATISTICS\n" + trennlinie("="))

werte = [4, 8, 15, 16, 23, 42]
print(f"  Werte:      {werte}")
print(f"  Mittelwert: {statistics.mean(werte):.2f}")
print(f"  Median:     {statistics.median(werte)}")
print(f"  Std.abw.:   {statistics.stdev(werte):.2f}")
print()
print(f"  math.sqrt(144):  {math.sqrt(144)}")
print(f"  math.floor(3.9): {math.floor(3.9)}")
print(f"  math.ceil(3.1):  {math.ceil(3.1)}")
print(f"  math.pi:         {math.pi:.6f}")

print("\n💡 Bevor du etwas selbst baust: schau in die Standardbibliothek!")
print("   https://docs.python.org/3/library/")
