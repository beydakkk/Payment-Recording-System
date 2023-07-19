from PyQt5.QtWidgets import QApplication,QDialog
from MainScreen import Ui_Dialog

class Main(QDialog):

    def __init__(self)->None:
        super().__init__()
        self.pencere = Ui_Dialog()
        self.pencere.setupUi(self)

app = QApplication([])
pencere = Main()
pencere.show()
app.exec_()