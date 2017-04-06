# https://www.youtube.com/watch?v=Jji_MrdUbNc
# http://www.adidas.com/us/ultraboost-x-shoes/BB1696.html?forceSelSize=BB1696_650 	(size 11)
import RandomUserAgent
import requests
import bs4
import webbrowser
import threading
import sys

# define global variables
THREADS 	= 5
PROXIES 	= {
	'http': 	"",
	'https': 	""
}
PURCHASED 	= False

# our main method to 
def shoebot(model,size,qty,evt):
	# grab URL of our product
	url 		= product(model,size)
	# loop as long as thread event is not set
	while not evt.isSet():
		# lets check whether or not it is in stock
		if stocked(url,size):
			# lets double check event isnt yet set
			if not evt.isSet():
				# set threading event so other threads stop working
				evt.set()

				# item is in stock, lets buy some shoes
				print('----------------------------------')
				print('item is stocked')
				print('purchasing qty: %s' % qty)
				addtocart(model,size,qty)
				print('purchasing size: %s' % size)

				for i in range(qty):
					print('purchasing #{}'.format(i+1))
				
				# after successful purchase(s), close thread
				print('purchase complete')
				print('----------------------------------')
			else:
				print('item has already been purchased')
		else:
			print('item is not in stock')


# method to grab the product URL
def product(model,size):
	code 	= shoecode(model,size)
	url 	= 'http://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(code)
	return url

# method to check if this item is in stock
def stocked(url,size):
	HTML 	= requests.get(url,headers=RandomUserAgent.load(),proxies=PROXIES)
	page 	= bs4.BeautifulSoup(HTML.text,"lxml")
	avail 	= page.select('.size-dropdown-block')
	avail 	= str(avail[0].getText()).replace('\n\n','')
	avail 	= avail.split()
	avail.remove('Select')
	avail.remove('size')

	# convert available to float
	avail 	= [float(i) for i in avail]

	# if size is available, select it
	if size in avail:
		return True
	else:
		return False

def addtocart(model,size,qty):
	# POST http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct
	''' 
	POST DATA:
	layer=Add+To+Bag+overlay
	pid=BB1696_650
	Quantity=1
	masterPid=BB1696
	sessionSelectedStoreID=null
	ajax=true
	'''
	#HTML 	= requests.post(url,headers=RandomUserAgent.load(),proxies=PROXIES)
	return True

def checkout():
	# https://www.adidas.com/us/delivery-start
	# submit this form
	# https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/COSummary-Start
	# submit CC details
	return True

def shoecode(model,size):
	base 	= 560 	# base is for shoe size 6.5
	shoe 	= size - 6.5
	shoe 	= shoe * 20
	raw 	= shoe + base
	code 	= int(raw)
	return code


# application start
model 	= input('Enter Model #: ')
#sku 	= input('Enter SKU: ')
size 	= float(input('Enter Shoe Size: (e.g. 11.0, 13.5, etc..) '))
qty 	= int(input('Enter Quantity: '))

# array of sizes
sizes 	= [size]

# setup threads
evt 	= threading.Event()
threads = [threading.Thread(name='ThreadNumber{}'.format(n), target=shoebot, args=(model,size,qty,evt)) for n in range(THREADS)]

# lets start our threads
for t in threads: 
	t.start()

