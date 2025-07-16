import random

def gerar_instancia(n=10, universo_tamanho=20):
    """
    Gera uma instância com um conjunto base e subconjuntos associados.
    """
    conjunto = list(range(n))
    subconjuntos = {
        i: random.sample(range(universo_tamanho), random.randint(2, 6))
        for i in conjunto
    }
    k = 3  # parâmetro arbitrário do k-sistema
    return conjunto, subconjuntos, k


def gerar_instancia_adaptativa(n=10, universo_tamanho=20):
    """
    Gera uma instância com estados aleatórios (0 ou 1),
    garantindo ao menos um estado 1 para viabilizar a execução adaptativa.
    """
    elementos, subconjuntos, _ = gerar_instancia(n, universo_tamanho)
    estados = {e: random.choice([0, 1]) for e in elementos}

    # Força pelo menos um estado igual a 1
    if all(e == 0 for e in estados.values()):
        escolhido = random.choice(elementos)
        estados[escolhido] = 1

    # DEBUG: imprime subconjuntos e estados
    print("\n===== DEBUG DA INSTÂNCIA ADAPTATIVA =====")
    for e in elementos:
        print(f"Elemento {e} | Estado: {estados[e]} | Subconjunto: {subconjuntos[e]}")
    print("=========================================\n")

    return elementos, subconjuntos, estados

