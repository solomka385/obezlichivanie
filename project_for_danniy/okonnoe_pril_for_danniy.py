import psycopg2
import pandas as pd
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QDrag
from PyQt5 import QtCore
import sys
from PyQt5.QtGui import QPalette, QBrush, QPixmap
win_width, win_height = 500, 700
win_x, win_y = 800, 80
global_strok,global_input = '',''
class MainWindow(QWidget):
    
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags) 
        global global_strok,global_input
        
        self.initUI()
        self.set_appear()  
        self.connects()
        self.show()
    def initUI(self):
        
        self.layout_line = QVBoxLayout()
        self.layout_line1 = QHBoxLayout()
        self.layout_line2 = QHBoxLayout()
        self.layout_line3 = QHBoxLayout()
        self.layout_line4 = QHBoxLayout()
        self.layout_line5 = QHBoxLayout()
        self.layout_line6 = QHBoxLayout()
        self.layout_line6 = QHBoxLayout()
        self.layout_line7 = QHBoxLayout()
        self.btn_1 = QPushButton('Сохранить', self)

        self.database = QLabel('Введите базу данных:')
        self.database_input = QLineEdit('')
        self.user = QLabel('Введите пользователя:')
        self.user_input = QLineEdit('')
        self.password = QLabel('Введите пароль:')
        self.password_input = QLineEdit('')
        self.host = QLabel('Введите хост:')
        self.host_input = QLineEdit('')
        self.port = QLabel('Введите порт:')
        self.port_input = QLineEdit('')
        self.table = QLabel('Введите таблицу:')
        self.table_input = QLineEdit('')
        
        self.layout_line1.addWidget(self.database)
        self.layout_line1.addWidget(self.database_input)

        self.layout_line2.addWidget(self.user)
        self.layout_line2.addWidget(self.user_input)

        self.layout_line3.addWidget(self.password)
        self.layout_line3.addWidget(self.password_input)

        self.layout_line4.addWidget(self.host)
        self.layout_line4.addWidget(self.host_input)

        self.layout_line5.addWidget(self.port)
        self.layout_line5.addWidget(self.port_input)

        self.layout_line6.addWidget(self.table)
        self.layout_line6.addWidget(self.table_input)
       
        self.layout_line7.addWidget(self.btn_1)
        
        self.database.setFont(QFont('Arial Bold',12, QFont.Bold))
        self.user.setFont(QFont('Arial Bold',12, QFont.Bold))
        self.password.setFont(QFont('Arial Bold',12, QFont.Bold))
        self.host.setFont(QFont('Arial Bold',12, QFont.Bold))
        self.port.setFont(QFont('Arial Bold',12, QFont.Bold))
        self.table.setFont(QFont('Arial Bold',12, QFont.Bold))
        
        self.layout_line.addLayout(self.layout_line1)
        self.layout_line.addLayout(self.layout_line2)
        self.layout_line.addLayout(self.layout_line3)
        self.layout_line.addLayout(self.layout_line4)
        self.layout_line.addLayout(self.layout_line5)
        self.layout_line.addLayout(self.layout_line6)
        self.layout_line.addLayout(self.layout_line7)

        self.setLayout(self.layout_line)
  #Обновление экрана
    def shor(self):
        global global_strok,global_input
        pass
        
    def set_appear(self):
        self.setWindowTitle('Окно вывода')
        self.resize(win_width+500, win_height)
        self.move(win_x-800, win_y)
    def connects(self):
        self.btn_1.clicked.connect(self.clicked)
    def clicked(self):
        cdi_stress=psycopg2.connect(database=str(self.database_input.text()),user=str(self.user_input.text()), password=str(self.password_input.text()),host=str(self.host_input.text()), port=str(self.port_input.text()))
        df = pd.read_sql(("SELECT * from "+str(self.table_input.text())+" limit 25;"),cdi_stress)
        print(df)
        cdi_stress.close()


app = QApplication(sys.argv)
mn = MainWindow()
app.exec_()