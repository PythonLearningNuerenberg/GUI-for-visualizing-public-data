
# This class will have all function for the visualization part of the GUI for visualization
import pandas as pd
#import matplotlib.pyplot as plt

import plotly
import plotly.graph_objs as go

import numpy as np





class DataParsing:

    def __init__(self, data=None):
        self.data = data
        self.df = pd.DataFrame()
        self.generalCheck = False
        self.outputDictonary = {}
       # self.check_data(self.data)

    def plot_data(self, column = None, row = None, plot_type= None):
        """ Everyone
        Phillip: Bubble Plot
        data = 2D np.array
        columns = list[x,y,z]?
        type = e.g. "scatter", "bar"
        filter = optional to filter the rows
        """

        #exact value
        if column is not None and row is not None:
            plotObject = self.df.loc[row, column]
        #only Rows    
        elif column is None and row is not None:
            self.outputDictonary['title'] = "%s: %s" % (self.outputDictonary['title'],row) 
            plotObject =self.df.loc[row,:]
            data = [go.Bar(
                    x=plotObject.index.values,
                    y=plotObject.values
            )]
        #only Columns    
        elif column is not None and row is None:
            self.outputDictonary['title'] = "%s: %s" % (self.outputDictonary['title'], column) 
            plotObject =self.df.loc[:,column]
            data = [go.Bar(
                    x=plotObject.index.values,
                    y=plotObject.values
            )]
         #everything   
        elif column is None and row is None:
            plotObject =self.df

            i=-1
            traces =[]
            for year in self.outputDictonary['xNames']:
                i += 1
                trace = go.Scatter(
                    x=self.outputDictonary['xNames'],
                    y=self.df.loc[self.outputDictonary['yNames'][i],:].values,
                    name=self.outputDictonary['yNames'][i],
                )
                traces.append(trace)

            data = traces
            

        plotly.offline.plot({
            "data": data,
            "layout": go.Layout(title=self.outputDictonary['title'])
        }, auto_open=True)


        return plotObject



    def process_data(self):

        self.check_data()
        if self.generalCheck == True:
            error = {'error': 'The data you provided is not valid', 'error_id': '01'}
            self.outputDictonary = {**self.outputDictonary, **error}

        else:
            error = {'error': 'Awesome', 'error_id': '00'}
            self.outputDictonary = {**self.outputDictonary, **error}
            self.transform_to_df()
            self.cleanup_data()
            self.extract_names()


    def transform_to_df(self):
        """

        :param data:
        :return:
        """

        self.df = pd.DataFrame(data=self.data[1:, 1:],  # values
                          index=self.data[1:, 0],  # 1st column as index
                          columns=self.data[0, 1:])
        self.outputDictonary['title'] = self.data[0, 0]



    def check_data(self):
        """ Phillip
        Check if data is empty.
        :param data:
        :return:
        """
        if self.data is not None:
            if self.data.size == 0:
                self.generalCheck = True  # numpy array is empty
            else:
                self.generalCheck = False # numpy array contains something
        else:
            self.generalCheck = True  # numpy array is empty

    def cleanup_data(self):
        """
        Delete Missings and strange values.

        :param data: numpy array
        :return:
        """
        self.df = self.df.dropna(how='all')

    def extract_names(self):
        """ Francesco
        Extract names and the type of the table.


        :param data:2D (or 3D)  np.array
        :return: 1D np.array with the possible column names
        """
        d = {}
        d['xNames'] = list(self.df.columns.values)
        d['yNames'] = list(self.df.index)


        self.outputDictonary = {**self.outputDictonary, **d}




#
# #windows
# table = pd.read_excel("Test Data/indicator gapminder population.xlsx", header = None)
#
#
# #mac
# #table = pd.read_excel("data_analysis/Test Data/indicator gapminder population.xlsx", header = None)
#
#
# table_numpy = table.values
#
# parsingObject = DataParsing(table_numpy)
# parsingObject.process_data()
#
#
#
# #plot only column - First case
# print(parsingObject.plot_data(1800, None, plot_type= None))
#
# #plot only row  -  Second Case
# #print(parsingObject.plot_data(None, "Italy", plot_type= None))
#
# #plot everything  - Third Case
# print(parsingObject.plot_data(None, None, plot_type= None))


