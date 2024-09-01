from PySide6.QtCore import QObject
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QPushButton, QComboBox, QLineEdit, QApplication, QMainWindow, QLabel
import json 

class App(QObject):

    def __init__(self) -> None:
        super().__init__()
        self.currencyValue = {}
        loader = QUiLoader()
        self.ui:QMainWindow = loader.load('F:\\Python\\Proiecte B\\Currency Converter\\Ui Design Elements\\main.ui')

        # Extract UI Elements for future manipulation 
        self.convertButton:QPushButton = self.ui.convertButton
        self.convertFromComboBox:QComboBox = self.ui.convertFromComboBox
        self.toComboBox:QComboBox = self.ui.toComboBox
        self.valueLineEdit:QLineEdit = self.ui.ammountLineEdit
        self.infoLabel:QLabel = self.ui.infoLabel
        self.currentStyleSheet = self.infoLabel.styleSheet()

        # Add functionalities to the Graphical Elements

        self.populateComboBoxes()
        self.ui.show()
        self.convertButton.pressed.connect(self.processPressedSignal)
    
    def populateComboBoxes(self) -> None:

        # Extract the currency symbols and place them in the Combo Boxes

        with open('currency_data.json', 'r') as js:
            data:dict = json.load(js)
            for value in data.values():
                symbol = value['symbol']
                self.convertFromComboBox.addItem(symbol)
                self.toComboBox.addItem(symbol)
                self.currencyValue.setdefault(symbol, value['value'])

        self.toComboBox.setCurrentIndex(1)
        self.convertFromComboBox.setCurrentIndex(0)

    def processPressedSignal(self) -> None:

        # Check if the input box contains a valid input 
        value = self.valueLineEdit.text()
        ok = len([ch for ch in value if not str.isdecimal(ch)]) > 0

        # Initialize stylesheet for invalid input
        redStyleSheet = f'{self.currentStyleSheet} color:red;'
        
        if ok == 1 or value == '':
            # Input is either empty or contains invalid characters
            self.infoLabel.setStyleSheet(redStyleSheet)
            if ok == 1:
                message ='Invalid value!\n The field contains bad characters\n'
            else:
                message = 'Invalid value!\n The field is empty.\nPlease provide a value'
            self.infoLabel.setText(message)

        else:
            symbol1, symbol2 = self.convertFromComboBox.currentText(), self.toComboBox.currentText()
            value = int(self.valueLineEdit.text())
            if symbol1 == symbol2:
                # Conversion has to be done between different currencies
                self.infoLabel.setStyleSheet(redStyleSheet)
                self.infoLabel.setText('Please choose different\n currencies for conversion')
            else:
                # Conversion is successful
                self.infoLabel.setStyleSheet(self.currentStyleSheet)
                currencyValue1, currencyValue2 = float(self.currencyValue[symbol1]), float(self.currencyValue[symbol2]) 
                conversionResult = round((currencyValue1 / currencyValue2) * value, 2) 
                self.infoLabel.setText(f'Conversion was successful!\n {value} {symbol1} is {conversionResult} {symbol2}') 
    

if __name__ == '__main__':     
    qApp = QApplication()
    app = App()
    qApp.exec()