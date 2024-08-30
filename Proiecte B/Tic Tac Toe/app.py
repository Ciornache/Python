from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
import sys 
from Ui_Objects.game import Game 
from Ui_Objects.menu import Menu

class App:

    def __init__(self) -> None:
        self.menu = Menu()
        self.menu.ui.show()
        self.menu.playXButton.pressed.connect(self.createXGame)
        self.menu.playOButton.pressed.connect(self.createOGame)
    
    def showMenu(self) -> None:
        self.menu.ui.show()
        self.game.reset()
        self.game.ui.hide()
    
    def createXGame(self) -> None:
        try:
            self.game = Game(1, self.menu.difficulty)
        except:
            self.game = Game(1)
        finally:
            self.game.ui.show()
            self.menu.togglePressedButton()
            self.menu.ui.hide()
            self.game.ui.goBackButton.pressed.connect(self.showMenu)
        
    
    def createOGame(self) -> None:
        try:
            self.game = Game(2, self.menu.difficulty)
        except:
            self.game = Game(2)
        finally:
            self.game.ui.show()
            self.menu.togglePressedButton()
            self.menu.ui.hide()
            self.game.ui.goBackButton.pressed.connect(self.showMenu)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    qApp = QApplication(sys.argv)
    app = App()
    qApp.exec()