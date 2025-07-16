def funcao_cobertura(selecionados, subconjuntos):
    """
    Soma os elementos únicos cobertos pelos subconjuntos associados.
    """
    cobertura = set()
    for elem in selecionados:
        cobertura.update(subconjuntos.get(elem, []))
    return len(cobertura)


def funcao_cobertura_adaptativa(selecionados, subconjuntos, observacoes):
    """
    Versão adaptativa que considera estados revelados dos elementos.
    """
    cobertura = set()
    for elem in selecionados:
        if elem in observacoes and observacoes[elem] == 1:
            cobertura.update(subconjuntos.get(elem, []))
    return len(cobertura)
