# Git pour Analystes - Starter Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Vous en avez marre de jongler avec des fichiers `analyse_ventes_v2_final_OK_CEO_vraiment.xlsx` ? Ce template est fait pour vous.

C'est un point de départ complet pour les analystes de données qui souhaitent adopter des pratiques de développement professionnelles avec **Git** et **DVC** sans se sentir intimidés. L'objectif : vous rendre plus productif, collaboratif et serein.

Ce projet est le compagnon de la **[Newsletter DataGyver #10 : Git pour Analystes](https://datagy.substack.com/)**.

---

## 🚀 Quick Start (5 étapes)

1.  **Utiliser ce template** : Cliquez sur "Use this template" en haut de la page GitHub pour créer votre propre copie du projet.
2.  **Cloner votre nouveau repo** : `git clone https://github.com/VOTRE_NOM/VOTRE_REPO.git`
3.  **Installer les dépendances** : Ce projet utilise `uv` pour une gestion rapide des environnements.
    ```bash
    # Installer uv (si ce n'est pas déjà fait)
    pip install uv
    # Créer un environnement virtuel et installer les dépendances
    uv venv
    uv pip sync requirements.txt
    ```
4.  **Activer l'environnement** : `source .venv/bin/activate` (sur Mac/Linux) ou `.venv\Scripts\activate` (sur Windows).
5.  **Explorer le projet** : Suivez le [TUTORIAL.md](./TUTORIAL.md) pour un workflow complet, de votre premier commit au versioning de données avec DVC.

---

## ✨ Fonctionnalités Principales

-   **Structure de Projet Claire** : Une organisation logique pour séparer les données, les notebooks, les scripts et les rapports.
-   **.gitignore Pré-configuré** : Ignore les fichiers inutiles (environnements virtuels, caches, secrets, etc.) pour garder un historique propre.
-   **Gestion des Données Volumineuses avec DVC** : Un setup de base pour versionner vos données (CSV, Parquet > 100Mo) avec DVC et Google Drive, sans alourdir votre repo Git.
-   **Exemples Concrets** : Des scripts, un notebook et un rapport Quarto pour illustrer les bonnes pratiques.
-   **Documentation Actionnable** :
    -   [TUTORIAL.md](./TUTORIAL.md) : Un guide pas à pas pour débuter.
    -   `docs/` : Des aide-mémoires et des guides pour les workflows courants et la résolution de problèmes.

---

## 📁 Structure du Repo

```
git-for-analysts-starter/
├── README.md                          # Cette documentation
├── TUTORIAL.md                        # Workflow complet étape par étape
├── .gitignore                         # Fichiers à ignorer par Git
├── requirements.txt                   # Dépendances Python
├── pyproject.toml                     # Configuration du projet et de 'uv'
├── .dvc/                              # Configuration DVC (à initialiser)
├── data/                              # Données brutes et transformées
├── notebooks/                         # Notebooks Jupyter pour l'exploration
├── scripts/                           # Scripts Python pour l'automatisation
├── reports/                           # Rapports (ex: Quarto, R Markdown)
├── docs/                              # Documentation et aide-mémoires
└── examples/                          # Exemples de workflows
```

---

## 🔧 Prérequis

-   **Git** : [Instructions d'installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
-   **Python** : >= 3.9
-   **uv** : Un gestionnaire de paquets et d'environnements Python rapide. `pip install uv`

## 🤝 Contribution

Ce projet est un template destiné à être amélioré par la communauté. Si vous avez des suggestions, ouvrez une "Issue" ou proposez une "Pull Request" !

## 🔗 Ressources Externes

-   **Newsletter DataGyver** : [datagy.substack.com](https://datagy.substack.com/)
-   **Mon profil LinkedIn** : [linkedin.com/in/gaelpenessot](https://linkedin.com/in/gaelpenessot/)

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
