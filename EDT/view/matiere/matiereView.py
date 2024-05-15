from PyQt5.QtWidgets import QWidget,QPushButton, QApplication, QLabel,QLineEdit, QComboBox
from controller.matiereController import MatiereController
class MatiereView(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.controller = MatiereController()
    self.build()
  def build(self):
    self.setWindowTitle("Matiere")
    self.intituleL = QLabel("Intitule :", self)
    self.vhL = QLabel("Volume horaire :", self)
    self.semestreL = QLabel("Semestre :", self)
    self.prof_idL = QLabel("Professeur",self)
    self.intituleE = QLineEdit(self)
    self.vhE = QLineEdit(self)
    self.semestreE = QLineEdit(self)
    self.prof_idE = QComboBox(self)
    self.ajouterBtn = QPushButton("Ajouter", self)
    self.listerBtn = QPushButton("Lister", self)
    self.setGeometry(400, 300, 600, 500)
    self.intituleL.setGeometry(20, 20, 120, 40)
    self.vhL.setGeometry(20, 60, 120, 40)
    self.prof_idL.setGeometry(20, 100, 120, 40)
    self.semestreL.setGeometry(20, 140, 120, 40)
    self.intituleE.setGeometry(140, 20, 150, 40)
    self.vhE.setGeometry(140, 60, 150, 40)
    self.prof_idE.setGeometry(140, 100, 150, 40)
    self.semestreE.setGeometry(140, 140, 150, 40)
    self.ajouterBtn.setGeometry(140, 180, 120, 40)
    self.listerBtn.setGeometry(260, 180, 120, 40)
    self.controller.ajouterItemProf(self.prof_idE)
    self.controller.intitule = self.intituleE
    self.controller.vh = self.vhE
    self.controller.prof_id = self.prof_idE
    self.controller.semestre = self.semestreE
    self.ajouterBtn.clicked.connect(self.controller.fonction_ajouter)
    self.listerBtn.clicked.connect(self.controller.pageListeMatiere)