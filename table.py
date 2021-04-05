# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import config
import mysql_functions


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 110, 160, 102))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.getAllDatabasesButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getAllDatabasesButton.setObjectName("getAllDatabasesButton")

        self.getAllDatabasesButton.clicked.connect(self.load_databases)

        self.verticalLayout.addWidget(self.getAllDatabasesButton)
        self.tableDatabases = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableDatabases.setObjectName("tableDatabases")
        self.tableDatabases.setColumnCount(0)
        self.tableDatabases.setRowCount(0)
        self.verticalLayout.addWidget(self.tableDatabases)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.getAllDatabasesButton.setText(_translate("MainWindow", "Get All Databases"))


    def load_databases(self):
        mysql_config = config.load_config("mysql_config.json")
        mysql_functions.connection(mysql_config["host"], mysql_config["user"], mysql_config["password"])
        columns = ["Database Name"]
        data = [db for db in mysql_functions.show_databases()]
        num_rows = len(data)
        num_cols = len(columns)

        self.tableDatabases.setRowCount(num_rows)
        self.tableDatabases.setColumnCount(num_cols)

        self.tableDatabases.setHorizontalHeaderLabels(columns)

        for row in range(num_rows):
            for column in range(num_cols):
                self.tableDatabases.setItem(row, column, QtWidgets.QTableWidgetItem((str(data[row][column]))))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
