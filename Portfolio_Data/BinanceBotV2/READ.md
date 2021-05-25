
# My personal Trading Bot
### Projet de trading Bot avec Flask sur l'exchange Binance

### Objectif du projet 

Pouvoir effectuer du trading à haute fréquence de mon portfeuille crypto sur l'exchange Binance


Language : Python 
Interface app: Flask
Server : Cloud provider App compute
Assets : ETH
Trading Pair (Asset + Symbol) : ETHUSDT
Amount to trade : 50 $

Strategy : Deux actions possibles "BUY" et "SELL"
Si le prix baisse de 10% 

1. place un ordre d'achat "BUY"==> update opération suivante "SELL"
Si le prix sur une moyenne mobile baisse de 10% ==> place un ordre d'achat "BUY"==> update opération suivante "SELL"

Si le prix augmente de 30%   
1. place un ordre de vente "BUY"==> update opération suivante "SELL"
Si le prix sur une moyenne mobile augmente de 30% ==> place un ordre de vente "SELL"==> update opération suivante "BUY"