import csv
import random

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

def quoteSelection():
    quoteNumber = random.randint(0, len(quotesArray))

    selectedQuote = quotesArray[quoteNumber]

    print(selectedQuote)

userInput = input('Would you like a Random Quote? Y/N \n')

if userInput == 'Y' or userInput == 'y':
    userWantQuotes = True
    quoteSelection()

else:
    print('Goodbye')
    userWantQuotes = False

while userWantQuotes:   
    userInput = input('Would you like another Quote? Y/N \n')

    if userInput == 'Y' or userInput == 'y':
        userWantQuotes = True
        quoteSelection()

    else:
        print('Goodbye')
        userWantQuotes = False