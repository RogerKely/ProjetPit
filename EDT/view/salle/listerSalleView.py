from PyQt5.QtWidgets import QWidget,QTableWidget
class ListerSalleView(QWidget):
  def __init__(self, salle):
    QWidget.__init__(self)
    self.salle = salle
    self.build()

  def build(self):
    self.setWindowTitle("Liste des salles ")
    self.table = QTableWidget(self)
    self.salle.listerSalle(self.table)
    self.setGeometry(400, 300, 600, 500)
    self.table.resize(600, 100)