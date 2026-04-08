from tkinter import *

# entry of values and operators to proceed with the calculations
def click_entry (values):
    entry.insert(END, values)
def click_clear():
    entry.delete(0, END) 
def click_equals ():
    try:
        expression = entry.get()
        expression = expression.replace("^","**") #for exponentials
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete (0, END)
        entry.insert (END, "Error")
def backspace():
    entry.delete (len(entry.get())-1,END)

# to begin and initaite the windows and space 

calculator = Tk()
entry = Entry (calculator)
calculator.title("My Simple calculator")
calculator.geometry("318x400")
calculator.config(background="#5c8bad")

#entry path to input calculations 
entry = Entry(calculator, textvariable = entry, font = ("Arial", 20), justify= "left")
entry.grid(row= 0, column = 0, columnspan = 5, padx = 10, pady = 10)

#now for the buttons lineup
buttons = [ 
    ['(', ')', '', 'C'],    
    ['1', '2', '3', '/'],
    ['6', '5', '4', '*'],
    ['7', '8', '9', '-'],
    ['.', '0', '+', '='],
    ['^','%', '', 'E']
]

for r, row in enumerate (buttons, 1):
    for c, char in enumerate (row):
        if char == "C":
            Button(calculator, text=char, width = 9, height=3, command= click_clear, bg = 'tomato', fg = 'white').grid(row = r, column = c)
        elif char == "=":
            Button(calculator, text=char, width = 9, height= 3, command = click_equals, bg = "blue", fg = 'white').grid (row = r, column = c)
        else:
            Button(calculator, text = char, width = 9, height = 3, command = lambda ch=char: click_entry(ch)).grid (row = r, column = c)

# a different bonus button 
backspace = Button (calculator, text=char, width = 9, height= 3, command = backspace, bg = 'orange' , fg ='black')
backspace.grid(row = r , column = c)


calculator.mainloop() #window screen appear, apparently 

