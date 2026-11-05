from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests



def update_currency_label(event):
    code = target_combobox.get()
    # code = combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)

def update_second_base_label(event):
    code = second_base_combobox.get()
    name = currencies[code]
    second_base_label.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    second_base_code = second_base_combobox.get().strip()
    # code = entry.get().upper().strip()
    # code = combobox.get()
    if target_code and base_code and second_base_code:
        try:
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response1.raise_for_status()
            data1 = response1.json()

            response2 = requests.get(f'https://open.er-api.com/v6/latest/{second_base_code}')
            response2.raise_for_status()
            data2 = response2.json()
            if target_code in data1['rates'] and target_code in data2['rates']:
                exchange_rate1 = data1['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]
                base = currencies[base_code]
                second_base = currencies[second_base_code]
                target = currencies[target_code]
                # currency_name = currencies[code]
                mb.showinfo(
                    'Курс обмена',
                    f'1 {base} = {exchange_rate1:.2f} {target}\n'
                    f'1 {second_base} = {exchange_rate2:.2f} {target}'
                )
            else:
                mb.showerror('Ошибка',
                            f'Валюта {target_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', str(er))

    else:
        mb.showwarning('Внимание', 'Введите все три валюты')


currencies = {
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'

}

root = Tk()
root.title('Курс обмена валют')
root.geometry('360x360')

Label(root, text='Базовая валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()

Label(root, text='Вторая базовая валюта').pack()
second_base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
second_base_combobox.pack(pady=3, padx=10)
second_base_combobox.bind('<<ComboboxSelected>>', update_second_base_label)
second_base_label = ttk.Label()
second_base_label.pack()

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

Button(text='Получить курс обмена',
       command=exchange).pack(pady=10, padx=10)


root.mainloop()
# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p.pprint(data)