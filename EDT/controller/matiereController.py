from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from model.prof import Prof
from model.matiere import Matiere
from view.matiere.listerMatiereView import ListerMatiereView
class MatiereController:
  def __init__(self):
    self.prof = Prof()
    self.listeProf = self.prof.read()

  def _get_intitule(self):
    return self._v_intitule
  def _get_vh(self):
    return self._v_vh
  def _get_prof_id(self):
    return self._v_prof_id
  def _get_semestre(self):
    return self._v_semestre
  def _set_intitule(self,intitule):
    self._v_intitule = intitule
  def _set_vh(self,vh):
    self._v_vh = vh
  def _set_prof_id(self,id):
    self._v_prof_id = id
  def _set_semestre(self,semestre):
    self._v_semestre = semestre

  intitule  = property(_get_intitule, _set_intitule)
  vh        = property(_get_vh, _set_vh)
  prof_id   = property(_get_prof_id, _set_prof_id)
  semestre  = property(_get_semestre, _set_semestre)
  def ajouterItemProf(self,prof):
    for item in self.listeProf:
      prof.addItem(item[1], item[0])
  def fonction_ajouter(self):
    matiere = Matiere(
      0,
      self._v_intitule.text(),
      self._v_vh.text(),
      self._v_prof_id.currentData(),
      self._v_semestre.text()
    )
    try:
      matiere.create()
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
      self._v_intitule.setText("")
      self._v_vh.setText("")
      self._v_semestre.setText("")
  def listerMatiere(self, table):
    matiere = Matiere()
    liste = matiere.read()
    table.setRowCount(len(liste))
    table.setColumnCount(len(liste[0]))
    enTete = ["Intitule", "Vh", "Prof", "Semestre"]
    table.setHorizontalHeaderLabels(enTete)
    for i in range(len(liste)):
      for j in range(len(liste[i])):
        table.setItem(i, j, QTableWidgetItem(str(liste[i][j])))

  def pageListeMatiere(self):
    self.list = ListerMatiereView(self)
    self.list.setWindowModality(Qt.ApplicationModal)
    self.list.show()
