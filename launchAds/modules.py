from CONSTANTS import *
#import os
#from os.path import exists
#from pg import pg
#import requests
#import csv
#import json
#import names
#import pathlib
#import argparse
#import seleniumwire.undetected_chromedriver.v2 as uc
#import seleniumwire.undetected_chromedriver as uc
#from multiprocessing import Pool
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException#,TimeoutException,ElementNotInteractableException,WebDriverException
from datetime import datetime
from time import sleep
from random import uniform,randint#,choice#,randint
#from utility.chrome_proxy_driver_setup import ChromeProxySetup as CPS
#from utility.extension_clean_up import cleanUp
#from setupProxy import ChromeProxySetup as CPS
#from clearProxy import cleanUp
from infos import *



def log(data):
        print(data)
        with open('log.txt', 'a') as log:
            log.write(f'{data}\n')