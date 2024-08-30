from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject, QTimer, Qt
from PySide6.QtWidgets import QPushButton
from ai import AIPlayer

class Game(QObject):

    def __init__(self, mode, difficulty = 0) -> None:

        # Loading the graphics

        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("F:\\Python\\Proiecte B\\Tic Tac Toe\\Ui_Design_Elements\\Game.ui")
        self.ui.setWindowTitle('Tic Tac Toe')
        self.mode = mode
        self.saveMode = self.mode
        self.difficulty = difficulty
        self.turn = 1

        # Extracting the Graphic Elements for future manipulation

        self.button11 = self.ui.pushButton_11
        self.button12 = self.ui.pushButton_12
        self.button13 = self.ui.pushButton_13
        self.button21 = self.ui.pushButton_21
        self.button22 = self.ui.pushButton_22
        self.button23 = self.ui.pushButton_23
        self.button31 = self.ui.pushButton_31
        self.button32 = self.ui.pushButton_32
        self.button33 = self.ui.pushButton_33
        self.goBackButton = self.ui.goBackButton
        self.playAgainButton = self.ui.playAgainButton        
        self.label = self.ui.turnLabel
        self.buttons = [self.button11, self.button12, self.button13, self.button21, self.button22, self.button23, self.button31, self.button32, self.button33]

        # Initializing the AI Player

        self.aiPlayer = AIPlayer(self.buttons)

        # Initializing the Game State

        for button in self.buttons:
            button.pressed.connect(self.buttonPressed)
            button.setCheckable(False)
        
        self.playAgainButton.pressed.connect(self.reset)
        self.playAgainButton.hide()
        self.goBackButton.hide()

        # Initializing a Timer for AI Moves

        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.checkForAiTurn)
        self.timer.start()

        # Initializing cursors

        self.goBackButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.playAgainButton.setCursor(Qt.CursorShape.PointingHandCursor)


    def buttonPressed(self):

        # Checking if it is AI Turn

        if self.mode == 2 and self.difficulty:
            return None

        sender:QPushButton = self.sender()

        # If button was not pressed before

        if sender.isCheckable() == False:
            
            # Updating with X or O
            if self.turn == 1:
                sender.setText('X')
            else:
                sender.setText('O')
            
            # Setting the button as pressed
            sender.setCheckable(True)

        # Updating game state

        over:bool = self.updateGameState()
        if over:
            self.endGame()
            
    
    def updateGameState(self):

        """ Return:
            True -> Game finished
            False -> Game is still running """

        # Checking if the game is over

        winConditions = [(self.button11, self.button22, self.button33), 
                         (self.button11, self.button12, self.button13),
                         (self.button21, self.button22, self.button23),
                         (self.button31, self.button32, self.button33),
                         (self.button13, self.button22, self.button31),
                         (self.button11, self.button21, self.button31), 
                         (self.button12, self.button22, self.button32),
                         (self.button13, self.button23, self.button33)]

        for condition in winConditions:
            
            # X Wins

            if (condition[0].text(), condition[1].text(), condition[2].text()) == ('X', 'X', 'X'):
                self.label.setText('X WINS')
                return True 
             
            # O Wins

            if (condition[0].text(), condition[1].text(), condition[2].text()) == ('O', 'O', 'O'):
                self.label.setText('O WINS')
                return True  
            
        freeSpots = len([btn for btn in self.buttons if not btn.isCheckable()])
        
        if freeSpots == 0:
            self.label.setText('DRAW')
            return True

        # Updating the player order

        self.turn = 3 - self.turn
        if self.turn == 1:
            self.label.setText('X TURN')
        else:
            self.label.setText('O TURN')
        
        self.mode = 3 - self.mode
        return False 

    
    def reset(self):

        # Hiding end game menu
        self.playAgainButton.hide()
        self.goBackButton.hide()

        # Resetting the game
        for button in self.buttons:
            button.setCheckable(False)
            button.setText('')

        self.turn = 1
        self.mode = self.saveMode
        self.label.setText('X TURN')
        self.timer.start()
    

    def checkForAiTurn(self):
        
        # Handle AI Move
        if self.mode == 2 and self.difficulty:
            self.aiPlayer.makeMove(self.difficulty, self.turn)
            over = self.updateGameState()
            if over:
                self.endGame()
    
    def endGame(self):

        # Display the End Game State
        for button in self.buttons:
                button.setCheckable(True)
        self.playAgainButton.show()
        self.goBackButton.show()
        self.timer.stop()