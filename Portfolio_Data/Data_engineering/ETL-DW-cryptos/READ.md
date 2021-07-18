# Création d'un ETL dans un datarehouse Bigquery avec Airflow

Je vais créer une pipeline de données des données provenant 3 différentes sources décrivant le comportement des blockchains et cryptos associés ADA et ETH.
J'ai choisi de créer un projet de Blockchian Analytics afin de pouvoir mettre à disposition dans un dashboard Data Studio à disposition du public. 

Nous allons utiliser Cloud Storage, Bigquery ainsi que Airlfow pour construire le datawarehouse de notre projet.
##sources :
    - Binances cryptos : historiques prix symbol ADA, ETH,
1. Extract data from data source
1. Load the data into a file
2. Drop the file into Cloud Storage
3. Run a BigQuery Load Job on these files (load job is free)
    - Tweet sur les cryptos : ADA, ETH :
  
#### Etapes sentiment analysis
        - Recueillir des données Twitter pertinentes 
        - Nettoyez vos données à l'aide de techniques de prétraitement
        - Créer un modèle d'apprentissage automatique pour l'analyse des sentiments
        - Analysez vos données Twitter à l'aide de votre modèle d'analyse des sentiments
        - Visualisez les résultats de votre analyse des sentiments Twitter  

