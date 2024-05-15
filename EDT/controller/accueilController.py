from view.prof.profView import ProfView
from view.matiere.matiereView import MatiereView
from view.salle.salleView import SalleView
from view.edt.edtView import EdtView
from view.classe.classeView import ClasseView
from PyQt5 import QtCore
class AccueilController:
  def pageProf(self):
    self.prof = ProfView()
    self.prof.setWindowModality(QtCore.Qt.ApplicationModal)
    self.prof.show()
  def pageMatiere(self):
    self.matiere = MatiereView()
    self.matiere.setWindowModality(QtCore.Qt.ApplicationModal)
    self.matiere.show()
  def pageSalle(self):
    self.salle = SalleView()
    self.salle.setWindowModality(QtCore.Qt.ApplicationModal)
    self.salle.show()
  def pageClasse(self):
    self.classe = ClasseView()
    self.classe.setWindowModality(QtCore.Qt.ApplicationModal)
    self.classe.show()
  def pageEdt(self):
    self.edt = EdtView()
    self.edt.setWindowModality(QtCore.Qt.ApplicationModal)
    self.edt.show()
