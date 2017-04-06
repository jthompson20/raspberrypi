import RandomUserAgent
import requests
import bs4
import webbrowser
import threading

# define global variables
THREADS 	= 5
PROXIES 	= {
	'http': 	"",
	'https': 	""
}

# our main method to 
def shoebot(model,sku,size,qty):
	# init vars
	purchased 	= False
	# grab URL of our product
	url 		= product(model,sku)
	# check if product in stock
	while not purchased:
		if stocked(url):
			print('we can purchase - item is stocked')
			print('purchasing qty: %s' % qty)
			print('purchasing size: %s' % size)

			for i in range(qty):
				print('purchasing #{}'.format(i+1))
			
			# after successful purchase(s), close thread
			purchased 	= True
			print('purchase complete')
		else:
			print('we can not purchase - item is not stocked')


# method to grab the product URL
def product(model,sku):
	URL 	= 'http://www.footlocker.com/product/model:%s/sku:%s' % (model,sku)

# method to check if this item is in stock
def stocked(url):
	return True

def addtocart():
	return True

def checkout():
	return True


# application start
model 	= input('Enter Model #: ')
sku 	= input('Enter SKU: ')
size 	= input('Enter Shoe Size: (e.g. 11.0, 13.5, etc..) ')
qty 	= int(input('Enter Quantity: '))

# array of sizes
sizes 	= [size]

try:
	shoebot(model,sku,size,qty)
except KeyboardInterrupt:
	print('keyboard interrupt')
finally:
	print('done')

'''
# setup threads
threads = [threading.Thread(name='ThreadNumber{}'.format(n), target=shoebot, args(model,sku,shoesize,qty,)) for shoesize in sizes for n in range(THREADS)]
 
# lets start our threads
for t in threads: 
	t.start()
'''


