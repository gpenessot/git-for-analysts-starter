# Aide-Mémoire Git pour Analystes

Cet aide-mémoire se concentre sur les 5 commandes qui couvrent 95% des besoins quotidiens d'un analyste de données.

---

## ⭐️ Les 5 Commandes Essentielles

### 1. `git init` : La Machine à Remonter le Temps

Transforme un dossier ordinaire en un "repository" Git, créant un historique vide pour suivre vos modifications.

```bash
# À n'utiliser qu'une seule fois au tout début d'un projet
git init
```

### 2. `git add` & `git commit` : Le Checkpoint

Enregistre un "instantané" de votre travail. C'est un processus en deux étapes.

```bash
# Étape 1: Sélectionnez les fichiers que vous voulez inclure dans le checkpoint
# Pour un fichier spécifique :
git add chemin/vers/mon_fichier.py

# Pour tous les fichiers modifiés (à utiliser avec prudence) :
git add .

# Étape 2: Créez le checkpoint avec un message descriptif
git commit -m "feat(analyse): ajoute le calcul de la croissance mensuelle"
```

**Règle d'or pour les messages de commit :** Soyez spécifique ! Un message comme "fix bug" est inutile. "fix(calcul): corrige la division par zéro pour les nouveaux clients" est parfait.

### 3. `git log` : Explorer l'Historique

Affiche la liste de tous les checkpoints (commits) que vous avez créés, du plus récent au plus ancien.

```bash
# Affiche l'historique complet
git log

# Une version plus jolie et concise (ma préférée)
git log --oneline --graph --decorate
```

### 4. `git checkout` : Le Bouton "Annuler"

Permet de revenir à une version précédente d'un fichier ou de naviguer entre les branches.

```bash
# Annuler les modifications sur un fichier depuis le dernier commit
git checkout -- chemin/vers/mon_fichier.py

# Revenir à la version d'un fichier d'un commit spécifique
# (trouvez le <commit_hash> avec git log)
git checkout <commit_hash> -- chemin/vers/mon_fichier.py
```

### 5. `git push` & `git pull` : Collaborer et Sauvegarder

Synchronise votre travail avec un serveur distant comme GitHub.

```bash
# Envoyer vos commits vers le serveur distant (sauvegarde)
git push origin main

# Récupérer les commits du serveur distant (mise à jour)
git pull origin main
```
**Règle d'or :** Toujours `pull` avant de commencer à travailler pour avoir la version la plus récente.

---

## Commandes Utiles Additionnelles

-   **`git status`**
    -   **À quoi ça sert ?** Montre l'état actuel de votre projet : quels fichiers sont modifiés, lesquels sont dans la "staging area", etc.
    -   **Quand l'utiliser ?** Tout le temps ! C'est votre tableau de bord.

-   **`git branch`**
    -   **À quoi ça sert ?** Gère les "branches", des lignes de développement parallèles. Essentiel pour travailler sur une nouvelle fonctionnalité sans casser le code principal.
    -   **Commandes courantes :**
        -   `git branch <nom_branche>` : Crée une nouvelle branche.
        -   `git checkout <nom_branche>` : Passe sur cette branche pour y travailler.
        -   `git merge <nom_branche>` : Fusionne les changements de la branche dans votre branche actuelle (ex: `main`).

-   **`git diff`**
    -   **À quoi ça sert ?** Montre les différences exactes (ligne par ligne) entre vos modifications actuelles et le dernier commit.
    -   **Quand l'utiliser ?** Juste avant de faire `git add`, pour vérifier que vous n'avez inclus que les changements désirés.
