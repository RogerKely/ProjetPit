import sys

from PyQt5.QtWidgets import QApplication,QLabel,QPushButton, QWidget, QLineEdit, QDateEdit, QComboBox
from PyQt5 import QtCore
from controller.Membre_controller import *

class MembreView(QWidget):
  fermetureMembre = QtCore.pyqtSignal(str)
  def __init__(self):
    QWidget.__init__(self)
    self.controller = Membre_controller()
    self.build()

  def build(self):
    self.setWindowTitle("Ajouter membre")
    self.nomL = QLabel("Nom :", self)
    self.dateL = QLabel("Date de naissance :", self)
    self.abonnementL = QLabel("Abonnement :", self)
    self.contactL = QLabel("Contact :", self)
    self.nomE = QLineEdit(self)
    self.dateE = QDateEdit(self)
    self.dateE.setCalendarPopup(True)
    self.abonnementE = QComboBox(self)
    self.contactE = QLineEdit(self)
    self.ajouterBtn = QPushButton("Ajouter", self)
    self.listerBtn = QPushButton("Lister", self)
    self.abonnementE.addItems(["Mensuel", "Journalier", "Annuel"])
    self.setGeometry(400,300,600,500)
    self.nomL.setGeometry(20,20, 120,40)
    self.dateL.setGeometry(20,60, 120,40)
    self.abonnementL.setGeometry(20,100, 120,40)
    self.contactL.setGeometry(20,140, 120,40)
    self.nomE.setGeometry(140,20, 150, 40)
    self.dateE.setGeometry(140,60,150,40)
    self.abonnementE.setGeometry(140,100,150,40)
    self.contactE.setGeometry(140,140,150,40)
    self.ajouterBtn.setGeometry(140,180, 120,40)
    self.listerBtn.setGeometry(260,180, 120,40)
    self.controller.nom = self.nomE
    self.controller.date = self.dateE
    self.controller.abonnement = self.abonnementE
    self.controller.contact = self.contactE
    self.ajouterBtn.clicked.connect(self.controller.fonction_ajouter)
    self.listerBtn.clicked.connect(self.controller.pageListeMembre)

  def ajouterMembre(self):
    self.fermetureMembre.emit(self.nomE.text())
    self.close()


