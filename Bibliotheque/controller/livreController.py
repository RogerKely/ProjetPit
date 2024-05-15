from PyQt5.QtCore import QDate,Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from model.livres import Livres
from view.ListerLivreView import ListerLivreView

class LivreController:
  def _set_titre(self,titre):
    self._v_titre = titre
  def _set_categorie(self,categorie):
    self._v_categorie = categorie
  def _get_titre(self):
    return self._v_titre
  def _get_categorie(self):
    return self._v_categorie

  titre = property(_get_titre, _set_titre)
  categorie = property(_get_categorie, _set_categorie)
  def fonction_ajouter(self):
    livre = Livres(self.titre.text(),self.categorie.text())
    try :
      livre.create()
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
    finally:
      self._v_titre.setText("")
      self._v_categorie.setText("")
  def listerLivres(self,table):
    livre = Livres()
    liste = livre.read()
    table.setRowCount(len(liste))
    table.setColumnCount(len(liste[0]))
    enTete = ["id", "Titre", "Categorie", "Date d'ajout"]
    table.setHorizontalHeaderLabels(enTete)
    for i in range(len(liste)):
      for j in range(len(liste[i])):
        table.setItem(i, j, QTableWidgetItem(str(liste[i][j])))
  def pageListeLivre(self):
    self.list = ListerLivreView(self)
    self.list.setWindowModality(Qt.ApplicationModal)
    self.list.show()

