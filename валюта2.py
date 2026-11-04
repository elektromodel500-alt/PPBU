from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests

#from bottle import response


def update_base_label(event):
    name = base_combobox.get()
    base_label.config(text=name)

def get_currencies():
    try:
        response = requests.get(
            'https://api.kraken.com/0/public/AssetPairs',
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        currencies = {}

        for pair, info in data['result'].items():
            if info.get('quote') == 'ZUSD':
                currencies[info['altname']] = info['altname']

        return currencies

    except Exception as er:
        mb.showerror('Ошибка', str(er))
        return {}



def exchange():
    base_code = base_combobox.get().strip()

    if base_code:
        try:
            response = requests.get(
                'https://api.kraken.com/0/public/Ticker',
                params={'pair': base_code},
                timeout=10
            )

            response.raise_for_status()
            data = response.json()

            if data['error'] or not data['result']:
                mb.showerror('Ошибка', 'Курс не найден')
                return

            ticker = next(iter(data['result'].values()))
            price = float(ticker['c'][0])

            base = base_code

            mb.showinfo(
                'Курс криптовалюты',
                f'{base}\n'
                f'Стоимость: {price:,.2f} USD'
            )

        except Exception as er:
            mb.showerror('Ошибка', str(er))

    else:
        mb.showwarning('Внимание', 'Выберите криптовалюту')


currencies = get_currencies()



root = Tk()
root.title('Курс обмена криптовалют Kraken')
root.geometry('360x180')

Label(root, text='Выберите криптовалюту').pack()

base_combobox = ttk.Combobox(
    root,
    values=list(currencies.keys()),
    state='readonly'
)
base_combobox.pack(pady=5)

base_combobox.bind(
    '<<ComboboxSelected>>',
    update_base_label
)

base_label = ttk.Label(root, text='')
base_label.pack(pady=5)

Button(
    root,
    text='Получить курс к USD',
    command=exchange
).pack(pady=10)





root.mainloop()
# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p.pprint(data)