# Projet Python pour la data science : Vérification de la Loi d'Okun 
 

## Introduction

L'objectif de ce travail est de mettre en pratique les différents élements parcourus en cours sur le language 'Python' et ce par le choix d'une problématique que nous sommes amenés à traiter. La problématique choisie est à dimension économique, il s'agit de vérifier empiriquement la validité de la loi d'Okun. Cette dernière, définit une relation inverse entre le taux de chômage et le taux de croissance économique, postulant qu'une augmentation dans la demande globale incite les entreprises à embaucher davantage de travailleurs pour répondre à la demande croissante des biens et services.

Nous disposons pour cela de bases de données **Open source** fournies par la Banque mondiale, ces dernières comportent les taux de chomage etde croissance économique pour différents pays du monde.
   -Les données de la base de données sur le taux de chomage sont mensuelles et s'étalent sur plusieurs années, allant de **Décembre 1993** à **Octobre 2023**.
   -Les données de la base de données sur le taux de croissance du PIB sont trimestrielles et s'étalent sur plusieurs années, allant du premier trimestre de **1994** au quatrième trimestre de **2023**.

**Précision :** La base de données sur le taux de croissance du PIB est celle du PIB déflaté (PIB réel), l'effet de l'inflation étant alors éliminé.


## Objectifs

1. Collecter des données sur le taux de chômage et le PIB de plusieurs pays du monde.
2. Analyser les relations entre le taux de croissance du PIB et le taux de chômage pour chaque pays.
3. Utiliser des visualisations pour présenter les résultats de manière claire et compréhensible.

## Bases de données

Les données utilisées dans ce projet proviennent des sources suivantes :
- Taux de chômage : [Banque mondiale - Indicateurs du travail](lien_vers_la_source)
- PIB : [Global Economic Monitor](https://datacatalog.worldbank.org/search/dataset/0037798/Global-Economic-Monitor)
- Indicateurs socio-économiques : https://datacatalog.worldbank.org/search/dataset/0037652/Health-Nutrition-and-Population-Statistics
- Inégalités : [Spatial Inequalities] : https://datacatalog.worldbank.org/search/dataset/0064524/Spatial-Inequalities

## Méthodes utilisées

- Pandas pour la manipulation des données
- Matplotlib et Seaborn pour la visualisation
- Jupyter Notebook pour l'analyse interactive

## Structure du Projet

- `notebooks/` : Contient les notebooks Jupyter utilisés pour l'analyse.
- `data/` : Emplacement pour stocker les données collectées.
- `scripts/` : Scripts Python réutilisables pour la manipulation des données.

## Comment exécuter le projet

1. Clonez ce dépôt sur votre machine locale.

   ```bash
   git clone https://github.com/Marimar4/Projet-Python.git

