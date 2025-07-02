import tkinter as tk
from forex_python.converter import CurrencyRates

common_currencies=['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD','INR']

class CurrencyConverter:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Currency Converter")
        self.root.geometry('400x300')

        self.from_var = tk.StringVar()
        self.from_var.set('USD')
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *common_currencies)
        self.from_menu.pack(pady=1)

        self.to_var = tk.StringVar()
        self.to_var.set('INR')
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *common_currencies)
        self.to_menu.pack(pady=1)


        self.amount_label = tk.Label(self.root, text="Amount:")
        self.amount_label.pack(pady=1)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=1)

        self.converter_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.converter_button.pack(pady=1)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=1)

        self.root.mainloop()


    def convert_currency(self):
        try:
            from_currency = self.from_var.get()
            to_currency = self.to_var.get()
            amount=float(self.amount_entry.get())

            c_rates= CurrencyRates()

            rate = c_rates.get_rate(from_currency, to_currency)
            converted_amount = amount * rate

            self.result_label.config(text=f'{amount}{from_currency} = {converted_amount:.2f} {to_currency}')
        except ValueError:
            self.result_label.config(text="plese enter a valid amount")
        except Exception: 
            self.result_label.config(text="Error Occured")


if __name__ == "__main__":
    CurrencyConverter()
