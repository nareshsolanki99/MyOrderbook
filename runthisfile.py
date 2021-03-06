# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from orderwindow import OrderWindow
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                            QApplication,QMainWindow)
class Ui_MainWindow(object):
    s1 = {"name":"Reliance","ltp":"1911",'change':'-0.16%',"open":"1920.5",'p.close':'1914.25','high':'1945','low':'1905.15'}
    s2 = {"name":"Nationalum","ltp":"48.10",'change':'2.12%',"open":"47.5",'p.close':'47.1','high':'48.85','low':'47.75'}
    s3 = {"name":"Marico","ltp":"423.85",'change':'1.45%',"open":"418.8",'p.close':'417.8','high':'425.8','low':'418.8'}
    s4 = {"name":"Pel","ltp":"1558.15",'change':'4.10%%',"open":"1503",'p.close':'1496.85','high':'1569.85','low':'1500.1'}
    s = [s1,s2,s3,s4]

    def buy(self):
        "This will open the orderwindow for buying purpose"
        row = self.tableWidget.currentRow()
        stk = []
        for x in range(6):
            stock = self.tableWidget.item(row,x).text()
            stk.append(stock)
        self.win = OrderWindow()
        self.win.label_order.setText("Buy")
        self.win.label_stock.setText(stk[0])
        self.win.pushButton_bs.setText("Buy")
        qty = self.win.lineEdit_qty.text()
        self.win.label_ltp1.setText(stk[1])
        margin = float(stk[1])* int(qty)
        self.win.label_margin.setText(str(margin))
        self.win.show()

    def sell(self):
        "This will open the orderwindow for selling purpose"
        row = self.tableWidget.currentRow()
        stk = []
        for x in range(6):
            stock = self.tableWidget.item(row,x).text()
            stk.append(stock) 
        self.win = OrderWindow()
        self.win.label_order.setText("Sell")
        self.win.label_stock.setText(stk[0])
        self.win.pushButton_bs.setText("Sell")
        qty = self.win.lineEdit_qty.text()
        self.win.label_ltp1.setText(stk[1])
        margin = float(stk[1])* int(qty)
        self.win.label_margin.setText(str(margin))
        self.win.show()

    def vieworder(self):
        "This will open the orderbook to show executed orders"
        self.win = OrderBook()
        for x in range(len(OrderWindow.order)):
            self.win.tableWidget.insertRow(x)
            orderId = QtWidgets.QTableWidgetItem(str(OrderWindow.order[x].get('orderId')))
            orderId.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            time = QtWidgets.QTableWidgetItem(str(OrderWindow.order[x].get('time')))
            time.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            stock = QtWidgets.QTableWidgetItem(OrderWindow.order[x].get('stock'))
            stock.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            qty = QtWidgets.QTableWidgetItem(OrderWindow.order[x].get('qty'))
            qty.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            bs = QtWidgets.QTableWidgetItem(OrderWindow.order[x].get('bs'))
            bs.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            ltp = QtWidgets.QTableWidgetItem(OrderWindow.order[x].get('ltp'))
            ltp.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            trdp = QtWidgets.QTableWidgetItem(OrderWindow.order[x].get('tradeprice'))
            trdp.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            trdv = QtWidgets.QTableWidgetItem(OrderWindow.order[x].get('tradevalue'))
            trdv.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            product = QtWidgets.QTableWidgetItem(OrderWindow.order[x].get('product'))
            product.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            ordertype = QtWidgets.QTableWidgetItem(OrderWindow.order[x].get('ordertype'))
            ordertype.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            stoploss = QtWidgets.QTableWidgetItem(OrderWindow.order[x].get('stoploss'))
            stoploss.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.win.tableWidget.setItem(x , 0,orderId)
            self.win.tableWidget.setItem(x , 1,time)
            self.win.tableWidget.setItem(x , 2,stock)
            self.win.tableWidget.setItem(x , 3,qty)
            self.win.tableWidget.setItem(x , 4,bs)
            self.win.tableWidget.setItem(x , 5,ltp)
            self.win.tableWidget.setItem(x , 6,trdp)
            self.win.tableWidget.setItem(x , 7,trdv)
            self.win.tableWidget.setItem(x , 8,product)
            self.win.tableWidget.setItem(x , 9,ordertype)
            self.win.tableWidget.setItem(x , 10, stoploss)
        self.win.show()
        
            
        
        

    def setupUi(self, MainWindow):
        "UI Design"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000,800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 30, 731, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 900, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton_ob = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ob.setGeometry(QtCore.QRect(300, 510, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_ob.setFont(font)
        self.pushButton_ob.setObjectName("pushButton_ob")
        self.pushButton_buy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_buy.setGeometry(QtCore.QRect(440, 510, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_buy.setFont(font)
        self.pushButton_buy.setObjectName("pushButton_buy")
        self.pushButton_sell = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sell.setGeometry(QtCore.QRect(572, 510, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_sell.setFont(font)
        self.pushButton_sell.setObjectName("pushButton_sell")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        # Populating tableWidget with the stock data
        for x in range(len(self.s)):
            self.tableWidget.insertRow(x)
            name = QtWidgets.QTableWidgetItem(self.s[x].get('name'))
            name.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            ltp = QtWidgets.QTableWidgetItem(self.s[x].get('ltp'))
            ltp.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            change = QtWidgets.QTableWidgetItem(self.s[x].get('change'))
            change.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            pclose = QtWidgets.QTableWidgetItem(self.s[x].get('p.close'))
            pclose.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            opens = QtWidgets.QTableWidgetItem(self.s[x].get('open'))
            opens.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            close = QtWidgets.QTableWidgetItem(self.s[x].get('close'))
            close.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            high = QtWidgets.QTableWidgetItem(self.s[x].get('high'))
            high.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            low = QtWidgets.QTableWidgetItem(self.s[x].get('low'))
            low.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.tableWidget.setItem(x , 0,name)
            self.tableWidget.setItem(x , 1,ltp)
            self.tableWidget.setItem(x , 2,change)
            self.tableWidget.setItem(x , 3,pclose)
            self.tableWidget.setItem(x , 4,opens)
            self.tableWidget.setItem(x , 5,high)
            self.tableWidget.setItem(x , 6,low)
        #Signals    
        self.pushButton_buy.clicked.connect(self.buy)
        self.pushButton_sell.clicked.connect(self.sell)
        self.pushButton_ob.clicked.connect(self.vieworder)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Nifty 50"))
        self.label_4.setText(_translate("MainWindow", "14137   -0.06%"))
        self.label.setText(_translate("MainWindow", "Sensex"))
        self.label_3.setText(_translate("MainWindow", "48093   -0.17%"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Stock Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LTP"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "%Change"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P. Close"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Open"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "High"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Low"))
        self.pushButton_buy.setText(_translate("MainWindow", "Buy"))
        self.pushButton_sell.setText(_translate("MainWindow", "Sell"))
        self.pushButton_ob.setText(_translate("MainWindow", "Order Book"))

class OrderBook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("OrderBook")
        self.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 1200, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 510, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)


        self.setCentralWidget(self.centralwidget)
        


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self,OrderBook):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("OrderBook", "OrderBook"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("OrderBook", "Order Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("OrderBook", "Date Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("OrderBook", "Stock"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("OrderBook", "Qty"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("OrderBook", "B/S"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("OrderBook", "LTP"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("OrderBook", "Trade Price"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("OrderBook", "Trade Value"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("OrderBook", "Product"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("OrderBook", "Order Type"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("OrderBook", "Stop Loss"))
        self.pushButton.setText(_translate("OrderBook", "OK"))
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
