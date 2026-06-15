from random import randint

def search_component():
    return randint(0,6)

def csp_component(move):
    return 0 <= move <= 6

def probability_component():
    return 0.75

move=search_component()
if csp_component(move):
    print("Move:",move)
    print("Win Probability:",probability_component())
