import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg

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
        self.setLayout(layout)



def gogogo():
    app = qtw.QApplication()
    fen = BoiteACoucou()
    fen.show()
    app.exec()

if __name__ == '__main__':
    gogogo()
