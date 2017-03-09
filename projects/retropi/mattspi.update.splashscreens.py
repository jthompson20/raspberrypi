# import scripts
import urllib
import urllib2
import os
import sys
import json

# init vars
api             = 'http://jsonapi.net/mattspi'
splash          = '/home/pi/RetroPie/splashscreens/mattspi/'


# grab array of local splashscreens
local 		= []
for (path, dirnames, filenames) in os.walk(splash):
    local.extend(os.path.join(path, name).replace(splash,'') for name in filenames)

# grab array of remote games
response        = urllib2.urlopen(api + '/splashscreens/read.php')
remote          = json.load(response)

# compare local and remote games
screens 		= []
for screen in remote:
	if screen not in local:
		screens.append(screen)

# iterate all games to add and download to proper place
for filepath in screens:
        # request the download
	encoded	 	= urllib.quote(filepath)
	download 	= urllib2.urlopen(api + '/splashscreens/downloads/' + encoded)
        # open local file for writing
        with open(splash + filepath, 'wb') as local_file:
                local_file.write(download.read())