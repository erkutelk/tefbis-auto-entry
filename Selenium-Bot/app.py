from PyQt5 import QtWidgets
import sys
from MainApp import Ui_MainWindow
from okulOncesiBirimlerModulu import okulOncesiBirimler
from okulAileBirligiModulu import okulAileBirliğiModülü
class Myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(Myapp,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.fonksiyon)
        self.ui.pushButton_2.clicked.connect(self.fonksiyon2)


    def fonksiyon(self):
        okulOncesiBirimler()

        
    def fonksiyon2(self):
        okulAileBirliğiModülü()


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Myapp()  # Myapp sınıfından bir nesne oluşturun
    win.show()
    sys.exit(app.exec_())

app()