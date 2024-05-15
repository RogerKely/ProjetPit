import sys

from PyQt5.QtWidgets import QWidget, QTableWidget
from PyQt5 import QtCore

class ListerLivreView(QWidget):
  fermetureListeLivre = QtCore.pyqtSignal(str)
  def __init__(self,livre):
    QWidget.__init__(self)
    self.livre = livre
    self.build()
  def build(self):
    self.setWindowTitle("Liste livre")
    self.table = QTableWidget(self)
    self.livre.listerLivres(self.table)
    self.setGeometry(400,300,600,500)
    self.table.resize(600,100)
