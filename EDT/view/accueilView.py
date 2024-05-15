import sys
from PyQt5.QtWidgets import QWidget,QPushButton, QApplication
from controller.accueilController import AccueilController

class AccueilView(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.build()
  def build(self):
    self.setWindowTitle("Accueil employe de temps")
    self.profBtn = QPushButton("Prof", self)
    self.matiereBtn = QPushButton("Matière", self)
    self.salleBtn = QPushButton("Salle", self)
    self.classeBtn = QPushButton("Classe", self)
    self.edtBtn = QPushButton("Edt", self)

    self.setGeometry(300,200,800,800)
    self.profBtn.setGeometry(150, 20, 450, 100)
    self.matiereBtn.setGeometry(150, 120, 450, 100)
    self.salleBtn.setGeometry(150, 220, 450, 100)
    self.classeBtn.setGeometry(150, 320, 450, 100)
    self.edtBtn.setGeometry(150, 420, 450, 100)


    self.controller = AccueilController()
    self.profBtn.clicked.connect(self.controller.pageProf)
    self.matiereBtn.clicked.connect(self.controller.pageMatiere)
    self.salleBtn.clicked.connect(self.controller.pageSalle)
    self.classeBtn.clicked.connect(self.controller.pageClasse)
    self.edtBtn.clicked.connect(self.controller.pageEdt)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  accueil = AccueilView()
  accueil.build()
  accueil.show()
  app.exit(app.exec_())