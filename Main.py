#Libralis
import shutil
import pathlib
from pathlib import Path
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel,QFileDialog
from PySide6.QtCore import Slot
from PySide6 import QtCore, QtWidgets, QtGui

#Main class
class App(QtWidgets.QWidget):
    #Layout
    def __init__(self):
        super().__init__()
        #none direction
        self.direction = ""
        #Ui components
        self.direction_button = QtWidgets.QPushButton("Choose directory")
        self.copy_button = QtWidgets.QPushButton("Copy")
        self.label = QtWidgets.QLabel("choose direction",
                                     alignment=QtCore.Qt.AlignCenter)
        #creating layout
        self.layout = QtWidgets.QVBoxLayout(self)
        #adding widgets to layout
        self.layout.addWidget(self.direction_button)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.copy_button)
        #button clicked
        self.direction_button.clicked.connect(self.get_direction)
        self.copy_button.clicked.connect(self.cloning)

    #geting copy direction
    @QtCore.Slot()
    def get_direction(self):
        self.direction = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "choose folder for copy"
        )
        
        
    #cloning files
    @QtCore.Slot()
    def cloning(self):
    
        home_dir = Path.home()
        destination = self.direction
        
        desktoptheme = pathlib.Path("/usr/share/plasma/desktoptheme/")
        look_and_feel = pathlib.Path(f"{home_dir}/.local/share/plasma/look-and-feel/")

        if (destination == ""):
            self.text.setText("Please choose a folder")

        shutil.copytree(desktoptheme, destination, dirs_exist_ok=True)
        shutil.copytree(look_and_feel, destination, dirs_exist_ok=True)
        
        self.text.setText("Done")





#starting app
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = App()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
    