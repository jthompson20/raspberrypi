from SimpleCV import *
from time import time

cam = Camera(0, {'width': 640, 'height': 480})
capture_times = []
grayscale_times = []
threshold_times = []
find_times = []
show_times = []
loop_times = []

for i in range(100):
    loop_start = start = time()
    img = cam.getImage()
    capture_times.append(time() - start)
    start = time()
    img = img.grayscale()
    grayscale_times.append(time() - start)
    start = time()
    img = img.threshold(45)
    threshold_times.append(time() - start)
    start = time()
    blob = img.findBlobs()
    find_times.append(time() - start)
    start = time()
    img.show()
    show_times.append(time() - start)
    loop_times.append(time() - loop_start)

def mean(l):
    return sum(l) / len(l)

mean_loop_time = mean(loop_times)
mean_capture_time = mean(capture_times)
mean_grayscale_time = mean(grayscale_times)
mean_threshold_time = mean(threshold_times)
mean_find_time = mean(find_times)
mean_show_time = mean(show_times)

print('Average loop time: %.3fs (%.2ffps)' % (mean_loop_time, 1 / mean_loop_time))
print('Average capture time: %.3fs (%.1f%%)' % (mean_capture_time, mean_capture_time * 100 / mean_loop_time))
print('Average grayscale time: %.3fs (%.1f%%)' % (mean_grayscale_time, mean_grayscale_time * 100 / mean_loop_time))
print('Average threshold time: %.3fs (%.1f%%)' % (mean_threshold_time, mean_threshold_time * 100 / mean_loop_time))
print('Average findBlobs time: %.3fs (%.1f%%)' % (mean_find_time, mean_find_time * 100 / mean_loop_time))
print('Average display time: %.3fs (%.1f%%)' % (mean_show_time, mean_show_time * 100 / mean_loop_time))