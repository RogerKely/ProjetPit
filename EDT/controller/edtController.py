from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from model.salle import Salle
from model.matiere import Matiere
from model.edt import Edt
from model.classe import Classe
from view.edt.listerEdtView import ListerEdtView

class EdtController:
  def __init__(self):
    self.matieres = Matiere()
    self.salles = Salle()
    self.classes = Classe()
    self.listeMatiere = self.matieres.read(True)
    self.listeSalle = self.salles.read()
    self.listeClasse = self.classes.read()
  def _get_matiere(self):
    return self._v_matiere
  def _get_salle(self):
    return self._v_salle
  def _get_classe(self):
    return self._v_classe
  def _get_hDebut(self):
    return self._v_hDebut
  def _get_date(self):
    return self._v_date
  def _get_hFin(self):
    return self._v_hFin
  def _set_matiere(self,matiere):
    self._v_matiere = matiere
  def _set_salle(self,salle):
    self._v_salle = salle
  def _set_classe(self,classe):
    self._v_classe = classe
  def _set_date(self,date):
    self._v_date = date
  def _set_hDebut(self,hDebut):
    self._v_hDebut = hDebut
  def _set_hFin(self,hFin):
    self._v_hFin = hFin

  def ajouterItemMatiere(self,matiere):
    for item in self.listeMatiere:
      matiere.addItem(item[1], item[0])
  def ajouterItemSalle(self,salle):
    for item in self.listeSalle:
      salle.addItem(item[1], item[0])
  def ajouterItemClasse(self,classe):
    for item in self.listeClasse:
      classe.addItem(item[1], item[0])
  def fonction_ajouter(self):
    edt = Edt(
      self.matiere.currentData(),
      self.salle.currentData(),
      self.classe.currentData(),
      self.date.date().toPyDate(),
      self.hDebut.time(),
      self.hFin.time()
    )
    try:
      edt.create()
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
  def listerEdt(self, table):
    edt = Edt()
    liste = edt.read()
    if (liste != None):
      table.setRowCount(len(liste))
      table.setColumnCount(len(liste[0]))
      enTete = ["Intitule", "Vh", "Prof", "Semestre"]
      table.setHorizontalHeaderLabels(enTete)
      for i in range(len(liste)):
        for j in range(len(liste[i])):
          table.setItem(i, j, QTableWidgetItem(str(liste[i][j])))
    else:
      table.setRowCount(1)
      table.setColumnCount(4)
      enTete = ["Intitule", "Vh", "Prof", "Semestre"]
      table.setHorizontalHeaderLabels(enTete)


  def pageListeEdt(self):
    self.list = ListerEdtView(self)
    self.list.setWindowModality(Qt.ApplicationModal)
    self.list.show()

  matiere = property(_get_matiere, _set_matiere)
  salle = property(_get_salle, _set_salle)
  classe = property(_get_classe, _set_classe)
  date = property(_get_date, _set_date)
  hDebut = property(_get_hDebut, _set_hDebut)
  hFin = property(_get_hFin, _set_hFin)