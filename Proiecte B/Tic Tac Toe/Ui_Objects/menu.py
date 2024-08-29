from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication, QPushButton
import sys 

class Menu(QObject):

    def __init__(self):
        
        # Loading the graphics

        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("F:\\Python\\Proiecte B\\Tic Tac Toe\\Ui-Elements\\Menu.ui")
        self.ui.setWindowTitle('Main Menu')
        self.pressed = None 

        # Extracting the graphical elements for future manipulation

        self.playXButton = self.ui.playXButton
        self.playOButton = self.ui.playOButton
        self.easyButton = self.ui.easyButton
        self.mediumButton = self.ui.mediumButton
        self.hardButton = self.ui.hardButton

        # Initiliazing the signals

        self.easyButton.pressed.connect(self.difficultyButtonPressed)
        self.mediumButton.pressed.connect(self.difficultyButtonPressed)
        self.hardButton.pressed.connect(self.difficultyButtonPressed)

    def difficultyButtonPressed(self):

        self.togglePressedButton()
        sender = self.sender()
        self.pressed = sender

        # Register the difficulty

        match sender.text():
            case 'Easy':
                self.easyButton.setStyleSheet("""
                                            background-color:darkgreen;
                                            border: 1px solid black;
                                            font-size:13px;
                                            font-family: Comic Sans MS;
                                            font-weight: bold;
                                            border-radius: 10px;
                                            padding: 5px;    """)
                self.difficulty = 1
            case 'Medium':
                self.mediumButton.setStyleSheet("""background-color: darkorange;
                                                   border: 1px solid black;
                                                   font-size:13px;
                                                   font-family: Comic Sans MS;
                                                   font-weight: bold;
                                                   border-radius: 10px;
                                                   padding: 5px;""")
                self.difficulty = 2
            
            case 'Hard':
                self.hardButton.setStyleSheet("""background-color: darkred; 
                                                 border: 1px solid black;
                                                 font-size:13px;
                                                 font-family: Comic Sans MS;
                                                 font-weight: bold;
                                                 border-radius: 10px;
                                                 padding: 5px;""")
                self.difficulty = 3
        
    def togglePressedButton(self):

        # Reset difficulty button

        if self.pressed != None:
            match self.pressed.text():
                case 'Easy':
                    self.easyButton.setStyleSheet("""
                                                background-color: lightgreen;
                                                border-radius: 10px;
                                                padding: 5px;
                                                border: 2px solid green;
                                                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 lightgreen, stop: 1 green);
                                                font-size:13px;
                                                font-family: Comic Sans MS;
                                                font-weight:bold; """)
                case 'Medium':
                    self.mediumButton.setStyleSheet(""" background-color: lightyellow;
                                                        border-radius: 10px;
                                                        padding: 5px;
                                                        border: 2px solid orange;
                                                        background:  qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 lightyellow, stop: 1 orange);
                                                        font-size:13px;
                                                        font-family: Comic Sans MS;
                                                        font-weight: bold;""")
                
                case 'Hard':
                    self.hardButton.setStyleSheet("""background-color: lightcoral;
                                                    border-radius: 10px;
                                                    padding: 5px;
                                                    border: 2px solid red;
                                                    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 lightcoral, stop: 1 red);
                                                    font-size:13px;
                                                    font-family: Comic Sans MS;
                                                    font-weight: bold;""")