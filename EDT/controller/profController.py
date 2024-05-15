from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem
from PyQt5.QtCore import Qt
from view.prof.listerProfView import ListerProfView
from model.prof import Prof
class ProfController:
  def _set_nom(self,nom):
    self._v_nom = nom
  def _set_adresse(self,adresse):
    self._v_adresse = adresse
  def _set_specialiter(self,specialiter):
    self._v_specialiter = specialiter
  def _set_contact(self,contact):
    self._v_contact = contact
  def _get_nom(self):
    return self._v_nom
  def _get_specialiter(self):
    return self._v_specialiter
  def _get_adresse(self):
    return self._v_adresse
  def _get_contact(self):
    return self._v_contact
  contact = property(_get_contact, _set_contact)
  adresse = property(_get_adresse, _set_adresse)
  nom = property(_get_nom, _set_nom)
  specialiter = property(_get_specialiter, _set_specialiter)
  def fonction_ajouter(self):
    prof = Prof(
      0,
      self._v_nom.text(),
      self._v_adresse.text(),
      self._v_contact.text(),
      self._v_specialiter.text())
    try:
      prof.create()
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
      self._v_specialiter.setText("")
      self._v_contact.setText("")
      self._v_adresse.setText("")

  def listerProf(self, table):
    prof = Prof()
    liste = prof.read()
    table.setRowCount(len(liste))
    table.setColumnCount(len(liste[0]))
    enTete = ["id", "Nom", "Adresse", "Contact", "Specialiter"]
    table.setHorizontalHeaderLabels(enTete)
    for i in range(len(liste)):
      for j in range(len(liste[i])):
        table.setItem(i, j, QTableWidgetItem(str(liste[i][j])))

  def pageListeProf(self):
    self.list = ListerProfView(self)
    self.list.setWindowModality(Qt.ApplicationModal)
    self.list.show()
