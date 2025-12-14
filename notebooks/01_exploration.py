import marimo as mo
import polars as pl
import plotly.express as px
from io import StringIO

mo.md("# Exploration des Données avec Marimo")

mo.md(
    """
    Ce notebook est un exemple d'analyse exploratoire utilisant **Marimo**.
    Marimo est un notebook réactif pour Python qui stocke les fichiers en `.py` purs,
    le rendant parfait pour le versioning avec Git. Les "diffs" sont lisibles et le repo reste léger.
    """
)

# --- Création d'un DataFrame de démonstration ---
# Dans un vrai projet, vous liriez des données depuis `data/processed/`
csv_data = """
date,product,sales,region
2024-01-01,A,150,North
2024-01-01,B,220,South
2024-01-02,A,160,North
2024-01-02,B,240,South
2024-01-03,A,180,North
2024-01-03,C,300,North
2024-01-04,B,280,South
2024-01-04,C,320,North
"""
df = pl.read_csv(StringIO(csv_data))
df = df.with_columns(pl.col("date").str.to_date(format="%Y-%m-%d"))

mo.md("### 1. Aperçu des Données Brutes")
mo.ui.table(df, selection=None)

mo.md("### 2. Statistiques Descriptives")
mo.ui.table(df.describe(), selection=None)


mo.md("### 3. Analyse et Visualisation")

region_selector = mo.ui.slider(start=1, stop=len(df['region'].unique()), value=len(df['region'].unique()), step=1, label="Top N Régions:")
region_selector

# --- Graphiques interactifs ---
sales_by_day = df.group_by("date").agg(pl.sum("sales").alias("total_sales"))
fig_line = px.line(
    sales_by_day.to_pandas(),
    x='date',
    y='total_sales',
    title='Évolution des ventes journalières'
)

sales_by_product = df.group_by("product").agg(pl.sum("sales").alias("total_sales"))
fig_bar = px.bar(
    sales_by_product.to_pandas(),
    x='product',
    y='total_sales',
    title='Ventes totales par produit'
)

# Affiche les deux graphiques côte à côte
mo.hstack([fig_line, fig_bar])


mo.md(
    """
    ---
    **Conclusion :** Ce format `.py` est facile à lire et à comparer dans une Pull Request.
    Les changements sont clairs, contrairement aux diffs JSON des fichiers `.ipynb`.

    Pour lancer ce notebook, utilisez la commande à la racine du projet :
    ```bash
    marimo edit notebooks/01_exploration.py
    ```
    """
)
