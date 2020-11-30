#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt

def f_att():
    print("ceci est la fonction d'atterrissage")

def f_dec():
    print("ceci est la fonction de décollage")

def fonction():
    a = bouton.text()
    if a == "Atterrissage":
        bouton.setText("Décollage")
        return f_att()
    else:
        bouton.setText("Atterrissage")
        return f_dec()


app = QApplication(sys.argv)
ex = QWidget()
bouton = QPushButton("Décollage")
bouton.clicked.connect(lambda: fonction())
vbox = QVBoxLayout()
vbox.addWidget(bouton)
ex.setLayout(vbox)


ex.setGeometry(100, 100, 200, 200)

ex.show()

app.exec_()

