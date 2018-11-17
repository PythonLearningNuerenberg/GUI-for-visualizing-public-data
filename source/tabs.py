from tkinter import ttk
import platform
from tab1 import Tab1
from tab2 import Tab2
from tab3 import Tab3


def get_res():
    if platform.system() == 'Darwin':
        results = str(subprocess.Popen(['system_profiler SPDisplaysDataType | grep Resolution'],
                                       stdout=subprocess.PIPE, shell=True).communicate()[0])
    elif platform.system() == 'Linux':
        results = str(subprocess.Popen(['xdpyinfo | grep dimensions'],
                                       stdout=subprocess.PIPE, shell=True).communicate()[0])
    filtered_results = ''
    for char in results:
        if char in '0987654321x':
            filtered_results = filtered_results + char
    width, height = filtered_results.split('x')[0:2]
    return int(width), int(height )

try:
    from win32api import GetSystemMetrics
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
except ModuleNotFoundError:
    import subprocess
    width, height = get_res()


class Tabs(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self,master)
        self.width = width
        self.height = height
        self.create_widgets()
    def create_widgets(self):
        self.tabs = ttk.Notebook(self,width=int(self.width) -850, height=int(self.height/2))
        self.tabs.pack(side="top", expand=True, fill="both")

        self.tab1 = Tab1(self.tabs)
        self.tabs.add(self.tab1, text="Fetch/Plot")

        # self.tab2 = Tab2(self.tabs)
        # self.tabs.add(self.tab2, text="Tab 2")
        #
        # self.tab3 = Tab3(self.tabs)
        # self.tabs.add(self.tab3, text="Tab 3")



