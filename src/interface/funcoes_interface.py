from algoritmos.randommultigreedy import executar_randommultigreedy
from algoritmos.adaptrandomgreedy import executar_adaptrandomgreedy

def executar_random(n, l, p):
    return executar_randommultigreedy(n, l, p)

def executar_adapt(n, p):
    return executar_adaptrandomgreedy(n, p)
