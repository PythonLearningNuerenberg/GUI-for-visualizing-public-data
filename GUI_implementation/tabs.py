from tkinter import ttk
from tab1 import Tab1
from tab2 import Tab2
from tab3 import Tab3
from win32api import GetSystemMetrics


class Tabs(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self,master)
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)
        self.create_widgets()
    def create_widgets(self):
        self.tabs = ttk.Notebook(self,width=int(self.width/3), height=int(self.height/2))
        self.tabs.pack(side="top", expand=True, fill="both")

        self.tab1 = Tab1(self.tabs)
        self.tabs.add(self.tab1, text="Fetch/Plot")

        #self.tab2 = Tab2(self.tabs)
        #self.tabs.add(self.tab2, text="Tab 2")

        #self.tab3 = Tab3(self.tabs)
        #self.tabs.add(self.tab3, text="Tab 3")

