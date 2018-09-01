from tkinter import ttk, N, S, E, W


class Tab1(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.create_widgets()

    def create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.frame_1 = ttk.Frame(self)
        self.frame_1.grid(row=0, column=0, columnspan=3, sticky=W + E, padx=10, pady=(2, 5))
        style_label_1 = ttk.Style()
        style_label_1.configure("label_1.TLabel", background="green",font=('Frutiger LT Com 4', 80))
        self.label_1 = ttk.Label(self.frame_1, text='Label 1',style='label_1.TLabel')
        self.label_1.grid(row=0, column=1, sticky=W + E, padx=10, pady=(2, 5))
