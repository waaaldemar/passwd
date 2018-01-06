"""
passwd_gui.py
@wale
"""
import sys
#import pyqt4
from PyQt4 import QtGui, QtCore
import random 
import string


from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *


class Window(QtGui.QMainWindow):
    #win = QWidget() 
    #app = QApplication(sys.argv)
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(70, 120, 240, 200)
        self.setWindowTitle("Password Generator")
        

        self.home()
        
        #Quit button
    def home(self):
        layout = QFormLayout()
        #Quit button
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(80,170)
 
        #Start button
        btn2 = QtGui.QPushButton("Start", self)
        btn2.clicked.connect(self.passwd_generator)
        btn2.resize(btn.minimumSizeHint())
        btn2.move(80,80)
        
        #Character amount
        self.nameLabel = QLabel(self)
        self.nameLabel.setText("How many characters: ")
        self.line = QLineEdit(self)
        
        self.line.move(50, 40)
        self.line.resize(145, 32)
        self.nameLabel.move(65, 10)
        self.nameLabel.resize(200,40)
        
        
        #Password field
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 120)
        self.textbox.resize(200,40)
        
        self.show()
        
        
        
    def getint(self):
        num,ok = QInputDialog.getInt(self,"integer input dualog","enter a number")

        if ok:
            self.le1.setText(str(num))
    
    def passwd_generator(self):
        #Idk what im doing
        charAmount = int(self.line.text())
        if(charAmount >= 101):
            print("Too big")
        
        elif(charAmount <= 3):
            print("Too small")
        
        else:
            allchar = string.ascii_letters + string.digits
            #Generates password
            passWd = ("".join(random.choice(allchar) for i in range(charAmount)))
            print(passWd)
            self.textbox.setText(passWd)

        
    
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Quit",
                                            "Are you 100% sure you want to exit this cool program?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting")
            sys.exit()
        else:
            pass
            
        
def run():
       
    #win.show()
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()            
