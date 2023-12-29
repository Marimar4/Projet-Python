# Projet Python pour la data science : Vérification de la Loi d'Okun 
 

## Introduction

L'objectif de ce travail est de mettre en pratique les différents élements parcourus en cours sur le language 'Python' et ce par le choix d'une problématique que nous sommes amenés à traiter. La problématique choisie est à dimension économique, il s'agit de vérifier empiriquement la validité de la loi d'Okun. Cette dernière, définit une relation inverse entre le taux de chômage et le taux de croissance économique, postulant qu'une augmentation dans la demande globale incite les entreprises à embaucher davantage de travailleurs pour répondre à la demande croissante des biens et services.

Nous disposons pour cela de bases de données **Open source** fournies par la Banque mondiale, ces dernières comportent les taux de chomage, taux de croissance économique ainsi que d'autres indicateurs socio-économique pour différents pays du monde.
   -Les données de la base de données sur le taux de chômage sont mensuelles et s'étalent sur plusieurs années, allant de **Décembre 1993** à **Octobre 2023**.
   -Les données de la base de données sur le taux de croissance du PIB sont trimestrielles et s'étalent sur plusieurs années, allant du premier trimestre de **1994** au quatrième trimestre de **2023**.

**Précision :** La base de données sur le taux de croissance du PIB est celle du PIB déflaté (PIB réel), l'effet de l'inflation étant alors éliminé.



## Revue de littérature : 

Loi d'Okun :

## Objectifs

1. Collecter des données sur le taux de chômage, le taux de croissance du PIB ainsi que d'autres indicateurs socio-économiques de plusieurs pays du monde.
2. Analyser les relations entre le taux de croissance du PIB et le taux de chômage pour chaque pays.
3. Utiliser des visualisations pour présenter les résultats de manière claire et compréhensible.

## Bases de données

Les données utilisées dans ce projet proviennent des sources suivantes :
- Taux de chômage : [Banque mondiale - Indicateurs du travail](https://datacatalog.worldbank.org/search/dataset/0037798/Global-Economic-Monitor)
- PIB : [Global Economic Monitor](https://datacatalog.worldbank.org/search/dataset/0037798/Global-Economic-Monitor)
- Indicateurs socio-économiques : [Health Nutrition And Population Statistics](https://datacatalog.worldbank.org/search/dataset/0037652/Health-Nutrition-and-Population-Statistics)

**Précision :** 

   -Les bases de données sur le 'Taux de chômage' et le 'Taux de croissance du PIB déflaté' portent respectivement les noms : 'Unemployment Rate, seas. adj.' et 'GDP Deflator at Market Prices, LCU' dans le fichier .zip ('GemDataEXTR') fourni par la banque mondiale. Lesdites bases de données sont des fichiers de type .xlsx.

   -Les indicateurs socio-économiques notamment le taux de croissance démographique ainsi que l'esperance de vie sont tirés du fichier .xlsx ('HNP_StatsEXCEL') fourni par la banque mondiale.

## Fonctionnalités utilisées

- Jupyter Notebook pour la création de notebook simplifiée et légère.
- Fonctionnalités offertes par Pandas pour la manipulation des données.
- Matplotlib et Seaborn pour la visualisation.
- Numpy pour le calcul scientifique en Python. 

## Brainstorm

- **Jupyter Notebook**[^1] est un environnement interactif de développement et d'exécution de code qui permet de créer et de partager des documents contenant du code, des visualisations et du texte explicatif.
- **Pandas**[^2] est une bibliothèque open source fournissant des structures de données et des outils d'analyse de données hautes performances. Elle offre des structures de données flexibles et performantes, notamment le **DataFrame**, l'objet le plus utilisé de Pandas et qui permet de stocker et de manipuler des données tabulaires de manière efficace. 
- **Matplotlib**[^3] Matplotlib est une bibliothèque complète permettant de créer des visualisations statiques, animées et interactives.
- **Seaborn**[^4] est une bibliothèque de visualisation de données Python basée sur matplotlib . Il fournit une interface de haut niveau pour dessiner des graphiques statistiques attrayants et informatifs. Elle facilite la création de graphiques basés sur des données DataFrame de pandas.
- **NumPy**[^5] est un package pour le calcul scientifique en Python. 


## Structure du Projet

- `notebooks/` : Contient les notebooks Jupyter utilisés pour l'analyse.
- `data/` : Emplacement pour stocker les données collectées.
- `scripts/` : Scripts Python réutilisables pour la manipulation des données.

## Comment exécuter le projet ?

1. Clonez ce dépôt sur votre machine locale.

   ```bash
   git clone https://github.com/Marimar4/Projet-Python.git


[^1] : https://docs.jupyter.org/en/latest/ <br>
[^2] : https://pandas.pydata.org/docs/index.html <br>
[^3] : https://matplotlib.org/stable/index.html <br>
[^4] : https://seaborn.pydata.org/ <br>
[^5] : https://numpy.org/doc/
