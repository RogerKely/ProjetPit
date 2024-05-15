import sys

from PyQt5.QtWidgets import QWidget, QTableWidget
from PyQt5 import QtCore

class ListerMembreView(QWidget):
  fermetureListeMembre = QtCore.pyqtSignal(str)
  def __init__(self,membre):
    QWidget.__init__(self)
    self.membre = membre
    self.build()
  def build(self):
    self.setWindowTitle("Liste membre")
    self.table = QTableWidget(self)
    self.membre.listerMembres(self.table)
    self.setGeometry(400,300,600,500)
    self.table.resize(600,100)
