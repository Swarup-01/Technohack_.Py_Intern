import tkinter as tk
#import math
def on_button_click(value):
    current_text = result_var.get()
    if current_text == "0":
        result_var.set(value)
    else:

        result_var.set(current_text + value)
def clear():
    result_var.set("0")
def calculate():
    try:

        expression = result_var.get()
        result = eval(expression)
        result_var.set(str(result))
    except:
        
        result_var.set("Error")

#====================================================
root = tk.Tk()
root.title("Basic Calculator")
result_var = tk.StringVar()
result_var.set("0")

entry = tk.Entry(root, textvariable=result_var,bg = "LightPink", font=('Helvetica', 20))
entry.grid(row=0, column=0, columnspan=8)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 20),bg = "LightPink", command=calculate).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 20), command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 20), command=lambda value=button: on_button_click(value)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
