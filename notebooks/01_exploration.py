import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def __():
    from io import StringIO

    import marimo as mo
    import plotly.express as px
    import polars as pl

    return StringIO, mo, pl, px


@app.cell
def __(mo):
    mo.md("# Exploration des Données avec Marimo")
    return


@app.cell
def __(mo):
    mo.md(
        """
        Ce notebook est un exemple d'analyse exploratoire utilisant **Marimo**.
        Marimo est un notebook réactif pour Python qui stocke les fichiers en `.py` purs,
        le rendant parfait pour le versioning avec Git. Les "diffs" sont lisibles et le repo reste léger.
        """
    )
    return


@app.cell
def __(StringIO, pl):
    # --- Création d'un DataFrame de démonstration ---
    # Dans un vrai projet, vous liriez des données depuis `data/processed/`
    csv_data = """
    date,product,sales,region
    2024-01-01,Product_A,150,North
    2024-01-01,Product_B,220,South
    2024-01-02,Product_A,160,North
    2024-01-02,Product_B,240,South
    2024-01-03,Product_A,180,North
    2024-01-03,Product_C,300,North
    2024-01-04,Product_B,280,South
    2024-01-04,Product_C,320,North
    """
    df = pl.read_csv(StringIO(csv_data))
    df = df.with_columns(pl.col("date").str.to_date(format="%Y-%m-%d"))
    return csv_data, df


@app.cell
def __(mo):
    mo.md("### 1. Aperçu des Données Brutes")
    return


@app.cell
def __(df, mo):
    mo.ui.table(df, selection=None)
    return


@app.cell
def __(mo):
    mo.md("### 2. Statistiques Descriptives")
    return


@app.cell
def __(df, mo):
    mo.ui.table(df.describe(), selection=None)
    return


@app.cell
def __(mo):
    mo.md("### 3. Analyse et Visualisation")
    return


@app.cell
def __(df, mo):
    region_selector = mo.ui.slider(
        start=1,
        stop=len(df["region"].unique()),
        value=len(df["region"].unique()),
        step=1,
        label="Top N Régions:",
    )
    region_selector
    return (region_selector,)


@app.cell
def __(df, mo, pl, px):
    # --- Graphiques interactifs ---
    sales_by_day = df.group_by("date").agg(pl.sum("sales").alias("total_sales"))
    fig_line = px.line(
        sales_by_day.to_pandas(),
        x="date",
        y="total_sales",
        title="Évolution des ventes journalières",
    )

    sales_by_product = df.group_by("product").agg(pl.sum("sales").alias("total_sales"))
    fig_bar = px.bar(
        sales_by_product.to_pandas(),
        x="product",
        y="total_sales",
        title="Ventes totales par produit",
    )

    # Affiche les deux graphiques côte à côte
    mo.hstack([fig_line, fig_bar])
    return fig_bar, fig_line, sales_by_day, sales_by_product


@app.cell
def __(mo):
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
    return


if __name__ == "__main__":
    app.run()
