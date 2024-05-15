from PyQt5.QtCore import Qt

from model.candidat import Candidat
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem
from view.rapportView import RapportView
class Controller:
  def __init__(self):
    self.candidats = Candidat()
  def listeCandidat(self,selection):
    self.selection = selection
    for items in self.candidats.read():
      self.selection.addItem(items[1], items[0])
  def ajouterCandidat(self):
    candidat = Candidat(self.selection.currentData(), self.selection.currentText())
    try:
      candidat.add()
    except:
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Critical)
      msg.setWindowTitle("Erreur d'enregistrement")
      msg.setText("Impossible d'effectuer votre choix , veuillez enregistrer de nouveau s'il vous plaît !!")
      msg.exec_()
    else:
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)
      msg.setWindowTitle("Ajout réussie")
      msg.setText("Ajout réussie!!")
      msg.exec_()
  def listerRapport(self,table):
    candidat = Candidat()
    listeCandidat = candidat.read()
    total = 0
    votes = {}
    for vote in candidat.compteurCandidat():
      total += vote[0]
      votes[vote[1]] = vote[0]
    pourcentage = []
    i = 0
    for items in listeCandidat:
      j = 0
      try:
        tmp = [items[1],votes[items[1]] * 100 / total]
      except:
        pourcentage.append([items[1], 0])
      else:
        pourcentage.append(tmp)


      i += 1
    table.setRowCount(len(pourcentage))
    table.setColumnCount(len(pourcentage[0]))
    head = ["Nom", "Pourcentage"]
    table.setHorizontalHeaderLabels(head)
    for i in range (len(pourcentage)):
      for j in range (len(pourcentage[i])):
        table.setItem(i,j, QTableWidgetItem(str(pourcentage[i][j])))

  def pageRapport(self):
    self.rapport = RapportView(self)
    self.rapport.setWindowModality(Qt.ApplicationModal)
    self.rapport.show()
