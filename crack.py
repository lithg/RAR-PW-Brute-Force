# -*- coding: utf-8 -*-

'''
RAR Password Cracker
Author: lithg
github.com/lithg
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import webbrowser
import sys
import style
import rarfile
from colorama import Fore, Back, Style
from datetime import datetime, timedelta
import time
import gerador
import threading

wordlist_txt = 'pt_br_wordlist.txt'
comb_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
comb_lower = 'abcdefghijklmnopqrstuvwxyz'
comb_numb = '0123456789'
comb_especial = '!@#$%¨&*()-_=+´`[{}}:>;.,<'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(30, 10, 91, 71))
        self.btn_open.setStyleSheet(style.styleBtn)
        self.btn_open.setObjectName("btn_open")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(200, 10, 91, 71))
        self.btn_start.setStyleSheet(style.styleBtn)
        self.btn_start.setObjectName("btn_start")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(370, 10, 91, 71))
        self.btn_stop.setStyleSheet(style.styleBtn)
        self.btn_stop.setObjectName("btn_stop")
        self.btn_help = QtWidgets.QPushButton(self.centralwidget)
        self.btn_help.setGeometry(QtCore.QRect(540, 10, 91, 71))
        self.btn_help.setStyleSheet(style.styleBtn)
        self.btn_help.setObjectName("btn_help")
        self.btn_about = QtWidgets.QPushButton(self.centralwidget)
        self.btn_about.setGeometry(QtCore.QRect(710, 10, 91, 71))
        self.btn_about.setStyleSheet(style.styleBtn)
        self.btn_about.setObjectName("btn_about")
        self.label_path_rar = QtWidgets.QLabel(self.centralwidget)
        self.label_path_rar.setGeometry(QtCore.QRect(20, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_path_rar.setFont(font)
        self.label_path_rar.setObjectName("label_path_rar")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 120, 481, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_tipo_ataque = QtWidgets.QLabel(self.centralwidget)
        self.label_tipo_ataque.setGeometry(QtCore.QRect(550, 95, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_tipo_ataque.setFont(font)
        self.label_tipo_ataque.setObjectName("label_tipo_ataque")
        self.combo_tipo_ataque = QtWidgets.QComboBox(self.centralwidget)
        self.combo_tipo_ataque.setGeometry(QtCore.QRect(550, 120, 251, 31))
        self.combo_tipo_ataque.setObjectName("combo_tipo_ataque")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 80, 831, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 105, 371, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(8, 150, 502, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 110, 20, 51))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 103, 8, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(500, 110, 20, 50))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(530, 107, 20, 54))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(540, 100, 8, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(540, 150, 271, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(800, 106, 20, 51))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(670, 97, 141, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 170, 811, 181))
        self.tabWidget.setObjectName("tabWidget")
        self.brute_tab = QtWidgets.QWidget()
        self.brute_tab.setObjectName("brute_tab")
        self.spinBox = QtWidgets.QSpinBox(self.brute_tab)
        self.spinBox.setGeometry(QtCore.QRect(710, 40, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.cb_upper = QtWidgets.QCheckBox(self.brute_tab)
        self.cb_upper.setGeometry(QtCore.QRect(10, 43, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_upper.setFont(font)
        self.cb_upper.setObjectName("cb_upper")
        self.cb_numb = QtWidgets.QCheckBox(self.brute_tab)
        self.cb_numb.setGeometry(QtCore.QRect(10, 77, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_numb.setFont(font)
        self.cb_numb.setObjectName("cb_numb")
        self.label_spin = QtWidgets.QLabel(self.brute_tab)
        self.label_spin.setGeometry(QtCore.QRect(550, 43, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_spin.setFont(font)
        self.label_spin.setObjectName("label_spin")
        self.label_5 = QtWidgets.QLabel(self.brute_tab)
        self.label_5.setGeometry(QtCore.QRect(10, 7, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cb_especial = QtWidgets.QCheckBox(self.brute_tab)
        self.cb_especial.setGeometry(QtCore.QRect(240, 77, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_especial.setFont(font)
        self.cb_especial.setObjectName("cb_especial")
        self.cb_lower = QtWidgets.QCheckBox(self.brute_tab)
        self.cb_lower.setGeometry(QtCore.QRect(240, 43, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_lower.setFont(font)
        self.cb_lower.setObjectName("cb_lower")
        self.cb_numb.raise_()
        self.spinBox.raise_()
        self.cb_upper.raise_()
        self.cb_numb.raise_()
        self.label_spin.raise_()
        self.label_5.raise_()
        self.cb_especial.raise_()
        self.cb_lower.raise_()
        self.tabWidget.addTab(self.brute_tab, "")
        self.dict_tab = QtWidgets.QWidget()
        self.dict_tab.setObjectName("dict_tab")
        self.line_16 = QtWidgets.QFrame(self.dict_tab)
        self.line_16.setGeometry(QtCore.QRect(0, 15, 20, 51))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_15 = QtWidgets.QFrame(self.dict_tab)
        self.line_15.setGeometry(QtCore.QRect(8, 55, 502, 20))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.label_dict_path = QtWidgets.QLabel(self.dict_tab)
        self.label_dict_path.setGeometry(QtCore.QRect(20, 5, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dict_path.setFont(font)
        self.label_dict_path.setObjectName("label_dict_path")
        self.txtEdt_dict = QtWidgets.QTextEdit(self.dict_tab)
        self.txtEdt_dict.setGeometry(QtCore.QRect(20, 25, 481, 31))
        self.txtEdt_dict.setObjectName("txtEdt_dict")
        self.line_12 = QtWidgets.QFrame(self.dict_tab)
        self.line_12.setGeometry(QtCore.QRect(10, 8, 8, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.dict_tab)
        self.line_13.setGeometry(QtCore.QRect(500, 15, 20, 50))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.dict_tab)
        self.line_14.setGeometry(QtCore.QRect(140, 10, 371, 16))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.btn_buscar = QtWidgets.QPushButton(self.dict_tab)
        self.btn_buscar.setGeometry(QtCore.QRect(520, 15, 91, 51))
        self.btn_buscar.setStyleSheet(style.styleBtn)
        self.btn_buscar.setObjectName("btn_buscar")
        self.cb_all_comb = QtWidgets.QCheckBox(self.dict_tab)
        self.cb_all_comb.setGeometry(QtCore.QRect(20, 110, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_all_comb.setFont(font)
        self.cb_all_comb.setObjectName("cb_all_comb")
        self.cb_dict_padrao = QtWidgets.QCheckBox(self.dict_tab)
        self.cb_dict_padrao.setGeometry(QtCore.QRect(20, 80, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_dict_padrao.setFont(font)
        self.cb_dict_padrao.setObjectName("cb_dict_padrao")
        self.tabWidget.addTab(self.dict_tab, "")
        self.label_tentando = QtWidgets.QLabel(self.centralwidget)
        self.label_tentando.setGeometry(QtCore.QRect(50, 490, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_tentando.setFont(font)
        self.label_tentando.setObjectName("label_tentando")
        self.label_tentando_valor = QtWidgets.QLabel(self.centralwidget)
        self.label_tentando_valor.setGeometry(QtCore.QRect(130, 490, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_tentando_valor.setFont(font)
        self.label_tentando_valor.setStyleSheet("color: red")
        self.label_tentando_valor.setObjectName("label_tentando_valor")
        self.label_velocidade_valor = QtWidgets.QLabel(self.centralwidget)
        self.label_velocidade_valor.setGeometry(QtCore.QRect(310, 490, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_velocidade_valor.setFont(font)
        self.label_velocidade_valor.setStyleSheet("color: red")
        self.label_velocidade_valor.setObjectName("label_velocidade_valor")
        self.label_velocidade = QtWidgets.QLabel(self.centralwidget)
        self.label_velocidade.setGeometry(QtCore.QRect(220, 490, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_velocidade.setFont(font)
        self.label_velocidade.setObjectName("label_velocidade")
        self.label_dur_valor = QtWidgets.QLabel(self.centralwidget)
        self.label_dur_valor.setGeometry(QtCore.QRect(460, 490, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dur_valor.setFont(font)
        self.label_dur_valor.setStyleSheet("color: red")
        self.label_dur_valor.setObjectName("label_dur_valor")
        self.label_dur = QtWidgets.QLabel(self.centralwidget)
        self.label_dur.setGeometry(QtCore.QRect(390, 490, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dur.setFont(font)
        self.label_dur.setObjectName("label_dur")
        self.label_eta_valor = QtWidgets.QLabel(self.centralwidget)
        self.label_eta_valor.setGeometry(QtCore.QRect(660, 490, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_eta_valor.setFont(font)
        self.label_eta_valor.setStyleSheet("color: red")
        self.label_eta_valor.setObjectName("label_eta_valor")
        self.label_eta = QtWidgets.QLabel(self.centralwidget)
        self.label_eta.setGeometry(QtCore.QRect(600, 490, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_eta.setFont(font)
        self.label_eta.setObjectName("label_eta")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(260, 370, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")
        self.label_status_valor = QtWidgets.QLabel(self.centralwidget)
        self.label_status_valor.setGeometry(QtCore.QRect(340, 370, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_status_valor.setFont(font)
        self.label_status_valor.setStyleSheet("color: red")
        self.label_status_valor.setObjectName("label_status_valor")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(257, 410, 331, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(0, 460, 821, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAttack = QtWidgets.QMenu(self.menubar)
        self.menuAttack.setObjectName("menuAttack")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSair)
        self.menuAttack.addAction(self.actionStart)
        self.menuAttack.addAction(self.actionStop)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAttack.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tabWidget.setStyleSheet(style.tabStyle)

        self.btn_open.setIcon(QtGui.QIcon('img/rar.png'))
        self.btn_open.setIconSize(QtCore.QSize(100,100))
        self.btn_about.setIcon(QtGui.QIcon('img/star.png'))
        self.btn_about.setIconSize(QtCore.QSize(60,60))
        self.btn_start.setIcon(QtGui.QIcon('img/start.png'))
        self.btn_start.setIconSize(QtCore.QSize(65,65))
        self.btn_stop.setIcon(QtGui.QIcon('img/stop.png'))
        self.btn_stop.setIconSize(QtCore.QSize(65,65))
        self.btn_help.setIcon(QtGui.QIcon('img/info.png'))
        self.btn_help.setIconSize(QtCore.QSize(65,65))
        self.textEdit.setReadOnly(True)
        self.txtEdt_dict.setReadOnly(True)
        self.combo_tipo_ataque.addItem("Brute-force")
        self.combo_tipo_ataque.addItem("Dicionário")
        self.spinBox.setValue(1)
        self.label_status_valor.hide()
        self.label_dur_valor.setStyleSheet('font-size: 12pt; color: green')




        #---------------------- SINGALS ---------------------
        self.combo_tipo_ataque.currentIndexChanged.connect(self.combobox_tipo)
        self.btn_open.clicked.connect(self.abrir_rar)
        self.btn_start.clicked.connect(self.t1)
        self.btn_about.clicked.connect(self.gitstar)







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RAR Password Cracker // github.com/lithg"))
        self.label_path_rar.setText(_translate("MainWindow", "Path do arquivo: "))
        self.label_tipo_ataque.setText(_translate("MainWindow", "Tipo de ataque: "))
        self.cb_upper.setText(_translate("MainWindow", "Todas as letras maiúsculas (A - Z)"))
        self.cb_numb.setText(_translate("MainWindow", "Todos os números (0 - 9)"))
        self.label_spin.setText(_translate("MainWindow", "Quantidade de caracteres"))
        self.label_5.setText(_translate("MainWindow", "Configuração"))
        self.cb_especial.setText(_translate("MainWindow", "Todos os caracteres especiais (!@#$...)"))
        self.cb_lower.setText(_translate("MainWindow", "Todas as letras minúsculas (a - z)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.brute_tab), _translate("MainWindow", "Brute-force"))
        self.label_dict_path.setText(_translate("MainWindow", "Path do arquivo: "))
        self.btn_buscar.setText(_translate("MainWindow", "BUSCAR"))
        self.cb_all_comb.setText(_translate("MainWindow", "Tentar todas as combinações maiúscula / minúscula"))
        self.cb_dict_padrao.setText(_translate("MainWindow", "Usar dicionário padrão (wordlist.txt)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dict_tab), _translate("MainWindow", "Dicionário"))
        self.label_tentando.setText(_translate("MainWindow", "Tentando:"))
        self.label_tentando_valor.setText(_translate("MainWindow", "0000"))
        self.label_velocidade_valor.setText(_translate("MainWindow", "0000"))
        self.label_velocidade.setText(_translate("MainWindow", "Tentativas:"))
        self.label_dur_valor.setText(_translate("MainWindow", "0d/0h/0m/0s"))
        self.label_dur.setText(_translate("MainWindow", "Duração:"))
        self.label_eta_valor.setText(_translate("MainWindow", "0d/0h/0m/0s"))
        self.label_eta.setText(_translate("MainWindow", "ETA:"))
        self.label_status.setText(_translate("MainWindow", "STATUS:"))
        self.label_status_valor.setText(_translate("MainWindow", "Brute-force em andamento..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAttack.setTitle(_translate("MainWindow", "Attack"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.statusbar.setToolTip(_translate("MainWindow", "Feito por: lithg // github.com/lithg"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file..."))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))


    def combobox_tipo(self):
        if (self.combo_tipo_ataque.currentIndex() == 0):
            self.tabWidget.setCurrentIndex(0)

        elif (self.combo_tipo_ataque.currentIndex() == 1):
            self.tabWidget.setCurrentIndex(1)

    def abrir_rar(self):
        global fileName
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"Escolha o arquivo .rar", "","RAR (*.rar)" , options=options)
        if fileName:
            print(fileName)
            self.textEdit.setText(fileName)



    def t1(self):
        t1 = threading.Thread(target=self.crack)
        t1.start()

    def t2(self):
        t2 = threading.Thread(target=self.bruteforce)
        t2.start()

    def t3(self):
        t3 = threading.Thread(target=self.stopb)
        t3.start()


    def crack(self):
        self.label_status_valor.setText("Quebrando senha...")
        self.label_status_valor.show()
        global charset
        global length
        length = self.spinBox.value()
        l = []
        ataque = self.combo_tipo_ataque.currentText()
        if (ataque == 'Brute-force'):

            if self.cb_numb.isChecked():
                l.append(comb_numb)

            if self.cb_lower.isChecked():
                l.append(comb_upper)

            if self.cb_upper.isChecked():
                l.append(comb_upper)

            if self.cb_especial.isChecked():
                l.append(comb_especial)

            charset = ''.join(l)

            try:
                self.t2()

            except:
                self.label_status_valor.setText('Arquivo inválido ou vazio!')
                self.label_status_valor.show()



    def dict(self):
        global tempo
        passwd_testados = 0
        encontrou = False

        if rarfile.is_rarfile('rarf.rar'):
            with rarfile.RarFile('rarf.rar') as rf:
                wordlist = open(wordlist_txt, 'r')
                start = time.time()         # inicia contador de duracao
                for senha in wordlist:

                    try:
                        rf.extractall(path='.', members=rf.namelist(), pwd=senha.strip())

                    except:
                        print(Fore.RED + '[+] Testando: ' + senha.strip())
                        self.label_tentando_valor.setText(senha.strip())

                    else:
                        print(Fore.RED + '[+] Testando: ' + senha + '\n')
                        self.label_tentando_valor.setText(senha.strip())
                        print(Fore.GREEN + '[*] SENHA ENCONTRADA: {}'.format(senha))
                        self.label_status_valor.setText('[*] SENHA ENCONTRADA: {}'.format(senha))
                        self.label_status_valor.show()
                        print(Fore.GREEN + '[*] TENTATIVAS: ' + str(passwd_testados))
                        self.label_velocidade_valor.setText(str(passwd_testados))
                        end = time.time()  # finaliza contador
                        tempo = end - start
                        self.duracao()
                        encontrou = True
                        break

                    passwd_testados += 1

                if not encontrou:
                    print(Fore.LIGHTRED_EX + '[*] SENHA NÃO ENCONTRADA')

                else:

                    for f in rf.infolist():
                        print(Fore.LIGHTBLUE_EX + 'Arquivo: ' + f.filename)
                        print(Fore.LIGHTBLUE_EX + 'Tamanho: ' + str(f.file_size) + ' KB\n')

        else:
            print('Arquivo inválido')



    def bruteforce(self):
        lista = list(gerador.gerador(charset, length))
        global tempo
        global stop_flag
        stop_flag = False
        passwd_testados = 0
        encontrou = False

        try:
            fileName

        except NameError:
            self.label_status_valor.setText('ERR! ARQUIVO NÃO EXISTE')

        if rarfile.is_rarfile(fileName) and fileName != None:
            with rarfile.RarFile(fileName) as rf:
                start = time.time()         # inicia contador de duracao
                self.btn_start.setStyleSheet(style.styleBtnDisabled)
                self.btn_start.setDisabled(True)

                for senha in lista:
                    senha = ''.join(senha)

                    try:
                        rf.extractall(path='.', members=rf.namelist(), pwd=senha)

                    except:
                        end2 = time.time()
                        print(Fore.RED + '[+] Testando: ' + senha)
                        self.label_tentando_valor.setText(senha)
                        self.label_velocidade_valor.setText(str(passwd_testados))

                        self.label_dur_valor.setText(time.strftime("%H:%M:%S", time.gmtime(end2-start)))


                    else:

                        print(Fore.RED + '[+] Testando: ' + senha + '\n')
                        self.label_tentando_valor.setText(senha)
                        self.label_status_valor.setStyleSheet('font-size: 12pt; font-family: Courier;, color: green')
                        print(Fore.GREEN + '[*] SENHA ENCONTRADA: {}'.format(senha))
                        self.label_status_valor.setText('SENHA ENCONTRADA: {}'.format(senha))
                        print(Fore.GREEN + '[*] TENTATIVAS: ' + str(passwd_testados))
                        self.label_velocidade_valor.setText(str(passwd_testados))
                        end = time.time()  # finaliza contador
                        tempo = end - start
                        self.duracao()
                        encontrou = True
                        self.btn_start.setStyleSheet(style.styleBtn)
                        self.btn_start.setDisabled(False)
                        break

                    passwd_testados += 1

                if not encontrou:
                    print(Fore.LIGHTRED_EX + '[*] SENHA NÃO ENCONTRADA')

                else:

                    for f in rf.infolist():
                        print(Fore.LIGHTBLUE_EX + 'Arquivo: ' + f.filename)
                        print(Fore.LIGHTBLUE_EX + 'Tamanho: ' + str(f.file_size) + ' KB\n')

        else:
            self.label_status_valor.setText('ERR! ARQUIVO INVÁLIDO')

    def duracao(self):
        sec = timedelta(seconds=tempo)
        d = datetime(1,1,1) + sec

        print("Duração: %dd:%dh:%dm:%ds" % (d.day-1, d.hour, d.minute, d.second))
        print()
        self.label_dur_valor.setStyleSheet('font-size: 12pt; color: green')
        self.label_dur_valor.setText("%dd:%dh:%dm:%ds" % (d.day-1, d.hour, d.minute, d.second))

    def sair(self):
        sys.exit()

    def stopb(self):
        stop_flag = True

    def gitstar(self):
        webbrowser.open('https://github.com/lithg/RAR-PW-Brute-Force')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

