from PyQt5.QtWidgets import QApplication,QDialog
from MainScreen import Ui_Dialog

class Main(QDialog):

    def __init__(self)->None:
        super().__init__()
        self.pencere = Ui_Dialog()
        self.pencere.setupUi(self)
        self.pencere.pushButton.clicked.connect(self.handle_button_click)
        self.pencere.pushButton_2.clicked.connect(self.handle_button_click_2)

    def handle_button_click(self):
        # This method will be called when the button is clicked
        print("Button Clicked!")

    def handle_button_click_2(self):
        # This method will be called when the button is clicked
        print("Button 2 Clicked!")

app = QApplication([])
pencere = Main()
pencere.show()
app.exec_()