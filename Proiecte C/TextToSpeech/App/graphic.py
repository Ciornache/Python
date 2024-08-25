import tkinter as tk
from text_to_speech import play


def playTheSentence() -> None:
    play(entryText.get())


mainWindow = tk.Tk()
mainWindow.geometry('500x120')
mainWindow.title('Text-To-Speech')

entryText = tk.StringVar()

frame = tk.Frame(mainWindow, width=500, height=100, pady=10)
label = tk.Label(frame, text='Enter the phrase').pack()
textBox = tk.Entry(frame, width=50, textvariable=entryText).pack()
playBtn = tk.Button(mainWindow, text='Play', command = playTheSentence)

frame.pack()
playBtn.pack()

mainWindow.mainloop()
