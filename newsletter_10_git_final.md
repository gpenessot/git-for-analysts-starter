# DataGyver #10 : Git pour Analystes — Arrêtez de versionner vos fichiers avec _v2_final_vraiment_final.xlsx

**Hello ! Vous êtes 1046 à me suivre, merci pour votre confiance !**

## 🚀 Actualités

Avant de plonger dans Git, quelques nouvelles rapides :

**Streamlit Unleashed** : Les 16 beta-testeurs ont terminé le parcours, les retours sont excellents. Lancement grand public prévu pour janvier avec un bonus exclusif pour les lecteurs de cette newsletter.

**SQL Mastery** : 182 beta-testeurs inscrits, la plateforme évolue bien. J'intègre progressivement tout le contenu. Patience, ça arrive.

**Formation LinkedIn Learning** : Discussions avancées pour un premier cours sur Polars prévu février 2026. Je vous tiens au courant.

---

## La scène du crime que vous connaissez tous

Lundi matin, 9h15. Vous ouvrez votre dossier de travail. Voici ce que vous voyez :

```
📁 Rapports/
  📄 analyse_ventes_Q4.xlsx
  📄 analyse_ventes_Q4_v2.xlsx
  📄 analyse_ventes_Q4_v2_final.xlsx
  📄 analyse_ventes_Q4_v2_FINAL.xlsx
  📄 analyse_ventes_Q4_v2_FINALE_vraiment.xlsx
  📄 analyse_ventes_Q4_v2_FINALE_OK_CEO.xlsx
  📄 analyse_ventes_Q4_v2_FINALE_OK_CEO_modif_jeudi.xlsx
```

Vous devez présenter ce rapport dans 10 minutes. Quelle version prenez-vous ? Celle avec "CEO" ? Ou celle de jeudi ? Ou peut-être que la bonne version était en fait `analyse_ventes_Q4_v2_final.xlsx` (sans les majuscules) ?

Vous ouvrez trois fichiers en même temps pour comparer. Les chiffres diffèrent légèrement. Vous ne vous souvenez plus pourquoi. La panique monte.

Cette scène, je l'ai vécue. Vous l'avez vécue. Tout le monde l'a vécue.

Le pire ? C'est qu'un analyste senior que je respecte énormément m'a écrit récemment : *"Mon versioning, c'est avoir plusieurs versions de fichiers et utiliser des conventions de nommage... ça marche très bien."*

Et vous savez quoi ? Il a raison. **Ça marche**. Mais seulement si vous êtes seul. Seulement si vous avez une mémoire d'éléphant. Seulement si vous ne faites jamais d'erreur.

Le jour où vous travaillez à deux, ou que vous voulez retrouver "cette version d'il y a 3 semaines qui marchait mieux", c'est fini. Vous êtes coincé.

---

## Le coût invisible que personne ne calcule

Faisons les comptes ensemble. Soyons honnêtes.

Combien de temps passez-vous chaque semaine à :
- Chercher "la bonne version" d'un fichier ? **15-20 minutes**
- Comparer deux versions pour voir ce qui a changé ? **20-30 minutes**
- Recréer quelque chose que vous aviez fait "il y a quelques jours" mais que vous ne retrouvez plus ? **30-45 minutes**
- Expliquer à un collègue quelle version utiliser ? **10-15 minutes**

**Total conservateur : 1h30 par semaine. Soit 78 heures par an.**

À 45€/heure (tarif analyste moyen), ça fait **3 510€ par an de temps perdu**. Pour une seule personne.

Une équipe de 5 analystes ? **17 550€/an qui partent en fumée**.

Mais le pire n'est pas le temps. C'est la **peur d'expérimenter**.

Un analyste sur StackOverflow l'exprime parfaitement : *"Sometimes the report just looked better 45 minutes ago."*

Sans version control, impossible de revenir en arrière proprement. Alors vous n'expérimentez pas. Vous restez sur ce qui marche. Vous stagnez.

---

## Les 4 catégories d'analystes (et pourquoi la plupart bloquent au niveau 2)

Il y a quelques années, j'ai découvert un article qui a changé ma vision du métier. L'auteur divise les analystes en 4 catégories :

**Catégorie 1 : Excel-only**
- Tout est fait dans Excel (data management, calculs, visualisation)
- Outils spécialisés (SAS, Stata, R) uniquement pour la modélisation statistique
- **Problème** : Ne scale pas, erreurs difficiles à tracer, impossible à automatiser

**Catégorie 2 : Code + Naming Conventions**
- Utilise R, Python ou SQL pour tout le workflow
- Versionne avec des noms de fichiers : `script_v1.py`, `script_v2.py`, `script_final.py`
- **Problème** : Fonctionne seul, explose en équipe

**Catégorie 3 : Code + Git + Standards**
- Version control avec Git
- Coding style guide défini
- Peer review systématique
- **Avantage** : Scalable, professionnel, collaboratif

**Catégorie 4 : Catégorie 3 + DevOps**
- Tests automatisés
- CI/CD pipelines
- Release cycles définis
- Documentation complète

L'auteur note quelque chose de crucial : **"A threshold of professionalism is really crossed in the progression from category #2 to #3."**

C'est là que vous passez d'exécutant à professionnel reconnu. C'est là que vous devenez scalable. C'est là que vous pouvez vraiment collaborer.

La bonne nouvelle ? Le passage de 2 à 3 ne demande pas des mois d'apprentissage. **Vous pouvez l'adopter en une journée** si vous suivez le bon workflow.

---

## Cassons un mythe : Git n'est PAS réservé aux développeurs

Je sais ce que vous pensez. *"Gaël, Git c'est pour les devs qui font du JavaScript toute la journée. Moi je fais de l'analyse de données, pas du développement logiciel."*

Faux. Archi-faux.

Git a été créé en 2005 par Linus Torvalds pour gérer le code du kernel Linux. Oui, à la base c'est pour les devs. Mais devinez quoi ? **Votre code Python, vos scripts SQL, vos notebooks Jupyter, vos rapports Quarto... c'est du code.**

Et même vos fichiers Excel peuvent être versionnés avec Git (même si c'est pas optimal, on y reviendra).

La vraie question n'est pas "est-ce que Git est fait pour moi ?" mais "est-ce que je veux gagner 78 heures par an et arrêter de flipper à chaque fois que je modifie un script qui marche ?"

Si la réponse est oui, continuez à lire.

---

## Les 5 commandes Git qui changent tout (vraiment, juste 5)

Oubliez les tutoriels qui vous balancent 50 commandes. Vous n'avez pas besoin de devenir un expert Git. **Vous avez besoin de 5 commandes. C'est tout.**

Ces 5 commandes couvrent 95% des besoins d'un analyste data. Le reste ? Vous l'apprendrez au fur et à mesure, si vous en avez besoin. Mais pour démarrer et être immédiatement productif, concentrez-vous sur ces 5-là.

### Commande 1 : Créer votre machine à remonter le temps

La première commande transforme un dossier normal en machine à remonter le temps. C'est `git init`. En une fraction de seconde, Git crée un historique vide qui va enregistrer chaque version de votre travail.

Ce qui se passe en coulisses ? Git crée un dossier caché `.git/` dans votre projet. C'est là que toute la magie opère. Vous ne verrez jamais ce dossier, vous n'aurez jamais besoin d'y toucher. Mais c'est lui qui stocke tout : chaque version, chaque modification, chaque point de sauvegarde.

### Commande 2 : Créer un checkpoint (comme dans un jeu vidéo)

Vous avez passé 2 heures à coder une nouvelle analyse. Ça marche. Les graphiques sont beaux. Les chiffres ont du sens. C'est le moment de sauvegarder, avant de continuer.

Avec Git, sauvegarder se fait en deux temps. D'abord, vous "stagez" les fichiers que vous voulez sauvegarder. Puis vous créez le checkpoint avec un message qui explique ce que vous avez fait.

La clé ici, c'est le message. Ne faites jamais l'erreur que tout le monde fait au début : des messages vagues comme "fix", "update", "changes". Dans 3 semaines, vous ne vous souviendrez plus de ce que c'était.

À la place, soyez spécifique. "Ajouter graphique évolution ventes par région". "Corriger bug calcul taux de croissance négatifs". "Mettre à jour données Q4 avec corrections comptables". Votre futur vous dira merci.

### Commande 3 : Explorer votre historique

Imaginez que vous puissiez voir une liste de tous vos points de sauvegarde, avec la date, l'heure, et ce que vous aviez fait à chaque fois. C'est exactement ce que `git log` fait.

Mais la vraie magie, c'est quand vous ajoutez quelques options pour rendre ça lisible. Vous obtenez une vue chronologique de votre projet, comme une frise temporelle. Chaque ligne représente un moment où vous avez dit "OK, ça marche, je sauvegarde".

Cette commande devient votre meilleure amie quand vous cherchez "cette version d'il y a 2 semaines où les calculs étaient justes". Au lieu de fouiller dans 15 fichiers, vous scannez l'historique en 10 secondes.

### Commande 4 : Le bouton "undo" ultime

C'est là que ça devient vraiment puissant. Vous avez expérimenté une nouvelle approche. Vous avez modifié 5 fichiers. Et maintenant, rien ne marche. Vous ne vous rappelez plus exactement ce que vous avez changé.

Sans Git, vous êtes coincé. Vous allez passer 1 heure à debugger, ou à tout recommencer.

Avec Git, vous identifiez dans l'historique le dernier point où tout marchait. Vous prenez son identifiant (un code comme `8b4e5f2`). Et vous restaurez n'importe quel fichier à cet état exact.

**C'est ça, le vrai game-changer.** Vous pouvez expérimenter, casser des trucs, essayer des approches risquées. Si ça marche pas ? Un checkout et vous êtes revenu à la version stable. En 10 secondes.

Un data scientist que je connais m'a dit un jour : *"Depuis que j'utilise Git, je code différemment. Avant, j'avais peur de toucher au code qui marchait. Maintenant, j'expérimente sans arrêt. Parce que je sais que je peux toujours revenir en arrière."*

C'est cette liberté mentale qui change tout.

### Commande 5 : Votre backup cloud gratuit et illimité

La dernière commande pousse tout votre travail sur GitHub. Backup cloud gratuit, illimité, accessible de partout.

Votre laptop peut tomber dans la Seine, votre disque dur peut exploser, votre bureau peut brûler. Votre code est safe sur GitHub. Vous pouvez le récupérer de n'importe où, en 30 secondes.

Mais au-delà du backup, c'est aussi votre portfolio professionnel. Les recruteurs regardent votre GitHub. Les collègues peuvent voir votre code. C'est votre vitrine de compétences, accessible 24/7.

---

## Ces 5 commandes résolvent quoi concrètement ?

Laissez-moi vous raconter deux histoires vraies qui illustrent exactement pourquoi Git change la donne.

### Histoire 1 : La refonte qui a mal tourné

Il y a 6 mois, je bossais sur un dashboard Streamlit pour analyser les performances commerciales d'un client. Tout marchait nickel. Interface intuitive, graphiques réactifs, filtres qui fonctionnaient parfaitement.

Je me lance dans une refonte de l'UI pour la rendre plus moderne. J'expérimente avec de nouveaux composants. Je restructure le code. 2 heures plus tard, plus rien ne fonctionne. L'application crash au démarrage. Et impossible de me rappeler exactement ce que j'ai changé.

Sans Git, j'aurais été coincé pendant des heures. Soit à debugger ligne par ligne, soit à tout recommencer.

Avec Git, j'ai ouvert l'historique, trouvé le dernier commit où tout marchait (45 minutes avant), et restauré la version stable. **Temps perdu : 10 secondes au lieu de 2 heures.**

J'ai ensuite recommencé la refonte, mais cette fois en faisant des petits commits à chaque étape fonctionnelle. Si quelque chose cassait, je savais exactement quel changement était responsable.

### Histoire 2 : "Ressors-moi les chiffres d'il y a 2 mois"

Un analyste avec qui j'ai bossé devait livrer un rapport mensuel. Pas de Git. Juste des fichiers versionnés à la main : `rapport_janvier.py`, `rapport_fevrier.py`, `rapport_mars.py`, etc. À chaque fois qu'il modifiait quelque chose, il copiait le fichier.

Un jour, son manager lui demande : *"Les chiffres que tu m'avais donnés en février étaient plus cohérents avec notre budget prévisionnel. Tu peux me les ressortir ?"*

Le problème ? Il avait 7 versions de scripts différentes. Laquelle était celle de février ? `rapport_v2.py` ? Ou `rapport_v3.py` ? Il a dû ouvrir chaque fichier, regarder la date de modification (pas toujours fiable), exécuter les scripts un par un, comparer les résultats.

**Temps perdu : 1h30.**

Avec Git, ça aurait pris 2 minutes. Chercher dans l'historique les commits de février, identifier le bon, restaurer le script, l'exécuter. Terminé.

### Le pattern que je vois partout

Ces deux histoires illustrent quelque chose que j'observe chez tous les analystes qui adoptent Git : **le changement n'est pas dans les features avancées, mais dans la tranquillité d'esprit.**

Vous codez différemment quand vous savez que vous pouvez revenir en arrière. Vous expérimentez plus. Vous prenez plus de risques. Vous êtes plus créatif.

Et paradoxalement, vous produisez du code de meilleure qualité. Parce que vous n'avez pas peur de refactoriser. Pas peur de tout casser pour tout reconstruire mieux.

---

## Git + DVC : Le duo pour versionner code ET données

OK, Git c'est génial pour le code. Mais qu'en est-il de vos données ?

Votre CSV de 2 Go qui change chaque mois ? Votre base SQLite de 500 Mo ? Vos fichiers Parquet qui évoluent chaque semaine ?

Git ne gère pas bien les gros fichiers. C'est une limitation fondamentale de son architecture. Si vous versionnez un fichier de 2 Go dans Git, votre repo va exploser en taille. Après 10 versions, vous vous retrouvez avec un repo de 20 Go. Les opérations deviennent lentes. Cloner le repo prend 10 minutes. C'est l'enfer.

**C'est là que DVC (Data Version Control) intervient.**

### Le concept de DVC en 3 phrases

DVC, c'est Git mais pour les données. Au lieu de stocker vos gros fichiers dans Git, DVC stocke juste un petit fichier `.dvc` (quelques Ko) qui pointe vers vos vraies données. Ces données, elles, sont stockées ailleurs : Google Drive, Amazon S3, Azure Blob Storage, ou même simplement un disque dur externe.

Le résultat ? Git reste léger et rapide, mais vos données sont quand même versionnées.

### Pourquoi c'est un game-changer pour les analystes

J'ai récemment migré un projet client vers DVC. Avant, leur repo Git faisait 8 Go à cause des datasets versionnés dedans. Chaque nouveau membre de l'équipe devait attendre 20 minutes pour cloner le repo. Les opérations Git étaient devenues insupportablement lentes.

Après migration vers DVC :
- **Repo Git : 65 Mo** (contre 8 Go avant)
- **Temps de clone : 8 secondes** (contre 20 minutes avant)
- **Données versionnées sur S3** : toujours accessibles, mais ne ralentissent plus Git

Le plus impressionnant ? Ils peuvent maintenant revenir à n'importe quelle version de leurs données aussi facilement qu'à n'importe quelle version de leur code. Besoin des données de février pour reproduire une analyse ? Une commande, 30 secondes.

### Le workflow en pratique

Imaginez que vous recevez de nouvelles données chaque mois. Vous les mettez à jour, vous lancez vos analyses, vous générez vos rapports.

Avec DVC, chaque version de vos données est tagguée et liée à la version du code qui l'a produite ou analysée. Dans 6 mois, vous pourrez dire "je veux reproduire exactement l'analyse de mars" et récupérer à la fois le bon code ET les bonnes données.

Sans DVC, vous auriez cherché `sales_march_backup.csv` dans vos archives. En espérant qu'il existe. Et que c'est la bonne version.

### Google Drive comme remote storage (gratuit et simple)

Un truc que j'adore avec DVC, c'est qu'il s'intègre avec Google Drive. Vous avez 15 Go gratuits. C'est amplement suffisant pour versionner les datasets de la plupart des projets d'analyse.

Setup en 5 minutes : vous créez un dossier dans Drive, vous récupérez son ID depuis l'URL, vous configurez DVC pour l'utiliser. Terminé. Vos données sont versionnées et backupées gratuitement.

Pas besoin de S3, de Azure, de serveurs complexes. Juste votre Google Drive que vous avez déjà.

### Benchmark réel : Git seul vs Git + DVC

J'ai fait le test sur un projet d'analyse de données financières. Dataset de 480 Mo (fichiers Parquet) qui évolue chaque mois. 12 versions à versionner.

**Avec Git seul** (versionnant directement les fichiers de données) :
- Taille du repo après 12 mois : **5.8 GB**
- Temps pour cloner : **7 min 30s**
- Temps pour `git status` : **11 secondes** (insupportable au quotidien)
- Consommation disque locale : **5.8 GB**

**Avec Git + DVC** (données sur Google Drive) :
- Taille du repo Git : **52 MB** (juste le code et les pointeurs .dvc)
- Temps pour cloner le code : **4 secondes**
- Temps pour récupérer une version spécifique des données : **~40 secondes** (dépend de la connexion)
- Consommation disque locale : **52 MB + 480 MB** (seulement la version courante des données)

Le choix est vite fait. Et en prime, vos données sont backupées sur le cloud.

---

## Les outils GUI (pour ceux qui préfèrent les boutons)

Écoutez, je vais être honnête avec vous. Le terminal, c'est pas pour tout le monde. Et c'est OK.

Moi-même, pour certaines opérations Git complexes, j'utilise une interface graphique. Pourquoi se compliquer la vie ?

Il y a quelques années, j'étais puriste. "Le terminal c'est mieux, c'est plus puissant, c'est ce que font les vrais devs". Puis j'ai réalisé que je perdais du temps à taper des commandes alors qu'un clic aurait suffi.

Aujourd'hui, j'utilise VS Code pour 80% de mes opérations Git. Et GitKraken quand j'ai un merge conflict complexe ou que je veux visualiser l'historique de branches qui s'entrecroisent.

### Option 1 : VS Code + GitLens (mon préféré au quotidien)

Si vous codez déjà dans VS Code, vous avez Git intégré sans rien installer de plus. Mais installez l'extension GitLens et vous débloquez des superpouvoirs.

GitLens vous montre, directement dans votre code, qui a modifié chaque ligne, quand, et pourquoi (le message du commit). C'est incroyablement utile quand vous vous demandez "pourquoi cette ligne de code bizarre est là".

L'interface est familière. Le panneau "Source Control" sur la gauche liste vos fichiers modifiés. Vous cochez ceux que vous voulez commiter. Vous écrivez votre message. Vous cliquez "Commit". C'est intuitif.

Le gros avantage ? Vous ne quittez jamais votre éditeur. Vous codez, vous commitez, vous continuez à coder. Pas de context-switching.

### Option 2 : GitHub Desktop (parfait pour débuter)

Si Git vous intimide, commencez par GitHub Desktop. L'interface est tellement simple qu'un enfant de 10 ans pourrait l'utiliser.

Pas de jargon technique. Pas de commandes obscures. Juste des boutons clairs : "Commit to main", "Push origin", "Pull origin".

Le seul défaut : c'est focalisé sur GitHub. Si votre équipe utilise GitLab ou Bitbucket, c'est moins optimal. Mais pour 90% des cas (GitHub), c'est parfait.

Une fonctionnalité que j'adore : le diff visuel. Vous voyez exactement ce qui a changé dans chaque fichier, avec les anciennes lignes en rouge et les nouvelles en vert. Vous pouvez même sélectionner ligne par ligne ce que vous voulez commiter.

### Option 3 : GitKraken (le couteau suisse)

GitKraken, c'est l'outil que j'utilise quand les choses deviennent complexes. Merge conflicts avec 3 branches impliquées ? GitKraken. Besoin de cherry-pick des commits spécifiques ? GitKraken. Rebase interactif sur 15 commits ? GitKraken.

La killer feature : **le bouton Undo**.

Vous avez supprimé une branche par erreur ? Undo.  
Vous avez fait un reset --hard qui a tout cassé ? Undo.  
Vous avez mergé la mauvaise branche ? Undo.

Un développeur a tweeté : *"@GitKraken just saved me after a discard all."* Et c'est vrai. Ce bouton m'a sauvé la vie plusieurs fois.

Autre truc génial : le graphe visuel des branches. Vous voyez votre historique Git comme un diagramme, avec toutes les branches qui divergent et se rejoignent. Pour comprendre des projets complexes, c'est irremplaçable.

Le défaut ? C'est payant après 7 jours pour les repos privés. Mais franchement, si vous travaillez en équipe sur des projets complexes, les $4.95/mois sont largement rentabilisés.

### Option 4 : SourceTree (l'alternative gratuite)

Développé par Atlassian, SourceTree est puissant mais... l'interface date de 2015. Fonctionnellement solide, visuellement moche.

Si vous êtes déjà dans l'écosystème Atlassian (Jira, Bitbucket), ça fait sens. Sinon, passez votre chemin.

Un problème frustrant : l'interface diffère entre Windows et Mac. Ce qui complique le support d'équipe quand la moitié utilise Windows et l'autre Mac.

### Mon conseil selon votre profil

**Vous débutez en Git** → GitHub Desktop  
**Vous codez dans VS Code** → VS Code + GitLens  
**Vous êtes en équipe avec projets complexes** → GitKraken Pro  
**Vous êtes dans l'écosystème Atlassian** → SourceTree

Et rappelez-vous : vous pouvez mélanger. Moi j'utilise VS Code pour les commits quotidiens, et GitKraken quand j'ai besoin de visualiser ou manipuler l'historique de façon complexe.

Il n'y a pas de "bonne" réponse. Il y a juste ce qui marche pour vous.

---

## Les 7 erreurs fatales (et comment les éviter en 2 minutes)

Parlons des erreurs que TOUT LE MONDE fait au début. Moi y compris. Autant les connaître pour les éviter.

### Erreur #1 : Commiter vos mots de passe

**Le scénario** : Vous commitez un script qui contient `API_KEY = "sk-1234567890abcdef"`. Vous pushez sur GitHub. Repo public.

**Ce qui se passe** : GitHub vous envoie une alerte dans les 5 minutes. Des bots scannent GitHub 24/7 pour trouver des secrets. Si c'est une vraie API key, elle est compromise avant même que vous ayez fini votre café.

**Comment l'éviter** : Créez un fichier `.gitignore` dès le début qui exclut `.env`, `config.py`, `credentials.json`. Stockez vos secrets dans un fichier `.env` qui n'est jamais commité. Et utilisez `python-dotenv` pour les charger.

Si c'est trop tard ? Il ne suffit PAS de supprimer le fichier et faire un nouveau commit. Le secret est toujours dans l'historique. Il faut réécrire l'historique avec `git filter-repo`, puis révoquer immédiatement le secret compromis.

### Erreur #2 : Messages de commit inutiles

Un développeur sur DEV Community : *"We've all done it: 'fix stuff,' 'asdf,' or my personal favorite—'PLEASE WORK.'"*

Une semaine plus tard, vous cherchez "ce commit où j'avais corrigé le bug de calcul". Vous ouvrez l'historique. 15 commits qui disent "fix". Bonne chance.

**Comment l'éviter** : Format simple — Verbe + Quoi + Pourquoi optionnel. "Fix calcul taux croissance (divisait par zéro)". "Add graphique évolution ventes par région". "Update données Q4 avec corrections comptables".

Pas besoin d'écrire un roman. 50-60 caractères max. Mais soyez spécifique.

### Erreur #3 : Commits géants avec 47 fichiers

Vous codez 6 heures d'affilée. Vous modifiez 15 fichiers. Vous ajoutez 3 features, corrigez 2 bugs, refactorez du code. Et vous faites un seul commit : "Mise à jour du projet".

**Le problème** : Impossible de revenir en arrière sur une seule feature. Et si un bug apparaît, bon courage pour identifier quel changement l'a introduit.

**Comment l'éviter** : Commits atomiques. Un commit = une chose. Règle simple : si vous mettez "et" dans votre message, c'est que vous commitez trop de choses à la fois.

### Erreur #4 : Versionner des fichiers de 500 Mo

Vous versionnez un Excel de 200 Mo ou une vidéo dans Git. Votre repo passe de 10 Mo à 500 Mo. Cloner prend 10 minutes au lieu de 5 secondes. Vos collègues vous détestent.

**Comment l'éviter** : Pour les données, utilisez DVC. Pour les assets binaires (images, vidéos), utilisez Git LFS. Pour tout ce qui n'a pas besoin d'être versionné, ajoutez-le au `.gitignore`.

### Erreur #5 : Travailler directement sur `main`

Vous commencez à coder une nouvelle analyse directement sur `main`. Vous cassez quelque chose. Le code ne marche plus. Votre collègue pull et son environnement explose aussi.

**Comment l'éviter** : Branches feature. Avant tout nouveau développement : créez une branche. Expérimentez sur cette branche. Quand tout marche, mergez dans `main`. `main` reste toujours stable.

### Erreur #6 : Oublier de pull avant de push

Vous essayez de pusher. Erreur : "Updates were rejected because the remote contains work that you do not have locally".

Votre collègue a pushé pendant que vous bossiez. Votre version est obsolète.

**Comment l'éviter** : Toujours pull AVANT de push. Encore mieux : prenez l'habitude de pull au début de chaque session de travail. Vous êtes à jour, vous pouvez bosser sereinement.

### Erreur #7 : Force push sans comprendre

Vous trouvez une commande sur StackOverflow : `git push --force`. Vous lancez. Vous venez d'écraser 3 commits sur le repo distant. Y compris le travail de vos collègues.

**Comment l'éviter** : JAMAIS de `--force` sur des branches partagées (`main`, `develop`). Le seul cas acceptable : votre branche feature personnelle, avant de créer une pull request. Et même là, utilisez `--force-with-lease` qui refuse si quelqu'un a pushé entre temps.

---

## Du chaos au workflow qui tourne tout seul

Maintenant qu'on a vu les concepts, parlons de comment ça se passe concrètement dans votre quotidien.

### Le setup initial : 30 minutes pour ne plus jamais en perdre

La première fois que vous mettez en place Git + DVC sur un projet, ça prend du temps. Faut être honnête. Mais c'est un investissement qui se rentabilise dès le premier mois.

Vous créez votre structure de projet. Vous configurez le `.gitignore` pour exclure les fichiers temporaires, les environnements Python, les données brutes. Vous initialisez Git. Vous configurez DVC pour pointer vers Google Drive ou S3. Vous faites votre premier commit.

**Temps investi : 30 minutes.**

Mais après ? Chaque mise à jour prend 5 minutes max. Et vous économisez 2-3 heures par mois à ne plus chercher "la bonne version".

Pour vous faciliter la vie, j'ai créé un template complet avec tout configuré. Structure de projet, `.gitignore` optimisé pour analystes, exemples de scripts, configuration DVC de base. **Tout est sur GitHub : github.com/gpenessot/git-for-analysts-starter**

Clonez-le, adaptez-le à vos besoins, et vous partez avec une base solide.

### La routine mensuelle qui devient un réflexe

Tous les mois, vous recevez de nouvelles données. Voici votre routine :

Vous mettez à jour vos fichiers de données. DVC détecte le changement. Vous commitez la nouvelle version avec un message clair ("Update données ventes - décembre 2024"). Vous pushez le code sur GitHub, les données sur Drive. Vous régénérez vos rapports avec les nouvelles données.

**Total : 5 minutes de travail Git/DVC.**

Le reste du temps, vous l'investissez dans ce qui compte vraiment : analyser les tendances, identifier les insights, créer de la valeur.

### Le moment où ça sauve votre peau

Trois mois plus tard, votre manager débarque : *"Les chiffres de septembre avaient l'air plus cohérents. Tu peux me ressortir exactement ce que tu m'avais montré ?"*

Sans Git + DVC, c'est la panique. Vous fouillez dans vos archives. Vous espérez avoir gardé la bonne version. Vous croisez les doigts.

Avec Git + DVC, vous ouvrez l'historique, vous trouvez le commit de septembre, vous restaurez code ET données, vous relancez l'analyse. **Temps total : 2 minutes.**

Et vous obtenez exactement les mêmes résultats qu'en septembre. Parce que vous avez reproduit exactement le même environnement.

---

## Le défi pour vous cette semaine

Stop la théorie. Passons à l'action.

Je ne vais pas vous demander de lire 3 livres sur Git. Je vais vous demander quelque chose de simple et mesurable : **créez votre premier repo Git cette semaine.**

### Ce que vous allez faire concrètement

Choisissez un projet simple que vous avez déjà. Un script Python que vous utilisez régulièrement. Un notebook Jupyter d'analyse. Un rapport Quarto. Même un fichier SQL avec vos requêtes favorites.

Pas besoin que ce soit parfait. Pas besoin que ce soit un gros projet. L'important, c'est de pratiquer.

Initialisez Git dans ce projet. Faites 3 commits minimum, représentant 3 étapes de votre travail. Poussez sur GitHub (repo privé si vous préférez garder ça confidentiel).

**Temps estimé : 30 minutes max.**

Si vous avez des données >100 Mo, ajoutez DVC. Configurez Google Drive comme remote. Versionnez vos données.

**Temps additionnel : 15 minutes.**

### Le repo template pour vous faciliter la vie

J'ai préparé un repo complet avec tout ce qu'il faut pour démarrer. Structure de projet recommandée. `.gitignore` pré-configuré pour analystes (Python, R, Jupyter, CSV, Excel, etc.). Configuration DVC de base. Scripts d'exemple.

**👉 github.com/gpenessot/git-for-analysts-starter**

Clonez-le, explorez-le, adaptez-le. C'est le point de départ parfait.

Vous y trouverez aussi un **TUTORIAL.md complet** avec toutes les commandes étape par étape, des exemples concrets, et les solutions aux problèmes courants.

### Les 3 meilleurs gagnent

Pour vous motiver, j'offre des prix aux 3 meilleures adoptions.

Partagez votre expérience sur LinkedIn avant le **15 janvier 2025**. Postez des captures d'écran de votre repo GitHub. Expliquez ce que vous versionnez, pourquoi, et le gain de temps estimé. Taggez-moi (@gaelpenessot) avec **#GitPourAnalystes**.

**Les 3 meilleurs posts gagnent** :

1. **🏆 Un call 1-to-1 de 30 min** pour optimiser votre workflow Git + revue de code de votre projet
2. **🥈 Accès early bird à SQL Mastery** (valeur 50€) + accès beta à la future formation LinkedIn Learning sur Polars
3. **🥉 Featured dans la newsletter de janvier** avec promotion de votre profil LinkedIn + repo partagé à 1000+ lecteurs

### Pourquoi partager publiquement ?

Parce que ça vous engage. Quand vous dites publiquement "je me lance dans Git", vous vous créez une accountability. Et en prime, vous aidez d'autres personnes qui hésitent à se lancer.

---

## De la peur à la confiance

Il y a 5 ans, Git me faisait peur. J'avais peur de tout casser. Peur de perdre mon travail. Peur de faire une mauvaise manipulation et de ruiner un projet entier.

Cette peur venait d'une méconnaissance. Je ne comprenais pas vraiment comment Git fonctionnait sous le capot. Alors j'imaginais des scénarios catastrophe qui n'existaient pas.

Aujourd'hui, Git c'est mon filet de sécurité. C'est l'outil qui me permet d'expérimenter sans peur. De refactoriser sans stress. De tester des approches risquées en sachant que je peux toujours revenir en arrière.

Grâce à Git, je peux :
- Expérimenter sans peur de tout casser → J'essaie des approches nouvelles que je n'aurais jamais tentées avant
- Revenir en arrière quand ça marche pas → En 10 secondes, pas en 2 heures de debug
- Collaborer sans écraser le travail des autres → Chacun travaille sur sa branche, on merge proprement
- Travailler sur plusieurs features en parallèle → Context switching facile entre branches

Un témoignage d'un data analyst sur StackOverflow résume parfaitement :

*"The time I have saved by having the option to rewind has single-handedly paid back my investment in learning a version control system many, many times. Sometimes the report just looked better 45 minutes ago."*

C'est exactement ça. Git ne vous rend pas seulement plus productif. **Il change votre façon de travailler.**

Vous n'avez pas besoin de maîtriser 50 commandes. Vous n'avez pas besoin de comprendre tous les détails techniques du fonctionnement interne de Git. Vous avez besoin des 5 commandes que je vous ai données, d'un outil GUI si vous préférez les boutons, et de la volonté de tester.

Le reste viendra naturellement, au fur et à mesure que vous pratiquez.

---

## Les ressources pour aller plus loin

**Cheat sheets visuels** :
- Git Cheat Sheet interactif : https://ndpsoftware.com/git-cheatsheet.html (cliquez sur les commandes, ça montre ce qu'elles font)
- GitHub Git Cheat Sheet : https://education.github.com/git-cheat-sheet-education.pdf

**Tutoriels interactifs** :
- Learn Git Branching : https://learngitbranching.js.org/ (apprenez en jouant, c'est génial)
- Git Katas : https://github.com/eficode-academy/git-katas (exercices progressifs)

**Documentation** :
- Pro Git (livre gratuit) : https://git-scm.com/book/en/v2 (la bible, mais dense)
- DVC Documentation : https://dvc.org/doc/start (très bien faite)
- GitHub Skills : https://skills.github.com/ (parcours guidés gratuits)

**Vidéos** :
- Git Explained in 100 Seconds (Fireship) : Parfait pour comprendre les concepts en 2 minutes
- GitKraken Git Tutorials : Série complète pour débutants avec interface graphique

**Mon repo template** :
- github.com/gpenessot/git-for-analysts-starter : Structure complète, `.gitignore` configuré, exemples DVC, TUTORIAL complet

---

## Ce qui arrive en janvier

La newsletter de janvier couvrira **Luigi : L'orchestration pour analystes qui ne veulent pas devenir DevOps**.

Si vous automatisez déjà vos rapports avec Python (comme on a vu dans la newsletter #4 avec Quarto), vous allez adorer Luigi.

Imaginez : votre rapport se génère automatiquement chaque lundi matin. Vos données se mettent à jour seules. Vos dashboards se refreshent sans intervention. Vos pipelines gèrent les dépendances intelligemment.

Tout ça avec du Python pur. Sans Airflow. Sans Kubernetes. Sans serveurs complexes. Juste Luigi qui orchestre tout en local ou dans le cloud.

On se retrouve le mois prochain pour découvrir comment passer de scripts manuels à pipelines robustes qui tournent en production.

---

**P.S.** — Vous connaissez quelqu'un qui galère encore avec `rapport_v2_final_vraiment_final.xlsx` ? Transférez-lui cette newsletter. Il vous remerciera. 😉

**P.P.S.** — Si vous testez Git cette semaine, envoyez-moi un message avec vos questions. Je réponds à tous les emails. Vraiment tous.

Gaël

---

## Questions fréquentes

**Q: Git va remplacer mon workflow actuel ?**  
R: Non. Git **complète** votre workflow. Vous continuez à coder dans votre IDE préféré. Vous ajoutez juste Git pour versionner proprement au lieu de dupliquer des fichiers.

**Q: Est-ce que je peux utiliser Git avec Excel/Power BI ?**  
R: Excel oui, mais pas optimal (fichiers binaires). Mieux vaut exporter en CSV et versionner le CSV. Power BI non (fichiers .pbix trop lourds). Versionnez plutôt vos scripts Power Query et DAX extraits en texte.

**Q: DVC est-il obligatoire ?**  
R: Non. Si vos données font <100 Mo, Git seul suffit. DVC devient indispensable au-delà de 100-200 Mo par fichier.

**Q: Mon IT bloque GitHub, que faire ?**  
R: Git fonctionne en local même sans serveur distant. Vous versionnez localement. Si besoin de partager, utilisez un serveur Git interne (GitLab self-hosted, Gitea, etc.).

**Q: Combien de temps avant de maîtriser Git ?**  
R: Les 5 commandes de base : **1 heure de pratique**. Être autonome sur 90% des cas : **2-3 semaines**. Expert : 6+ mois (mais pas nécessaire pour un analyste).

**Q: Ça fonctionne sur Windows ?**  
R: Oui. Git, DVC, tous les outils GUI sont multiplateformes (Windows, Mac, Linux).

**Q: Je peux utiliser Git pour mes notebooks Jupyter ?**  
R: Oui, mais le format `.ipynb` (JSON) crée des diffs illisibles. Solution : utilisez `nbdime` pour des diffs propres, ou mieux, utilisez Marimo/Quarto (fichiers texte purs, diffs lisibles).
