import os
import sys

from PyQt5.QtCore import QFile, QFileInfo
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QLineEdit, QDateEdit, QComboBox, QFileDialog
from PyQt5 import QtCore

class MembreView(QWidget):
  fermetureMembre = QtCore.pyqtSignal(str)
  def __init__(self):
    QWidget.__init__(self)
    self.build()

  def build(self):
    self.setWindowTitle("Ajouter membre")
    self.nomL = QLabel("Nom :", self)
    self.dateL = QLabel("Date de naissance :", self)
    self.abonnementL = QLabel("Abonnement :", self)
    self.contactL = QLabel("Contact :", self)
    self.nomE = QImage()
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
    self.dateE.setGeometry(140,60,150,40)
    self.abonnementE.setGeometry(140,100,150,40)
    self.contactE.setGeometry(140,140,150,40)
    self.ajouterBtn.setGeometry(140,180, 120,40)
    self.listerBtn.setGeometry(260,180, 120,40)
    self.ajouterBtn.clicked.connect(self.ajout)
    self.labelImage = QLabel(self)
    self.labelImage.setGeometry(QtCore.QRect(300, 150, 320, 240))
    self.labelImage.setStyleSheet((" background-color: rgb(180, 180, 180); "))
    self.labelImage.setText(("  "))
    self.labelImage.setObjectName((" labelImage "))
    self.image=QImage(self.labelImage.size(),QImage.Format_RGB32)
    self.pixmap = QPixmap.fromImage(self.image)
    self.updatePixmap()

  def updatePixmap(self):

    # chargement du QImage dans le QPixmap
    self.pixmap.convertFromImage(self.image)  # recharge le QImage dans le QPixmap existant – met à jour le QPixmap

    # – affichage du QPixmap dans QLabel
    self.labelImage.setPixmap(self.pixmap)  # met à jour le qpixmap affiché dans le qlabel

  def ajout(self):
    """info = QFileInfo(self.contactE.text())
    #self.filenameImage = QFileDialog.getSaveFileName(self, 'Ouvrir fichier', info.absoluteFilePath(), " *.png *.jpg;; *.gif ")  # ouvre l'interface fichier – à partir chemin – avec sélection
    #self.contactE.setText(str(self.filenameImage))
    fileName = QFileDialog.getOpenFileName(self,str("Open Image"), "/home/jana", str("Image Files (*.png *.jpg *.bmp)"))
    print(fileName)

    if self.contactE.text() == "":
      # self.filename=QFileDialog.getSaveFileName(self, 'Ouvrir fichier', os.getenv('HOME')) # ouvre l'interface fichier – home par défaut
      self.filenameImage = QFileDialog.getSaveFileName(self, 'Ouvrir fichier', os.getenv('HOME')," *.png *.jpg;; *.gif ")  # ouvre l'interface fichier – avec sélection
      # self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier – chemin courant par défaut
    else:
      info = QFileInfo(self.contactE.text())  # définit un objet pour manipuler info sur fichier à partir chaine champ
      print(info.absoluteFilePath())  # debug
      self.filenameImage = QFileDialog.getSaveFileName(self, 'Ouvrir fichier', info.absoluteFilePath()," *.png *.jpg;; *.gif ")  # ouvre l'interface fichier – à partir chemin – avec sélection
      # ;; pour avoir choix de sélection sur plusieurs lignes ex : " Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml) "

    print(self.filenameImage)
    self.contactE.setText(str(self.filenameImage))"""
    print(" Bouton <Sélectionner Fichier> appuyé ")

    # ouvre fichier en tenant compte du chemin déjà saisi dans le champ
    if self.contactE.text() == "  ":
      self.filenameImage = QFileDialog.getOpenFileName(self, 'Ouvrir fichier',os.getenv('HOME'))  # ouvre l'interface fichier – home par défaut
      # self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier – chemin courant par défaut
    else:
      info = QFileInfo(self.contactE.text())  # définit un objet pour manipuler info sur fichier à partir chaine champ
      print(info.absoluteFilePath())  # debug
      self.filenameImage = QFileDialog.getOpenFileName(self, 'Ouvrir fichier',info.absoluteFilePath())  # ouvre l'interface fichier – à partir chemin

    # self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', os.getenv('HOME')) # ouvre l'interface fichier – home par défaut
    # self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier – chemin courant par défaut
    # getOpenFileName ouvre le fichier sans l'effacer

    print(self.filenameImage)  # affiche le chemin obtenu dans la console
    self.contactE.setText(str(self.filenameImage))  # affiche le chemin obtenu dans le champ texte
    self.image.load(self.filenameImage[0])
    self.image = self.image.scaled(self.labelImage.size())  # redimensionne l'image
    self.updatePixmap()  # met à jour le pixmap et qlabel

  def ajouterMembre(self):
    self.fermetureMembre.emit(self.nomE.text())
    self.close()
if __name__ == "__main__":
  app = QApplication(sys.argv)
  accueil = MembreView()
  accueil.show()
  app.exit(app.exec_())

