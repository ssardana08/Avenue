import sys
from PyQt4 import QtGui, QtCore

# This class is made for Window in our app
class Window(QtGui.QMainWindow):

	#this is called everytime a new object of this class is created
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("PyQT tuts!")
		self.setWindowIcon(QtGui.QIcon('../ui_files/logo.png'))
		
		
		#Declaring Exit Actions
		extractAction = QtGui.QAction("&Exit", self)
		extractAction.setShortcut("Ctrl+q")
		extractAction.setStatusTip("Leave The App")
		extractAction.triggered.connect(self.close_application)

		
		#declaring Settings Action
		settingAction = QtGui.QAction("&Settings", self)
		#settingAction.setShortcut("")
		settingAction.setStatusTip("Change the settings")
		settingAction.triggered.connect(self.test)

		#declaring Documentation Action
		docAction = QtGui.QAction("&Documentation", self)
		#docAction.setShortcut("")
		docAction.setStatusTip("Read the Documentation")
		docAction.triggered.connect(self.test)

		#declaring About Action
		aboutAction = QtGui.QAction("&About Avenue", self)
		#aboutAction.setShortcut("")
		aboutAction.setStatusTip("Know More About Avenue")
		aboutAction.triggered.connect(self.test)


		self.statusBar()

		#Creating a Menu Bar
		mainMenu = self.menuBar()

		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(settingAction)
		fileMenu.addAction(extractAction)

		helpMenu = mainMenu.addMenu('&Help')
		helpMenu.addAction(docAction)
		helpMenu.addAction(aboutAction)

		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit", self)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		#Create a Button Of OUR own
		btn.clicked.connect(self.close_application)

		#btn.resize(100,100)
		btn.move(100,100)


		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		#checkBox.move(100,25)
		checkBox.stateChanged.connect(self.enlarge_window) 


		self.show()

	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50, 50, 1000, 600)
		else:
			self.setGeometry(50, 50, 500, 300)

	def close_application(self):
		
		choice = QtGui.QMessageBox.question(self,'Extract',
											"Are you sure to quit?",
											QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

		if choice == QtGui.QMessageBox.Yes:
			print("Time to go My Buoyyy")
			sys.exit()
		else:
			pass




	def test(self):
		print("Hello World")


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()

	sys.exit(app.exec_())

# Lets run this thing up
run()