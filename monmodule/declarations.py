# Déclaration des modules
# Importation des bases des packages

import pycodestyle as pep8 # not used
import zipfile
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pycountry
import io
from io import BytesIO
import seaborn as sns
import missingno as msno
<<<<<<< HEAD
from statistics import *
import panel as pn
import hvplot.pandas
import geopandas as gpd


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import plotly.express as px

=======
import statistics 
>>>>>>> c384057ace56608a429d326a4945f7e32fc56241

np.random.seed(123)



"""
class MonProjet:
    def __init__(self) -> None:
        self.f_gmd = "GMD"
        self.f_countrycode = "countrycode"
        self.f_countryname = "countryname"
        self.f_year = "year"
        self.f_region = "region"
        self.f_regionname = "regionname"
        self.f_incomelevelname = "incomelevelname"
        self.f_lendingtypename = "lendingtypename"
        self.f_index = "index"
        self.f_between = "between"
        self.f_within = "within"
        self.f_noregion = "noregion"
        self.f_nobs = "nobs"
        self.f_minwelfare_median = "minwelfare_median"
        self.f_maxwelfare_median = "maxwelfare_median"
        self.f_minwelfare_mean = "minwelfare_mean"
        self.f_maxwelfare_mean = "maxwelfare_mean"
        self.f_minwelfare_b1 = "minwelfare_b1"
        self.f_maxwelfare_b1 = "maxwelfare_b1"
        self.f_minwelfare_t1 = "minwelfare_t1"
        self.f_maxwelfare_t1 = "maxwelfare_t1"
        self.f_ineq = "ineq"
        self.f_withinreg = "withinreg"
        self.f_ny_gdp_pcap_pp_kd = "ny_gdp_pcap_pp_kd"
        self.f_sp_urb_totl_in_zs = "sp_urb_totl_in_zs"
        self.f_sp_pop_totl = "sp_pop_totl"
        self.f_en_urb_lcty_ur_zs = "en_urb_lcty_ur_zs"
        self.f_si_pov_lmic = "si_pov_lmic"
        self.f_loggdp = "loggdp"
        self.f_logpop = "logpop"
        self.f_pib = "pib"
        self.f_unemployment_rate = "unemployment_rate"

        #Rajouter les méthodes
        pass """


# Déclaration des fonctions

# Télécharger le fichier


def load(url, nom_fichier):
    response = requests.get(url)

    """Vérifier si le téléchargement a réussi (code d'état 200)"""
    if response.status_code == 200:
        """Enregistrer le contenu dans un fichier ("nom_fichier")"""
        with open(nom_fichier, "wb") as file:
            file.write(response.content)
        print("Téléchargement de base", nom_fichier, "réussi.")
    else:
        print(f"Erreur de téléchargement : {response.status_code}")


# Fonction d'extraction de base dans un fichier zippé


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


# Méthode search_fuzzy de pycountry pour corrections des noms des pays
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


# ********** visualisation des données manquantes ***********#
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


# *********** affichage des valeurs manquantes **********#


def missing(df):
    # Suppression de certaines valeurs manquantes
    df.dropna(axis=1, thresh=len(df) * 0.9, inplace=True)

    print("Pourcentage de valeurs manquantes par variable")
    print(
        (
        df.isna().sum() / len(df) * 100)[df.isna().any()].sort_values(ascending=False)
        )
    return df


# ************ remplissage des valeurs manquantes ***********#


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


# ************extraction de données dans une base ***********#
def extract2(big_data, keyword1, keyword2):
    # Créer le masque
    mask = big_data["Indicator Name"].str.contains(keyword1, case=False) & big_data[
        "Indicator Name"
    ].str.contains(keyword2, case=False, regex=True)

    # Appliquer le masque pour obtenir un nouveau DataFrame
    df = big_data[mask]

    return df


# ************Traitement des données extraites pour constituer une base *********** #


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


# ************ Transformation des bases en formant long ***********#


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
<<<<<<< HEAD


## ************ visualisation avec la carte***********###

=======
>>>>>>> c384057ace56608a429d326a4945f7e32fc56241
