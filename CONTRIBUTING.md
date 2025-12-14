# Contribuer au Projet

Merci de votre intérêt pour ce projet ! Ce template est conçu pour la communauté des analystes de données qui souhaitent adopter Git et DVC.

---

## 🎯 Participer au Défi Newsletter

Si vous participez au défi de la [Newsletter DataGyver #10](https://datagy.substack.com/), voici comment partager votre expérience :

### Étapes pour Participer

1. **Utilisez ce template** pour créer votre propre projet
2. **Suivez le TUTORIAL.md** pour faire votre premier repo Git
3. **Partagez votre expérience sur LinkedIn** avant le **15 janvier 2025**

### Format du Post LinkedIn

Voici un template de post pour partager votre adoption de Git :

```markdown
🚀 Je viens de créer mon premier repo Git pour mes analyses de données !

Grâce au template de @gaelpenessot, j'ai pu :
✅ Versionner mon code proprement (plus de fichier_v2_final.xlsx !)
✅ Configurer DVC pour mes données volumineuses
✅ Mettre en place un workflow reproductible

📊 Mon projet : [Lien vers votre repo GitHub]

💡 Temps investi : ~30 minutes
🎯 Gain de temps estimé : ~78h par an

#GitPourAnalystes #DataAnalytics #Python #Git

---
Défi inspiré de la newsletter DataGyver → https://datagy.substack.com/
```

### Que Partager ?

Dans votre post, incluez :

- **Screenshot de votre repo GitHub** (montrez la structure, les commits)
- **Screenshot de votre historique Git** (`git log --oneline --graph`)
- **Votre cas d'usage** (quel projet vous versionnez ?)
- **Le gain de temps estimé** pour votre workflow
- **Les difficultés rencontrées** (si vous en avez eu)

### Taggez-moi !

- LinkedIn : [@gaelpenessot](https://linkedin.com/in/gaelpenessot/)
- Utilisez le hashtag : **#GitPourAnalystes**

### Prix pour les 3 Meilleurs Posts

🏆 **1er Prix** : Call 1-to-1 de 30 min + revue de code personnalisée

🥈 **2ème Prix** : Accès early bird SQL Mastery + Accès beta formation LinkedIn Learning Polars

🥉 **3ème Prix** : Featured dans la newsletter de janvier + promotion de votre profil auprès de 1000+ lecteurs

---

## 🐛 Signaler un Bug

Si vous trouvez un bug dans le template :

1. Vérifiez qu'il n'a pas déjà été signalé dans les [Issues](https://github.com/gpenessot/git-for-analysts-starter/issues)
2. Ouvrez une nouvelle Issue avec :
   - Une description claire du problème
   - Les étapes pour reproduire le bug
   - Votre environnement (OS, version Python)
   - Les messages d'erreur complets

---

## 💡 Proposer une Amélioration

Vous avez une idée pour améliorer le template ?

1. Ouvrez une [Issue](https://github.com/gpenessot/git-for-analysts-starter/issues) avec le tag `enhancement`
2. Décrivez votre proposition
3. Expliquez pourquoi cela serait utile pour les analystes

---

## 🔧 Contribuer au Code

Si vous souhaitez contribuer du code :

### Setup Local

```bash
# Cloner le repo
git clone https://github.com/gpenessot/git-for-analysts-starter.git
cd git-for-analysts-starter

# Créer l'environnement
uv venv
source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows
uv pip install -r requirements.txt

# Installer les pre-commit hooks
pre-commit install
```

### Workflow de Contribution

1. **Créez une branche** pour votre feature
   ```bash
   git checkout -b feature/ma-super-feature
   ```

2. **Faites vos modifications**
   - Assurez-vous que le code passe les tests pre-commit
   - Ajoutez de la documentation si nécessaire

3. **Testez vos changements**
   ```bash
   # Lancer pre-commit sur tous les fichiers
   pre-commit run --all-files

   # Tester les scripts
   python scripts/load_data.py data/raw/sales_december_2024.csv data/processed/test.parquet
   python scripts/analyze.py data/processed/test.parquet

   # Vérifier le notebook Marimo
   marimo check notebooks/01_exploration.py
   ```

4. **Commitez avec un message clair**
   ```bash
   git commit -m "feat(scripts): add data validation function"
   ```

5. **Poussez et créez une Pull Request**
   ```bash
   git push origin feature/ma-super-feature
   ```

### Conventions de Code

- **Python** : Nous utilisons Ruff pour le linting et le formatage
- **Messages de commit** : Format `type(scope): description`
  - Types : `feat`, `fix`, `docs`, `style`, `refactor`, `test`
  - Exemple : `feat(dvc): add S3 remote configuration example`
- **Documentation** : Toute nouvelle feature doit être documentée

---

## 📚 Ressources

- [Newsletter DataGyver](https://datagy.substack.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [DVC Documentation](https://dvc.org/doc)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

---

## 📞 Questions ?

- Ouvrez une [Issue](https://github.com/gpenessot/git-for-analysts-starter/issues)
- Contactez-moi sur [LinkedIn](https://linkedin.com/in/gaelpenessot/)

---

**Merci de contribuer à rendre Git plus accessible aux analystes de données !** 🚀
