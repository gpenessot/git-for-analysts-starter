# Guide du Dossier `notebooks/`

Ce dossier contient les notebooks pour l'exploration, l'expérimentation et la visualisation itérative, en utilisant **Marimo**.

## Pourquoi Marimo et pas Jupyter ?

Conformément à la philosophie de ce template, nous privilégions les outils qui fonctionnent bien avec Git.

-   **Fichiers `.py` purs** : Les notebooks Marimo sont de simples scripts Python. Contrairement aux fichiers `.ipynb` de Jupyter qui sont du JSON complexe, les notebooks `.py` sont lisibles par les humains.
-   **"Diffs" Clairs** : Comparer deux versions d'un notebook Marimo dans une Pull Request est simple et clair. Vous ne voyez que les lignes de code qui ont changé, pas des métadonnées ou des outputs encodés en base64.
-   **Pas d'Output Stocké** : Les résultats des cellules ne sont pas stockés dans le fichier, ce qui garde le repo léger et les "diffs" propres.
-   **Réactivité** : Marimo est réactif. Modifier une cellule met automatiquement à jour toutes les cellules qui en dépendent, ce qui évite les erreurs d'état caché communes dans les notebooks Jupyter.

## Bonnes Pratiques

1.  **Un Notebook, Un Objectif** : Chaque notebook doit avoir un objectif clair et défini (ex: `01_exploration_donnees_ventes.py`).

2.  **Nommage Clair** : Préfixez vos notebooks avec des numéros pour indiquer l'ordre de lecture logique (`01_`, `02_`, ...).

3.  **Du Notebook au Script** : Une fois qu'une logique est stable et doit être réutilisée, transformez-la en fonctions ou en script Python standard dans le dossier `scripts/`.

4.  **Documentation** : Utilisez `mo.md()` pour expliquer votre démarche, vos hypothèses et vos conclusions.

## Lancement

Pour éditer ou exécuter un notebook Marimo, utilisez la commande suivante à la racine du projet :
```bash
marimo edit notebooks/01_exploration.py
```
