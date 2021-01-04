import tkinter as tk
from tkinter import font
import os

root = tk.Tk()

displayLabelFont = font.Font(family='Helvetica', name='quotesFont', size=14)

txtFile = open('file.txt')


canvas = tk.Canvas(root, height=500, width=800)
canvas.grid(columnspan=3, rowspan=4)


updatingQuestionText = tk.StringVar()
updatingAnswerText = tk.StringVar()
questionDisplayLabel = tk.Label(root, textvariable=updatingQuestionText, font=displayLabelFont)
answerDisplayLabel = tk.Label(root, textvariable=updatingAnswerText, font=displayLabelFont)
questionDisplayLabel.grid(column=1, row=1)
answerDisplayLabel.grid(column=2, row=1)

line = txtFile.readline()
wordsInLine = line.split('-')


def displayQuestionWord():
    updatingQuestionText.set(wordsInLine[0])
    return

def revealAnswer():
    updatingAnswerText.set(wordsInLine[1])
    return



btnDisplayWords = tk.Button(root, text='Display a Word', padx=10, pady=10, fg="white", bg="#263042", command=displayQuestionWord)
btnRevealAnswer = tk.Button(root, text='Display the Answer', padx=10, pady=10, fg="white", bg="#263042", command=revealAnswer)

btnDisplayWords.grid(column=1, row=2)
btnRevealAnswer.grid(column=2, row=2)

root.mainloop()