import os

from PyQt5.QtCore import QFileInfo,QFile
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from model.traitement import Traitement


class TraitementController:
  def __init__(self,fenetre):
    self.fenetre = fenetre
  def _set_Image(self, image):
    self.images = image
  def _set_image_label(self,label):
    self.ImageLabels = label
  def _set_pix(self,pix):
    self.pixmaps = pix
  def _set_image_edit(self,image):
    self._ImageEdit = image
  def _get_Image(self):
    return self.images
  def _get_image_label(self):
    return self.ImageLabels
  def _get_pic(self):
    return self.pixmaps
  def _get_image_edit(self):
    return self._ImageEdit
  def _set_filtre(self,filtre):
    self._filtre = filtre
  def _get_filtre(self):
    return self._filtre

  Image = property(_get_Image, _set_Image)
  ImageLabel = property(_get_image_label, _set_image_label)
  pixmap = property(_get_pic, _set_pix)
  ImageEdit = property(_get_image_edit, _set_image_edit)
  filtre = property(_get_filtre, _set_filtre)
  def rafraichirPix(self):
    self.pixmap.convertFromImage(self.Image)
    self.ImageLabel.setPixmap(self.pixmap)
  def ouvrir(self):
    if self.ImageEdit.text() == " ":
      self.nomImage = QFileDialog.getOpenFileName(self.fenetre, "Ouvrir une image", os.getenv('HOME'),str("Image Files (*.png *.jpg *.bmp)"))
      self.info = QFileInfo(self.nomImage[0])
    else:
      self.info = QFileInfo(self.ImageEdit.text())
      self.nomImage = QFileDialog.getOpenFileName(self.fenetre, "Ouvrir fichier" , self.info.absoluteFilePath(),str("Image Files (*.png *.jpg *.bmp)"))

    self.ImageEdit.setText(str(self.nomImage))
    self.Image.load(self.nomImage[0])
    self.Image = self.Image.scaled(self.ImageLabel.size())
    self.rafraichirPix()
  def sauver(self):
    self.traitement = Traitement(self.nomImage[0],self.info.baseName())
    if self.filtre.currentText() == "Rouge":
      self.traitement.Rouge()
    elif self.filtre.currentText() == "Vert":
      self.traitement.Vert()
    elif self.filtre.currentText() == "Bleu":
      self.traitement.Bleu()
    elif self.filtre.currentText() == "Jaune":
      self.traitement.Jaune()
    elif self.filtre.currentText() == "N/B":
      self.traitement.NB()

