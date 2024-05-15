from PyQt5.QtWidgets import QWidget,QTableWidget
class ListerMatiereView(QWidget):
  def __init__(self, matiere):
    QWidget.__init__(self)
    self.matiere = matiere
    self.build()

  def build(self):
    self.setWindowTitle("Liste des professeur ")
    self.table = QTableWidget(self)
    self.matiere.listerMatiere(self.table)
    self.setGeometry(400, 300, 600, 500)
    self.table.resize(600, 100)