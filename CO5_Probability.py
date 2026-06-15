def bayes_rule(prior, likelihood, evidence):
    return round((prior*likelihood)/evidence,2)

def expected_utility(probability,reward):
    return probability*reward

p=bayes_rule(0.5,0.8,1)
print("Posterior Probability =",p)
print("Expected Utility =",expected_utility(p,100))
