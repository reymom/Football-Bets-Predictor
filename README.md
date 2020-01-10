# Football-Bets-Predictor
Trying to maximize the benefits of the possible bets for matches in recent seasons of the Spanish League.

Given the odds of certain houses, I train a model with a specific custom loss metric in order to predict a maximum in the future landscape of the benefits. The goal is not to predict the results of the matches, as houses have very good predictors and the margin of improvement is insignificant and non-profitable, moreover having in mind they offer biased odds for maximizing their own benefit. Rather than that, we use their predictions and some stable features in order to grasp flaws in the offered odds and get an optimum balance of risk-benefit. Feature extraction involves scrapping the web of the FIFA and take the scores of attack-deffense-midfield, of every team in the moment of the match.


Losses and benefits for every match and cumulative benefits in the season of 18/19
![alt text](https://github.com/reymom/Football-Bets-Predictor/blob/master/VirtualGain1819_modelfin.png)
