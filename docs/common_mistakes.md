# Les 7 Erreurs Fatales de l'Analyste (et comment les éviter)

Ce guide reprend les erreurs courantes mentionnées dans la [newsletter #10](https://datagy.substack.com/) et vous donne des solutions concrètes pour les éviter et les corriger.

---

### Erreur #1 : Commiter des Mots de Passe ou des Secrets

-   **Le scénario** : Vous codez en dur une clé API, un mot de passe de base de données ou un token dans votre script, et vous le commitez.
-   **Pourquoi c'est grave** : Si le repo est public, des bots scannent GitHub en permanence et trouveront votre secret en quelques minutes. Votre compte sera compromis. Même dans un repo privé, c'est une mauvaise pratique de sécurité.
-   **Prévention** :
    1.  Utilisez un fichier `.env` à la racine de votre projet pour stocker les secrets (`API_KEY="votre_secret"`).
    2.  Assurez-vous que `.env` est bien listé dans votre `.gitignore`.
    3.  Dans votre code Python, utilisez la librairie `python-dotenv` pour charger ces secrets en toute sécurité.
-   **Correction (si c'est trop tard)** :
    1.  **Révoquez immédiatement le secret** auprès du fournisseur (AWS, Google, etc.). C'est l'étape la plus urgente.
    2.  Supprimer le secret de votre historique Git est complexe. Le plus simple est d'utiliser des outils comme [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/). Un simple `git commit` qui supprime le fichier ne suffit pas, car le secret reste dans l'historique.

### Erreur #2 : Messages de Commit Inutiles

-   **Le scénario** : Des commits avec des messages comme "fix", "update", "changes", "wip".
-   **Pourquoi c'est grave** : Dans trois mois, quand vous chercherez pourquoi un calcul a été modifié, cet historique ne vous sera d'aucune aide.
-   **Prévention** : Adoptez une convention, par exemple `type(scope): description`. Soyez bref mais spécifique.
    -   **Mauvais** : `git commit -m "fix"`
    -   **Bon** : `git commit -m "fix(calcul): corrige la division par zéro dans le taux de conversion"`

### Erreur #3 : Commits Géants avec 50 Fichiers

-   **Le scénario** : Vous travaillez toute la journée, modifiez 12 fichiers, ajoutez 3 fonctionnalités, et faites un seul gros commit.
-   **Pourquoi c'est grave** : Il devient impossible d'annuler une seule modification sans impacter les autres. La revue de code (Pull Request) est un cauchemar.
-   **Prévention** : Faites des **commits atomiques**. Un commit = une seule idée logique. Si votre message de commit contient le mot "et", c'est souvent le signe que vous devriez faire deux commits.

### Erreur #4 : Versionner des Fichiers de 500 Mo

-   **Le scénario** : Vous faites un `git add` sur un gros fichier CSV, une vidéo ou une base de données SQLite.
-   **Pourquoi c'est grave** : Votre repo Git explose en taille. Le cloner prend des heures. Les commandes Git deviennent lentes.
-   **Prévention** :
    -   Pour les fichiers de **données** (`.csv`, `.parquet`, etc.) > 100 Mo : Utilisez **DVC**.
    -   Pour les autres gros fichiers binaires (assets, modèles) : Utilisez **Git LFS** (Large File Storage).
    -   Pour tout le reste qui est généré (rapports `.html`, etc.) : Ajoutez-les au `.gitignore`.

### Erreur #5 : Travailler Directement sur `main`

-   **Le scénario** : Vous codez votre nouvelle analyse directement sur la branche `main`. Vous cassez quelque chose, et le projet principal ne fonctionne plus.
-   **Pourquoi c'est grave** : `main` devrait toujours être stable et fonctionnelle. C'est la version de référence.
-   **Prévention** : Utilisez des **branches de fonctionnalité** (feature branches).
    1.  Avant de commencer : `git checkout -b nouvelle-analyse-ventes`
    2.  Travaillez et commitez sur cette branche.
    3.  Quand c'est terminé et que tout fonctionne, fusionnez-la dans `main` via une Pull Request.

### Erreur #6 : Oublier de `git pull` avant de Travailler

-   **Le scénario** : Vous commencez à coder. Pendant ce temps, un collègue a poussé ses modifications. Quand vous essayez de `git push`, vous avez une erreur de conflit.
-   **Pourquoi c'est grave** : Cela crée des fusions non désirées et peut être déroutant pour les débutants.
-   **Prévention** : Prenez l'habitude de toujours exécuter `git pull` avant de commencer à travailler.

### Erreur #7 : Utiliser `git push --force` sans Comprendre

-   **Le scénario** : Vous avez un conflit, vous trouvez `git push --force` sur Stack Overflow et vous l'exécutez.
-   **Pourquoi c'est grave** : Vous venez potentiellement de réécrire l'historique sur le serveur, écrasant et faisant disparaître le travail de vos collègues.
-   **Prévention** : **N'utilisez JAMAIS `git push --force` sur une branche partagée (`main`, `develop`)**. La seule utilisation (à peu près) acceptable est sur votre propre branche de fonctionnalité, pour nettoyer votre historique avant une Pull Request. Et même là, préférez `git push --force-with-lease`.
