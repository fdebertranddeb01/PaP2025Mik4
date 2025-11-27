# Copyright 2022 Francois de Bertrand de Beuvron
#
# This file is part of CoursBeuvron.
#
# CoursBeuvron is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CoursBeuvron is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CoursBeuvron.  If not, see <http://www.gnu.org/licenses/>.
'''
Created on 25 juin 2022

@author: Francois de Bertrand de Beuvron
'''

import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg

class BoiteACoucou(qtw.QWidget) :

    def __init__(self):
        super().__init__()
        lanom = qtw.QLabel("nom :")
        self.tfnom = qtw.QLineEdit()
        lentete = qtw.QHBoxLayout()
        lentete.addWidget(lanom)
        lentete.addWidget(self.tfnom)
        lentete.setStretchFactor(self.tfnom,2)

        self.tamessage = qtw.QPlainTextEdit()
        self.tamessage.setReadOnly(True)

        self.bcoucou = qtw.QPushButton("coucou")
        self.bcoucou.clicked.connect(self.doCoucou)

        self.bsalut = qtw.QPushButton("salut")
        self.bsalut.clicked.connect(self.doSalut)
        lboutons = qtw.QHBoxLayout()
        lboutons.addWidget(self.bcoucou)
        lboutons.addWidget(self.bsalut)

        main_layout = qtw.QVBoxLayout()
        main_layout.addLayout(lentete)
        main_layout.addWidget(self.tamessage)
        main_layout.addLayout(lboutons)
        self.setLayout(main_layout)
        self.setWindowTitle("Boite à Coucou")

    def doCoucou(self):
        print("coucou clicked")
        nom = self.tfnom.text()
        self.tamessage.appendPlainText("coucou " + nom)


    def doSalut(self):
        print("salut clicked")
        nom = self.tfnom.text()
        self.tamessage.appendPlainText("salut " + nom)


def gogogo() :
    app = qtw.QApplication()  # toujours 1 objet de type QApplication
    main = BoiteACoucou()
    main.show()
    app.exec()  # démarre l'application QT.


if __name__ == '__main__':
    gogogo()
