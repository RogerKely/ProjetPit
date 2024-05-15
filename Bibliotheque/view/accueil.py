import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel ,QPushButton, QGridLayout
from controller.accueilController import *
class Accueil (QWidget):
  def __init__(self):
    QWidget.__init__(self)
  def build(self):
    self.setWindowTitle("Accueil bibliothèque")
    self.membreBtn = QPushButton("Membres",self)
    self.livreBtn = QPushButton("Livres",self)
    self.empruntBtn = QPushButton("Emprunts", self)

    self.setGeometry(400,300,500,400)
    self.membreBtn.setGeometry(150,20,250,100)
    self.livreBtn.setGeometry(150,120,250,100)
    self.empruntBtn.setGeometry(150,220,250,100)

    self.controller = AccueilController()
    self.membreBtn.clicked.connect(self.controller.pageMembre)
    self.livreBtn.clicked.connect(self.controller.pageLivre)
    self.empruntBtn.clicked.connect(self.controller.pageEmprunt)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  accueil = Accueil()
  accueil.build()
  accueil.show()
  app.exit(app.exec_())