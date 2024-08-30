from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject, Qt

class Menu(QObject):

    def __init__(self):
        
        # Loading the graphics

        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("F:\\Python\\Proiecte B\\Tic Tac Toe\\Ui_Design_Elements\\Menu.ui")
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

        # Initializing cursors

        self.easyButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.mediumButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.hardButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.playOButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.playXButton.setCursor(Qt.CursorShape.PointingHandCursor)
        

    def difficultyButtonPressed(self):

        self.togglePressedButton()
        sender = self.sender()

        # In case is the same button just toggle

        if sender == self.pressed:
            return None 
    
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
                                                QPushButton {background-color: lightgreen;
                                                border-radius: 10px;
                                                padding: 5px;
                                                border: 2px solid green;
                                                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 lightgreen, stop: 1 green);
                                                font-size:13px;
                                                font-family: Comic Sans MS;
                                                font-weight:bold;
                                                  }
                                                  QPushButton:hover {
                                              background-color:darkgreen;
                                            border: 1px solid black;
} """)
                case 'Medium':
                    self.mediumButton.setStyleSheet("""QPushButton {
                                                    background-color: lightyellow;
                                                        border-radius: 10px;
                                                        padding: 5px;
                                                        border: 2px solid orange;
                                                        background:  qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 lightyellow, stop: 1 orange);
                                                        font-size:13px;
                                                        font-family: Comic Sans MS;
                                                        font-weight: bold;
                                                    }
                                                        QPushButton:hover {
                                                        background-color: darkorange; 
                                                        border: 1px solid black;
                                                    } """)
                
                case 'Hard':
                    self.hardButton.setStyleSheet("""
                                                  QPushButton {
                                                  background-color: lightcoral;
                                                    border-radius: 10px;
                                                    padding: 5px;
                                                    border: 2px solid red;
                                                    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 lightcoral, stop: 1 red);
                                                    font-size:13px;
                                                    font-family: Comic Sans MS;
                                                    font-weight: bold;
                                                  }
                                                    QPushButton:hover {
                                                    background-color: darkred;
                                                    border: 1px solid black;
                                                }""")