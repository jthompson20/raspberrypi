import numpy as np 
import matplotlib.pyplot as plt 

# count in our dataset
greyhounds 	= 500 
labradors 	= 500 

# random height's +- 4
greyhound_height 	= 28 + 4 * np.random.randn(greyhounds)
labrador_height 	= 24 + 1 * np.random.randn(labradors)

plt.hist([greyhound_height, labrador_height], stacked=True, color=['r','b'])
plt.show()