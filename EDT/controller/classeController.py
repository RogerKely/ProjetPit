from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox
from model.classe import Classe
from view.classe.listerClasseView import ListerClasseView


class ClasseController:
  def __init__(self):
    pass
  def _get_intitule(self):
    return self._v_intitule
  def _set_intitule(self,intitule):
    self._v_intitule = intitule
  intitule = property(_get_intitule, _set_intitule)

  def fonction_ajouter(self):
    print(self.intitule.text())
    classe = Classe(self._v_intitule.text())
    try:
      classe.create()
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
      self.intitule.setText("")
  def listerClasse(self, table):
    classe = Classe()
    liste = classe.read()
    if (liste != []):
      table.setRowCount(len(liste))
      table.setColumnCount(len(liste[0]))
      enTete = ["Id","Titre"]
      table.setHorizontalHeaderLabels(enTete)
      for i in range(len(liste)):
        for j in range(len(liste[i])):
          table.setItem(i, j, QTableWidgetItem(str(liste[i][j])))
    else:
      table.setRowCount(1)
      table.setColumnCount(4)
      enTete = ["Id", "Titre"]
      table.setHorizontalHeaderLabels(enTete)


  def pageListeClasse(self):
    self.list = ListerClasseView(self)
    self.list.setWindowModality(Qt.ApplicationModal)
    self.list.show()