from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

if __name__ == "__main__":
    app = QApplication([])
    w = QWidget()
    w.setWindowTitle("new app")

    l = QLineEdit(w)
    p = QPushButton(w)
    w.show()



    app.exec_()
