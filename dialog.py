from PyQt5 import QtCore, QtGui, QtWidgets
import mysql_functions
from functools import partial

class Dialog(QtWidgets.QDialog):
    def __init__(self, db_name, table_name, data, mode):
        super().__init__()

        self.search_results = []

        columns = [column[0] for column in mysql_functions.show_columns(db_name, table_name)]

        # self.db_name = db_name
        # self.table_name = table_name
        # self.columns = columns

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

        if mode == "update":
            for i, t in enumerate(self.texts):
                t.setText(str(data[i]))
            self.button.setObjectName("updateButton")
            self.button.setText("Update")
            self.button.clicked.connect(partial(self.update, db_name, table_name, columns))
        elif mode == "insert":
            self.button.setObjectName("insertButton")
            self.button.setText("Insert")
            self.button.clicked.connect(partial(self.insert, db_name, table_name, columns))
            # self.button.clicked.connect(self.insert)
        elif mode == "search":
            self.button.setObjectName("searchButton")
            self.button.setText("Search")
            self.button.clicked.connect(partial(self.search, db_name, table_name, columns))



        self.layout.addWidget(self.button)
        
        # OVA LINIJA ISPOD JE DODATA NAKNADNO DA BI DIJALOG IZGLEDAO KAKO TREBA JER NISMO STIGLI NA VJEZBAMA
        # POSTAVLJANJE (SETOVANJE) LAYOUT-A DIJALOGU
        self.setLayout(self.layout)


    # def insert(self):
    #   values = tuple([text.text().strip() for text in self.texts])
    #   mysql_functions.insert(self.db_name, self.table_name, self.columns, values)
    def insert(self, db_name, table_name, columns):
        values = tuple([text.text().strip() for text in self.texts])
        mysql_functions.insert(db_name, table_name, columns, values)
        self.clear_all()

    def clear_all(self):
        for t in self.texts:
            t.clear()

    def update(self, db_name, table_name, columns):
        values = tuple([text.text().strip() for text in self.texts])
        mysql_functions.update(db_name, table_name, columns, values)
        self.close()

    def search(self, db_name, table_name, columns):
        values = tuple([text.text().strip() for text in self.texts])
        
        # OVA LINIJA ISPOD JE MODIFIKOVANA JER NISMO STIGLI NA VJEZBAMA
        # KREIRANJE LISTE ITERISANJEM KROZ MYSQL CURSOR KOJEG DOBIJAMO KAO POVRATNU VRIJEDNOST FUNKCIJE mysql_functions.search
        self.search_results = [result for result in mysql_functions.search(db_name, table_name, columns, values)]

    def get_search_results(self):
        return self.search_results

