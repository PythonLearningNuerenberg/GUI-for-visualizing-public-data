import os
import logging
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class DataCrawler:
    def __init__(self, folderpath=''):
        # logging
        logging.basicConfig(level=logging.INFO)

        # config
        with open('config.json') as config_file:
            self.config = json.load(config_file)

        # selenium
        self.driver_options = Options()
        self.driver_options.add_argument("--headless")
        self.driver = webdriver.Chrome(self.config['Selenium']['chrome_driver_path'],
                                       chrome_options=self.driver_options)

        # target folder
        self.folderpath = folderpath
        if self.folderpath is None:
            self.folderpath = ''
        if self.folderpath != '' and not os.path.exists(self.folderpath):
            os.makedirs(self.folderpath)


    def crawl_all_csv_files_from_page(self, page_link):
        # get files list at page
        csv_file_list = self.crawl_csv_file_list_from_page(page_link)
        print('Number of files on page: ' + str(len(csv_file_list)))
        print('\n\n')

        # download the content of all files from list
        for link_on_page in csv_file_list:
            if '.csv' in link_on_page['text']:
                print(link_on_page['text'])
                print('- ' + link_on_page['link'])
                result = self.download_csv(link_on_page['link'])

                # store
                if(len(result['csv'])>0 and len(result['filename'])>0):
                    self.store_data_in_file(result['csv'], result['filename'])
                else:
                    print('skipping......')

    def crawl_csv_file_list_from_page(self, page_link):
        self.driver.get(page_link)
        links_elements = self.driver.find_elements_by_tag_name('a')

        links_on_page = [{'text': link.text, 'link': link.get_attribute('href')}
                         for link in links_elements if link.get_attribute('href').endswith('csv') and link.text.endswith('csv')]

        return links_on_page

    def download_csv(self, link):
        redir_url=''
        csv_string=''
        try:
            self.driver.get(link)
            csv_link = self.driver.find_element_by_id('raw-url').get_attribute('href')
            self.driver.get(csv_link)

            # wait for redirect
            wait = WebDriverWait(self.driver, 10)
            wait.until(ec.url_changes(csv_link))
            redir_url = self.driver.current_url

            # get url and data
            element_presence = ec.presence_of_element_located((By.TAG_NAME,'pre'))
            WebDriverWait(self.driver,10).until(element_presence)
            csv_string = self.driver.find_element_by_tag_name('pre').text
        except:
            logging.warning(link)
        return {'filename': str(redir_url).split('/')[-1], 'csv': csv_string}

    def store_data_in_file(self, csv_string, filename):
        full_path = os.path.join(self.folderpath, filename)
        with open(full_path, 'w+') as csv_file_handle:
            csv_file_handle.write(csv_string)


if __name__ == '__main__':
    dc = DataCrawler('Downloaded Data')
    github_link = dc.config['github']['csv_page']
    dc.crawl_all_csv_files_from_page(github_link)
