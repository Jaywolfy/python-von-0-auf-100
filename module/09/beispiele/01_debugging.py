"""
Modul 09 - Beispiel 1: Debugging-Techniken

Diese Datei zeigt, WIE man einen Fehler findet - nicht nur, dass er da ist.
"""

# ====================================================================
# TECHNIK 1: print-Debugging mit {x=}
# ====================================================================
print("=" * 60)
print("TECHNIK 1: print-Debugging")
print("=" * 60)


def durchschnitt_kaputt(werte):
    """Diese Funktion hat einen Logikfehler. Wo?"""
    summe = 0
    for w in werte:
        summe = w              # 🐛 sollte += sein!
    return summe / len(werte)


def durchschnitt_mit_debug(werte):
    """Dieselbe Funktion - mit Debug-Ausgaben."""
    print(f"  [DEBUG] Eingabe: {werte=}")
    print(f"  [DEBUG] Typ: {type(werte).__name__}, Länge: {len(werte)}")

    summe = 0
    for i, w in enumerate(werte):
        summe = w              # der Fehler
        print(f"  [DEBUG] Schritt {i}: {w=}, {summe=}")   # ← hier sieht man es!

    ergebnis = summe / len(werte)
    print(f"  [DEBUG] Rückgabe: {ergebnis}")
    return ergebnis


zahlen = [10, 20, 30, 40]
print(f"\nErwartet:  {sum(zahlen) / len(zahlen)}")
print(f"Bekommen:  {durchschnitt_kaputt(zahlen)}\n")

print("Mit Debug-Ausgaben sieht man den Fehler sofort:")
durchschnitt_mit_debug(zahlen)
print("  → summe wird ÜBERSCHRIEBEN statt aufaddiert. Fix: summe += w\n")


def durchschnitt_richtig(werte):
    """Korrigierte Version."""
    summe = 0
    for w in werte:
        summe += w
    return summe / len(werte)


print(f"Repariert: {durchschnitt_richtig(zahlen)} ✅")


# ====================================================================
# TECHNIK 2: Typen prüfen
# ====================================================================
print("\n" + "=" * 60)
print("TECHNIK 2: Typen prüfen")
print("=" * 60)

eingabe = "42"          # z.B. aus input() oder einer Datei

print(f"  {eingabe=}")
print(f"  type: {type(eingabe).__name__}")
# print(eingabe + 1)   ->  TypeError!
print(f"  eingabe + 1 würde krachen. Nach int(): {int(eingabe) + 1} ✅")


# ====================================================================
# TECHNIK 3: Zwischenschritte sichtbar machen
# ====================================================================
print("\n" + "=" * 60)
print("TECHNIK 3: Zwischenschritte prüfen")
print("=" * 60)

zeile = "Anna; 30 ;Berlin"

print(f"  1. Roh:        {zeile!r}")
teile = zeile.split(";")
print(f"  2. Nach split: {teile}")
print("     ⚠️ Achtung: ' 30 ' hat Leerzeichen!")
sauber = [t.strip() for t in teile]
print(f"  3. Nach strip: {sauber}")
print(f"  4. Alter als Zahl: {int(sauber[1])} ✅")


# ====================================================================
# TECHNIK 4: assert - Annahmen prüfen
# ====================================================================
print("\n" + "=" * 60)
print("TECHNIK 4: assert (Annahmen absichern)")
print("=" * 60)


def teile(a, b):
    """Teilt a durch b."""
    assert b != 0, "b darf nicht 0 sein!"     # bricht mit klarer Meldung ab
    return a / b


print(f"  teile(10, 2) = {teile(10, 2)}")
try:
    teile(10, 0)
except AssertionError as fehler:
    print(f"  teile(10, 0) -> AssertionError: {fehler}")
print("  💡 assert sagt dir GENAU, welche Annahme verletzt wurde.")


# ====================================================================
# DEBUGGER-ÜBUNG
# ====================================================================
print("\n" + "=" * 60)
print("DEBUGGER-ÜBUNG (in VS Code)")
print("=" * 60)
print("""
  1. Setze einen Breakpoint (F9) in die Zeile 'summe += zahl' unten
  2. Drücke F5
  3. Schau links ins Panel "Variables"
  4. Drücke mehrfach F10 und beobachte, wie summe wächst
  5. Füge im Panel "Watch" den Ausdruck  summe / (i+1)  hinzu
""")


def debugger_spielwiese():
    """Zum Ausprobieren mit dem Debugger."""
    zahlen = [5, 12, 8, 3, 20]
    summe = 0
    groesste = zahlen[0]

    for i, zahl in enumerate(zahlen):
        summe += zahl                    # ← 🔴 Breakpoint hierhin!
        if zahl > groesste:
            groesste = zahl

    return summe, groesste, summe / len(zahlen)


s, g, d = debugger_spielwiese()
print(f"  Ergebnis: Summe={s}, Größte={g}, Ø={d:.1f}")
