import requests
import re
# singleton class to fetch the data from different source.
# TODO: In which format the data will be available
# TODO: From where the data will come and in which form.
# TODO: A method to get the data from the below interface
# TODO: Online/ Offline datasource options

class DataSource:
    '''A singleton Data source class'''
    __instance = None;

    def __init__(self):
        if DataSource.__instance != None:
            raise Exception("Singleton class, use getInstance() method to create instances")
        else:
            self.onlineDataSource = []
            DataSource.__instance = self;

    @staticmethod
    def getInstance():
        """static method instance to get the instance of this class"""
        if DataSource.__instance == None:
            DataSource();
        return DataSource.__instance

    def getDataSourceLocations(self):
        '''read config file to get the data sources'''
        # with block simplifies file handling, instead of try, except
        with open("config.txt","r") as configFileHandle:
            for lines in configFileHandle:
                # one can check here if the data source link in correctly written here, skip the # comments
                if(lines[0] != '#'):
                    self.onlineDataSource.append(lines)
        if len(self.onlineDataSource) > 0:
            return True
        else:
            return False

    def generateDataBank(self):
        '''generates the data bank'''
        if(self.getDataSourceLocations()):
            for source in self.onlineDataSource:
                '''check if there is a new line character at the end, remove it'''
                if(source[-1] == "\n"):
                    page = requests.get(source[:-1])
                else:
                    page = requests.get(source)
                # check status here
                if (page.status_code != 404):
                    # if status code is OK then, think how to get the data from that page
                    print("Status code returned: OK")
                    matchObj = re.findall(r'href=\"(http.*csv)\"',page.text,re.M|re.I)
                    for links in matchObj:
                        print("Data source:",links)
                    print("No of csv:",len(matchObj))
                else:
                    print("Status code is 404!!")

# check whether the class gives the same instance to all the caller

dataSource1 = DataSource.getInstance();
dataSource1.generateDataBank()
