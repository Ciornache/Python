from PySide6.QtWidgets import QPushButton 
import random 

class AIPlayer:

    __slots__ = ('buttons', 'grid')

    def __init__(self, buttons:list[QPushButton]) -> None:
        self.buttons = buttons

    def makeMove(self, difficulty, turn):
        match difficulty:
            case 1:
                self.easyDifficulty(turn)
            case 2:
                self.mediumDifficulty(turn)
            case 3:
                self.hardDifficulty(turn)

    def easyDifficulty(self, turn):

        # The AI picks a random available move

        emptyButtons = [button for button in self.buttons if not button.isCheckable()]
        if emptyButtons != []:
            move = random.choice(emptyButtons)
            if turn == 1:
                move.setText('X')
            else:
                move.setText('O')
            move.setCheckable(True)

    def hardDifficulty(self, turn):

        # AI will make the best move for the current configuration
        # We implement the MinMax algorithm to find such move

        move = self.getMinMaxMove(turn)
        if move != None:            
            if turn == 1:
                move.setText('X')
            else:
                move.setText('O')
            move.setCheckable(True)
    
    def mediumDifficulty(self, turn):

        # Medium difficulty: The AI will alternate between easy and hard mode
        # We pick randomly one of the two methods

        nr = random.choice([1, 2, 3, 4])
        if nr % 2:
            self.hardDifficulty(turn)
        else:
            self.easyDifficulty(turn)
         
    def getMinMaxMove(self, turn):

        # Picks the best move for the current configuration of the table
        # If there is more than one good move we will pick it up randomly so that the AI doesn't always have same pattern in playing

        self.makeGrid()
        bestCoefficient = -2; moves = None

        for i in range(0,3):
            for j in range(0,3):
                if self.grid[i][j] == 0:
                    self.grid[i][j] = turn
                    coefficient = self.branchAndBound(3 - turn, turn)
                    if coefficient > bestCoefficient:
                        bestCoefficient = coefficient
                        moves = [self.buttons[i * 3 + j]]
                    elif coefficient == bestCoefficient:
                        moves.append(self.buttons[i * 3 + j])
                    self.grid[i][j] = 0
        
        return random.choice(moves) if moves != None else None
    

    def branchAndBound(self, turn, aiTurn):

        # Check if AI Wins

        ok, ok2 = 0, 0
        for i in range(0, 3):
            if (self.grid[i][0], self.grid[i][1], self.grid[i][2]) == (aiTurn, aiTurn, aiTurn):
                return 1
            if (self.grid[0][i], self.grid[1][i], self.grid[2][i]) == (aiTurn, aiTurn, aiTurn):
                return 1
            ok += (self.grid[i][i] == aiTurn); ok2 += (self.grid[i][2-i] == aiTurn)

        if ok == 3 or ok2 == 3:
            return 1
        
        # Check if Player wins

        ok, ok2 = (0, 0)
        for i in range(0, 3):
            if (self.grid[i][0], self.grid[i][1], self.grid[i][2]) == (3 - aiTurn, 3 - aiTurn,  3 - aiTurn):
                return -1
            if (self.grid[0][i], self.grid[1][i], self.grid[2][i]) == (3 - aiTurn, 3 - aiTurn, 3 - aiTurn):
                return -1
            ok += (self.grid[i][i] == 3 - aiTurn); ok2 += (self.grid[i][2-i] == 3 - aiTurn)
        
        if ok == 3 or ok2 == 3:
            return -1

        # Check if Draw is the only possible outcome
        # If all the possible winning situations have at least one 1 and one 2, than it means there are no win conditions so a Draw is on the table

        ok = True; nr3, nr4 = (0, 0)
        for i in range(0, 3):
            nr, nr2 = (0, 0)
            for j in range(0, 3):
                nr |= self.grid[i][j]; nr2 |= self.grid[j][i]
            ok = False if nr != 3 or nr2 != 3 else ok
            nr3 |= self.grid[i][i]; nr4 |= self.grid[i][2 - i]

        if nr3 != 3 or nr4 != 3:
            ok = False

        if ok == True:
            return 0    

        # Get the coefficients from all the branches

        coefficients = []        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[i][j] == 0:
                    self.grid[i][j] = turn
                    coefficients.append(self.branchAndBound(3 - turn, aiTurn))
                    self.grid[i][j] = 0

        """
        The AI wants the move that has the biggest score, so the pick will be the biggest coefficient (max(coefficients))
        The Player would make the move that has the lowest score, so the pick will be lowest coefficient (min(coefficients))
        
        """

        # If no coefficient was found then it means no possible move exists on the current grid, so we get a Draw

        coefficients = coefficients + [0] if coefficients == [] else coefficients
        if turn == aiTurn:
            return max(coefficients)
        else:
            return min(coefficients)
        

    def makeGrid(self):
        """
        Grid Map

        Ex: 101
            202
            000
        
        0 - empty
        1 - X
        2 - O

        """
        self.grid = []
        for i in range(0, 3):
            self.grid.append([])
            for j in range(0, 3):
                text = self.buttons[i * 3 + j].text()
                element = 0 if text == '' else 1 if text == 'X' else 2
                self.grid[-1].append(element)