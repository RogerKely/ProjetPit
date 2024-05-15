
#!/usr/bin/python
# -*- coding: utf-8 -*-

# par X. HINAULT – Mai 2013 – Tous droits réservés
# GPLv3 – www.mon-club-elec.fr

# modules a importer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *  # inclut QTimer..
import os,sys

from  tuto_pyqt_dessin_qpixmap_save_file import * # fichier obtenu à partir QtDesigner et pyuic4

# +/- variables et objets globaux

class myApp(QWidget, Ui_Form): # la classe reçoit le Qwidget principal ET la classe définie dans test.py obtenu avec pyuic4
        def __init__(self, parent=None):
                QWidget.__init__(self) # initialise le Qwidget principal
                self.setupUi(parent) # Obligatoire

                # — Variables de classe

                # — Paramétrage des widgets de l'interface GUI si nécessaire —

                # — Connexions entre signaux des widgets et fonctions
                # connecte chaque signal utilisé des objets à l'appel de la fonction voulue

                self.connect(self.pushButtonOuvrirImage, SIGNAL(" clicked() "), self.pushButtonOuvrirImageClicked)  # connecte le signal Clicked de l'objet à l'appel de la fonction voulue
                self.connect(self.pushButtonEnregistrerImage, SIGNAL(" clicked() "), self.pushButtonEnregistrerImageClicked) # connecte le signal Clicked de l'objet bouton à l'appel de la fonction voulue
                self.connect(self.pushButtonNouveauImage, SIGNAL(" clicked() "), self.pushButtonNouveauImageClicked) # connecte le signal Clicked de l'objet bouton à l'appel de la fonction voulue

                # — Code actif initial  —

                # Dessin avec QPixmap (affichage) et QImage (I/O, accès pixels)

                # création d'un QImage permettant l'accès aux pixels
                self.image=QImage(self.labelImage.size(),QImage.Format_RGB32) # crée image RGB 32 bits même taille que label

                #– initialisation du QImage
                self.image.fill(QColor(255,255,255)) # fond blanc

                # coordonnées centre du QPixmap (même taille que label)
                xo=self.image.width()/2
                yo=self.image.height()/2

                #trace le point
                #self.image.setPixel(xo,yo,qRgb(0,0,0)) # modifie la couleur du pixel x,y – noter qRgb renvoie valeur RGB 0xFFRRGGBB

                #— dessin initial sur QImage —
                self.painterImage=QPainter(self.image) # associe QPainter (classe de dessin) au Qimage

                # tracé de formes
                self.painterImage.setPen(QPen(QColor(0,0,255),2)) # fixe la couleur du crayon et la largeur pour le dessin – forme compactée           
                self.painterImage.drawRect(10,10,50,50) # dessin rectangle : drawRect (self, int x, int y, int w, int h)
                #self.painterImage.drawPoint(xo,yo) # trace un point drawPoint (self, int x, int y)
                #self.painterImage.fillRect(150,150,30,30,QColor(255,255,0)) # fillRect (self, int x, int y, int w, int h, QColor b)
                self.painterImage.drawEllipse(xo,yo,50,50) # dessin cercle – x-y = coin sup gauche rect encadrant : drawEllipse (self, int x, int y, int w, int h)
                #self.painterImage.drawEllipse(QPointF(xo,yo),50,50) # dessin cercle avec x,y centre et rayon : drawEllipse (self, QPointF center, float rx, float ry)
                self.painterImage.drawLine(0,0,xo*2,yo) # trace une ligne : drawLine (self, int x1, int y1, int x2, int y2)
                #self.painterImage.drawText(QPointF(xo/2, yo/2), " Hello ") # drawText (self, QPointF p, QString s)

                # il existe d'autres possibilités de dessin (polygone, chemin, etc..) voir : http://pyqt.sourceforge.net/Docs/PyQt4/qpainter.html

                self.painterImage.end() # ferme le painter – n'est plus accessible après

                # — fin dessin sur QImage

                #– Initialisation du QPixmap
                self.pixmap=QPixmap.fromImage(self.image) # initialise  le QPixmap…

                self.updatePixmap()

        # — les fonctions appelées, utilisées par les signaux des widgets —

        def pushButtonOuvrirImageClicked(self):
                print(" Bouton <Sélectionner Fichier> appuyé ")

                # ouvre fichier en tenant compte du chemin déjà saisi dans le champ
                if self.lineEditCheminImage.text()=="  ":
                        self.filenameImage=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', os.getenv('HOME')) # ouvre l'interface fichier – home par défaut
                        #self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier – chemin courant par défaut
                else:
                        info=QFileInfo(self.lineEditCheminImage.text()) # définit un objet pour manipuler info sur fichier à partir chaine champ
                        print( info.absoluteFilePath()) # debug
                        self.filenameImage=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', info.absoluteFilePath()) # ouvre l'interface fichier – à partir chemin

                #self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', os.getenv('HOME')) # ouvre l'interface fichier – home par défaut
                #self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier – chemin courant par défaut
                # getOpenFileName ouvre le fichier sans l'effacer

                print(self.filenameImage) # affiche le chemin obtenu dans la console
                self.lineEditCheminImage.setText(self.filenameImage) # affiche le chemin obtenu dans le champ texte

                self.image.load(self.filenameImage)
                self.image=self.image.scaled(self.labelImage.size()) # redimensionne l'image
                self.updatePixmap() # met à jour le pixmap et qlabel

        def pushButtonNouveauImageClicked(self):
                print(" Bouton NOUVEAU appuyé ")

                # ouvre fichier en tenant compte du chemin déjà saisi dans le champ
                if self.lineEditCheminImage.text()=="  ":
                        #self.filename=QFileDialog.getSaveFileName(self, 'Ouvrir fichier', os.getenv('HOME')) # ouvre l'interface fichier – home par défaut
                        self.filenameImage=QFileDialog.getSaveFileName(self, 'Ouvrir fichier', os.getenv('HOME'), " *.png *.jpg;; *.gif ") # ouvre l'interface fichier – avec sélection
                        #self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier – chemin courant par défaut
                else:
                        info=QFileInfo(self.lineEditCheminImage.text()) # définit un objet pour manipuler info sur fichier à partir chaine champ
                        print(info.absoluteFilePath() )# debug
                        self.filenameImage=QFileDialog.getSaveFileName(self, 'Ouvrir fichier', info.absoluteFilePath(), " *.png *.jpg;; *.gif ") # ouvre l'interface fichier – à partir chemin – avec sélection
                        # ;; pour avoir choix de sélection sur plusieurs lignes ex : " Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml) "

                print(self.filenameImage)
                self.lineEditCheminImage.setText(self.filenameImage)

        def pushButtonEnregistrerImageClicked(self):           
                print(" Bouton <ENREGISTRE> appuyé ")                    

                if self.lineEditCheminImage.text()!="  ":

                        self.image.save(self.filenameImage) # le suffixe utilisé est celui du nom de fichier

        # — les fonctions appelées, utilisées par les signaux hors widgets —

        # — fonctions de classes autres—    

        # fonction de MAJ du QPixmap : chargement QImage +/- dessin + affichage dans QLabel
        def updatePixmap(self):

                # chargement du QImage dans le QPixmap
                self.pixmap.convertFromImage(self.image) # recharge le QImage dans le QPixmap existant – met à jour le QPixmap

                #– affichage du QPixmap dans QLabel
                self.labelImage.setPixmap(self.pixmap) # met à jour le qpixmap affiché dans le qlabel  

# — Autres Classes utiles —

# — Classe principale (lancement)  —
def main(args):
        a=QApplication(args) # crée l'objet application
        f=QWidget() # crée le QWidget racine
        c=myApp(f) # appelle la classe contenant le code de l'application
        f.show() # affiche la fenêtre QWidget
        r=a.exec_() # lance l'exécution de l'application
        return r

if __name__==" __main__ ": # pour rendre le code exécutable
        main(sys.argv) # appelle la fonction main
