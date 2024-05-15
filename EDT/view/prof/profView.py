from PyQt5.QtWidgets import QWidget,QPushButton, QApplication, QLabel,QLineEdit
from controller.profController import ProfController
class ProfView(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.controller = ProfController()
    self.build()
  def build(self):
    self.setWindowTitle("Professeur")
    self.nomL = QLabel("Nom :", self)
    self.adresseL = QLabel("Adresse :", self)
    self.contactL = QLabel("Contact :", self)
    self.specialiteL = QLabel("Spécialiter :", self)
    self.nomE = QLineEdit(self)
    self.adresseE = QLineEdit(self)
    self.contactE = QLineEdit(self)
    self.specialiteE = QLineEdit(self)
    self.ajouterBtn = QPushButton("Ajouter", self)
    self.listerBtn = QPushButton("Lister", self)
    self.setGeometry(400, 300, 600, 500)
    self.nomL.setGeometry(20, 20, 120, 40)
    self.adresseL.setGeometry(20, 60, 120, 40)
    self.specialiteL.setGeometry(20, 100, 120, 40)
    self.contactL.setGeometry(20, 140, 120, 40)
    self.nomE.setGeometry(140, 20, 150, 40)
    self.adresseE.setGeometry(140, 60, 150, 40)
    self.specialiteE.setGeometry(140, 100, 150, 40)
    self.contactE.setGeometry(140, 140, 150, 40)
    self.ajouterBtn.setGeometry(140, 180, 120, 40)
    self.listerBtn.setGeometry(260, 180, 120, 40)
    self.controller.nom = self.nomE
    self.controller.adresse = self.adresseE
    self.controller.specialiter = self.specialiteE
    self.controller.contact = self.contactE
    self.ajouterBtn.clicked.connect(self.controller.fonction_ajouter)
    self.listerBtn.clicked.connect(self.controller.pageListeProf)