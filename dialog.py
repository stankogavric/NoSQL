from PyQt5 import QtCore, QtGui, QtWidgets
import mysql_functions

class Dialog(QtWidgets.QDialog):
    def __init__(self, db_name, table_name, data, mode):
        super().__init__()

        columns = [column[0] for column in mysql_functions.show_columns(db_name, table_name)]

        self.setWindowTitle("Dialog")

        self.layout = QtWidgets.QVBoxLayout()

        self.texts = []

        for column in columns:
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.label = QtWidgets.QLabel(self)
            self.label.setObjectName(column)
            self.label.setText(column)
            self.horizontalLayout.addWidget(self.label)
            self.lineEdit = QtWidgets.QLineEdit(self)
            self.lineEdit.setObjectName(column+"lineEdit")
            self.horizontalLayout.addWidget(self.lineEdit)
            self.layout.addLayout(self.horizontalLayout)
            self.texts.append(self.lineEdit)

        self.button = QtWidgets.QPushButton(self)

        self.button.setObjectName("insertButton")
        self.button.setText("Insert")
        self.button.clicked.connect(self.insert)

        self.layout.addWidget(self.button)
        
        # OVA LINIJA ISPOD JE DODATA NAKNADNO DA BI DIJALOG IZGLEDAO KAKO TREBA JER NISMO STIGLI NA VJEZBAMA
        # POSTAVLJANJE (SETOVANJE) LAYOUT-A DIJALOGU
        self.setLayout(self.layout)


    def insert(self):
        values = tuple([text.text().strip() for text in self.texts])
        # insert
