from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json
import pprint

#from bottle import response


def update_currency_label(event):
    code = target_combobox.get()
    # code = combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    # code = entry.get().upper().strip()
    # code = combobox.get()
    if target_code and base_code:
        try:

            response = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={base_code}')
            response.raise_for_status()
            data = response.json()
            if data['error']:
                mb.showerror('Ошибка', data['error'])
                return
            ticker = next(iter(data['result'].values()))
            exchange_rate = float(ticker['c'][0])
            base = currencies[base_code]
                #target = currencies[target_code]
                # currency_name = currencies[code]
            mb.showinfo('Курс обмена криптовалют',
                            f'Курс: {exchange_rate:.2f} USD за 1 {base}')

        except Exception as er:
            mb.showerror('Ошибка', str(er))

    else:
        mb.showwarning('Внимание', 'Введите код валюты')



currencies = {
    'XBTUSD': 'Bitcoin',
    'ETHUSD': 'Ethereum',
    'SOLUSD': 'Solana',
    'XRPUSD': 'XRP',
    'XDGUSD': 'Dogecoin',
    'ADAUSD': 'Cardano',
    'LTCUSD': 'Litecoin'
}



root = Tk()
root.title('Курс обмена валют USD')
root.geometry('360x180')

Label(root, text='Базовая валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()

Label(root, text='Целевая валюта' ).pack(padx=10)
# popular_currencies = ['EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF',
#                       'CNY', 'RUB', 'KZT', 'UZS']
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack()
# entry = Entry(root)
# entry.pack()

Button(text='Получить курс обмена к доллару',
       command=exchange).pack(pady=10, padx=10)


root.mainloop()
# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p.pprint(data)