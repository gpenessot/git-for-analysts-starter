# Exemple : Scénarios de Récupération (Disaster Recovery)

Même avec de l'expérience, on fait tous des erreurs. Ce guide vous montre comment vous sortir des situations les plus courantes avec Git. Pas de panique !

---

### Scénario 1 : "J'ai modifié un fichier, mais c'était mieux avant."

Vous avez fait des modifications dans un fichier depuis votre dernier commit, mais elles ne sont pas bonnes et vous voulez juste revenir à la version sauvegardée.

**Solution : `git checkout`**

```bash
# Annule toutes les modifications sur ce fichier et le restaure
# à sa version du dernier commit.
git checkout -- chemin/vers/le/fichier.py
```
**Attention :** Cette commande est destructive. Les modifications que vous annulez sont perdues pour de bon.

---

### Scénario 2 : "J'ai supprimé un fichier par erreur !"

Vous avez fait `rm mon_script.py`, mais vous ne vouliez pas. Le fichier était dans le dernier commit.

**Solution : `git checkout`**

```bash
# Restaure le fichier depuis le dernier commit
git checkout -- mon_script.py
```

---

### Scénario 3 : "Mon code marchait ce matin, mais plus maintenant."

Vous avez fait plusieurs commits, et l'un d'entre eux a introduit un bug. Vous ne savez pas lequel.

**Solution : `git log` et `git checkout` (ou `git bisect` pour les experts)**

1.  **Explorez l'historique** pour trouver le dernier commit où vous êtes sûr que tout fonctionnait.
    ```bash
    git log --oneline --graph
    ```
    Copiez le "hash" du commit (ex: `a1b2c3d`).

2.  **Créez une branche temporaire** pour inspecter cet ancien état sans perdre votre travail actuel.
    ```bash
    git checkout -b investigation a1b2c3d
    ```
    Votre projet est maintenant exactement comme il était à ce commit. Testez et confirmez que le code fonctionnait. Vous savez maintenant que le bug a été introduit *après* ce commit.

3.  Revenez à votre travail actuel et analysez les commits suivants.
    ```bash
    git checkout main
    ```

---

### Scénario 4 : "J'ai commité des secrets par erreur !"

Vous avez commité un fichier avec une clé API. **C'est le scénario le plus urgent.**

**Solution : Révoquer et Nettoyer l'Historique**

1.  **URGENT : RÉVOQUEZ LE SECRET.** Allez sur la plateforme du fournisseur (AWS, Google, etc.) et invalidez immédiatement la clé ou le mot de passe. Considérez-le comme compromis.

2.  **NE FAITES PAS** un simple commit qui supprime le fichier. Le secret restera visible dans l'historique de Git.

3.  **Utilisez un outil spécialisé** pour nettoyer l'historique. Le plus simple aujourd'hui est [**BFG Repo-Cleaner**](https://rtyley.github.io/bfg-repo-cleaner/). Suivez leur documentation attentivement. C'est une opération complexe et destructive. Si vous n'êtes pas à l'aise, demandez de l'aide.

---

### Scénario 5 : "J'ai fait un commit, mais je veux le modifier."

Vous venez de faire un commit, mais vous avez oublié d'ajouter un fichier, ou il y a une faute de frappe dans le message.

**Solution : `git commit --amend`**

```bash
# Si vous avez oublié un fichier :
git add le_fichier_oublie.py
git commit --amend --no-edit  # --no-edit garde le même message de commit

# Si vous voulez juste changer le message du dernier commit :
git commit --amend -m "Un nouveau message de commit plus clair"
```
**Attention :** N'utilisez `git commit --amend` que sur des commits qui n'ont **pas encore été poussés** sur un repo partagé.

---

### La Règle d'Or : En cas de doute, demandez de l'aide

Git est puissant mais complexe. Si vous êtes face à une situation que vous ne comprenez pas, surtout si elle implique de réécrire l'historique (`rebase`, `filter-repo`), il vaut mieux demander à un collègue plus expérimenté plutôt que de risquer d'aggraver la situation.
