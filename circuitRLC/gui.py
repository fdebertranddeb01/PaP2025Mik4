import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg
import model

class PremFen(qtw.QFrame) :
    def __init__(self):
        super().__init__()
        layout = qtw.QVBoxLayout()
        bCoucou = qtw.QPushButton("coucou")
        taMessage = qtw.QPlainTextEdit();
        layout.addWidget(bCoucou)
        self.setLayout(layout)

class BoiteACoucou(qtw.QFrame):
    def __init__(self):
        super().__init__()
        layout = qtw.QVBoxLayout()
        lnom = qtw.QHBoxLayout()
        lnom.addWidget(qtw.QLabel("nom :"))
        self._tf_nom = qtw.QLineEdit();
        lnom.addWidget(self._tf_nom)
        layout.addLayout(lnom)
        self._ta_messages = qtw.QPlainTextEdit()
        layout.addWidget(self._ta_messages)
        lboutons = qtw.QHBoxLayout()
        self._b_coucou = qtw.QPushButton("coucou")
        self._b_coucou.clicked.connect(self.gereCoucou)
        self._b_salut = qtw.QPushButton("salut")
        lboutons.addWidget(self._b_coucou)
        lboutons.addWidget(self._b_salut)
        layout.addLayout(lboutons)
        self.setLayout(layout)

    def gereCoucou(self):
        nom = self._tf_nom.text()
        self._ta_messages.appendPlainText(
            f"coucou {nom}")

class EditNoeud(qtw.QFrame) :
    def __init__(self,main : 'MainCircuit'):
        super().__init__()
        self._main = main
        layout = qtw.QHBoxLayout()
        llabel = qtw.QVBoxLayout()
        llabel.addWidget(qtw.QLabel("px"))
        llabel.addWidget(qtw.QLabel("py"))
        ltext = qtw.QVBoxLayout()
        self._tfPx = qtw.QLineEdit()
        self._tfPy = qtw.QLineEdit()
        ltext.addWidget(self._tfPx)
        ltext.addWidget(self._tfPx)
        layout.addLayout(llabel)
        layout.addLayout(ltext)
        self.setLayout(layout)

    def creation(self):
        acreer = model.Noeud(2,2)
        self._main.circuit

class MainCircuit(qtw.QFrame) :
    def __init__(self,circuit : 'Circuit'):
        super().__init__()
        self._circuit = circuit
        layout = qtw.QHBoxLayout()
        self._editN = EditNoeud()
        layout.addWidget(self._editN)
        self._bcree = qtw.QPushButton("creer")
        layout.addWidget(self._bcree)
        self.setLayout(layout)

    @property
    def circuit(self):
        return self._circuit


class DeuxCoucous(qtw.QFrame):
    def __init__(self):
        super().__init__()
        layout = qtw.QHBoxLayout()
        layout.addWidget(BoiteACoucou())
        layout.addWidget(BoiteACoucou())
        self.setLayout(layout)


def gogogo():
    app = qtw.QApplication()
    fen = MainCircuit()
    fen.show()
    app.exec()

if __name__ == '__main__':
    gogogo()
