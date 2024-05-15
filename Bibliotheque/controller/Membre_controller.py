from model.membres import Membre
from view.listerMembreView import ListerMembreView
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5.QtCore import *

class Membre_controller:

  def _set_nom(self,nom):
    self._v_nom = nom
  def _set_abonnement(self,abonnement):
    self._v_abonnement = abonnement
  def _set_date(self,date):
    self._v_date = date
  def _set_contact(self,contact):
    self._v_contact = contact
  def _get_nom(self):
    return self._v_nom
  def _get_date(self):
    return self._v_date
  def _get_abonnement(self):
    return self._v_abonnement
  def _get_contact(self):
    return self._v_contact
  nom = property(_get_nom,_set_nom)
  date = property(_get_date, _set_date)
  abonnement = property(_get_abonnement, _set_abonnement)
  contact = property(_get_contact, _set_contact)
  def fonction_ajouter(self):
    membre = Membre(
          0,
                    self._v_nom.text(),
                    self._v_date.date().toPyDate(),
                    self._v_abonnement.currentText(),
                    self._v_contact.text())
    try :
      membre.create()
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
      self._v_nom.setText("")
      self._v_date.setDate(QDate())
      self._v_contact.setText("")
  def listerMembres(self,table):
    membre = Membre()
    liste = membre.read()
    table.setRowCount(len(liste))
    table.setColumnCount(len(liste[0]))
    enTete = ["id", "Nom", "Date de naissance", "Abonnement", "Contact", "Date d'ajout"]
    table.setHorizontalHeaderLabels(enTete)
    for i in range(len(liste)):
      for j in range(len(liste[i])):
        table.setItem(i, j, QTableWidgetItem(str(liste[i][j])))
  def pageListeMembre(self):
    self.list = ListerMembreView(self)
    self.list.setWindowModality(Qt.ApplicationModal)
    self.list.show()


