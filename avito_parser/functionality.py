from tkinter import *
from tkinter import ttk
from avito_parser.main_parsing import main_parsing


class PriceParser:
    def __init__(self, root):
        root.title('Parser')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding='60 40')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Search term
        self.search_term = StringVar()
        (
            ttk.Label(mainframe, text='Enter your search: ')
            .grid(column=1, row=1, sticky=E)
        )
        search_term_entry = (
            ttk.Entry(mainframe, width=20, textvariable=self.search_term)
        )
        search_term_entry.grid(column=2, row=1, columnspan=3, sticky=(W, E))

        # Amount of searched items
        self.items = IntVar()
        self.items.set(50)
        (
            ttk.Label(mainframe,
                      text='Enter amount of items: ')
            .grid(column=1, row=2, sticky=E)
        )
        items_entry = ttk.Entry(mainframe, width=6, textvariable=self.items)
        items_entry.grid(column=2, row=2, columnspan=3, sticky=W)

        # Minimum price of search
        self.price_min = IntVar()
        (
            ttk.Label(mainframe, text='Minimum price: ')
            .grid(column=1, row=3, sticky=E)
        )
        price_min_entry = (
            ttk.Entry(mainframe, width=15, textvariable=self.price_min)
        )
        price_min_entry.grid(column=2, row=3, sticky=W)

        # Maximum price of search
        self.price_max = IntVar()
        (
            ttk.Label(mainframe, text='Maximum price: ')
            .grid(column=3, row=3, sticky=E)
        )
        price_max_entry = (
            ttk.Entry(mainframe, width=15, textvariable=self.price_max)
        )
        price_max_entry.grid(column=4, row=3, sticky=W)

        # Start search button
        (
            ttk.Button(mainframe,
                       text='Search',
                       command=self.calculate)
            .grid(column=2, row=4, sticky=W)
        )

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            search_term_entry.focus()
            root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        search = self.search_term.get()
        items = self.items.get()
        prices = self.price_min.get(), self.price_max.get()
        # am i stupid?
        value = main_parsing(search_term=search, items=items, prices=prices)
        InfoWindow(root, value)


class InfoWindow:
    def __init__(self, root, value):
        root.title('Info')
        self.value = value

        mainframe = ttk.Frame(root, padding='60 40')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        (
            ttk.Label(mainframe,
                      text=f'Here is data for you {self.value}')
            .grid(column=1, row=1, sticky=E)
        )
        (
            ttk.Label(mainframe,
                      text='There will be average price')
            .grid(column=1, row=2, sticky=E)
        )
        (
            ttk.Button(mainframe,
                       text='Search Again',
                       command=self.back_button)
            .grid(column=2, row=2, sticky=W)
        )

    def back_button(self):
        PriceParser(root)


if __name__ == '__main__':
    root = Tk()
    PriceParser(root)
    root.mainloop()
