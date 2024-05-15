from PyQt5.QtWidgets import QWidget,QPushButton, QApplication, QLabel,QLineEdit, QComboBox, QDateEdit
from controller.edtController import EdtController

class EdtView(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.controller = EdtController()
    self.build()
  def build(self):
    self.setWindowTitle("Emploie du temps")
    self.matiereL = QLabel("Matière :", self)
    self.salleL = QLabel("Salle :", self)
    self.classeL = QLabel("Classe :", self)
    self.dateL = QLabel("Date :",self)
    self.hDebutL = QLabel("Heure début :", self)
    self.hFinL = QLabel("Heure fin :",self)
    self.matiereE = QComboBox(self)
    self.salleE = QComboBox(self)
    self.classeE = QComboBox(self)
    self.dateE = QDateEdit(self)
    self.hDebutE = QLineEdit(self)
    self.hFinE = QLineEdit(self)
    self.ajouterBtn = QPushButton("Ajouter", self)
    self.listerBtn = QPushButton("Lister", self)
    self.setGeometry(400, 300, 600, 500)
    self.matiereL.setGeometry(20, 20, 120, 40)
    self.salleL.setGeometry(20, 60, 120, 40)
    self.classeL.setGeometry(20, 100, 120, 40)
    self.dateL.setGeometry(20, 140, 120, 40)
    self.hDebutL.setGeometry(20, 180, 120, 40)
    self.hFinL.setGeometry(20, 220, 120, 40)
    self.matiereE.setGeometry(140, 20, 150, 40)
    self.salleE.setGeometry(140, 60, 150, 40)
    self.classeE.setGeometry(140, 100, 150, 40)
    self.dateE.setGeometry(140, 140, 150, 40)
    self.hDebutE.setGeometry(140, 180, 120, 40)
    self.hFinE.setGeometry(140, 220, 120, 40)
    self.ajouterBtn.setGeometry(140, 260, 120, 40)
    self.listerBtn.setGeometry(260, 260, 120, 40)
    self.controller.ajouterItemMatiere(self.matiereE)
    self.controller.ajouterItemSalle(self.salleE)
    self.controller.ajouterItemClasse(self.classeE)
    self.controller.matiere = self.matiereE
    self.controller.salle = self.salleE
    self.controller.classe = self.classeE
    self.controller.date = self.dateE
    self.controller.hDebut = self.hDebutE
    self.controller.hFin = self.hFinE
    self.ajouterBtn.clicked.connect(self.controller.fonction_ajouter)
    self.listerBtn.clicked.connect(self.controller.pageListeEdt)