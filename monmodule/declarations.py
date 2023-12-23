
# Importation des bases des packages
import io 
from io import BytesIO 
import pycodestyle as pep8
import zipfile
import requests
import openpyxl as xl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pycountry
import seaborn as sns
import missingno as msno
from statistics import *

np.random.seed(123)

# declaration des fonctions

## Télécharger le fichier

def load(url,nom_fichier):
    response = requests.get(url)

    # Vérifier si le téléchargement a réussi (code d'état 200)
    if response.status_code == 200:
        # Enregistrer le contenu dans un fichier  ( "nom_fichier")
        with open(nom_fichier, 'wb') as file:
            file.write(response.content)
        print("Téléchargement de base",nom_fichier,"réussi.")
    else:
        print(f"Erreur de téléchargement : {response.status_code}")

## Fonction d'extraction de base dans un fichier zippé


def extraire_fichier_zip(chemin_zip, nom_fichier, nom_feuille):
    with zipfile.ZipFile(chemin_zip, 'r') as zip_ref:
        with zip_ref.open(nom_fichier) as fichier_in_zip:
            df= pd.read_excel(BytesIO(fichier_in_zip.read()),sheet_name=nom_feuille, header=0)\
                        .rename(columns={'Unnamed: 0':'Year'})\
                            .assign(Year=lambda x: x['Year'].astype(str).str.rstrip('.0'))
            
            if nom_feuille == 'quarterly':
                # Convertir la colonne 'Year' en format de date trimestriel
                df['Year'] = pd.to_datetime(df['Year'], format='%YQ%m')
            else:
                 # Convertir la colonne 'Year' en format de date mensuelle
                df['Year'] = pd.to_datetime(df['Year'], format='%YM%m')

            # Définir 'Year' comme index pour faciliter la manipulation des périodes
            df.set_index('Year', inplace=True)

            return df
        


# Méthode search_fuzzy de pycountry pour corrections des noms des pays
def correct_country_name(col_names):
    countries_detected = []
    
    for name in col_names:
        try:
            # Essayer de trouver le pays par son nom
            pays= pycountry.countries.search_fuzzy(name)[0]
            countries_detected.append(pays.name)
        except LookupError:
            # Conserver les noms qui ne correspondent à aucun pays
            countries_detected.append(name)
             # Ignorer les noms qui ne correspondent à aucun pays
            #pass
    
    return countries_detected

def detect_country_name(col_names):
    countries_detected = []
    
    for name in col_names:
        try:
            # Essayer de trouver le pays par son nom
            pays= pycountry.countries.search_fuzzy(name)[0]
            countries_detected.append(pays.name)
        except LookupError:
            # Conserver les noms qui ne correspondent à aucun pays
            #countries_detected.append(name)
             # Ignorer les noms qui ne correspondent à aucun pays
            pass
    
    return countries_detected


## visualisation des données manquantes
def missing_plot(df):
    """
    Visualise les valeurs manquantes avec un diagramme à barres et un heatmap.
    Utilise les bibliothèques missingno et seaborn.
    """
    # Diagramme à barres des valeurs manquantes
    msno.bar(df)
    plt.title(r'$\bf{Diagramme\ à\ barres\ des\ valeurs\ manquantes}$', color='green')
    plt.show()

    # Heatmap des valeurs manquantes
    sns.heatmap(df.isna(), cbar=False)
    plt.title(r'$\bf{Heatmap\ des\ valeurs\ manquantes}$', color='green')
    plt.show()

## affichage des valeurs manquantes 

def missing(df):

    # Suppression des deux prmières lignes

    df = df.iloc[2:]
    # Suppression de certaines valeurs manquantes

    df.dropna(axis=1, thresh=len(df) * 0.9, inplace=True)

    return (df.isna().sum() / len(df) * 100)[df.isna().any()].sort_values(ascending=False)

    ## affichage du pourcentage de valeurs manquantes par pays pour des pays ayant des valeurs manquantes

    (df.isna().sum() / len(df) * 100)[df.isna().any()].sort_values(ascending=False)

