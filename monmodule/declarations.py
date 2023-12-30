# I- Déclaration des modules

# I-1. Imports liés à l'analyse de données et à la visualisation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output

# I-2. Imports liés à la manipulation de données
import pycountry
from statistics import mean, median, stdev
import io
from io import BytesIO

# I-3. Imports liés à la modélisation et à la statistique
import statsmodels.api as sm
import statsmodels.tsa.filters.hp_filter as smf
import statsmodels.tsa.ardl as sma
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

# I-4.  Imports liés à l'apprentissage automatique
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

# I-5. Autres imports
import zipfile
import requests
import os
import missingno as msno
from scipy.signal import find_peaks

# Pour assurer la reproductibilité de nos résultats, on définit la graine aléatoire sur 123

np.random.seed(123)

# II- Déclaration des fonctions

# II-1. Téléchargement du fichier


def load(url, nom_fichier):
    response = requests.get(url)

    """Vérifier si le téléchargement a réussi (code d'état 200)"""
    if response.status_code == 200:
        """Enregistrer le contenu dans un fichier ("nom_fichier")"""
        chemin_fichier = os.path.join('bases', nom_fichier)
        with open(chemin_fichier, "wb") as file:
            file.write(response.content)
        print("Téléchargement de base", nom_fichier, "réussi.")
    else:
        print(f"Erreur de téléchargement : {response.status_code}")


# II-2. Fonction d'extraction de base dans un fichier zippé


def extraire_fichier_zip(chemin_zip, nom_fichier, nom_feuille):
    with zipfile.ZipFile(chemin_zip, "r") as zip_ref:
        with zip_ref.open(nom_fichier) as fichier_in_zip:
            df = pd.read_excel(
                BytesIO(fichier_in_zip.read()), sheet_name=nom_feuille, header=0
            )

            if nom_feuille == "quarterly":
                df = df.rename(columns={"Unnamed: 0": "Year"}).assign(
                    Year=lambda x: x["Year"].astype(str).str.rstrip(".0")
                )
                """ Convertir la colonne 'Year' en format de date trimestriel """
                df["Year"] = pd.to_datetime(df["Year"], format="%YQ%m")
                """ Définir 'Year' comme index pour faciliter la manipulation des périodes """
                df.set_index("Year", inplace=True)
            elif nom_feuille == "monthly":
                df = df.rename(columns={"Unnamed: 0": "Year"}).assign(
                    Year=lambda x: x["Year"].astype(str).str.rstrip(".0")
                )
                # Convertir la colonne 'Year' en format de date mensuelle
                df["Year"] = pd.to_datetime(df["Year"], format="%YM%m")
                """ Définir 'Year' comme index pour faciliter la manipulation des périodes """
                df.set_index("Year", inplace=True)

            return df


# II-3. Méthode search_fuzzy de pycountry pour corrections des noms des pays


def correct_country_name(col_names):
    countries_detected = []
    """ Dictionnaire de correspondance entre noms complets des pays et leurs codes """
    corresp = {
        country.name: country.alpha_3 for country in pycountry.countries
        }

    for name in col_names:
        try:
            # Essayer de trouver le pays par son nom
            country = pycountry.countries.search_fuzzy(name)[0]
            # Transformation des noms complets des colonnes en abréviations
            abbreviation = corresp.get(country.name, country.name)
            countries_detected.append(abbreviation)
        except (LookupError, IndexError):
            # Conserver les noms qui ne correspondent à aucun pays
            countries_detected.append(name)

    return countries_detected

    # def detect_country_name(col_names):
    countries_detected = []

    for name in col_names:
        try:
            # Essayer de trouver le pays par son nom
            pays = pycountry.countries.search_fuzzy(name)[0]
            countries_detected.append(pays.name)
        except LookupError:
            # Ignorer les noms qui ne correspondent à aucun pays
            pass

    return countries_detected


def detect_country_name(col_names):
    countries_detected = []
    """ Dictionnaire de correspondance entre noms complets des pays et leurs codes """
    corresp = {
        country.name: country.alpha_3 for country in pycountry.countries
        }

    for name in col_names:
        # Vérifier si le nom de colonne est une abréviation existante
        if name in corresp.values():
            countries_detected.append(name)

    return countries_detected


# II-4. Visualisation des données manquantes 


def missing_plot(df):
    """
    Visualise les valeurs manquantes avec un diagramme à barres et un heatmap.
    Utilise les bibliothèques missingno et seaborn.
    """
    # Diagramme à barres des valeurs manquantes
    msno.bar(df)
    plt.title(
        r"$\bf{Diagramme\ à\ barres\ des\ valeurs\ manquantes}$", color="green"
        )
    plt.show()

    # Heatmap des valeurs manquantes
    sns.heatmap(df.isna(), cbar=False)
    plt.title(r"$\bf{Heatmap\ des\ valeurs\ manquantes}$", color="green")
    plt.show()


# II-5. Suppression des valeurs manquantes


def missing(df):
    # Suppression de certaines valeurs manquantes
    df.dropna(axis=1, thresh=len(df) * 0.9, inplace=True)

    print("Pourcentage de valeurs manquantes par variable")
    print(
        (df.isna().sum() / len(df) * 100)[df.isna().any()].sort_values(ascending=False)
        )
    return df


#II-6. Imputation des valeurs manquantes


def fill_missing_with_median(df, window_size=30):
    """ Utiliser apply avec une fonction lambda pour remplir les valeurs manquantes"""
    df_filled = df.apply(
        lambda col: col.fillna(
            col.shift(-window_size).rolling(window=window_size, min_periods=1).median()
        )
    )
    """ Remplir les valeurs manquantes en fin de base avec les valeurs précédentes """
    df = df_filled.ffill(axis=0)

    return df


# II-7. Extraction de données dans une base 


def extract2(big_data, keyword1, keyword2):
    # Créer le masque
    mask = big_data["Indicator Name"].str.contains(keyword1, case=False) & big_data[
        "Indicator Name"
    ].str.contains(keyword2, case=False, regex=True)

    # Appliquer le masque pour obtenir un nouveau DataFrame
    df = big_data[mask]

    return df


# II-8. Traitement des données extraites pour constituer une base


def treat_info(df, codes):
    """ vérification des doublons """
    print(
        "Nombre total de doublons dans la base est:", df[df.duplicated()].shape[0]
        )

    """ Filtrer les colonnes qui contiennent des années ou les noms des pays: regex """
    col = df.columns[df.columns.str.contains(r"\d{4}|Indicator Name|Country Code")]

    # Créer un nouveau DataFrame avec les colonnes filtrées
    df = df[col]

    df = df.drop(columns="Indicator Name")

    df.set_index("Country Code", inplace=True)

    # transposer
    df = df.transpose()

    # Sélectionner à partir de l'année 1994
    df = df.loc["1994":]

    # Convertir l'index en datetime
    df.index = pd.to_datetime(df.index, format="%Y")

    # Utiliser resample pour convertir les données en trimestrielles
    df = df.resample("Q").mean()

    # Remplir les valeurs manquantes avec la méthode forward fill
    df.ffill(inplace=True)

    # Ignorer les jours dans l'index
    df.index = df.index.to_period("Q").strftime("%Y-Q%q")

    # Appliquer le format trimestre au index
    df.index = pd.to_datetime(df.index + "-01", format="%Y-Q%m-%d")

    # Formater l'index pour obtenir '1994-01' au lieu de '1994-01-01'
    df.index = df.index.strftime("%Y-%m")

    # selectionner les pays qui sont les bases precedentes
    df = df[codes]

    return df


# II-9. Transformation des bases en formant long 


def transform(df, nom):
    df["YEAR"] = df.index

    # Utiliser la méthode melt pour transformer le DataFrame
    df_transformed = pd.melt(
        df, id_vars="YEAR", var_name="COUNTRY", value_name=nom
        )

    # Trier le DataFrame par 'ID' pour ordonner
    df_transformed.sort_values(by="YEAR", inplace=True)

    # Réinitialiser l'index si nécessaire
    df_transformed.reset_index(drop=True, inplace=True)
    return df_transformed


# II-10. Analyse des séries temporellesś


def analyse_serie_temporelle_pays(data, indicateur, pays):
    df = data.copy()
    # Utilisation de la fonction pivot pour remodeler le dataframe
    df = df.pivot(index=['YEAR'], columns='COUNTRY', values=indicateur)
    df['YEAR'] = pd.to_datetime(df.index)

    # Sélectionner la série temporelle du pays spécifique
    serie_temporelle = df[pays].dropna()

    # Moyenne mobile d'ordre 4
    rolling_mean = serie_temporelle.rolling(window=4).mean()

    # Visualisation de la série temporelle et de la moyenne mobile dans le même plot
    plt.figure(figsize=(10, 6))
    plt.plot(serie_temporelle, label=f'Série Temporelle - {indicateur} en {pays}', color='blue')
    plt.plot(rolling_mean, label='Moyenne Mobile', color='red')
    plt.title(f'Série Temporelle et Moyenne Mobile - {indicateur} en {pays}')
    plt.legend()
    plt.show()

    # Décomposition saisonnière
    decomposition = seasonal_decompose(serie_temporelle, model='multiplicative', period=4)

    # Visualisation des composants décomposés
    plt.figure(figsize=(12, 8))

    # Série Temporelle
    plt.subplot(4, 1, 1)
    plt.plot(serie_temporelle)
    plt.title(f'Série Temporelle - {indicateur} en {pays}')

    # Tendance
    plt.subplot(4, 1, 2)
    plt.plot(decomposition.trend)
    plt.title('Tendance')

    # Saisonnalité
    plt.subplot(4, 1, 3)
    plt.plot(decomposition.seasonal)
    plt.title('Saisonnalité')

    # Résidus
    plt.subplot(4, 1, 4)
    plt.plot(decomposition.resid)
    plt.title('Résidus')

    plt.tight_layout()
    plt.show()

    # Test de stationnarité (Augmented Dickey-Fuller)
    result = adfuller(serie_temporelle)
    print(f'Test de Dickey-Fuller Augmenté:\nStatistique de test = {result[0]}\nValeur critique (5%) = {result[4]["5%"]}')
