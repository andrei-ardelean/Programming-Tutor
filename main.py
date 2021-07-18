import sys

from PyQt5.QtWidgets import QApplication

from view import View


class Main:
    def __init__(self):
        app = QApplication(sys.argv)
        ui = View()
        ui.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main = Main()
