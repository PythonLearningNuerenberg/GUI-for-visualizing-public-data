
# This class will have all function for the visualization part of the GUI for visualization


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

    def check_data(self, data):
        """ Phillip
        Check if data is empty.
        :param data:
        :return:
        """

        message = True
        message = False
        return message

    def cleanup_data(self, data):
        """ Francesco
        Delete Missings and strange values.

        :param data: numpy array
        :return:
        """

        return data

    def extract_names(self, data):
        """ Marie
        Extract names and the type of the table.


        :param data:2D (or 3D)  np.array
        :return: 1D np.array with the possible column names
        """


        return arrayOfColumnName







