# Projet d’analyse de données footballistiques pour l'optimisation des performances d'équipe

## Description du projet :
Ce projet vise à explorer les données footballistiques pour identifier des tendances et corrélations entre les performances individuelles des joueurs et les résultats globaux des équipes. Nous avons utilisé plusieurs ensembles de données provenant de **Kaggle** et **understat.com**, couvrant une période de cinq ans, afin de mieux comprendre les performances des équipes et des joueurs en fonction de plusieurs métriques telles que les **expected goals (xG)** et le **ppda_coef** (passes adverses par action défensive).

## Objectifs du projet :
1. **Analyser les performances des équipes** en fonction de leur capacité à convertir les occasions en buts à travers les différentes ligues.
2. **Étudier l'impact du pressing défensif** sur les résultats des équipes, en comparant l'intensité du pressing à la réussite offensive.
3. **Évaluer l'efficacité des joueurs** dans la conversion des expected goals en buts réels.
4. **Explorer la corrélation entre les performances individuelles** des joueurs et les résultats de leur équipe dans chaque ligue.

## Datasets utilisés :
- **Understat.com** : Données détaillées sur les équipes des ligues européennes (2014-2019).
- **Kaggle** : Statistiques des joueurs professionnels (2016-2020).

## Technologies utilisées :
- **Python** (Pandas, NumPy) : Pour le traitement et l’analyse des données.
- **Altair** : Pour la visualisation interactive des données.
- **Jupyter Notebook** : Pour le développement et la documentation du projet.


## Méthodologie :
1. **Préparation des données** : Nettoyage et structuration des jeux de données, vérification des valeurs manquantes, transformation des noms d’équipes pour correspondre entre les datasets.
2. **Analyse exploratoire** :
   - Analyse du **xG_diff** (différence entre expected goals et buts marqués) pour mesurer la capacité des équipes à concrétiser leurs occasions.
   - Étude du **ppda_coef** pour mesurer l'intensité du pressing défensif des équipes.
3. **Visualisation** : Utilisation d’Altair pour produire des graphiques interactifs illustrant les performances des équipes et des joueurs.
4. **Interprétation des résultats** : Identification de corrélations significatives entre les métriques de performance des équipes/joueurs et les résultats globaux.

## Résultats :
- Les équipes avec un **xG_diff** plus faible, c'est-à-dire celles qui concrétisent davantage leurs occasions, ont généralement de meilleurs résultats.
- Une pression défensive intense (faible **ppda_coef**) est corrélée à de meilleures performances offensives dans plusieurs cas, bien que cela varie selon les équipes et les tactiques.

## Conclusion :
Ce projet démontre l'importance de l'analyse de données dans la compréhension des performances footballistiques. Les visualisations et les métriques utilisées permettent de mieux appréhender les facteurs qui influencent les résultats des équipes et des joueurs.

## Comment lancer le projet :
1. Cloner le dépôt :
   ```bash
   git clone git@github.com:Mkbrad77/projet_analyse_exploratoire_et_machine_learning.git
   ```
2. Installer les dépendances
    ```bash
    pip install -r requirements.txt
    ```
