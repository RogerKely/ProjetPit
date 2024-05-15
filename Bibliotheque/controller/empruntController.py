from PyQt5.QtCore import QDate,Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from model.emprunt import Emprunt
from model.membres import Membre
from model.livres import Livres
from view.ListerEmpruntView import ListerEmpruntView

class EmpruntController:
  def __init__(self):
    self.membres = Membre()
    self.livres = Livres()
    self.listMembre = self.membres.read()
    self.listLivre = self.livres.read()
  def _set_livre(self,livre):
    self._v_livre = livre
  def _set_membre(self,membre):
    self._v_membre = membre
  def _get_livre(self):
    return self._v_livre
  def _get_membre(self):
    return self._v_membre

  livre = property(_get_livre, _set_livre)
  membre = property(_get_membre, _set_membre)
  def fonction_ajouter(self):
    emprunt = Emprunt(self.membre.currentData(),self.livre.currentData())
    try :
      emprunt.create()
    except:
      msg_box = QMessageBox()
      msg_box.setIcon(QMessageBox.Critical)
      msg_box.setWindowTitle("Erreur")
      msg_box.setText("Échec d'enregistrement ! Veuillez remplir soignieusement svp! (-_-) ")
      msg_box.exec_()
    else:
      msg_box = QMessageBox()
      msg_box.setIcon(QMessageBox.Information)
      msg_box.setWindowTitle("Valider")
      msg_box.setText("Enregistrement réussi (0_-) ")
      msg_box.exec_()

  def ajouterItemMembre(self, membre):
    for items in self.listMembre:
      membre.addItem(items[1], items[0])
  def ajouterItemLivre(self, livre):
    for items in self.listLivre:
      print(items[0])
      livre.addItem(items[1], items[0])
  def listerEmprunt(self,table):
    emprunt = Emprunt()
    liste = emprunt.read()
    table.setRowCount(len(liste))
    table.setColumnCount(len(liste[0]))
    enTete = ["id", "Membre", "Livre", "Rendue le"]
    table.setHorizontalHeaderLabels(enTete)
    for i in range(len(liste)):
      for j in range(len(liste[i])):
        table.setItem(i, j, QTableWidgetItem(str(liste[i][j])))
  def pageListeEmprunt(self):
    self.list = ListerEmpruntView(self)
    self.list.setWindowModality(Qt.ApplicationModal)
    self.list.show()

