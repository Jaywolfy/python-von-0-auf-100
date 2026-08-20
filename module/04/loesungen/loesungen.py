"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 04 · MUSTERLÖSUNGEN — Bedingungen                         ║
║  ⛔ Erst nach eigenem Versuch!                                    ║
╚══════════════════════════════════════════════════════════════════╝
"""

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)

zahl = 47
if zahl % 2 == 0:
    print(f"{zahl} ist gerade")
else:
    print(f"{zahl} ist ungerade")


print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)

alter = 16
if alter >= 18:
    print("Volljährig")
elif alter >= 14:
    print("Jugendlich")
else:
    print("Kind")


print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)

a, b, c = 17, 42, 23

if a >= b and a >= c:
    groesste = a
elif b >= a and b >= c:
    groesste = b
else:
    groesste = c

print(f"Die größte von {a}, {b}, {c} ist {groesste}")
print(f"(Zur Kontrolle mit max(): {max(a, b, c)})")


print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)

punkte = 87

if punkte < 0 or punkte > 100:
    print(f"Ungültige Punktzahl: {punkte}")
elif punkte >= 92:
    note = 1
elif punkte >= 81:
    note = 2
elif punkte >= 67:
    note = 3
elif punkte >= 50:
    note = 4
elif punkte >= 30:
    note = 5
else:
    note = 6

if 0 <= punkte <= 100:
    print(f"{punkte} Punkte -> Note {note}")


print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)

alter_gast = 25
ist_student = True
ist_dienstag = True

# Reihenfolge: vom günstigsten/spezifischsten zum allgemeinsten
if alter_gast < 6:
    preis = 0
elif alter_gast < 18:
    preis = 6
elif ist_student or alter_gast >= 65:
    preis = 8
else:
    preis = 12

if ist_dienstag:
    preis = max(0, preis - 2)      # nie unter 0

print(f"Alter {alter_gast}, Student: {ist_student}, Dienstag: {ist_dienstag}")
print(f"Eintrittspreis: {preis} €")


print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)

passwort = "Sonne2026"
erfuellt = 0

lang_genug = len(passwort) >= 8
hat_ziffer = any(z.isdigit() for z in passwort)
hat_gross = any(z.isupper() for z in passwort)
hat_klein = any(z.islower() for z in passwort)
gemischt = hat_gross and hat_klein
nicht_bekannt = passwort.lower() not in ("passwort", "123456", "qwertz")

print(f"Passwort: {passwort}\n")
print(f"{'✅' if lang_genug else '❌'} Mindestens 8 Zeichen")
print(f"{'✅' if hat_ziffer else '❌'} Enthält eine Ziffer")
print(f"{'✅' if gemischt else '❌'} Groß- UND Kleinbuchstaben")
print(f"{'✅' if nicht_bekannt else '❌'} Kein bekanntes Standardpasswort")

erfuellt = lang_genug + hat_ziffer + gemischt + nicht_bekannt   # bool zählt als 0/1!

if erfuellt <= 2:
    staerke = "SCHWACH 🔴"
elif erfuellt == 3:
    staerke = "MITTEL 🟡"
else:
    staerke = "STARK 🟢"

balken = "█" * erfuellt + "░" * (4 - erfuellt)
print(f"\nStärke: {balken}  {erfuellt}/4 — {staerke}")


print("\n" + "=" * 60, "\nAUFGABE 7 🔴\n", "=" * 60)

for jahr in (2024, 1900, 2000, 2100, 2026):
    if jahr % 400 == 0:
        schaltjahr = True
    elif jahr % 100 == 0:
        schaltjahr = False
    elif jahr % 4 == 0:
        schaltjahr = True
    else:
        schaltjahr = False

    print(f"{jahr}: {'Schaltjahr ✅' if schaltjahr else 'kein Schaltjahr ❌'}")

# In einer Zeile (für Fortgeschrittene):
print("\nEinzeiler-Variante für 2000:",
      (2000 % 4 == 0 and 2000 % 100 != 0) or 2000 % 400 == 0)


print("\n" + "=" * 60, "\nAUFGABE 8 🔴\n", "=" * 60)

for dateiname in ("urlaub_2026.JPG", "rechnung.pdf", "song.mp3",
                  "clip.MOV", "daten.xyz"):

    name_klein = dateiname.lower()

    if name_klein.endswith((".jpg", ".jpeg", ".png", ".gif")):
        ordner = "Bilder"
    elif name_klein.endswith((".pdf", ".docx", ".txt")):
        ordner = "Dokumente"
    elif name_klein.endswith((".mp3", ".wav")):
        ordner = "Musik"
    elif name_klein.endswith((".mp4", ".mov")):
        ordner = "Videos"
    else:
        ordner = "Sonstiges"

    print(f"{dateiname:<20} -> {ordner}/")

print("\n💡 endswith() akzeptiert ein Tupel - das spart viele or-Verknüpfungen!")


print("\n" + "=" * 60, "\nAUFGABE 9 ⭐\n", "=" * 60)

benutzer_existiert = True
passwort_korrekt = True
gesperrt = False
zwei_faktor_ok = False

# Guard Clauses: die Fehlerfälle zuerst, der Erfolgsfall zuletzt.
if not benutzer_existiert:
    print("Benutzer unbekannt")
elif not passwort_korrekt:
    print("Falsches Passwort")
elif gesperrt:
    print("Konto gesperrt")
elif not zwei_faktor_ok:
    print("2FA fehlgeschlagen")
else:
    print("Login erfolgreich")

print("\n💡 Gleiche Logik, aber nur EINE Einrückungsebene statt vier.")
print("   Solchen Code liest man in 5 Sekunden statt in 30.")

print("\n🎉 Modul 04 geschafft!")
