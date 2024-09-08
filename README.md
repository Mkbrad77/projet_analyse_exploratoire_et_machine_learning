# Football Data Analysis Project for Team Performance Optimization

## Project Description:
This project aims to explore football data to identify trends and correlations between individual player performances and overall team results. We used several datasets from **Kaggle** and **understat.com**, spanning a five-year period, to gain insights into team and player performances based on various metrics, such as **expected goals (xG)** and **ppda_coef**(opponent passes per defensive action).

## Project Objectives:
1. **Analyze team performance** based on their ability to convert chances into goals across different leagues.
2. **Examine the impact of defensive pressing** on team results by comparing pressing intensity to offensive success.
3. **Assess player efficiency** in converting expected goals into actual goals.
4. **Explore the correlation between individual player performance** and their team's results in each league.

## Datasets Used:
- **Understat.com** : Detailed data on European league teams (2014-2019).
- **Kaggle** : Professional player statistics (2016-2020).

## Technologies Used:
- **Python** (Pandas, NumPy) : For data processing and analysis.
- **Altair** : For data processing and analysis.
- **Jupyter Notebook** : For data processing and analysis.


## Methodology:
1. **Data Preparation** : Cleaning and structuring datasets, checking for missing values, and matching team names across datasets.
2. **Exploratory Analysis** :
   - Analysis of **xG_diff**(difference between expected goals and actual goals) to measure team efficiency in converting chances. 
   - Study of **ppda_coef** to gauge teams' defensive pressing intensity.
3. **Visualization** : Use Altair to create interactive charts illustrating team and player performance.
4. **Result Interpretation** : Identification of significant correlations between team/player performance metrics and overall results.

## Résults :
- Teams with a lower **xG_diff** those that convert more chances—generally achieve better results.
- Intense defensive pressing (faible **ppda_coef**) is correlated with better offensive performance in several cases, although it varies depending on the teams and tactics.

## Conclusion :
This project demonstrates the importance of data analysis in understanding football performance. The visualizations and metrics used provide better insights into the factors that influence team and player outcomes.

## Before run this Project
Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
