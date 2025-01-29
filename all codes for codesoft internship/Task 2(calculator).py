import tkinter as tk

#defining a functions
def add():
    result.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result.set(float(entry1.get()) * float(entry2.get()))

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        result.set("Error! Division by zero.")

window = tk.Tk()
window.title("Calculator")

#input entries
entry1 = tk.Entry(window, width=25)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(window, width=25)
entry2.grid(row=0, column=1, padx=10, pady=10)

#string
result = tk.StringVar()


result_label = tk.Label(window, textvariable=result, width=20)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

#Assigning Buttons 
button_add = tk.Button(window, text="Add", width=15, command=add)
button_add.grid(row=1, column=0, padx=5, pady=5)

button_subtract = tk.Button(window, text="Subtract", width=15, command=subtract)
button_subtract.grid(row=1, column=1, padx=5, pady=5)

button_multiply = tk.Button(window, text="Multiply", width=15, command=multiply)
button_multiply.grid(row=2, column=0, padx=5, pady=5)

button_divide = tk.Button(window, text="Divide", width=15, command=divide)
button_divide.grid(row=2, column=1, padx=5, pady=5)


window.mainloop()
