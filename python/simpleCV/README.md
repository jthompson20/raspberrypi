Installation Instructions:

http://simplecv.readthedocs.io/en/latest/HOWTO-Install%20on%20RaspberryPi.html

You must run below due to error: ImportError: No module named svgwrite

sudo pip install svgwrite

BE SURE TO CHMOD /dev/video0

sudo chmod +x /dev/video0

You need to install uv4l driver:

https://www.linux-projects.org/uv4l/installation/

You may need this (if simplecv errors):

sudo aptitude install lsof

I also had motion installed (as a bg service) which was causing the resource to be busy.  You can kill all of those processes:

sudo killall -9 motion