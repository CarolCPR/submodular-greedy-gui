import random
import matplotlib.pyplot as plt
from utils.funcoes_submodulares import funcao_cobertura
from utils.simulador_instancias import gerar_instancia


def plotar_resultado(valores, nomes):
    """Gera gráfico de barras com os valores de f(S) por solução."""
    plt.figure(figsize=(6, 4))
    plt.bar(nomes, valores, color="#4caf50")
    plt.title("Valor da Função Submodular por Solução")
    plt.xlabel("Soluções Candidatas")
    plt.ylabel("f(S)")
    plt.tight_layout()
    plt.show()


def executar_randommultigreedy(n=10, l=2, p=0.5, k=3):
    """
    Implementa o algoritmo RANDOMMULTIGREEDY com parâmetros ajustáveis.
    :param n: Tamanho do conjunto base
    :param l: Número de soluções candidatas simultâneas
    :param p: Probabilidade de adicionar o elemento
    :param k: Restrição de tamanho (não usada diretamente aqui, mas reservada)
    """
    conjunto_base, subconjuntos, _ = gerar_instancia(n)
    solucoes = [[] for _ in range(l)]
    elementos_restantes = conjunto_base.copy()

    while elementos_restantes:
        candidatos = []
        for i in range(l):
            if not elementos_restantes:
                break
            vi = max(
                elementos_restantes,
                key=lambda u: funcao_cobertura(solucoes[i] + [u], subconjuntos)
                              - funcao_cobertura(solucoes[i], subconjuntos)
            )
            candidatos.append((vi, i))

        melhor_elem, melhor_idx = max(
            candidatos,
            key=lambda x: funcao_cobertura(solucoes[x[1]] + [x[0]], subconjuntos)
                          - funcao_cobertura(solucoes[x[1]], subconjuntos)
        )

        ganho = funcao_cobertura(solucoes[melhor_idx] + [melhor_elem], subconjuntos) \
                - funcao_cobertura(solucoes[melhor_idx], subconjuntos)

        if ganho > 0 and random.random() < p:
            solucoes[melhor_idx].append(melhor_elem)

        elementos_restantes.remove(melhor_elem)

    # Resultados e gráfico
    valores = [funcao_cobertura(s, subconjuntos) for s in solucoes]
    nomes = [f"S{i + 1}" for i in range(len(solucoes))]

    plotar_resultado(valores, nomes)

    melhor = max(solucoes, key=lambda s: funcao_cobertura(s, subconjuntos))
    valor = funcao_cobertura(melhor, subconjuntos)
    return f"Melhor solução: {melhor}\nValor da função: {valor}"
