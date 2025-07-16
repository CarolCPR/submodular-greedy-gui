# Submodular Greedy GUI

Este projeto implementa dois algoritmos randomizados para maximização de funções submodulares:

- `RANDOMMULTIGREEDY`
- `ADAPTRANDOMGREEDY`

A aplicação inclui uma interface gráfica em PyQt5, parametrização interativa e visualização gráfica dos resultados.

## Tecnologias utilizadas

- Python 3.11
- PyQt5
- Matplotlib
- NumPy
- Anaconda + PyCharm

## Estrutura do projeto

```
src/
│
├── algoritmos/ # Implementações dos algoritmos
├── interface/ # Interface gráfica (PyQt5)
├── utils/ # Funções auxiliares e geradores de instância
└── main.py # Ponto de entrada da aplicação
```

## Como executar

Crie um ambiente virtual com Anaconda:

```bash
conda create -n algoritmos2025 python=3.11
conda activate algoritmos2025
pip install -r requirements.txt
python src/main.py
```

Créditos
Projeto desenvolvido por Caroline Pacheco da Rosa para a disciplina de Análise de Algoritmos – Mestrado em Computação Aplicada (Unisinos, 2025/1).

---