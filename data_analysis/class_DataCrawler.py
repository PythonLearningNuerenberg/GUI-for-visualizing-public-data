from time import sleep
import random
import logging
import json
import csv
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DataCrawler:
    def __init__(self, filepath):
        self.filepath = filepath

        # logging
        logging.basicConfig(level=logging.INFO)

        # selenium
        self.driver_options = Options()
        self.driver_options.add_argument("--headless")
        self.driver = webdriver.Chrome(self.config['Selenium']['chrome_driver_path'],
                                       chrome_options=self.driver_options)

        # config
        with open('config.json') as config_file:
            self.config = json.load(config_file)

    def crawl(self, links):
        for link in links:
            self.crawl_single_link(link)

    def crawl_single_link(self, page_link):
        self.driver.get(page_link)
        links_on_page = self.driver.find_elements_by_tag_name('a')
        csv_links_on_page = links_on_page

        for link_on_page in csv_links_on_page:
            dataframe = pd.read_csv(link_on_page)
            self.store_data_in_file(dataframe)

    def store_data_in_file(self, data):
        pass
