import sys

from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QApplication
from controller.controller import Controller

class AccueilView(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.controller = Controller()
    self.build()
  def build(self):
    self.setWindowTitle("Election")
    self.label = QLabel("Canidats", self)
    self.selection = QComboBox(self)
    self.selectionBtn = QPushButton("Selectionner", self)
    self.rpBtn = QPushButton("Rapport", self)
    self.setGeometry(300,300,300,100)
    self.label.setGeometry(20,10,120,40)
    self.selection.setGeometry(140,10, 120,40)
    self.selectionBtn.setGeometry(20,50,120,40)
    self.rpBtn.setGeometry(140,50,120,40)
    self.controller.listeCandidat(self.selection)
    self.selectionBtn.clicked.connect(self.controller.ajouterCandidat)
    self.rpBtn.clicked.connect(self.controller.pageRapport)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  accueil = AccueilView()
  accueil.build()
  accueil.show()
  app.exit(app.exec_())
