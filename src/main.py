from PyQt5.QtWidgets import QApplication
from interface.interface_algoritmos import InterfaceAlgoritmos
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = InterfaceAlgoritmos()
    janela.show()
    sys.exit(app.exec_())
