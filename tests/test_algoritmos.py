from algoritmos.randommultigreedy import executar_randommultigreedy
from algoritmos.adaptrandomgreedy import executar_adaptrandomgreedy

def test_randommultigreedy():
    resultado = executar_randommultigreedy()
    assert "Valor da função" in resultado

def test_adaptrandomgreedy():
    resultado = executar_adaptrandomgreedy()
    assert "Valor da função" in resultado
