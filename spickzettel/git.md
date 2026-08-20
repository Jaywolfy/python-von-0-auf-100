# 🌳 Spickzettel · Git & GitHub

> Ausführlich in **Modul 20**. Hier nur die Befehle, die du 95 % der Zeit brauchst.

## 🧠 Das Modell in einem Bild
```text
Arbeitsverzeichnis  →  Staging  →  Repository  →  GitHub
   (deine Dateien)      (add)      (commit)       (push)
```

## Einmalig einrichten
```bash
git config --global user.name  "Dein Name"
git config --global user.email "deine@mail.de"
git config --global init.defaultBranch main
```

## Tägliche Befehle
```bash
git status                  # 👀 Was ist los? (benutz das STÄNDIG)
git add datei.py            # Datei vormerken
git add .                   # alles vormerken
git commit -m "Beschreibung"  # Schnappschuss speichern
git log --oneline           # Verlauf ansehen
git diff                    # Was habe ich geändert?
```

## Mit GitHub arbeiten
```bash
git remote add origin https://github.com/NUTZER/REPO.git
git push -u origin main     # erstes Mal hochladen
git push                    # danach
git pull                    # Änderungen holen
git clone https://github.com/NUTZER/REPO.git   # Repo herunterladen
```

## Rückgängig machen
```bash
git restore datei.py            # Änderungen an Datei verwerfen
git restore --staged datei.py   # aus Staging nehmen
git commit --amend -m "neu"     # letzten Commit-Text ändern
git revert <hash>               # Commit rückgängig (sicher)
```

## Branches
```bash
git branch                  # alle Branches
git switch -c neue-idee     # neuen Branch + wechseln
git switch main             # zurück
git merge neue-idee         # zusammenführen
git branch -d neue-idee     # löschen
```

## 📝 Gute Commit-Nachrichten
```text
✅ "Fügt Passwort-Prüfung hinzu"
✅ "Behebt Absturz bei leerer Eingabe"
✅ "Refactor: Auswertung in eigene Funktion"

❌ "update"
❌ "asdf"
❌ "fix"
```

## `.gitignore` für Python
```gitignore
__pycache__/
*.pyc
.venv/
venv/
.env
.vscode/
.DS_Store
*.log
```

> 🔐 **NIEMALS** Passwörter, API-Keys oder `.env`-Dateien committen! Einmal gepusht, bleibt es in der History.
