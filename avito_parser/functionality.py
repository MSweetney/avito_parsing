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

        self.search_term = StringVar()
        (
            ttk.Label(mainframe, text='Enter your search: ')
            .grid(column=1, row=1, sticky=E)
        )
        search_term_entry = (
            ttk.Entry(mainframe, width=20, textvariable=self.search_term)
        )
        search_term_entry.grid(column=2, row=1, sticky=(W, E))

        self.items = StringVar()
        self.items.set('50')
        (
            ttk.Label(mainframe,
                      text='Enter amount of items: ')
            .grid(column=1, row=2, sticky=E)
        )
        items_entry = ttk.Entry(mainframe, width=10, textvariable=self.items)
        items_entry.grid(column=2, row=2, sticky=W)

        (
            ttk.Button(mainframe,
                       text='Search',
                       command=self.calculate)
            .grid(column=2, row=3, sticky=W)
        )

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            search_term_entry.focus()
            root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        search = self.search_term.get()
        items = self.items.get()
        value = main_parsing(search_term=search, items=items)
        InfoWindow(root, value)

    # TODO: Open a new statistic window.
    # Should show data and allow to make a new search.


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
