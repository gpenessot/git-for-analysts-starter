# Exemple : Workflow de Mise à Jour Mensuelle

Ce document décrit un scénario concret : vous êtes un analyste et vous recevez chaque mois une nouvelle version du fichier des ventes. Vous devez mettre à jour votre projet de manière propre et reproductible.

**Scénario** : Nous sommes le 14 janvier 2026. Vous venez de recevoir le fichier `sales_december_2025.csv`. Votre projet contient déjà `sales_november_2025.csv` qui est suivi par DVC.

**Temps estimé** : 5 minutes.

---

### Étape 1 : Ajouter le Nouveau Fichier

Placez le nouveau fichier `sales_december_2025.csv` dans le dossier `data/raw/`.

### Étape 2 : Mettre à Jour DVC

Nous allons dire à DVC de ne plus suivre l'ancien fichier (optionnel, mais propre) et de suivre le nouveau.

```bash
# Optionnel : Si vous voulez supprimer l'ancien fichier du suivi DVC
# dvc remove data/raw/sales_november_2025.csv.dvc

# Ajoutez le nouveau fichier au suivi DVC
dvc add data/raw/sales_december_2025.csv
```

### Étape 3 : Vérifier le Statut

Utilisez `git status` pour voir ce qui a changé du point de vue de Git.

```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   data/raw/sales_december_2025.csv.dvc
        deleted:    data/raw/sales_november_2025.csv.dvc # Si vous avez fait dvc remove

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore # DVC a peut-être ajouté le nouveau fichier ici

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        data/raw/sales_december_2025.csv
```
C'est normal :
- Le nouveau fichier `.dvc` est prêt à être commité.
- Le vrai fichier `.csv` est listé comme "untracked" (et devrait être ignoré par votre `.gitignore`).

### Étape 4 : Commiter le Changement de Pointeur

Ajoutez le(s) fichier(s) `.dvc` à la "staging area" et commitez.

```bash
git add data/raw/
git commit -m "data(raw): update sales data for December 2025"
```
Ce commit est très léger, il ne contient que le petit fichier pointeur.

### Étape 5 : Pousser Code et Données

C'est l'étape magique où tout se synchronise.

```bash
# 1. Poussez les VRAIES données (le gros CSV) sur votre stockage distant (Google Drive)
dvc push

# 2. Poussez le POINTEUR (le petit .dvc) sur GitHub
git push
```

### Vérifications Finales

1.  **Sur GitHub** : Vous devriez voir votre nouveau commit "data(raw): update sales data for December 2025". Si vous naviguez vers `data/raw/`, vous verrez le fichier `sales_december_2025.csv.dvc`.
2.  **Sur Google Drive** : Dans votre dossier de stockage DVC, vous verrez de nouveaux fichiers apparaître dans le sous-dossier `files/md5/`. Ce sont vos données, découpées et organisées par DVC.

Vous avez terminé ! Votre projet est à jour, de manière propre, traçable et reproductible. N'importe qui dans votre équipe peut maintenant faire `git pull` puis `dvc pull` pour récupérer exactement les mêmes données.
