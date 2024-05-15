from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit,QComboBox
from controller.TraitementController import TraitementController
import sys

class TraitementView(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.build()
  def build(self):
    self.setWindowTitle("Traitement d'image")
    self.ajoutImageLabel = QLabel("Image :", self)
    self.FiltresLabel = QLabel("Filtre : ", self)
    self.ImageLabel = QLabel(" ",self)
    self.ImageEdit = QLineEdit(self)
    self.FiltresEdit = QComboBox(self)
    self.FiltresEdit.addItems(["Rouge","Vert", "Bleu", "Jaune", "N/B", "Niveau de gris", "Subdiviser"])
    self.sauverBouton = QPushButton("Sauver", self)
    self.ouvrirBouton = QPushButton("Ouvrir", self)
    self.ImageLabel.setObjectName("ImageLabel")
    self.Image = QImage(self.ImageLabel.size(), QImage.Format_RGB32)
    self.pixmap = QPixmap.fromImage(self.Image)
    self.controller = TraitementController(self)
    self.controller.Image = self.Image
    self.controller.pixmap = self.pixmap
    self.controller.ImageLabel = self.ImageLabel
    self.controller.ImageEdit = self.ImageEdit
    self.controller.filtre = self.FiltresEdit
    self.controller.rafraichirPix()
    self.ouvrirBouton.clicked.connect(self.controller.ouvrir)
    self.sauverBouton.clicked.connect(self.controller.sauver)


    self.setGeometry(400,200,600,700)
    self.ajoutImageLabel.setGeometry(150, 30, 80, 40)
    self.ImageEdit.setGeometry(220, 30, 140, 40)
    self.ouvrirBouton.setGeometry(360, 30, 80, 40)
    self.FiltresLabel.setGeometry(150,70, 80, 40)
    self.FiltresEdit.setGeometry(220,70,140,40)
    self.ImageLabel.setGeometry(220,100,300,300)
    self.sauverBouton.setGeometry(220, 370,140, 40)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  accueil = TraitementView()
  accueil.show()
  app.exit(app.exec_())