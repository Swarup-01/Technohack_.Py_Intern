import tkinter as tk
from tkinter import PhotoImage
from forex_python.converter import CurrencyRates

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()

    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    output_listbox.insert(tk.END, f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")


root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x400")


bg_image = PhotoImage(file="BG1.png")


bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

label_amount = tk.Label(root, text="Amount:")

label_from_currency = tk.Label(root, text="From Currency:")
label_to_currency = tk.Label(root, text="To Currenc:")
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))

label_amount.grid(row=0, column=0, padx=10, pady=10, sticky="w")
label_from_currency.grid(row=1, column=0, padx=10, pady=10, sticky="w")
label_to_currency.grid(row=2, column=0, padx=10, pady=10, sticky="w")
result_label.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky="w")

# Create entry for amount
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

# Create dropdown menus for currency selection
currencies = ["USD", "EUR", "GBP", "JPY", "INR"]  # Added INR
combo_from_currency = tk.StringVar()
combo_to_currency = tk.StringVar()

combo_from_currency.set(currencies[0])
combo_to_currency.set(currencies[1])

option_menu_from_currency = tk.OptionMenu(root, combo_from_currency, *currencies)
option_menu_to_currency = tk.OptionMenu(root, combo_to_currency, *currencies)

option_menu_from_currency.grid(row=1, column=1, padx=10, pady=10)
option_menu_to_currency.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert",bg ="lightgreen", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

output_listbox = tk.Listbox(root, height=6, width=40)
output_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()
