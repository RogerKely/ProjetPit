from PyQt5.QtWidgets import QWidget,QLabel, QLineEdit, QPushButton
from PyQt5 import QtCore
from controller.livreController import *


class LivreView(QWidget):
  fermetureLivre = QtCore.pyqtSignal(str)
  def __init__(self):
    QWidget.__init__(self)
    self.controller = LivreController()
    self.build()
  def build(self):
    self.setWindowTitle("Page ajout livre")
    self.titreL = QLabel("Titre :",self)
    self.categoryL = QLabel("Categorie :", self)
    self.titreE = QLineEdit(self)
    self.categoryE = QLineEdit(self)
    self.ajouterBtn = QPushButton("Ajouter", self)
    self.listerBtn = QPushButton("Lister", self)

    self.setGeometry(400,300,600,500)
    self.titreL.setGeometry(50, 50, 120, 40)
    self.categoryL.setGeometry(50, 90, 120, 40)
    self.titreE.setGeometry(170, 50, 120, 40)
    self.categoryE.setGeometry(170, 90, 120, 40)
    self.ajouterBtn.setGeometry(50, 130, 120,40)
    self.listerBtn.setGeometry(170,130 , 120, 40)

    self.controller.titre = self.titreE
    self.controller.categorie = self.categoryE
    self.ajouterBtn.clicked.connect(self.controller.fonction_ajouter)
    self.listerBtn.clicked.connect(self.controller.pageListeLivre)