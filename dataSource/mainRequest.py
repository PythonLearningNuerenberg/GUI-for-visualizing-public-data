import requests

# singleton class to fetch the data from different source.
# TODO: In which format the data will be available
# TODO: From where the data will come and in which form.
# TODO: A method to get the data from the below interface

class DataSource:
    '''A singleton Data source class'''
    '''Since python does not have access specifiers like C++, all the attributes which starts with __ are mangled'''
    __instance = None;

    def __init__(self):
        if DataSource.__instance != None:
            raise Exception("Data Source is defined singleton, can't be used without getInstance()")
        else:
            DataSource.__instance = self;

    @staticmethod
    def getInstance():
        """static method instance to get the instance of this class"""
        if DataSource.__instance == None:
            DataSource();
        return DataSource.__instance

    def getAvailableDataFromGithub(self):
        page = requests.get("https://github.com/plotly/datasets")
        # check status here
        if (page.status_code != 404):
            # if status code is OK then, think how to get the data from that page
            print("Status code returned: OK")
            print(page.status_code)
            print(page.encoding)
            print(page.text)
        else:
            print("Status code is 404!!")


# check whether the class gives the same instance to all the caller

dataSource1 = DataSource.getInstance();
dataSource2 = DataSource.getInstance();
if dataSource1 is dataSource2:
    print("They are same")
else:
    print("They are not same")

