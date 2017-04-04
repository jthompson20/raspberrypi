from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import time

# init global variables
#json 	= 
SHOE 	= {
	'model': 	'236754',#'190074',
	'sku': 		'BA8841',#'55088007',
	'slug': 	'adidas-ultra-boost-mens/white/off-white/',
	'quantity': 3,
	'size': 	'11.0'
}

# setup
chrome 	= webdriver.Chrome()

chrome.implicitly_wait(1)

####################################
## LOG INTO FOOTLOCKER
chrome.get('https://www.footlocker.com/checkout/?uri=checkout')

