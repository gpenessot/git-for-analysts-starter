# Pre-commit Hooks et GitHub Actions

Ce guide explique comment fonctionnent les outils de qualité de code automatisés dans ce template.

---

## 🎯 Pourquoi Automatiser la Qualité du Code ?

En tant qu'analyste, vous voulez vous concentrer sur l'analyse, pas sur le formatage du code. Ces outils automatisent les tâches répétitives :

- ✅ **Formatage cohérent** : Tout le monde code avec le même style
- ✅ **Détection précoce des erreurs** : Les bugs sont trouvés avant le commit
- ✅ **Sécurité** : Les secrets (API keys) ne sont jamais commitez par accident
- ✅ **Collaboration facilitée** : Code propre = revues de code plus rapides

---

## 🪝 Pre-commit Hooks

### Qu'est-ce qu'un Hook ?

Un **hook** est un script qui s'exécute automatiquement à un moment précis du workflow Git. Les **pre-commit hooks** s'exécutent **avant** que le commit soit créé.

Si un hook échoue (ex: code mal formaté), le commit est bloqué jusqu'à ce que vous corrigiez le problème.

### Installation

```bash
# Installer pre-commit (déjà dans requirements.txt)
pip install pre-commit

# Activer les hooks dans votre repo
pre-commit install
```

### Hooks Configurés

Ce template utilise les hooks suivants (voir [`.pre-commit-config.yaml`](../.pre-commit-config.yaml)) :

#### 1. **Hooks Généraux**

- **trailing-whitespace** : Supprime les espaces en fin de ligne
- **end-of-file-fixer** : Assure une ligne vide en fin de fichier
- **check-yaml** : Vérifie la syntaxe des fichiers YAML
- **check-added-large-files** : Empêche l'ajout de fichiers >500KB (utilisez DVC pour les gros fichiers)
- **check-merge-conflict** : Détecte les marqueurs de conflit (`<<<<<<`, `>>>>>>`)

#### 2. **Ruff (Linter + Formatter Python)**

Ruff remplace Black, isort, et flake8. C'est un outil ultra-rapide écrit en Rust.

- **Linter** : Détecte les erreurs de code (variables non utilisées, imports inutiles, etc.)
- **Formatter** : Formate automatiquement le code selon PEP 8

**Configuration** : Voir `[tool.ruff]` dans [`pyproject.toml`](../pyproject.toml)

#### 3. **detect-secrets (Détection de Secrets)**

Scanne votre code pour détecter :
- Clés API (AWS, OpenAI, etc.)
- Tokens d'authentification
- Mots de passe hardcodés
- Clés privées

**Baseline** : Le fichier `.secrets.baseline` contient les "faux positifs" connus.

#### 4. **nbstripout (Nettoyage Notebooks Jupyter)**

Supprime automatiquement les outputs des notebooks Jupyter avant commit. Cela évite de polluer Git avec des images en base64 ou des résultats volumineux.

**Note** : Ce template utilise Marimo (`.py`), donc ce hook ne s'appliquera que si vous ajoutez des `.ipynb`.

### Utilisation

#### Workflow Normal

Lorsque vous faites un commit, les hooks s'exécutent automatiquement :

```bash
git add scripts/analyze.py
git commit -m "feat: add data validation"

# Pre-commit va automatiquement :
# 1. Formatter le code
# 2. Vérifier le linting
# 3. Scanner les secrets
# Si tout passe : commit créé ✅
# Si échec : vous devez corriger et recommiter ❌
```

#### Exécution Manuelle

Vous pouvez lancer les hooks manuellement sans faire de commit :

```bash
# Sur tous les fichiers
pre-commit run --all-files

# Sur les fichiers modifiés seulement
pre-commit run

# Sur un hook spécifique
pre-commit run ruff --all-files
```

#### Mettre à Jour les Hooks

Les hooks sont gérés par pre-commit et mis en cache. Pour mettre à jour :

```bash
pre-commit autoupdate
```

### Contourner les Hooks (À Éviter)

Si vous avez vraiment besoin de bypasser les hooks (ex: commit WIP) :

```bash
git commit -m "wip: work in progress" --no-verify
```

**⚠️ À utiliser avec parcimonie !** Les hooks sont là pour une bonne raison.

---

## 🤖 GitHub Actions (CI/CD)

### Qu'est-ce que GitHub Actions ?

GitHub Actions est un système d'intégration continue (CI/CD) qui exécute des **workflows** automatiquement sur des événements GitHub (push, pull request, etc.).

### Workflow Configuré

Le fichier [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) définit un workflow qui s'exécute sur chaque push ou pull request vers `main` ou `develop`.

#### Jobs Exécutés

**1. Linting et Formatage (Ruff)**
- Vérifie que le code respecte les standards
- Vérifie que le code est bien formaté

**2. Détection de Secrets**
- Scanne le code pour détecter les secrets
- Compare avec le baseline `.secrets.baseline`

**3. Tests des Scripts Python**
- Crée des données de test
- Exécute `load_data.py` et `analyze.py`
- Vérifie qu'ils ne plantent pas

**4. Validation Notebook Marimo**
- Vérifie la syntaxe du notebook Marimo
- S'assure qu'il est exécutable

**5. Build Status (Résumé)**
- Agrège les résultats de tous les jobs
- Échoue si au moins un job a échoué

### Voir les Résultats

1. Allez sur votre repo GitHub
2. Cliquez sur l'onglet **Actions**
3. Vous verrez la liste de tous les workflows exécutés
4. Cliquez sur un workflow pour voir les détails de chaque job

### Badges de Statut

Vous pouvez ajouter un badge dans votre README pour afficher le statut du build :

```markdown
![CI Status](https://github.com/VOTRE_NOM/VOTRE_REPO/actions/workflows/ci.yml/badge.svg)
```

### Désactiver GitHub Actions

Si vous ne voulez pas utiliser GitHub Actions :

1. Supprimez le dossier `.github/workflows/`
2. Ou renommez le fichier `.yml` en `.yml.disabled`

---

## 🔧 Configuration Ruff

### Fichier de Configuration

La configuration Ruff se trouve dans [`pyproject.toml`](../pyproject.toml) sous `[tool.ruff]`.

### Paramètres Importants

```toml
[tool.ruff]
line-length = 88          # Longueur max d'une ligne (standard Black)
target-version = "py39"   # Compatible Python 3.9+

[tool.ruff.lint]
select = [
    "E",   # Erreurs de style (pycodestyle)
    "W",   # Warnings de style
    "F",   # Erreurs Pyflakes (code mort, imports non utilisés)
    "I",   # Tri des imports (isort)
    "N",   # Conventions de nommage PEP 8
    "UP",  # Syntaxe moderne Python (pyupgrade)
    "B",   # Bugs potentiels (bugbear)
    "C4",  # Simplifications de compréhensions
]

ignore = [
    "E501",  # Ligne trop longue (géré par le formatter)
    "N807",  # Nom de fonction __ (standard Marimo)
]
```

### Personnaliser Ruff

Vous pouvez ajouter/retirer des règles selon vos besoins :

```toml
[tool.ruff.lint]
# Ajouter des règles
select = ["E", "W", "F", "I", "N", "UP", "B", "C4", "D"]  # D = docstrings

# Ignorer des règles spécifiques
ignore = ["E501", "N807", "D100"]  # D100 = docstring manquant au module
```

Voir toutes les règles : https://docs.astral.sh/ruff/rules/

---

## 📊 Workflow Complet

Voici le cycle complet de qualité de code :

### 1. Développement Local

```bash
# 1. Écrire du code
vim scripts/my_analysis.py

# 2. Tester manuellement
python scripts/my_analysis.py

# 3. (Optionnel) Lancer pre-commit manuellement
pre-commit run --all-files

# 4. Commiter
git add scripts/my_analysis.py
git commit -m "feat: add customer segmentation analysis"
# ➡️ Pre-commit s'exécute automatiquement

# 5. Pusher
git push origin main
# ➡️ GitHub Actions s'exécute automatiquement
```

### 2. Sur GitHub

1. Le push déclenche GitHub Actions
2. Les tests s'exécutent dans le cloud
3. Vous recevez une notification si ça échoue
4. Le badge dans le README se met à jour

### 3. Pull Request

Si vous travaillez avec une équipe :

1. Créez une branche feature
2. Faites vos commits (pre-commit valide à chaque fois)
3. Pushez et créez une PR
4. GitHub Actions vérifie la PR
5. Si tout est vert ✅, la PR peut être mergée

---

## 🐛 Dépannage

### "pre-commit command not found"

```bash
# Réinstallez pre-commit
pip install pre-commit

# Vérifiez l'installation
pre-commit --version
```

### "Hook failed but I need to commit anyway"

```bash
# Bypass les hooks (à éviter)
git commit --no-verify -m "wip: bypassing hooks"
```

### "GitHub Actions fails but works locally"

- Vérifiez la version de Python (Actions utilise Python 3.11 par défaut)
- Vérifiez que tous les fichiers sont bien commitez
- Les dépendances sont-elles à jour dans `requirements.txt` ?

### "detect-secrets trouve trop de faux positifs"

Ajoutez-les au baseline :

```bash
detect-secrets scan --update .secrets.baseline
git add .secrets.baseline
git commit -m "chore: update secrets baseline"
```

---

## 📚 Ressources

- [Pre-commit Documentation](https://pre-commit.com/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [detect-secrets](https://github.com/Yelp/detect-secrets)

---

**Automatiser la qualité = Plus de temps pour analyser !** 🚀
