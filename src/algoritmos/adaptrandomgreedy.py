import random
import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from utils.funcoes_submodulares import funcao_cobertura_adaptativa
from utils.simulador_instancias import gerar_instancia_adaptativa

def plotar_ganho_acumulado(lista_ganhos):
    try:
        if not lista_ganhos or all(g == 0 for g in lista_ganhos):
            print(">>> Lista de ganhos vazia ou sem progresso. Gráfico não será exibido.")
            return

        plt.close('all')
        acumulado = [sum(lista_ganhos[:i + 1]) for i in range(len(lista_ganhos))]
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(range(1, len(acumulado) + 1), acumulado, marker='o', color="#2196f3")
        ax.set_title("Ganho acumulado - ADAPTRANDOMGREEDY")
        ax.set_xlabel("Iteração")
        ax.set_ylabel("f(S) acumulado")
        ax.grid(True)
        fig.tight_layout()
        fig.show()
        print(">>> Gráfico exibido com sucesso.")
    except Exception as e:
        print("Erro ao gerar gráfico:", e)


def executar_adaptrandomgreedy(n=10, p=0.5):
    """
    Algoritmo ADAPTRANDOMGREEDY com ganhos adaptativos baseados em observações.
    :param n: Tamanho do conjunto base
    :param p: Probabilidade de aceitar um elemento
    """
    elementos, subconjuntos, estados = gerar_instancia_adaptativa(n=n)
    solucao = []
    observacoes = {}
    ganhos = []

    while elementos:
        candidatos = [e for e in elementos if e not in solucao]
        if not candidatos:
            break

        melhor = max(
            candidatos,
            key=lambda u: len(set().union(
                *[subconjuntos.get(e, []) for e in solucao + [u]]
            )) - len(set().union(
                *[subconjuntos.get(e, []) for e in solucao]
            ))
        )

        if random.random() < p:
            estado_real = estados[melhor]
            if estado_real == 1:
                solucao.append(melhor)
                observacoes[melhor] = estado_real
                ganho = funcao_cobertura_adaptativa(solucao, subconjuntos, observacoes)
                ganhos.append(ganho)
            else:
                # Mesmo que o elemento tenha estado 0, ele é marcado como observado
                observacoes[melhor] = estado_real
        elementos.remove(melhor)

    # Cálculo do valor final com base na solução construída
    valor_final = funcao_cobertura_adaptativa(solucao, subconjuntos, observacoes)

    # Verifica se há dados para gerar o gráfico
    print(">>> Ganhos:", ganhos)
    print(">>> Tamanho da lista de ganhos:", len(ganhos))
    plotar_ganho_acumulado(ganhos)

    return f"Solução adaptativa: {solucao}\nValor da função: {valor_final}"
