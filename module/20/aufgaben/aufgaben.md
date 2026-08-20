# ⌨️ Modul 20 · Aufgaben (Terminal-Übungen)

> Alles im Terminal. Hak ab, was du geschafft hast. ✅

---

## Aufgabe 1 🟢 — Erstes Repository

- [ ] Ordner `git-uebung` anlegen, hineinwechseln
- [ ] `git init`
- [ ] `git status` → was sagt Git?
- [ ] Datei `hallo.py` mit `print("Hallo Git!")` anlegen
- [ ] `git status` → in welchem Zustand ist die Datei? (untracked)
- [ ] `git add hallo.py`
- [ ] `git status` → was hat sich geändert? (staged)
- [ ] `git commit -m "Erster Commit: Hallo-Programm"`
- [ ] `git log --oneline`

**Notiere:** Die drei Zustände, die eine Datei in Git haben kann.

---

## Aufgabe 2 🟢 — Änderungen verfolgen

- [ ] Ändere `hallo.py`: eine zweite `print`-Zeile
- [ ] `git status`
- [ ] `git diff` → was zeigt Git genau an?
- [ ] `git add .` und `git diff` nochmal → warum ist jetzt nichts mehr da?
- [ ] `git diff --staged` → jetzt siehst du es wieder
- [ ] Committen mit sinnvoller Nachricht

---

## Aufgabe 3 🟢 — .gitignore

- [ ] Lege an: `geheim.env`, Ordner `__pycache__/` mit einer Datei, `test.log`
- [ ] `git status` → alle drei tauchen auf
- [ ] `.gitignore` anlegen mit:
  ```gitignore
  __pycache__/
  *.log
  *.env
  .venv/
  ```
- [ ] `git status` → alle drei sind verschwunden ✅
- [ ] `.gitignore` selbst committen

---

## Aufgabe 4 🟡 — Rückgängig machen

- [ ] Ändere `hallo.py` kaputt (z. B. Syntaxfehler)
- [ ] `git diff` ansehen
- [ ] `git restore hallo.py` → Datei ist wieder heil 🎉
- [ ] Nochmal ändern, `git add`, dann `git restore --staged hallo.py`
- [ ] Was ist der Unterschied zwischen beiden `restore`-Varianten?

---

## Aufgabe 5 🟡 — Eine echte History bauen

Mach **mindestens 5 Commits** mit jeweils einer sinnvollen Änderung:

- [ ] Funktion `begruesse(name)` hinzufügen
- [ ] Docstring ergänzen
- [ ] Zweite Funktion hinzufügen
- [ ] `README.md` schreiben
- [ ] Einen Bug einbauen und im nächsten Commit beheben

- [ ] `git log --oneline` → liest sich die History wie eine Geschichte?
- [ ] `git log --stat` → welche Dateien wurden je Commit geändert?

---

## Aufgabe 6 🟡 — Branches

- [ ] `git switch -c experiment`
- [ ] Baue etwas Riskantes ein (große Änderung)
- [ ] Committen
- [ ] `git switch main` → schau in die Datei: die Änderung ist weg! 🪄
- [ ] `git switch experiment` → wieder da
- [ ] `git switch main` und `git merge experiment`
- [ ] `git branch -d experiment`
- [ ] `git log --oneline --graph --all`

---

## Aufgabe 7 🔴 — Konflikt erzeugen und lösen

Das passiert dir irgendwann — besser einmal absichtlich üben. 💪

- [ ] `git switch -c version-a`, Zeile 1 der Datei ändern, committen
- [ ] `git switch main`, **dieselbe** Zeile anders ändern, committen
- [ ] `git merge version-a` → 💥 CONFLICT
- [ ] Öffne die Datei — du siehst:
  ```text
  <<<<<<< HEAD
  deine Version aus main
  =======
  Version aus version-a
  >>>>>>> version-a
  ```
- [ ] Entscheide dich, lösche die Markierungen
- [ ] `git add datei` und `git commit`

**Merke:** Ein Konflikt ist kein Fehler. Git fragt nur: *„Welche Version willst du?"*

---

## Aufgabe 8 🔴 — GitHub

- [ ] GitHub-Konto anlegen (falls nicht vorhanden)
- [ ] Neues Repo erstellen — **Private** wählen! 🔒
- [ ] **Kein** README/gitignore ankreuzen (hast du schon lokal)
- [ ] Verbinden:
  ```bash
  git remote add origin https://github.com/DEINNAME/git-uebung.git
  git push -u origin main
  ```
- [ ] Auf github.com nachschauen — alles da?
- [ ] Auf GitHub eine Datei online bearbeiten und committen
- [ ] Lokal `git pull` → Änderung angekommen?

---

## Aufgabe 9 ⭐ Bonus — Deine Projekte veröffentlichen

Für **jedes** bisherige Kursprojekt:

- [ ] Eigenes privates Repo
- [ ] `.gitignore` **vor** dem ersten Commit
- [ ] Aussagekräftige `README.md`
- [ ] `requirements.txt` (falls Pakete nötig)
- [ ] Mindestens 3 saubere Commits
- [ ] Push

---

## 🚨 Notfall-Kommandos

| Situation | Befehl |
|---|---|
| Ich weiß nicht, was los ist | `git status` |
| Änderung an Datei verwerfen | `git restore datei` |
| Aus Staging nehmen | `git restore --staged datei` |
| Letzte Commit-Nachricht ändern | `git commit --amend -m "..."` |
| Commit rückgängig (sicher) | `git revert <hash>` |
| Alten Stand ansehen | `git checkout <hash>` |
| Zurück zur Gegenwart | `git switch main` |
