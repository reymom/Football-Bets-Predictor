# Football-Bets-Predictor
Trying to maximize the benefits of the possible bets for matches in recent seasons of the Spanish Leage.

Given the odds of certain houses, I train a model with a specific custom loss metric in order to predict a maximum in the future landscape of the benefits. The goal is not to predict the results of the matches, as houses have a very good predictors and the margin of improvement is trivial. Rather than that, we use their predictions and some strong features in order to grasp flaws in the odds and get a balance of risk-benefit. Feature extraction involves scrapping the web of the FIFA and take the score values of attack, deffense, mid, of every team in the moment of the match.

Benefit in single maps and cumulative benefits of some particular output:
![alt text](https://github.com/reymom/Football-Bets-Predictor/blob/master/VirtualGain1819_modelfin.png)
