from tkinter import Tk
from tkinter import ttk
from tabs import Tabs



root = Tk()
root.wm_title('GUI')
#root.iconbitmap('.ico')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
tbs = Tabs(master=root)
tbs.grid(sticky='nsew')
root.mainloop()
try:
    root.destroy()
except:
    pass
