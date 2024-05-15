from PyQt5.QtWidgets import QWidget,QPushButton, QApplication, QLabel,QLineEdit, QComboBox
from controller.salleController import SalleController
class SalleView(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.controller = SalleController()
    self.build()
  def build(self):
    self.setWindowTitle("Salle")
    self.codeL = QLabel("Code :", self)
    self.etageL = QLabel("Etage :", self)
    self.codeE = QLineEdit(self)
    self.etageE = QLineEdit(self)
    self.ajouterBtn = QPushButton("Ajouter", self)
    self.listerBtn = QPushButton("Lister", self)
    self.setGeometry(400, 300, 600, 500)
    self.codeL.setGeometry(20, 20, 120, 40)
    self.etageL.setGeometry(20, 60, 120, 40)
    self.codeE.setGeometry(140, 20, 150, 40)
    self.etageE.setGeometry(140, 60, 150, 40)
    self.ajouterBtn.setGeometry(140, 100, 120, 40)
    self.listerBtn.setGeometry(260, 100, 120, 40)
    self.controller.code = self.codeE
    self.controller.etage = self.etageE
    self.ajouterBtn.clicked.connect(self.controller.fonction_ajouter)
    self.listerBtn.clicked.connect(self.controller.pageListeSalle)