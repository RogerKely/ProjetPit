from PyQt5.QtWidgets import QWidget,QTableWidget
class ListerClasseView(QWidget):
  def __init__(self,classe):
    QWidget.__init__(self)
    self.classe = classe
    self.build()
  def build(self):
    self.setWindowTitle("Emploie du temps")
    self.table = QTableWidget(self)
    self.classe.listerClasse(self.table)
    self.setGeometry(400,300,600,500)
    self.table.resize(600,100)