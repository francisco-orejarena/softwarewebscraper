import concurrent.futures
import json
import random
import sys
import time
import urllib.parse

import pymongo
import requests
from bs4 import BeautifulSoup
from bson.objectid import ObjectId
from concurrent.futures import wait
import config
import logging

log_format = '%(asctime)s :: %(levelname)s :: %(message)s'
logging.basicConfig(format=log_format)

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.DEBUG)

'''
The above code is copied directly from the example code that was given to me.
'''

# Scrapes all software categories
def scrape_categories():
    software = "https://www.featuredcustomers.com/software"
    soft_cat = requests.get(software)
    broccoli_cheddar = BeautifulSoup(soft_cat.text, 'html.parser')
    chicken_noodle = broccoli_cheddar.find_all('div', {'class': 'categories_left'})
    chicken_orzo = chicken_noodle[0].ul.find_all('a', {})
    i = 0
    while i < 510: 
        print(chicken_orzo[i].text)
        i += 1


# This function scrapes the company names on the specific page listed
def scrape_name():
    first_category = "https://www.featuredcustomers.com/software/3d-printing-solutions"
    three_d = requests.get(first_category)
    gazpacho = BeautifulSoup(three_d.text, 'html.parser')
    cream_of_mushroom = gazpacho.find_all('div', {'class': 'row cls-vendor-name'})
    i = 0
    while i < 14: 
        print(cream_of_mushroom[i].text)
        i += 1


# This function scrapes all of the websites listed on the specific page listed; the page is category specific and was not looped through categories
def scrape_website():
    first_category = "https://www.featuredcustomers.com/software/3d-printing-solutions"
    three_d = requests.get(first_category)
    gazpacho = BeautifulSoup(three_d.text, 'html.parser')
    tomato = gazpacho.find_all('li', {'class': 'cls-website'})
    i = 0
    while i < 14: 
        print(tomato[i].text)
        i += 1


# This function scrapes all of the phone numbers listed on the specific page listed; the page is category specific and was not looped through categories
def scrape_phone():
    first_category = "https://www.featuredcustomers.com/software/3d-printing-solutions"
    three_d = requests.get(first_category)
    gazpacho = BeautifulSoup(three_d.text, 'html.parser')
    motzaball = gazpacho.find_all('li', {'class': 'cls-phone'})
    i = 0
    while i < 14: 
        print(motzaball[i].text)
        i += 1


# This function scrapes all of the headqurters' locations listed on the specific page listed; the page is company specific and was not looped through companies
def scrape_headquarters():
    specific_company = "https://www.featuredcustomers.com/vendor/3dsystems"
    three_d_sys = requests.get(specific_company)
    bone_broth = BeautifulSoup(three_d_sys.text, 'html.parser')
    newengland_clam_chowder = bone_broth.find('span', {'class': 'rg'})
    print(newengland_clam_chowder.text)


'''
def scrape_specialty():
'''


# This function scrapes all of the description listed on the specific page listed; the page is category specific and was not looped through categories
def scrape_about():
    first_category = "https://www.featuredcustomers.com/software/3d-printing-solutions"
    three_d = requests.get(first_category)
    gazpacho = BeautifulSoup(three_d.text, 'html.parser')
    chowder = gazpacho.find_all('p', {'class': 'description'})
    i = 0
    while i < 14:
        print(chowder[i].text)
        i += 1

'''
The last section needing to be scraped is the 'Specialties' section which I found to be redundant. 
I discuss this in the problems that I faced, so I think whatever conclusion we come up with should be implemented.
'''

if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise Exception("Please provide action name. Available actions : \n scrape_categories \n scrape_name \n scrape_website \n scrape_phone \n scrape_headquaters \n scrape_about \n ")

    action_name = sys.argv[1]
    file_handler = logging.FileHandler('capterra_log.log')

    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(file_handler)

    if action_name == 'scrape_categories':
        logging.info('Scraping Categories')
        scrape_categories()
    elif action_name == 'scrape_name':
        logging.info('Scraping Names')
        scrape_name()
    elif action_name == 'scrape_website':
        logging.info('Scraping Websites from Listings')
        scrape_website()
    elif action_name == 'scrape_phone':
        logging.info('Scraping Phone Numbers from Listings')
        scrape_phone()
    elif action_name == 'scrape_headquarters':
        logging.info('Scraping Headquarters Location')
        scrape_headquarters()
    elif action_name == 'scrape_about':
        logging.info('Scraping About Companies')
        scrape_about()
