from PyQt5.QtWidgets import QWidget,QTableWidget
class RapportView(QWidget):
  def __init__(self,rapport):
    QWidget.__init__(self)
    self.rapport = rapport
    self.build()
  def build(self):
    self.setWindowTitle("Emploie du temps")
    self.table = QTableWidget(self)
    self.rapport.listerRapport(self.table)
    self.setGeometry(400,300,600,500)
    self.table.resize(600,100)