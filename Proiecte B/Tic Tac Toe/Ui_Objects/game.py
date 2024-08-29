from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication, QPushButton
import sys 

class Game(QObject):

    def __init__(self, turn) -> None:

        # Loading the graphics

        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("F:\\Python\\Proiecte B\\Tic Tac Toe\\Ui-Elements\\Game.ui")
        self.ui.setWindowTitle('Tic Tac Toe')
        self.turn = turn
        text = 'O TURN' if self.turn == 2 else 'X TURN'
        self.ui.turnLabel.setText(text)

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

        # Initializing the Game State

        self.buttons = [self.button11, self.button12, self.button13, self.button21, self.button22, self.button23, self.button31, self.button32, self.button33]
        for button in self.buttons:
            button.pressed.connect(self.buttonPressed)
            button.setCheckable(False)
        
        self.playAgainButton.pressed.connect(self.reset)
        self.playAgainButton.hide()
        self.goBackButton.hide()

    def buttonPressed(self):

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
            for button in self.buttons:
                button.setCheckable(True)
            self.playAgainButton.show()
            self.goBackButton.show()
    
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
                        
        # Updating the player order

        if self.turn == 1:
            self.label.setText('X TURN')
        else:
            self.label.setText('O TURN')
        
        self.turn = 3 - self.turn

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
        self.label.setText('X TURN')