# Life is short, use Python
# ----      utf-8         ----
# @Time     : 2018/5/22  11:00
# @Author   : Gao DongShan
# @File     : main_menu.py
# @Start    :-----------------


import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, qApp, QTableView
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery

ID, SITE, NAME, PASS, REMARK = range(5)


class MainMenu(QMainWindow):

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)

        # -----------------  UI  --------------------------#
        loadUi("./UI/main_ui.ui", self)
        self.setWindowTitle("密码保险柜")
        self.setWindowIcon(QIcon("./image/1.ico"))

        # -----------------  按键  --------------------------#
        self.pushButtonExit.clicked.connect(QCoreApplication.instance().quit)
        self.pushButtonDel.clicked.connect(self.delete)
        self.pushButtonAdd.clicked.connect(self.add)
        self.refresh.clicked.connect(self.reselect)

        # -----------------  db  --------------------------#
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("./db/word.db")

        # -----------------  model  --------------------------#
        self.model = QSqlTableModel()
        self.model.setTable("warehouse")
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, "ID")
        self.model.setHeaderData(SITE, Qt.Horizontal, "站点")
        self.model.setHeaderData(NAME, Qt.Horizontal, "账号")
        self.model.setHeaderData(PASS, Qt.Horizontal, "密码")
        self.model.setHeaderData(REMARK, Qt.Horizontal, "备注")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

        # -----------------  tableView  --------------------------#
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        # -----------------  query  --------------------------#
        self.query = QSqlQuery()

    def contextMenuEvent(self, event):
        cmenu = QMenu()
        quitAct = cmenu.addAction("退出")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()

    def add(self):
        self.query.exec("insert into `warehouse` VALUES (NULL ,'example.com','example','example','example')")
        self.reselect()
        rows = self.model.rowCount()
        self.tableView.selectRow(rows)

    def delete(self):
        row = self.tableView.currentIndex().row()
        site_id = self.model.data(self.model.index(row, 0))
        sql = "delete from `warehouse` where id =" + str(site_id)
        self.query.exec(sql)
        self.reselect()

    def reselect(self):
        if self.model.data(self.model.index(self.model.rowCount(), 0)) != "":
            self.model.select()
