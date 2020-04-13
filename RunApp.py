import sys
import ui_myform
from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ui_myform.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())