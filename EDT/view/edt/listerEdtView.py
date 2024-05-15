from PyQt5.QtWidgets import QWidget,QTableWidget
class ListerEdtView(QWidget):
  def __init__(self,edt):
    QWidget.__init__(self)
    self.edt = edt
    self.build()
  def build(self):
    self.setWindowTitle("Emploie du temps")
    self.table = QTableWidget(self)
    self.edt.listerEdt(self.table)
    self.setGeometry(400,300,600,500)
    self.table.resize(600,100)