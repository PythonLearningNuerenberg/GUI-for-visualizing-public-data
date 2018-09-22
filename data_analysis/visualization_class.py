
# This class will have all function for the visualization part of the GUI for visualization
import pandas as pd
import matplotlib.pyplot as plt






class DataParsing:

    def __init__(self, data):
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

        if column is not None and row is not None:
            plotObject = self.df.loc[row, column]

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
        if self.data.size == 0:
            self.generalCheck = True  # numpy array is empty
        else:
            self.generalCheck = False # numpy array contains something


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
        d['Xnames'] = list(self.df.columns.values)
        d['Ynames'] = list(self.df.index)


        self.outputDictonary = {**self.outputDictonary, **d}







table = pd.read_excel("Test Data/indicator gapminder population.xlsx", header = None)
table_numpy = table.values

parsingObject = DataParsing(table_numpy)
parsingObject.process_data()


print(parsingObject.plot_data(1800.0, 'Austria', plot_type= None))
#print(parsingObject.outputDictonary)
