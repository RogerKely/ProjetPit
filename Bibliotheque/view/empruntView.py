from PyQt5.QtWidgets import QWidget,QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5 import QtCore
from controller.empruntController import *


class EmpruntView(QWidget):
  fermetureLivre = QtCore.pyqtSignal(str)
  def __init__(self):
    QWidget.__init__(self)
    self.controller = EmpruntController()
    self.build()
  def build(self):
    self.setWindowTitle("Page ajout livre")
    self.membreL = QLabel("Membre :",self)
    self.livreL = QLabel("Livre :", self)
    self.membreE = QComboBox(self)
    self.livreE = QComboBox(self)
    self.ajouterBtn = QPushButton("Emprunter", self)
    self.listerBtn = QPushButton("Lister", self)
    self.controller.ajouterItemMembre(self.membreE)
    self.controller.ajouterItemLivre(self.livreE)

    self.setGeometry(400,300,600,500)
    self.membreL.setGeometry(50, 50, 120, 40)
    self.livreL.setGeometry(50, 90, 120, 40)
    self.membreE.setGeometry(170, 50, 120, 40)
    self.livreE.setGeometry(170, 90, 120, 40)
    self.ajouterBtn.setGeometry(50, 130, 120,40)
    self.listerBtn.setGeometry(170,130 , 120, 40)

    self.controller.membre = self.membreE
    self.controller.livre = self.livreE
    self.ajouterBtn.clicked.connect(self.controller.fonction_ajouter)
    self.listerBtn.clicked.connect(self.controller.pageListeEmprunt)