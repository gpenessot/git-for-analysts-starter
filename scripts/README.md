# Guide du Dossier `scripts/`

Ce dossier contient les scripts Python qui constituent le cœur de votre projet d'analyse. Contrairement aux notebooks, les scripts sont destinés à être réutilisables, automatisables et robustes.

## Structure

-   `load_data.py`: Scripts responsables de charger les données brutes, de les nettoyer et de les sauvegarder dans `data/processed/`.
-   `analyze.py`: Scripts qui effectuent les analyses principales, les calculs et les agrégations.
-   `utils.py` (optionnel): Fonctions utilitaires partagées par plusieurs scripts pour éviter la duplication de code.

## Bonnes Pratiques

1.  **Fonctions Pures** : Écrivez des fonctions qui, pour une même entrée, produisent toujours la même sortie, sans effets de bord.
2.  **Docstrings et Type Hinting** : Documentez chaque fonction avec une docstring claire (expliquant ce qu'elle fait, ses paramètres et ce qu'elle retourne) et utilisez les "type hints" pour améliorer la lisibilité et la robustesse.
3.  **Gestion des Arguments (CLI)** : Utilisez `argparse` ou `typer` pour permettre à vos scripts d'être lancés depuis la ligne de commande avec des paramètres (ex: `python analyze.py --date 2024-12-14`).
4.  **Logging** : Utilisez le module `logging` pour afficher des informations sur l'exécution du script (ex: "Chargement du fichier X...", "Calcul Y terminé."). C'est plus propre et configurable que des `print()`.
5.  **Gestion des Erreurs** : Anticipez les problèmes (fichier non trouvé, colonne manquante) avec des blocs `try...except` pour que votre script ne plante pas de manière inattendue.
