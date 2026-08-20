"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 01 · MUSTERLÖSUNGEN                                       ║
║  ⛔ Erst nach 15 Minuten eigenem Versuch öffnen!                 ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

stadt = "Hamburg"
einwohner = 1900000
temperatur = 18.5
regnet = True

print(stadt, einwohner, temperatur, regnet)


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

print(stadt, "hat den Typ", type(stadt))
print(einwohner, "hat den Typ", type(einwohner))
print(temperatur, "hat den Typ", type(temperatur))
print(regnet, "hat den Typ", type(regnet))


print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)

punkte = 0
print("Start:      ", punkte)

punkte += 10
print("+10:        ", punkte)

punkte += 25
print("+25:        ", punkte)

punkte -= 5
print("-5:         ", punkte)

punkte *= 2
print("verdoppelt: ", punkte)


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)

erster = "Gold"
zweiter = "Silber"
print("Vorher: ", erster, "|", zweiter)

erster, zweiter = zweiter, erster
print("Nachher:", erster, "|", zweiter)


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

preis_text = "19.99"
menge_text = "3"

preis = float(preis_text)     # String -> float
menge = int(menge_text)       # String -> int
gesamtpreis = preis * menge

print("Gesamtpreis:", gesamtpreis)
print("Gesamtpreis: ", round(gesamtpreis, 2), " €", sep="")   # schöner


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)

monatsgehalt_euro = 1500
mehrwertsteuersatz = 0.19
ist_angemeldet = True
anzahl_artikel_warenkorb = 25

print("Gehalt:          ", monatsgehalt_euro)
print("MwSt-Satz:       ", mehrwertsteuersatz)
print("Angemeldet:      ", ist_angemeldet)
print("Artikel im Korb: ", anzahl_artikel_warenkorb)
print("\n💡 Der Code ist jetzt ohne Kommentare verständlich - das ist das Ziel.")


print("\n" + "=" * 60, "\nAUFGABE 7 🔴 - Vorhersagen\n", "=" * 60)

# print(5 + 3)          -> 8            Addition
# print("5" + "3")      -> 53           Verkettung von Strings
# print("5" * 3)        -> 555          String 3x wiederholt
# print(5 * "3")        -> 333          gleiche Sache, andere Reihenfolge
# print(int("5") + 3)   -> 8            erst umwandeln, dann addieren
# print(5 + 3.0)        -> 8.0          int + float ergibt IMMER float
# print(type(5 + 3.0))  -> <class 'float'>
# print(10 / 2)         -> 5.0          "/" ergibt IMMER float!
# print(type(10 / 2))   -> <class 'float'>   <- überrascht viele
# print(int(-3.7))      -> -3           schneidet Richtung 0 ab
# print(round(-3.7))    -> -4           rundet korrekt
# print(bool(""))       -> False        leerer String ist "falsy"
# print("5" + 3)        -> TypeError!   str + int geht nicht

print(5 + 3)
print("5" + "3")
print("5" * 3)
print(5 * "3")
print(int("5") + 3)
print(5 + 3.0)
print(type(5 + 3.0))
print(10 / 2)
print(type(10 / 2))
print(int(-3.7))
print(round(-3.7))
print(bool(""))
# print("5" + 3)   <- absichtlich auskommentiert, wirft TypeError


print("\n" + "=" * 60, "\nAUFGABE 8 ⭐\n", "=" * 60)

anzahl_artikel_a = 3
preis_artikel_a = 12.50
anzahl_artikel_b = 2
preis_artikel_b = 7.90
steuersatz = 0.19

summe_a = anzahl_artikel_a * preis_artikel_a
summe_b = anzahl_artikel_b * preis_artikel_b
nettosumme = summe_a + summe_b
steuerbetrag = nettosumme * steuersatz
bruttosumme = nettosumme + steuerbetrag

print("Artikel A:     ", round(summe_a, 2), "€")
print("Artikel B:     ", round(summe_b, 2), "€")
print("-" * 30)
print("Nettosumme:    ", round(nettosumme, 2), "€")
print("MwSt (19 %):   ", round(steuerbetrag, 2), "€")
print("Bruttosumme:   ", round(bruttosumme, 2), "€")

print("\n💡 Jede Zwischenvariable hat einen Namen, der ihren Inhalt erklärt.")
print("   Das ist der Unterschied zwischen Code und LESBAREM Code.")

print("\n🎉 Modul 01 geschafft!")
