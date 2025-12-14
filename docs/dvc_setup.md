# Guide d'Installation de DVC

Ce guide vous montre comment installer DVC et le configurer pour utiliser Google Drive comme stockage distant gratuit.

## 1. Installation de DVC

Si vous avez suivi le `TUTORIAL.md`, DVC est déjà installé car il fait partie de `requirements.txt`.

Pour vérifier que DVC est bien installé, tapez :
```bash
dvc --version
```

## 2. Configuration de Google Drive comme Stockage Distant

Utiliser Google Drive est une méthode simple et gratuite pour démarrer avec DVC.

### Étape 1 : Créer un Dossier sur Google Drive

1.  Allez sur votre [Google Drive](https://drive.google.com).
2.  Créez un nouveau dossier. Nommez-le de manière explicite, par exemple `DVC_Project_Storage`. **Ce dossier ne contiendra que les données de DVC, n'y mettez rien d'autre.**

### Étape 2 : Récupérer l'ID du Dossier

1.  Ouvrez le dossier que vous venez de créer.
2.  Regardez l'URL dans la barre d'adresse de votre navigateur. Elle ressemblera à :
    `https://drive.google.com/drive/folders/1a2B3c4D-5e6F7g8H9i0J_kLmNoPqRsTu`
3.  La longue chaîne de caractères à la fin est l'**ID de votre dossier**. Copiez-la.

### Étape 3 : Configurer le "Remote" DVC

1.  Ouvrez votre terminal à la racine de votre projet.
2.  Si vous n'avez pas encore initialisé DVC, faites-le :
    ```bash
    dvc init
    ```
3.  Ajoutez un "remote" DVC en remplaçant `<ID_DU_DOSSIER>` par l'ID que vous avez copié :
    ```bash
    dvc remote add -d mygdrive gdrive://<ID_DU_DOSSIER>
    ```
    -   `mygdrive` est le nom que vous donnez à votre stockage distant.
    -   `-d` (`--default`) en fait le remote par défaut pour `dvc push` et `dvc pull`.

### Étape 4 : Authentification

La première fois que vous utiliserez une commande qui interagit avec le remote (comme `dvc push`), DVC vous demandera de vous authentifier :
1.  Il ouvrira une page dans votre navigateur.
2.  Connectez-vous au compte Google où se trouve votre dossier de stockage.
3.  Autorisez DVC (PyDrive) à accéder à votre Google Drive.

Cette authentification est stockée localement et ne devra pas être répétée à chaque fois.

### Étape 5 : Commiter la Configuration

DVC a créé (ou modifié) le fichier `.dvc/config`. Vous devez le commiter pour que Git suive cette configuration.

```bash
git add .dvc/config
git commit -m "feat(dvc): configure google drive as remote storage"
git push
```

**Votre setup DVC est terminé !**

## Commandes DVC Essentielles

-   `dvc add <fichier_ou_dossier>`
    -   Commence à suivre un fichier/dossier de données avec DVC.

-   `dvc push`
    -   Envoie les données (les fichiers réels) vers votre stockage distant (Google Drive).

-   `dvc pull`
    -   Télécharge les données depuis votre stockage distant.

-   `dvc status`
    -   Montre l'état de vos données par rapport à ce qui est suivi par DVC.
