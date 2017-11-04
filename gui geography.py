from Tkinter import *
import Tkinter
import random
import tkMessageBox

european_capitals = {
            'Albania': 'Tirana',
            'Andorra': 'Andorra la Vella',
            'Armenia': 'Yerevan',
            'Austria': 'Vienna',
            'Azerbaijan': 'Baku',
            'Belarus': 'Minsk',
            'Belgium': 'Brussels',
            'Bosnia and Herzegovina': 'Sarajevo',
            'Bulgaria': 'Sofia',
            'Croatia': 'Zagreb',
            'Cyprus': 'Nicosia',
            'Czech Republic': 'Prague',
            'Denmark': 'Copenhagen',
            'Estonia': 'Tallinn',
            'Finland': 'Helsinki',
            'France': 'Paris',
            'Georgia': 'Tbilisi',
            'Germany': 'Berlin',
            'Greece': 'Athens',
            'Hungary': 'Budapest',
            'Iceland': 'Reykjavik',
            'Ireland': 'Dublin',
            'Italy': 'Rome',
            'Kazakhstan': 'Astana',
            'Kosovo': 'Pristina',
            'Latvia': 'Riga',
            'Liechtenstein': 'Vaduz',
            'Lithuania': 'Vilnius',
            'Luxembourg': 'Luxembourg',
            'Macedonia (FYROM)': 'Skopje',
            'Malta': 'Valletta',
            'Moldova': 'Chisinau',
            'Monaco': 'Monaco',
            'Montenegro': 'Podgorica',
            'Netherlands': 'Amsterdam',
            'Norway': 'Oslo',
            'Poland': 'Warsaw',
            'Portugal': 'Lisbon',
            'Romania': 'Bucharest',
            'Russia': 'Moscow',
            'San Marino': 'San Marino',
            'Serbia': 'Belgrade',
            'Slovakia': 'Bratislava',
            'Slovenia': 'Ljubljana',
            'Spain': 'Madrid',
            'Sweden': 'Stockholm',
            'Switzerland': 'Bern',
            'Turkey': 'Ankara',
            'Ukraine': 'Kiev',
            'United Kingdom': 'London',
            'Vatican City': 'Vatican City'
            }
european_capital = None

def generate():
    european_capital = random.choice(list(european_capitals.items()))
    # print european_capital
    return european_capital

def capital():
    guess = inputWindow.get()
    if guess == european_capital[1]:
        output = "\n\nWOOHOOO, that's right!"
    else:
        output = "\n\nWRONG! Guess again... "
    result.config(text=output)

def reset():
    global european_capital
    european_capital = generate()
    inputWindow.delete(0, Tkinter.END)
    inputWindow.config(text="")
    result.config(text="")
    instruction_label.config(text="What is the capital of " + european_capital[0] + "?")

#izgled okna
window = Tkinter.Tk()
window.geometry("300x400")
window.title("Guess the capital")
greeting = Tkinter.Label(window, text = "Let's rediscover capitals of good old Europe.\n\n\n")
greeting.pack()

instruction_label = Tkinter.Label(window, text = "")
instruction_label.pack()

inputWindow = Tkinter.Entry()   #vnosno okno
inputWindow.pack()

submit_button_pushed = Tkinter.Button(window, text="Submit", command = capital)
submit_button_pushed.pack()
reset_button_pushed = Tkinter.Button(window, text="Reset", command = reset)
reset_button_pushed.pack()
result = Tkinter.Label(window, text="")
result.pack()
reset()

window.mainloop()