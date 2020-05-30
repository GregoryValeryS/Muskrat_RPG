# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\Muskrat_RPG\NPC_generator\main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_add_or_remove_NPC = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_add_or_remove_NPC.setGeometry(QtCore.QRect(280, 10, 111, 51))
        self.groupBox_add_or_remove_NPC.setObjectName("groupBox_add_or_remove_NPC")
        self.pushButton_remove_NPC = QtWidgets.QPushButton(self.groupBox_add_or_remove_NPC)
        self.pushButton_remove_NPC.setGeometry(QtCore.QRect(60, 16, 41, 31))
        self.pushButton_remove_NPC.setObjectName("pushButton_remove_NPC")
        self.pushButton_add_NPC = QtWidgets.QPushButton(self.groupBox_add_or_remove_NPC)
        self.pushButton_add_NPC.setGeometry(QtCore.QRect(10, 16, 41, 31))
        self.pushButton_add_NPC.setObjectName("pushButton_add_NPC")
        self.groupBox_battlelog = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_battlelog.setGeometry(QtCore.QRect(10, 10, 261, 361))
        self.groupBox_battlelog.setObjectName("groupBox_battlelog")
        self.textEdit_battlelog = QtWidgets.QTextEdit(self.groupBox_battlelog)
        self.textEdit_battlelog.setGeometry(QtCore.QRect(10, 20, 241, 331))
        self.textEdit_battlelog.setObjectName("textEdit_battlelog")
        self.loot_generator = QtWidgets.QGroupBox(self.centralwidget)
        self.loot_generator.setGeometry(QtCore.QRect(280, 70, 111, 61))
        self.loot_generator.setObjectName("loot_generator")
        self.pushButton_loot = QtWidgets.QPushButton(self.loot_generator)
        self.pushButton_loot.setGeometry(QtCore.QRect(10, 20, 41, 31))
        self.pushButton_loot.setObjectName("pushButton_loot")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_add_or_remove_NPC.setTitle(_translate("MainWindow", "Add or Remove NPC"))
        self.pushButton_remove_NPC.setText(_translate("MainWindow", "-"))
        self.pushButton_add_NPC.setText(_translate("MainWindow", "+"))
        self.groupBox_battlelog.setTitle(_translate("MainWindow", "Battlelog"))
        self.loot_generator.setTitle(_translate("MainWindow", "Loot generator"))
        self.pushButton_loot.setText(_translate("MainWindow", "Loot!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
