import csv
import random
import time
import tkinter as tk
import textwrap

quotesArray = []

with open('quotes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
           quotesArray.append(row)

class QuotesApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.quotePrint = tk.Button(self)
        self.quotePrint['text'] = 'Print a Quote'
        self.quotePrint['command'] = self.quoteSelection
        self.quotePrint.pack(padx=100, pady=60)

        self.quoteLabel = tk.Label(self, wraplength=550)
        self.quoteLabel['text'] = 'Quote will display here'
        self.quoteLabel.pack(side='bottom')

        self.authorLabel = tk.Label(self, wraplength=500)
        self.authorLabel['text'] = 'Author'
        self.authorLabel.pack(padx=100)

    
    def quoteSelection(self):
        quoteNumber = random.randint(0, len(quotesArray)-1)
        selectedQuote = quotesArray[quoteNumber]
        self.quoteLabel['text'] = selectedQuote[0]
        self.authorLabel['text'] = selectedQuote[1]


root = tk.Tk()
app = QuotesApp(master=root)

app.master.minsize(800,500)
app.master.maxsize(800,500)
app.mainloop()