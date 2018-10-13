import requests
from html.parser import  HTMLParser


class DataSource:
    '''A singleton Data source class'''
    __instance = None;

    def __init__(self):
        if DataSource.__instance != None:
            raise Exception("This is singleton Class")
        else:
            DataSource.__instance = self;

    @staticmethod
    def getInstance():
        """static method instance"""
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


dataSource1 = DataSource.getInstance();
dataSource2 = DataSource.getInstance();
if dataSource1 is dataSource2:
    print("They are same")
else:
    print("They are not same")
