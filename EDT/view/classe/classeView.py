from PyQt5.QtWidgets import QWidget,QPushButton, QApplication, QLabel,QLineEdit, QDateEdit
from controller.classeController import ClasseController

class ClasseView(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.controller = ClasseController()
    self.build()
  def build(self):
    self.setWindowTitle("Classe")
    self.intituleL = QLabel("Nom du classe :", self)
    self.intituleE = QLineEdit(self)
    self.ajouterBtn = QPushButton("Ajouter", self)
    self.listerBtn = QPushButton("Lister", self)
    self.setGeometry(400, 300, 600, 500)
    self.intituleL.setGeometry(20, 20, 120, 40)
    self.intituleE.setGeometry(140, 20, 150, 40)
    self.ajouterBtn.setGeometry(140, 60, 120, 40)
    self.listerBtn.setGeometry(260, 60, 120, 40)
    self.controller.intitule = self.intituleE
    self.ajouterBtn.clicked.connect(self.controller.fonction_ajouter)
    self.listerBtn.clicked.connect(self.controller.pageListeClasse)