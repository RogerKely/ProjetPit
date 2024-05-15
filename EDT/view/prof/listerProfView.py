from PyQt5.QtWidgets import QWidget,QTableWidget
class ListerProfView(QWidget):
  def __init__(self,prof):
    QWidget.__init__(self)
    self.prof = prof
    self.build()
  def build(self):
    self.setWindowTitle("Liste des professeur ")
    self.table = QTableWidget(self)
    self.prof.listerProf(self.table)
    self.setGeometry(400,300,600,500)
    self.table.resize(600,100)