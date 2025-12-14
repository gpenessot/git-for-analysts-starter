# Tutorial : Workflow de l'Analyste Moderne

Bienvenue dans ce tutoriel ! L'objectif est de vous guider à travers un workflow complet, de l'installation des outils à votre première analyse reproductible, en utilisant Git, DVC et Marimo.

**Temps estimé : ~45 minutes**

---

## 1. SETUP INITIAL (30 min)

### 1.1. Installer les Outils

Avant toute chose, vous avez besoin des outils suivants. Si vous les avez déjà, passez à l'étape suivante.

-   **Git** : Suivez les instructions sur [git-scm.com](https://git-scm.com/book/fr/v2/D%C3%A9marrer-avec-Git-Installer-Git).
-   **Python** : Installez une version >= 3.9 depuis [python.org](https://www.python.org/downloads/).
-   **uv** : Un gestionnaire d'environnement et de paquets Python ultra-rapide.
    ```bash
    pip install uv
    ```

### 1.2. Configurer Git

Si c'est votre première fois avec Git, configurez votre nom et votre email. C'est l'identité qui sera attachée à tous vos "commits".

```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

### 1.3. Cloner le Projet et Installer les Dépendances

a. **Clonez votre copie du template** que vous avez créée sur GitHub :
```bash
git clone https://github.com/VOTRE_NOM/VOTRE_REPO.git
cd VOTRE_REPO
```

b. **Créez l'environnement virtuel et installez les paquets** avec `uv` :
```bash
# Crée l'environnement .venv
uv venv

# Installe les paquets listés dans requirements.txt
uv pip sync requirements.txt
```

c. **Activez l'environnement** pour pouvoir utiliser les paquets installés :
-   Sur macOS/Linux : `source .venv/bin/activate`
-   Sur Windows (PowerShell) : `.venv\Scripts\Activate.ps1`
-   Sur Windows (CMD) : `.venv\Scripts\activate.bat`

Votre terminal devrait maintenant afficher `(.venv)` au début de la ligne.

---

## 2. WORKFLOW DE BASE GIT (10 min)

Vous allez maintenant faire votre premier "commit" pour sauvegarder une modification.

### 2.1. Faire une modification

Ouvrez le fichier `reports/example_report.qmd` et changez le titre. Par exemple, remplacez `title: "Example Report"` par `title: "Mon Premier Rapport"`.

### 2.2. Comprendre la "Staging Area"

Git fonctionne en deux temps pour enregistrer une modification :

1.  **Ajouter à la Staging Area** (`git add`) : Vous sélectionnez les changements que vous voulez inclure dans le prochain "checkpoint".
2.  **Créer le Commit** (`git commit`) : Vous créez le checkpoint avec un message descriptif.

Voyons les fichiers modifiés :
```bash
git status
```
Git vous montrera que `reports/example_report.qmd` a été modifié.

### 2.3. Créer votre premier Commit

a. **Ajoutez le fichier à la "staging area"** :
```bash
git add reports/example_report.qmd
```

b. **Créez le "commit"** avec un message clair qui décrit ce que vous avez fait :
```bash
git commit -m "docs(report): update report title"
```
**Astuce pour les messages de commit** : Utilisez un format comme `type(scope): description`.
-   `feat`: Nouvelle fonctionnalité
-   `fix`: Correction de bug
-   `docs`: Changement dans la documentation
-   `style`: Changement de style (formatage)
-   `refactor`: Refactoring de code
-   `test`: Ajout/modification de tests

### 2.4. Pousser sur GitHub

Envoyez votre commit sur votre repo GitHub pour le sauvegarder en ligne.
```bash
git push origin main
```
Allez sur votre page GitHub, vous verrez votre commit apparaître !

---

## 3. WORKFLOW DONNÉES AVEC DVC (15 min)

Imaginons que vous recevez un gros fichier de données que vous ne pouvez pas mettre dans Git.

### 3.1. Initialiser DVC avec Google Drive

a. **Créez un dossier sur votre Google Drive**, par exemple `DVC_Storage`.
b. Ouvrez ce dossier et **copiez l'ID du dossier depuis l'URL**. Ce sera une longue chaîne de caractères.
   `https://drive.google.com/drive/folders/ID_DU_DOSSIER`

c. **Configurez DVC** pour utiliser ce dossier comme stockage distant. Remplacez `ID_DU_DOSSIER` par le vôtre.
```bash
# Initialise DVC dans le projet
dvc init

# Configure le remote Google Drive
dvc remote add -d gdrive gdrive://ID_DU_DOSSIER

# DVC va vous demander de vous authentifier via votre navigateur.
```

d. **Commitez la configuration DVC** :
```bash
git add .dvc/config .dvc/.gitignore
git commit -m "feat(dvc): configure google drive remote"
git push
```

### 3.2. Versionner un Fichier de Données

a. **Créez un fichier de données d'exemple** (ou téléchargez-en un) et placez-le dans `data/raw/`. Nommons-le `ventes_decembre.csv`.

b. **Ajoutez ce fichier à DVC** :
```bash
dvc add data/raw/ventes_decembre.csv
```
DVC crée un petit fichier `data/raw/ventes_decembre.csv.dvc` qui contient les métadonnées.

c. **Ajoutez ce pointeur `.dvc` à Git** :
```bash
git add data/raw/ventes_decembre.csv.dvc
git commit -m "feat(data): track december sales data"
```

### 3.3. Pousser les Données et le Code

a. **Poussez les données sur Google Drive** :
```bash
dvc push
```
b. **Poussez le code (le pointeur) sur GitHub** :
```bash
git push
```
Votre code est sur GitHub, vos données sont sur Google Drive, mais les deux sont liés !

### 3.4. Récupérer les Données

Imaginez un collègue qui clone votre projet. Il exécute simplement :
```bash
dvc pull
```
Et DVC téléchargera la bonne version des données depuis Google Drive.

---

## 4. WORKFLOW D'ANALYSE AVEC MARIMO (5 min)

Maintenant, explorons les données avec un notebook.

a. **Lancez Marimo** pour éditer le notebook d'exemple :
```bash
marimo edit notebooks/01_exploration.py
```
b. **Jouez avec le notebook** dans votre navigateur. Modifiez le code, ajoutez des cellules. Grâce à la nature réactive de Marimo, les changements se propagent instantanément.

c. Une fois vos modifications terminées, sauvegardez dans Marimo (Ctrl+S) et **commitez vos changements** avec Git comme vous l'avez appris :
```bash
git add notebooks/01_exploration.py
git commit -m "feat(notebook): add new analysis on sales data"
git push
```

---

Félicitations ! Vous avez complété un cycle complet :
-   Installé et configuré vos outils.
-   Versionné du code avec **Git**.
-   Versionné des données avec **DVC**.
-   Exploré des données de manière reproductible avec **Marimo**.

Vous êtes prêt à travailler de manière plus professionnelle et sereine ! Explorez le dossier `docs/` et `examples/` pour des scénarios plus avancés.
