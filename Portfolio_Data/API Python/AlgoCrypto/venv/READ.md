Nous allons coder une application de trading

- Decision helper : Charger et analyser les données du marchés des cours Cryptos
- Logging : Messages à l'utilisateur
- Stratégie de trading 
- Envoi des ordres d'achats 

Connectivité 

- On va lier l'application à Binance : API (REST et Webocket)
  - https://testnet.binancefuture.com/en/futures/BTCUSDT
  - https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
- On va lier l'application à Bitmex : API (REST et Webocket)

Authentification aux 2 APIs :

==> Deux connecteurs / classes (= 2 fichier)

Trading Automation 

- Parsing des paramètres utilisateurs
- Parsing des données du marché reçus par le connecteur
- Définition de la logique pour chaque stratégie
- Gestion des ordres / positions 

==> 1 stratégie = 1 fichier