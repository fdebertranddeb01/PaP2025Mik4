import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg
from model import Noeud,Composant,Circuit

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
        ltext.addWidget(self._tfPy)
        layout.addLayout(llabel)
        layout.addLayout(ltext)
        self.setLayout(layout)

    def get_px(self) -> float:
        return float(self._tfPx.text())

    def get_py(self) -> float:
        return float(self._tfPy.text())


class CreationNoeud(qtw.QFrame) :
    def __init__(self,main : 'MainCircuit'):
        super().__init__()
        self._main = main
        layout = qtw.QHBoxLayout()
        self._edit = EditNoeud(self._main)
        layout.addWidget(self._edit)
        self._bcreer = qtw.QPushButton("Creer")
        self._bcreer.clicked.connect(self.creation)
        layout.addWidget(self._bcreer)
        self.setLayout(layout)

    def creation(self):
        x = self._edit.get_px()
        y = self._edit.get_py()
        nn = Noeud(x,y)
        self._main.circuit.add_noeud(nn)
        self._main.update_view()

class AfficheText(qtw.QFrame) :
    def __init__(self,main : 'MainCircuit'):
        super().__init__()
        self._main = main
        layout = qtw.QVBoxLayout()
        self._message = qtw.QPlainTextEdit()
        layout.addWidget(self._message)
        self.setLayout(layout)

    def updateView(self):
        txt = str(self._main.circuit)
        self._message.setPlainText(txt)


class MainCircuit(qtw.QFrame) :
    def __init__(self,circuit : 'Circuit'):
        super().__init__()
        self._circuit = circuit
        layout = qtw.QVBoxLayout()
        self._editN = CreationNoeud(self)
        layout.addWidget(self._editN)
        self._message = AfficheText(self)
        layout.addWidget(self._message)
        self.setLayout(layout)
        self.update_view()

    def update_view(self):
        """ doit mettre à jour toute l'interface lorsque le model a été modifié
        appelle souvent update_view des sous-composants"""
        self._message.updateView()


    @property
    def circuit(self):
        return self._circuit

def gogogo():
    app = qtw.QApplication()
    circuit = Circuit.circuit_test()
    fen = MainCircuit(circuit)
    fen.show()
    app.exec()

if __name__ == '__main__':
    gogogo()
