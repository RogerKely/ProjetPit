from view.membreView import *
from view.livreView import *
from view.empruntView import *
from PyQt5 import QtCore

class AccueilController:
  def __init__(self):
    self.nom = ''
  def pageMembre(self):
    self.membre = MembreView()
    self.membre.setWindowModality(QtCore.Qt.ApplicationModal)
    self.membre.show()
  def pageLivre(self):
    self.livre = LivreView()
    self.livre.setWindowModality(QtCore.Qt.ApplicationModal)
    self.livre.show()
  def pageEmprunt(self):
    self.emprunt = EmpruntView()
    self.emprunt.setWindowModality(QtCore.Qt.ApplicationModal)
    self.emprunt.show()