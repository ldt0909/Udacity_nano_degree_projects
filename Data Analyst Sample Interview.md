## Udacity Data Analyst Sample Interview Questions

##### 1. Data Project Experience

> Describe a data project you worked on recently.


##### 2. Probability
> You are given a ten piece box of chocolate truffles. You know based on the label that six of the pieces have an orange cream filling and four of the pieces have a coconut filling. If you were to eat four pieces in a row, what is the probability that the first two pieces you eat have an orange cream filling and the last two have a coconut filling?

The problem is within `dependent probabilities` sphrere and can be calculated as follow:

Probability of first choice to be orange: 
```
P(1) = 6/10
```
Probability of second choice to be orange: 
```
P(2) = 5/9
```
Probability of third choice to be coconut: 
```
P(3) = 4/8
```
Probability of fourth choice to be coconut: 
```
P(4) = 3/7
```
Total Probably 
```
P(1st orange and 2nd orange and 3rd coconut and 4th coconut) = P(1)*P(2)*P(3)*P(4) = 0.074
```
> Follow up question: If you were given an identical box of chocolates and again eat four pieces in a row, what is the probability that exactly two contain coconut filling?

Within first 4 pieces of box of chocolates, there're 14 combinations, assuming each combinations have similar probability

Within those 14 combinations, there're 6 combinations have exactly 2 coconuts

Therefore, we have P(exactly 2 coconuts in 14 combinations) = 6/14 = 42.857%
```
