#to run this file please install the folloing packages first
#pip install pyyaml urljoin requests beautifulsoup4
#for mac users if above command does not work try
#pip3 install pyyaml urljoin requests beautifulsoup4

""" 
This class takes the initial website link stored in config.yaml 
which is for now the testpage url(Can be replaced by actual crkn link when ready) 
and parses the website for all excel files found on that webpage, 
it then stores the direct links for the excel file in config.yaml
"""
 


#imports the necessary libraries
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import yaml
import logging

class CrknExcelExtractor:
    def __init__(self, config_path='source/config/config.yaml'):
        self.config_path = config_path
        self.loadConfig() #gets config file path

    def loadConfig(self):
        try:
            with open(self.config_path, 'r') as config_file:
                self.config = yaml.safe_load(config_file) #opens config file
        except FileNotFoundError:# Returns error if config file not found/opened
            logging.info(f"Error: Config file '{self.config_path}' not found.") 
            self.config = {}

    def getInitialLink(self):
        return self.config.get('link')#gets initial website link to parse

    def extractExcelLinks(self):
        link = self.getInitialLink()

        if not link:
            logging.info("Error: 'link' not found in the config file.")
            return []

        try:#class uses initial link to parse website to find all excel files on the website
            response = requests.get(link)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            excel_links = [urljoin(link, a['href']) for a in soup.find_all('a', href=True) if a['href'].endswith('.xlsx')]
            
            # Update config.yaml with the extracted links


            return excel_links
        except requests.exceptions.RequestException as e:
            logging.critical(f"Error fetching content from {link}: {e}")

            return []

    def updateConfig(self, excel_links):#this class updates the config files with excel links found
        if 'excel_links' not in self.config:
            self.config['excel_links'] = []
        self.config['excel_links'].extend(excel_links)
        
        with open(self.config_path, 'r') as config_file:
            yaml_file = yaml.safe_load(config_file)
            yaml_file['excel_links'] = excel_links
        with open(self.config_path, 'w') as file:
            yaml.dump(yaml_file, file)


