import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg
from model import Noeud,Composant,Circuit

class FrameAvecBordure(qtw.QFrame):
    DEFAULT_BORDURE = True

    def __init__(self,bordure : bool = DEFAULT_BORDURE):
        super().__init__()
        if bordure :
            # une bordure simple; de nombreuses autres options possibles
            self.setFrameStyle(qtw.QFrame.Panel | qtw.QFrame.Plain)
            self.setLineWidth(3)

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
        acreer = Noeud(2,2)

class SceneCircuit(qtw.QGraphicsScene) :
    def __init__(self,main : 'MainCircuit'):
        super().__init__();
        self._main = main
        self.redessine()

    def redessine(self):
        ellipse = qtw.QGraphicsEllipseItem(50,25,30,60)
        # Define the brush (fill).
        brush = qtg.QBrush(qtg.QColor(100,0,0))
        ellipse.setBrush(brush)
        # Define the pen (line)
        pen = qtg.QPen(qtg.QPen(qtg.QColor(255,0,0), 2))
        ellipse.setPen(pen)
        # puis on l'ajoute à la scene
        self.addItem(ellipse)

    def mousePressEvent(self, event:qtw.QGraphicsSceneMouseEvent):
        self._main.controleur.gereClicSouris(event)


class DessinCircuit(qtw.QGraphicsView) :
    def __init__(self,main : 'MainCircuit'):
        super().__init__();
        self._main = main
        self._scene = SceneCircuit(main);
        self.setScene(self._scene)

class Controleur():
    def __init__(self,main : 'MainCircuit'):
        super().__init__();
        self._main = main

    def gereClicSouris(self,event : qtw.QGraphicsSceneMouseEvent):
        print(f"clic en : {event.scenePos().x()},{event.scenePos().x()}")

class CreationNoeud(FrameAvecBordure) :
    def __init__(self,main : 'MainCircuit'):
        super().__init__();
        self._main = main
        layout = qtw.QHBoxLayout()
        self._editN = EditNoeud(self)
        layout.addWidget(self._editN)
        self._bcreer = qtw.QPushButton("creer")
        layout.addWidget(self._bcreer)
        self.setLayout(layout)

class MainCircuit(qtw.QFrame) :
    def __init__(self,circuit : 'Circuit'):
        super().__init__()
        self._circuit = circuit
        self._controleur = Controleur(self)
        layout = qtw.QVBoxLayout()
        self._creerN = CreationNoeud(self)
        layout.addWidget(self._creerN)
        self._dessin = DessinCircuit(self)
        layout.addWidget(self._creerN)
        layout.addWidget(self._dessin)
        self.setLayout(layout)

    @property
    def circuit(self):
        return self._circuit

    @property
    def controleur(self):
        return self._controleur


class DeuxCoucous(qtw.QFrame):
    def __init__(self):
        super().__init__()
        layout = qtw.QHBoxLayout()
        layout.addWidget(BoiteACoucou())
        layout.addWidget(BoiteACoucou())
        self.setLayout(layout)


def gogogo():
    app = qtw.QApplication()
    circuit = Circuit()
    fen = MainCircuit(circuit)
    fen.show()
    app.exec()

if __name__ == '__main__':
    gogogo()
