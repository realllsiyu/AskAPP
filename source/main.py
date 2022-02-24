
import sys
from PyQt5.QtWidgets import QApplication
from ask_app import Ask_App

if __name__ == '__main__':
    app = QApplication([])

    askpage = Ask_App()
    askpage.show()
    sys.exit(app.exec_())