from MainWindow import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('HangMan')
    window.setWindowIcon(QtGui.QIcon('assets\\icon.png'))
    window.show()
    sys.exit(app.exec_())

    #to be fixed
    #try statement for word settings for internet
    #settings when not choosing all