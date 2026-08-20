"""
╔══════════════════════════════════════════════════════════════════╗
║  MODUL 10 · MUSTERLÖSUNGEN — Comprehensions & Builtins           ║
╚══════════════════════════════════════════════════════════════════╝
"""

zahlen = [12, -5, 33, 0, -18, 7, 45, -2, 8]
woerter = ["Programmierung", "Code", "Python", "Bug", "Debugger", "IDE"]
personen = [
    {"name": "Anna",  "alter": 30, "stadt": "Berlin",  "gehalt": 4200},
    {"name": "Bernd", "alter": 25, "stadt": "Hamburg", "gehalt": 3800},
    {"name": "Clara", "alter": 41, "stadt": "Berlin",  "gehalt": 5500},
    {"name": "David", "alter": 35, "stadt": "München", "gehalt": 4900},
]

print("=" * 60, "\nAUFGABE 1 🟢\n", "=" * 60)
print(f"a) {[z * 3 for z in zahlen]}")
print(f"b) {[z for z in zahlen if z > 0]}")
print(f"c) {[str(z) for z in zahlen]}")
print(f"d) {[x ** 2 for x in range(1, 11)]}")

print("\n" + "=" * 60, "\nAUFGABE 2 🟢\n", "=" * 60)
print(f"{[w.lower() for w in woerter if len(w) > 4]}")

print("\n" + "=" * 60, "\nAUFGABE 3 🟢\n", "=" * 60)
print([("positiv" if z > 0 else "negativ" if z < 0 else "null") for z in zahlen])

print("\n" + "=" * 60, "\nAUFGABE 4 🟡\n", "=" * 60)
namen = ["Anna", "Bernd", "Clara"]
punkte = [85, 92, 78]

print("a) Rangliste:")
for nr, name in enumerate(namen, start=1):
    print(f"   {nr}. {name}")

d = dict(zip(namen, punkte))
print(f"b) {d}")

print("c)")
for name, p in zip(namen, punkte):
    print(f"   {name} hat {p} Punkte")

bester = max(d, key=d.get)
print(f"d) Bester: {bester} mit {d[bester]} Punkten")

print("\n" + "=" * 60, "\nAUFGABE 5 🟡\n", "=" * 60)
print(f"a) nach Alter:    {[p['name'] for p in sorted(personen, key=lambda p: p['alter'])]}")
print(f"b) nach Gehalt ↓: {[p['name'] for p in sorted(personen, key=lambda p: p['gehalt'], reverse=True)]}")
print(f"c) Namenslänge:   {[p['name'] for p in sorted(personen, key=lambda p: len(p['name']))]}")
sortiert = sorted(personen, key=lambda p: (p["stadt"], p["name"]))
print(f"d) Stadt, Name:   {[(p['stadt'], p['name']) for p in sortiert]}")

print("\n" + "=" * 60, "\nAUFGABE 6 🟡\n", "=" * 60)
print(f"a) Jemand > 5000 €:     {any(p['gehalt'] > 5000 for p in personen)}")
print(f"b) Alle älter als 20:   {all(p['alter'] > 20 for p in personen)}")
print(f"c) Jemand in Köln:      {any(p['stadt'] == 'Köln' for p in personen)}")
print(f"d) Alle mit Vokal:      {all(any(v in w.lower() for v in 'aeiou') for w in woerter)}")

print("\n" + "=" * 60, "\nAUFGABE 7 🥗 MIX\n", "=" * 60)
print(f"a) {{name: alter}}:  {dict((p['name'], p['alter']) for p in personen)}")
print(f"b) über 30:          { {p['name']: p['gehalt'] for p in personen if p['alter'] > 30} }")
print(f"c) +5 %:             { {p['name']: round(p['gehalt'] * 1.05) for p in personen} }")

laengen = {w: len(w) for w in woerter}
print("d) Wortlängen sortiert:")
for wort, laenge in sorted(laengen.items(), key=lambda paar: paar[1]):
    print(f"   {wort:<16} {laenge:>2} {'▪' * laenge}")

print("\n" + "=" * 60, "\nAUFGABE 8 🔴\n", "=" * 60)

alter_liste = [p["alter"] for p in personen]
gehaelter = [p["gehalt"] for p in personen]

print(f"a) Ø Alter:        {sum(alter_liste) / len(alter_liste):.1f} Jahre")
print(f"b) Gesamtgehalt:   {sum(gehaelter):,} €")

top = max(personen, key=lambda p: p["gehalt"])
flop = min(personen, key=lambda p: p["gehalt"])
print(f"c) Höchstes:       {top['name']} ({top['gehalt']:,} €)")
print(f"   Niedrigstes:    {flop['name']} ({flop['gehalt']:,} €)")

print(f"d) Städte:         {sorted({p['stadt'] for p in personen})}")

pro_stadt = {}
for p in personen:
    pro_stadt[p["stadt"]] = pro_stadt.get(p["stadt"], 0) + 1
print(f"e) Pro Stadt:      {pro_stadt}")

print(f"f) Berliner:       {[p['name'] for p in personen if p['stadt'] == 'Berlin']}")

print("\n" + "=" * 60, "\nAUFGABE 9 🔴\n", "=" * 60)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"a) Flach:          {[z for zeile in matrix for z in zeile]}")
print(f"b) Verdoppelt:     {[[z * 2 for z in zeile] for zeile in matrix]}")
print(f"c) Nur gerade:     {[z for zeile in matrix for z in zeile if z % 2 == 0]}")
print(f"d) Diagonale:      {[matrix[i][i] for i in range(len(matrix))]}")
print(f"e) Zeilensummen:   {[sum(zeile) for zeile in matrix]}")

print("""
💡 Bei a): Die Reihenfolge der for-Teile ist wie bei einer normalen
   verschachtelten Schleife - von außen nach innen lesen:
        for zeile in matrix:
            for z in zeile:
""")

print("=" * 60, "\nAUFGABE 10 ⭐ - Refactoring-Urteil\n", "=" * 60)

# BLOCK A -> ✅ Comprehension. Ein Filter, eine Zeile, sofort lesbar.
grosse = [z for z in zahlen if z > 10]
print(f"Block A (Comprehension): {grosse}")

# BLOCK B -> ❌ SCHLEIFE LASSEN.
# Drei verschachtelte Bedingungen + Zwischenrechnung (bonus).
# Als Comprehension wäre das eine unlesbare Zeile.
ergebnis = []
for p in personen:
    if p["alter"] > 25 and p["stadt"] == "Berlin":
        bonus = p["gehalt"] * 0.1
        if bonus > 400:
            ergebnis.append((p["name"], round(bonus)))
print(f"Block B (Schleife bleibt): {ergebnis}")

# BLOCK C -> ✅ Comprehension. Reine Umformung, keine Bedingung.
namen_gross = [p["name"].upper() for p in personen]
print(f"Block C (Comprehension): {namen_gross}")

print("""
🎓 DIE ENTSCHEIDUNGSREGEL:
   ✅ Comprehension, wenn: eine Umformung, höchstens ein Filter,
      passt in eine Zeile, beim ersten Lesen verständlich.
   ❌ Schleife, wenn: mehrere Bedingungen, Zwischenvariablen,
      verschachtelte Logik - oder wenn du beim Lesen stolperst.

   Guter Code ist nicht der kürzeste. Er ist der, den dein
   zukünftiges Ich in 6 Monaten sofort versteht.
""")

print("🎉 Modul 10 geschafft!")
