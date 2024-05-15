import sys

from PyQt5.QtWidgets import QWidget, QTableWidget
from PyQt5 import QtCore

class ListerEmpruntView(QWidget):
  fermetureListeEmprunt = QtCore.pyqtSignal(str)
  def __init__(self,emprunt):
    QWidget.__init__(self)
    self.emprunt = emprunt
    self.build()
  def build(self):
    self.setWindowTitle("Liste livre")
    self.table = QTableWidget(self)
    self.emprunt.listerEmprunt(self.table)
    self.setGeometry(400,300,600,500)
    self.table.resize(600,100)
