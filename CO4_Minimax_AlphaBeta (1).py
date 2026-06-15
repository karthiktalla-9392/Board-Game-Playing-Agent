import math

def evaluate():
    return 10

def minimax(depth, alpha, beta, maximizing):
    if depth==0:
        return evaluate()
    if maximizing:
        value=-math.inf
        for _ in range(3):
            value=max(value,minimax(depth-1,alpha,beta,False))
            alpha=max(alpha,value)
            if alpha>=beta:
                break
        return value
    else:
        value=math.inf
        for _ in range(3):
            value=min(value,minimax(depth-1,alpha,beta,True))
            beta=min(beta,value)
            if alpha>=beta:
                break
        return value

print(minimax(3,-math.inf,math.inf,True))
