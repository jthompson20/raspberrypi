from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import time

# construct the argument parser and parse the arguments
ap 		= argparse.ArgumentParser()
ap.add_argument("-url","--website", required = True, help = "enum of companies we have crawlers for")
args 	= vars(ap.parse_args())
 
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
chrome.get(args['website'])
assert "Foot Locker" in chrome.title

# generate buttons needed
button 	= {
	'login': 	chrome.find_element_by_css_selector('#header_account_access')
}

# click login button
button['login'].click()
chrome.switch_to.frame(chrome.find_element_by_css_selector('iframe[id="loginIFrame"]'))
time.sleep(.5)

# lets login
email 		= chrome.find_element_by_css_selector('#login_email')
# set email address to login
email.send_keys('thompson20_91@hotmail.com')
email.send_keys(Keys.TAB)
time.sleep(.1)
# set password to login
password 	= chrome.find_element_by_css_selector('#login_password')
password.send_keys('Matthew20')
password.send_keys(Keys.TAB)
time.sleep(.1)
# submit data
submit 		= chrome.find_element_by_css_selector('.cta_button')
submit.click()
time.sleep(1)
## we are logged in
####################################


####################################
## ADD SHOE TO CART
# lets go to the shoe we want
chrome.get('http://www.footlocker.com/product/model:%s/sku:%s/%s' % (SHOE['model'],SHOE['sku'],SHOE['slug']))
# lets fill out the form fields
# add quantity
for i in range((SHOE['quantity']-1)):
	quantity 	= chrome.find_element_by_css_selector('.add_quantity')
	quantity.click()
	time.sleep(0.1)

# select size
chrome.find_element_by_css_selector('#pdp_size_select_mask').click()
# we need to wait for footlocker animation
time.sleep(0.5)
chrome.find_element_by_css_selector('a[value="%s"]' % SHOE['size']).click()
time.sleep(0.1)

# add to cart
chrome.find_element_by_css_selector("#pdp_addtocart_button").click()
time.sleep(0.5)
## we have added our shoe to the cart
####################################


####################################
## LET'S CHECKOUT
chrome.get('http://www.footlocker.com/shoppingcart/default.cfm')
chrome.switch_to_default_content()
time.sleep(0.5)
chrome.execute_script("sharedCart_panel.close()")

# click Checkout button
chrome.find_element_by_css_selector('#cart_checkout_button').click()

'''
# fill out CC details
chrome.find_element_by_css_selector('#billFirstName').send_keys('Matthew').send_keys(Keys.TAB)
chrome.find_element_by_css_selector('#billLastName').send_keys('Thompson').send_keys(Keys.TAB)
'''

# select pay method
chrome.find_element_by_css_selector('#CardNumber').send_keys('4242424242424242')
chrome.find_element_by_css_selector('#CardExpireDateMM').send_keys('08')
chrome.find_element_by_css_selector('#CardExpireDateYY').send_keys('19')
chrome.find_element_by_css_selector('#CardCCV').send_keys('999')

# next step
chrome.find_element_by_css_selector('#payMethodPaneContinue').click()
time.sleep(0.5)

# submit order
#chrome.find_element_by_css_selector('#orderSubmit').click()
chrome.execute_script("spco.skipConfirm();finishCMMiniCartCheckoutEvent();return false;")
# check if submission successful, if not - resubmit
####################################

print('found foot locker')
try:
	time.sleep(5000)
finally:
	chrome.close()

'''
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(5)
assert "No results found." not in driver.page_source
'''
#chrome.close()




