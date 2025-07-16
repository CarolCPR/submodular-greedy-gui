from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QComboBox, QMessageBox
)
from interface.funcoes_interface import executar_random, executar_adapt

class InterfaceAlgoritmos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Análise de Algoritmos - Submodular Max")

        # Layout principal
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Explicação
        explicacao = QLabel(
            "Este programa implementa algoritmos de maximização de funções submodulares, "
            "como o RANDOMMULTIGREEDY e o ADAPTRANDOMGREEDY.\n\n"
            "Esses algoritmos escolhem subconjuntos de elementos que maximizam uma função "
            "matematicamente definida (como cobertura de conjuntos). O processo é iterativo, "
            "aleatório e simula problemas reais como seleção de sensores, marketing viral, etc."
        )
        explicacao.setWordWrap(True)
        explicacao.setStyleSheet(
            "font-size: 12px; padding: 8px; background-color: #f0f0f0; "
            "border-radius: 8px; margin-bottom: 10px;"
        )
        self.layout.addWidget(explicacao)

        # Seletor de algoritmo
        self.label_algoritmo = QLabel("Selecione o algoritmo:")
        self.combo_algoritmo = QComboBox()
        self.combo_algoritmo.addItems(["RANDOMMULTIGREEDY", "ADAPTRANDOMGREEDY"])
        self.combo_algoritmo.currentTextChanged.connect(self.atualizar_parametros)

        self.layout.addWidget(self.label_algoritmo)
        self.layout.addWidget(self.combo_algoritmo)

        # Área para campos de parâmetro
        self.layout_parametros = QVBoxLayout()
        self.layout.addLayout(self.layout_parametros)

        # Botão executar
        self.botao_executar = QPushButton("Executar")
        self.botao_executar.clicked.connect(self.executar_algoritmo)
        self.layout.addWidget(self.botao_executar)

        # Campos iniciais
        self.campos = {}
        self.atualizar_parametros("RANDOMMULTIGREEDY")

    def limpar_parametros(self):
        for campo in self.campos.values():
            self.layout_parametros.removeWidget(campo["label"])
            campo["label"].deleteLater()
            self.layout_parametros.removeWidget(campo["input"])
            campo["input"].deleteLater()
        self.campos.clear()

    def atualizar_parametros(self, algoritmo):
        self.limpar_parametros()
        if algoritmo == "RANDOMMULTIGREEDY":
            self.add_parametro("n", "Tamanho do conjunto base (n):")
            self.add_parametro("l", "Número de soluções candidatas (l):")
            self.add_parametro("p", "Probabilidade de inclusão (p):")
        elif algoritmo == "ADAPTRANDOMGREEDY":
            self.add_parametro("n", "Tamanho do conjunto base (n):")
            self.add_parametro("p", "Probabilidade de inclusão (p):")

    def add_parametro(self, chave, descricao):
        label = QLabel(descricao)
        entrada = QLineEdit()

        # Valores padrão para cada campo
        valores_padrao = {
            "n": "15",
            "l": "3",
            "p": "0.8",
            "k": "2"
        }
        entrada.setText(valores_padrao.get(chave, ""))

        self.layout_parametros.addWidget(label)
        self.layout_parametros.addWidget(entrada)
        self.campos[chave] = {"label": label, "input": entrada}

    def executar_algoritmo(self):
        algoritmo = self.combo_algoritmo.currentText()
        try:
            if algoritmo == "RANDOMMULTIGREEDY":
                n = int(self.campos["n"]["input"].text())
                l = int(self.campos["l"]["input"].text())
                p = float(self.campos["p"]["input"].text())
                resultado = executar_random(n, l, p)
            elif algoritmo == "ADAPTRANDOMGREEDY":
                n = int(self.campos["n"]["input"].text())
                p = float(self.campos["p"]["input"].text())
                resultado = executar_adapt(n, p)
            else:
                resultado = "Algoritmo não implementado."

            QMessageBox.information(self, "Resultado", resultado)

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao executar o algoritmo: {e}")
