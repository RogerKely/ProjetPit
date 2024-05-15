import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class QuelClient(QtWidgets.QWidget):
  fermetureClient = QtCore.pyqtSignal(str)
  def __init__(self,parent=None):
    super(QuelClient,self).__init__(parent)
    self.setWindowTitle("Quel client ?")
    self.resize(300,100)
    self.lineEdit = QtWidgets.QLineEdit(self)
    self.bouton = QtWidgets.QPushButton("Ok", self)
    self.bouton.clicked.connect(self.ok_m)
    posit = QtWidgets.QGridLayout()
    posit.addWidget(self.lineEdit, 0,0)
    posit.addWidget(self.bouton, 1,0)
    self.setLayout(posit)
  def ok_m(self):
    self.fermetureClient.emit(self.lineEdit.text())
    self.close()

class Principal(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
    super(Principal,self).__init__(parent)
    self.setWindowTitle("Fenetre principale")
    self.resize(300,100)
    self.setCentralWidget(QtWidgets.QFrame())
    self.label = QtWidgets.QLabel(self.centralWidget())
    self.bouton =QtWidgets.QPushButton("Sélectionnez un client !", self.centralWidget())
    self.bouton.clicked.connect(self.quelclient_m)
    posit = QtWidgets.QGridLayout()
    posit.addWidget(self.bouton, 0, 0)
    posit.addWidget(self.label, 1,0)
    self.centralWidget().setLayout(posit)
  def quelclient_m(self):
    self.quelclient = QuelClient()
    self.quelclient.fermetureClient.connect(self.clientchoisi)
    self.quelclient.setWindowModality(QtCore.Qt.ApplicationModal)
    self.quelclient.show()
  def clientchoisi(self, client):
    self.label.setText("Client : %s" % client)

if __name__ == "__main__":
  app =QtWidgets.QApplication(sys.argv)
  QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('plastique'))
  main = Principal()
  main.show()
  sys.exit(app.exec_())