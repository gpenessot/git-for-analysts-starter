# Exemple : Workflow de Collaboration en Équipe

Ce guide illustre comment travailler à plusieurs sur le même projet en utilisant des **branches** et des **Pull Requests (PR)**. C'est le workflow standard dans la plupart des entreprises tech.

**Scénario** : Vous et votre collègue Alex devez travailler sur le projet.
-   Vous devez ajouter une nouvelle analyse de segmentation client.
-   Alex doit corriger un bug dans le script de chargement de données.

Vous allez travailler en parallèle sans vous marcher sur les pieds.

---

### Étape 1 : Synchroniser et Créer une Branche (Votre Travail)

Avant de commencer quoi que ce soit, assurez-vous d'être à jour et créez votre propre branche de travail.

```bash
# 1. Allez sur la branche principale
git checkout main

# 2. Récupérez les derniers changements depuis GitHub
git pull origin main

# 3. Créez votre branche pour la nouvelle fonctionnalité.
#    Choisissez un nom explicite !
git checkout -b feature/analyse-segmentation
```
Vous êtes maintenant sur votre branche `feature/analyse-segmentation`. Vous pouvez travailler en toute sécurité, vos changements sont isolés.

### Étape 2 : Travailler et Commiter (Votre Travail)

Modifiez les fichiers, créez des scripts, mettez à jour le notebook. Faites autant de commits que nécessaire sur votre branche.

```bash
# ... vous modifiez des fichiers ...
git add .
git commit -m "feat(analyse): add script for customer segmentation"
# ... vous continuez à travailler ...
git add .
git commit -m "feat(notebook): display segmentation results"
```

### Étape 3 : Pousser votre Branche (Votre Travail)

Quand votre fonctionnalité est prête, poussez votre branche (et pas `main` !) sur GitHub.

```bash
git push origin feature/analyse-segmentation
```

### Étape 4 : Ouvrir une Pull Request (Sur GitHub)

1.  Allez sur la page de votre repo GitHub.
2.  GitHub détectera que vous venez de pousser une nouvelle branche et vous proposera d'ouvrir une "Pull Request". Cliquez sur le bouton.
3.  **Une Pull Request (PR) est une demande pour fusionner vos changements (de votre branche) dans la branche `main`.**
4.  Donnez un titre clair à votre PR et décrivez les changements que vous avez faits.
5.  Assignez un "reviewer" (ex: Alex) pour qu'il puisse relire votre code.

### Étape 5 : Revue de Code et Discussion (Le Travail d'Équipe)

-   **Alex reçoit une notification**. Il va sur la PR et peut voir exactement tous les changements que vous avez faits.
-   Il peut laisser des commentaires ligne par ligne ("Pourrais-tu ajouter un commentaire ici ?", "Cette variable n'est pas très claire", etc.).
-   Vous recevez les commentaires, vous faites les modifications demandées, et vous poussez de nouveaux commits sur votre branche. La PR se met à jour automatiquement.

### Étape 6 : Fusionner la Pull Request (Merge)

Une fois qu'Alex a approuvé vos changements, vous (ou lui, selon les règles de l'équipe) pouvez "merger" la PR.

Cliquez sur le bouton "Merge Pull Request" sur GitHub.

Vos changements font maintenant partie de la branche `main`. Le projet a été mis à jour avec votre travail !

### Étape 7 : Nettoyage

Une fois la PR mergée, vous pouvez supprimer la branche de fonctionnalité, qui n'est plus utile.

```bash
# Sur votre machine locale, retournez sur main
git checkout main

# Mettez à jour votre main local
git pull origin main

# Supprimez la branche locale
git branch -d feature/analyse-segmentation
```
Vous pouvez aussi supprimer la branche distante via l'interface de GitHub.

**Pendant ce temps, Alex...** a fait exactement la même chose de son côté sur une branche `fix/bug-chargement-donnees`. Vos deux travaux n'ont jamais été en conflit car ils étaient sur des branches séparées. C'est toute la puissance de ce workflow.
