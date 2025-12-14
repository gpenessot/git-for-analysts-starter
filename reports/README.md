# Guide du Dossier `reports/`

Ce dossier contient les rapports finaux destinés à être partagés avec les parties prenantes (managers, clients, etc.). Ces rapports sont généralement créés avec des outils comme Quarto ou R Markdown.

## Contenu

-   Fichiers sources des rapports (ex: `.qmd`, `.Rmd`).
-   Les rapports rendus (ex: `.html`, `.pdf`) ne sont **pas versionnés** par Git (voir le fichier `.gitignore`). Ils doivent pouvoir être regénérés à tout moment à partir des fichiers sources et des données versionnées.

## Bonnes Pratiques

1.  **Reproductibilité** : Un rapport doit être entièrement reproductible. N'importe quel membre de l'équipe doit pouvoir cloner le projet, exécuter une commande (ex: `quarto render example_report.qmd`) et obtenir exactement le même fichier HTML ou PDF.

2.  **Séparation du Code et du Texte** : Utilisez des cellules de code pour la logique (chargement des données, graphiques) et du Markdown pour le texte, les explications et les conclusions.

3.  **Source de Données** : Les rapports doivent charger leurs données depuis le dossier `data/processed/`, jamais depuis `data/raw/`. L'analyse se base sur des données propres et préparées.

4.  **Paramétrisation** : Pour des rapports récurrents (ex: rapport mensuel), utilisez les paramètres de Quarto pour générer le rapport pour une date ou une région spécifique sans modifier le code.
