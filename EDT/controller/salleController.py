from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from model.salle import Salle
from view.salle.listerSalleView import ListerSalleView
class SalleController:
  def __init__(self):
    pass
  def _get_code(self):
    return self._code
  def _get_etage(self):
    return self._etage
  def _set_code(self, code):
    self._code = code
  def _set_etage(self, etage):
    self._etage = etage
  code = property(_get_code, _set_code)
  etage = property(_get_etage, _set_etage)

  def fonction_ajouter(self):
    salle = Salle(
      self._code.text(),
      self._etage.text()
    )
    try:
      salle.create()
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
      self._code.setText("")
      self._etage.setText("")
  def listerSalle(self, table):
    salle = Salle()
    liste = salle.read()
    table.setRowCount(len(liste))
    table.setColumnCount(len(liste[0]))
    enTete = ["id","Code", "Etage"]
    table.setHorizontalHeaderLabels(enTete)
    for i in range(len(liste)):
      for j in range(len(liste[i])):
        table.setItem(i, j, QTableWidgetItem(str(liste[i][j])))

  def pageListeSalle(self):
    self.list = ListerSalleView(self)
    self.list.setWindowModality(Qt.ApplicationModal)
    self.list.show()