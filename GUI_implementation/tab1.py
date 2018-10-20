from tkinter import ttk, N, S, E, W, END, DISABLED, NORMAL, IntVar
import tkinter
import time

class Tab1(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.create_widgets()

    def create_widgets(self):
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=0)

        self.labelFrame_fetchData = ttk.LabelFrame(self, text=' Fetch data ')
        self.labelFrame_fetchData.grid(row=0, column=0, sticky=W + E, padx=10, pady=(2, 5))
        self.button_fetchData = ttk.Button(self.labelFrame_fetchData, text='Fetch available data', command=self.fetch_data)
        self.button_fetchData.grid(row=0, column=0, sticky=W + E, padx=10, pady=(2, 5))
        self.labelFrame_outputMessages = ttk.LabelFrame(self, text=' Output Messages ')
        self.labelFrame_outputMessages.grid(row=0, column=1, columnspan=3, sticky=W + E, padx=10, pady=(2, 5))
        self.labelFrame_outputMessages.rowconfigure(0, weight=0)
        self.labelFrame_outputMessages.columnconfigure(0, weight=1)
        self.labelFrame_outputMessages.columnconfigure(1, weight=0)
        self.text_outputMessages = tkinter.Text(self.labelFrame_outputMessages, height=8)#, width=50)
        self.text_outputMessages.grid(row=0, column=0, columnspan=2,sticky=W + E, padx=10, pady=(2, 5))
        self.scrollbar_outputMessages = ttk.Scrollbar(self.labelFrame_outputMessages)
        self.scrollbar_outputMessages.grid(row=0, column=1, sticky=E + N + S)
        self.scrollbar_outputMessages.config(command=self.text_outputMessages.yview)
        self.text_outputMessages.config(yscrollcommand=self.scrollbar_outputMessages.set)

        self.outputMessagesHeader = "Message\t\t\t\t|TS"
        self.text_outputMessages.insert(END, self.outputMessagesHeader)
        self.text_outputMessages.insert(END, '\n'+'----------------------------------------------------------')
        self.update_output_message('GUI started.')
        self.text_outputMessages.config(state=DISABLED)

        self.labelFrame_selectData = ttk.LabelFrame(self, text=' Select data ')
        self.labelFrame_selectData.grid(row=1, column=0, columnspan=4,sticky=W + E, padx=10, pady=(2, 50))
        self.labelFrame_selectData.rowconfigure(0, weight=0)
        self.labelFrame_selectData.rowconfigure(1, weight=0)
        self.label_category = ttk.Label(self.labelFrame_selectData, text='Category ')
        self.label_category.grid(row=0, column=0, sticky=W + E, padx=10, pady=(2, 5))
        self.combobox_category = ttk.Combobox(self.labelFrame_selectData)
        self.combobox_category.grid(row=0, column=1, sticky=W + E, padx=10, pady=(2, 5))

        self.label_subCategory = ttk.Label(self.labelFrame_selectData, text='Sub category ')
        self.label_subCategory.grid(row=0, column=2, sticky=W + E, padx=10, pady=(2, 5))
        self.combobox_subCategory = ttk.Combobox(self.labelFrame_selectData)
        self.combobox_subCategory.grid(row=0, column=3, sticky=W + E, padx=10, pady=(2, 5))

        self.label_tableName = ttk.Label(self.labelFrame_selectData, text='Table name ')
        self.label_tableName.grid(row=0, column=4, sticky=W + E, padx=10, pady=(2, 5))
        self.combobox_tableName = ttk.Combobox(self.labelFrame_selectData)
        self.combobox_tableName.grid(row=0, column=5, sticky=W + E, padx=10, pady=(2, 5))

        self.labelFrame_configure2DPlot = ttk.LabelFrame(self, text=' Configure 2D plot ')
        self.labelFrame_configure2DPlot.grid(row=2, column=0, columnspan=4, sticky=W + E, padx=10, pady=(2, 5))
        self.labelFrame_configure2DPlot.rowconfigure(0, weight=0)
        self.labelFrame_configure2DPlot.rowconfigure(1, weight=0)
        self.labelFrame_configure2DPlot.rowconfigure(2, weight=0)
        self.labelFrame_configure2DPlot.columnconfigure(0, weight=0)
        self.labelFrame_configure2DPlot.columnconfigure(1, weight=0)
        self.labelFrame_configure2DPlot.columnconfigure(2, weight=0)
        self.label_Y_axis = ttk.Label(self.labelFrame_configure2DPlot, text='Y-axis ')
        self.label_Y_axis.grid(row=0, column=0, sticky=W + E, padx=10, pady=(2, 5))
        self.combobox_Y_axis = ttk.Combobox(self.labelFrame_configure2DPlot)
        self.combobox_Y_axis.grid(row=0, column=1, sticky=W + E, padx=10, pady=(2, 5))

        self.label_X_axis = ttk.Label(self.labelFrame_configure2DPlot, text='X-axis ')
        self.label_X_axis.grid(row=1, column=0, sticky=W + E, padx=10, pady=(2, 5))
        self.combobox_X_axis = ttk.Combobox(self.labelFrame_configure2DPlot)
        self.combobox_X_axis.grid(row=1, column=1, sticky=W + E, padx=10, pady=(2, 5))

        self.label_tableName = ttk.Label(self.labelFrame_configure2DPlot, text='Plot type ')
        self.label_tableName.grid(row=2, column=0, sticky=W + E, padx=10, pady=(2, 5))
        self.combobox_tableName = ttk.Combobox(self.labelFrame_configure2DPlot)
        self.combobox_tableName.grid(row=2, column=1, sticky=W + E, padx=10, pady=(2, 5))

        self.labelFrame_plot2DOptions = ttk.LabelFrame(self.labelFrame_configure2DPlot, text=' Plot options ')
        self.labelFrame_plot2DOptions.grid(row=0, rowspan=3, column=2, columnspan=4, sticky=W + E, padx=10, pady=(2, 5))
        self.labelFrame_plot2DOptions.rowconfigure(0, weight=0)
        self.labelFrame_plot2DOptions.rowconfigure(1, weight=0)
        self.labelFrame_plot2DOptions.rowconfigure(2, weight=0)
        self.labelFrame_plot2DOptions.columnconfigure(0, weight=0)
        self.labelFrame_plot2DOptions.columnconfigure(1, weight=0)
        self.labelFrame_plot2DOptions.columnconfigure(2, weight=0)
        self.labelFrame_plot2DOptions.columnconfigure(3, weight=0)

        self.label_legend = ttk.Label(self.labelFrame_plot2DOptions, text='Legend')
        self.label_legend.grid(row=0, column=0, sticky=W + E, padx=10, pady=(2, 5))
        self.checkbox_legend = tkinter.Checkbutton(self.labelFrame_plot2DOptions)
        self.checkbox_legend.grid(row=0, column=1, sticky=W + E, padx=10, pady=(2, 5))

        self.label_axisNames = ttk.Label(self.labelFrame_plot2DOptions, text='Axes names')
        self.label_axisNames.grid(row=1, column=0, sticky=W + E, padx=10, pady=(2, 5))
        self.checkbox_axisNames = tkinter.Checkbutton(self.labelFrame_plot2DOptions)
        self.checkbox_axisNames.grid(row=1, column=1, sticky=W + E, padx=10, pady=(2, 5))
        self.label_title = ttk.Label(self.labelFrame_plot2DOptions, text='Plot title')
        self.label_title.grid(row=2, column=0, sticky=W + E, padx=10, pady=(2, 5))
        self.checkbox_title = tkinter.Checkbutton(self.labelFrame_plot2DOptions)
        self.checkbox_title.grid(row=2, column=1, sticky=W + E, padx=10, pady=(2, 5))

        self.label_scale2x = ttk.Label(self.labelFrame_plot2DOptions, text='Scale 2x')
        self.label_scale2x.grid(row=0, column=2, sticky=W + E, padx=10, pady=(2, 5))
        self.var_scale2x = IntVar()
        self.checkbox_scale2x = tkinter.Checkbutton(self.labelFrame_plot2DOptions, command= lambda: self.update_scale_checkbuttons(0), variable=self.var_scale2x)
        self.checkbox_scale2x.grid(row=0, column=3, sticky=W + E, padx=10, pady=(2, 5))

        self.label_scale3x = ttk.Label(self.labelFrame_plot2DOptions, text='Scale 3x')
        self.label_scale3x.grid(row=1, column=2, sticky=W + E, padx=10, pady=(2, 5))
        self.var_scale3x = IntVar()
        self.checkbox_scale3x = tkinter.Checkbutton(self.labelFrame_plot2DOptions, command= lambda: self.update_scale_checkbuttons(1),variable=self.var_scale3x)
        self.checkbox_scale3x.grid(row=1, column=3, sticky=W + E, padx=10, pady=(2, 5))

        self.label_scale4x = ttk.Label(self.labelFrame_plot2DOptions, text='Scale 4x')
        self.label_scale4x.grid(row=2, column=2, sticky=W + E, padx=10, pady=(2, 5))
        self.var_scale4x = IntVar()
        self.checkbox_scale4x = tkinter.Checkbutton(self.labelFrame_plot2DOptions, command= lambda: self.update_scale_checkbuttons(2), variable=self.var_scale4x)
        self.checkbox_scale4x.grid(row=2, column=3, sticky=W + E, padx=10, pady=(2, 5))


    def fetch_data(self):
        self.update_output_message('fetching data')

    def update_output_message(self, text):
        text = self.format_output_message(text)
        self.text_outputMessages.config(state=NORMAL)
        self.text_outputMessages.insert(END, '\n'+text)
        self.text_outputMessages.config(state=DISABLED)

    def format_output_message(self, text):
        if len(text) <= len(self.outputMessagesHeader)+13:
            line = text
            lastLine = line
        else:
            line = ''
            for i, character in enumerate(text):
                if i % (len(self.outputMessagesHeader)+14) == 0.0 and i !=0:
                    if character != ' ':
                        line +='-\n'
                    else:
                        line += '\n'
                else:
                    line += character

            for i, character in enumerate(line):
                if character == '\n':
                    index = i
            lastLine = line[index:-1]
        toTS = len(self.outputMessagesHeader)+18-len(lastLine)
        for i in range(toTS):
            line += ' '
        line += '|'+self.get_time_stampe()
        return line

    def get_time_stampe(self):
        return str(time.strftime("%H:%M:%S") +' '+ time.strftime("%d/%m/%Y"))

    def update_scale_checkbuttons(self, number):
        scaleCheckButtons = [self.var_scale2x,
                             self.var_scale3x,
                             self.var_scale4x]
        for i, var in enumerate(scaleCheckButtons):
            if var.get() == 1 and i == number:
                var.set(1)
            else:
                var.set(0)









