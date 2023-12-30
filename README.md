# Projet Python pour la data science : Vérification de la Loi d'Okun 
 

## Introduction

L'objectif de ce travail est de mettre en pratique les différents élements parcourus en cours sur le language 'Python' et ce par le choix d'une problématique que nous sommes amenés à traiter. La problématique choisie est à dimension économique, il s'agit de vérifier empiriquement la validité de la loi d'Okun. Cette dernière, définit une relation inverse entre le taux de chômage et le taux de croissance économique, postulant qu'une augmentation dans la demande globale incite les entreprises à embaucher davantage de travailleurs pour répondre à la demande croissante des biens et services.

Nous disposons pour cela de bases de données **Open source** fournies par la Banque mondiale, ces dernières comportent les taux de chomage, taux de croissance économique ainsi que d'autres indicateurs socio-économiques pour différents pays du monde.
   -Les données de la base de données sur le taux de chômage sont mensuelles et s'étalent sur plusieurs années, allant de **Décembre 1993** à **Octobre 2023**.
   -Les données de la base de données sur le taux de croissance du PIB sont trimestrielles et s'étalent sur plusieurs années, allant du premier trimestre de **1994** au quatrième trimestre de **2023**.

**Précision :** La base de données sur le taux de croissance du PIB est celle du PIB déflaté (PIB réel), l'effet de l'inflation étant alors éliminé.



## Revue de littérature : 

**Loi d'Okun :** 
Pour ce projet de modélisation, nous nous sommes inspirés des travaux suivants : 

- [1]. Traoré, D. L., Diakite, S., & Mariko, O. (2021). Croissance et chômage au Mali : Vérification empirique de la loi d'Okun. Revue Malienne de Science et de Technologie, Série C : Sciences Humaines et Sociales, 02(25), Page. ISSN 1987-1031. CNRST, Bamako, Mali.

- [2]. Aassif, Z. L'extraction de la tendance cycle. Haut-Commissariat au Plan, Direction de la comptabilité nationale. 

- [3]. Mills, T. C. (2019). Chapter 12 - Transfer Functions and Autoregressive Distributed Lag Modeling. In Applied Time Series Analysis: A Practical Guide to Modeling and Forecasting (pp. 201-210). Loughborough University, Loughborough, United Kingdom. https://doi.org/10.1016/B978-0-12-813117-6.00012-0

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
- Geopandas pour faciliter l'utilisation des données géospatiales.
- Plotly particulièrement le module plotly.express.
- Dash pour la création de data apps en Python.
- Statsmodels pour la modélisation.

## Brainstorm

- [Jupyter Notebook](https://docs.jupyter.org/en/latest/) est un environnement interactif de développement et d'exécution de code qui permet de créer et de partager des documents contenant du code, des visualisations et du texte explicatif.
- [Pandas](https://pandas.pydata.org/docs/index.html) est une bibliothèque open source fournissant des structures de données et des outils d'analyse de données hautes performances. Elle offre des structures de données flexibles et performantes, notamment le **DataFrame**, l'objet le plus utilisé de Pandas et qui permet de stocker et de manipuler des données tabulaires de manière efficace. 
- [Matplotlib](https://matplotlib.org/stable/index.html) est une bibliothèque complète permettant de créer des visualisations statiques, animées et interactives.
- [Seaborn](https://seaborn.pydata.org/) est une bibliothèque de visualisation de données Python basée sur matplotlib . Il fournit une interface de haut niveau pour dessiner des graphiques statistiques attrayants et informatifs. Elle facilite la création de graphiques basés sur des données DataFrame de pandas.
- [NumPy](https://numpy.org/doc/) est un package pour le calcul scientifique en Python. 
- [Geopandas](https://geopandas.org/en/stable/) permet des opérations spatiales sur les types géométriques.
- [Plotly](https://plotly.com/python/) crée des graphiques interactifs de qualité publication. 
- [Dash](https://dash.plotly.com/)est un framework web interactif pour la création d'applications web analytiques en Python. C'est une extension de Flask, un framework web pour Python, et utilise également Plotly pour les visualisations interactives.
- [Statsmodels](https://www.statsmodels.org/stable/index.html) est une bibliothèque qui permet l'estimation de différents modèles statistiques, la réalisation de tests statistiques et l'exploration de données statistiques. 


## Structure du Projet

- `notebooks/` : Contient les notebooks Jupyter utilisés pour l'analyse.
- `bases/` : Emplacement pour stocker les données collectées.
- `scripts/` : Scripts Python réutilisables pour la manipulation des données.

## Comment exécuter le projet ?

1. Clonez ce dépôt sur votre machine locale.

   ```bash
   git clone https://github.com/Marimar4/Projet-Python.git
