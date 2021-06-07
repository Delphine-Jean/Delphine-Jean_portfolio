
# My personal Trading Bot
### Projet de trading Bot avec Flask sur l'exchange Binance

### Objectif du projet 

Pouvoir effectuer du day trading (pas de trading à haute fréquence) de mon portfeuille crypto sur l'exchange Binance
Je vais limiter le trading à 5 symbols : USDT, ADA, ETH, BTC, MATIC 
Voici les étapes de dévelopement du Bot 

#### Dévelopement du bot sous Flask

- Création des points d'entrée de l'API Binance
- Création des fonctions liées aux ordres
- Création d'une stratégie 
- Backtesting 
- Enregistrement des logs dans une base de données SQLlite (peut être dans BigQuery dans un second temps)

#### Mise en production
- Déploiement sous forme de projet Flask
- Déploiement de l'application sur Google Compute Engine


#### Seconde feature à ajouter :

Analyse de sentiments Twitter 
- Scraping des tweets 
- Data cleaning 
- Developpement de l'algorythme ML
- Déploiement sous forme de DAG airflow vers l'app
- enregistrement des logs dans BigQuery


