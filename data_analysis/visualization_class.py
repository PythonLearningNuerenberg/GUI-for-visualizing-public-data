
# This class will have all function for the visualization part of the GUI for visualization
import pandas as pd

class Visualization:



    def plot_everything(self, data, columns, type, filter = 0):
        """ Everyone
        Phillip: Bubble Plot
        data = 2D np.array
        columns = list[x,y,z]?
        type = e.g. "scatter", "bar"
        filter = optional to filter the rows
        """


class DataParsing:

    def __init__(self, data):
        self.data = data
        self.check_data(self.data)

    def return_x_y(self, data):

        message= self.check_data(data)
        if message == True:
            return 'The data you provided is not valid'
        else:
            df, title = self.transform_to_df(data)
            df_cleaned = self.cleanup_data(df)
            dictionary_x_y = self.extract_names(df_cleaned)

            return dictionary_x_y

    def transform_to_df(self, data):
        """

        :param data:
        :return:
        """

        df = pd.DataFrame(data=data[1:, 1:],  # values
                          index=data[1:, 0],  # 1st column as index
                          columns=data[0, 1:])
        title = data[0, 0]

        return df, title


    def check_data(self, data):
        """ Phillip
        Check if data is empty.
        :param data:
        :return:
        """
        if data.size == 0:
            message = True  # numpy array is empty
        else:
            message = False # numpy array contains something
        return message

    def cleanup_data(self, data):
        """
        Delete Missings and strange values.

        :param data: numpy array
        :return:
        """
        data_cleaned = data.dropna(how='all')
        return data_cleaned

    def extract_names(self, data):
        """
        Extract names and the type of the table.


        :param data:2D (or 3D)  np.array
        :return: 1D np.array with the possible column names
        """


        return arrayOfColumnName







