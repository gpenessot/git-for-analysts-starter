# Guide du Dossier `data/`

Ce dossier est destiné à contenir toutes les données utilisées dans le projet. Il est structuré pour fonctionner en harmonie avec Git et DVC.

## Structure

-   `data/raw/` : Contient les données brutes et immuables. Ce sont les fichiers que vous recevez (exports CSV, XLSX, etc.). **Ces fichiers ne doivent jamais être modifiés manuellement.** Ils sont la "source de vérité" unique. Les fichiers volumineux de ce dossier doivent être versionnés avec DVC.

-   `data/processed/` : Contient les données nettoyées, transformées ou enrichies, prêtes pour l'analyse. Ces fichiers sont générés par les scripts du dossier `scripts/`. Tout comme les données brutes, les fichiers volumineux ici doivent être versionnés avec DVC.

## Convention de Nommage

Pour assurer la clarté et la reproductibilité, suivez une convention de nommage simple :

-   `YYYY-MM-DD_<description>.<extension>` (ex: `2024-12-14_sales_extract.csv`)
-   Évitez les espaces et les caractères spéciaux. Utilisez des `_` pour séparer les mots.

## Utilisation de DVC

Les fichiers de données, en particulier ceux de plus de 100 Mo, ne doivent pas être stockés dans Git. Utilisez DVC pour les versionner.

**Exemple de workflow :**
1.  Ajoutez un nouveau fichier de données volumineux dans `data/raw/`.
2.  Utilisez `dvc add data/raw/mon_fichier.csv` pour que DVC commence à le suivre.
3.  Utilisez `git add data/raw/mon_fichier.csv.dvc .gitignore` pour ajouter le fichier pointeur DVC à Git.
4.  Commitez vos changements : `git commit -m "feat(data): add raw sales data for December 2024"`
5.  Poussez vos données sur le stockage distant DVC : `dvc push`
6.  Poussez votre code sur GitHub : `git push`
