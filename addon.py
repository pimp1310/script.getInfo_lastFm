import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import urllib2
import re
import cgi

def unescape(s):
    s = s.replace('&lt;', '<')
    s = s.replace('&gt;', '>')
    s = s.replace('&nbsp;', ' ')
    s = s.replace('&apos;', '\'')
    # this has to be last:
    s = s.replace('&amp;', '&')
    return s

#von Kodi uebermittelte Parameter
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = sys.argv[2][1:].split('&&') # ? entfernen

# Inhalt markieren
xbmcplugin.setContent(addon_handle, 'music')

# Request und Artist auslesen
request = args[0][8:]
artist = args[1][7:]

# Last FM API Key
api_key = '3534ab3b5df00fd053d0fd3b514a1820'

# HTTP URL bilden
http_url = ''
if request == 'getSimilar':
    http_url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=' + artist + '&api_key=' + api_key
elif request == 'getTopAlbums':
    http_url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist=' + artist + '&api_key=' + api_key
elif request == 'getTopTracks':
    http_url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=' + artist + '&api_key=' + api_key

# Internetseite laden
Socket = urllib.urlopen(http_url)
Quelltext = Socket.read()
Socket.close()

# Zeilemumbrueche aus Quelltext entfernen
Quelltext = Quelltext.replace('\n', '')
Quelltext = Quelltext.replace('\r', '')
Quelltext = Quelltext.replace('\t', '')
Quelltext = unescape(Quelltext)

# KP evtl loeschen
def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

# Daten auswerten je nach Request
if request == 'getSimilar':
    #Quelltext nach Artists splitten
    artists = Quelltext.split('</artist><artist>')

    # jeden match durchlaufen
    for entry in artists:
        temp = entry
        
        #Artistname
        temp = temp[temp.find('<name>') + 6:]
        artistname = temp[:temp.find('</name>')]
        
        #Image Small
        temp = temp[temp.find('small') + 7:]
        image_small = temp[:temp.find('</image>')]
        
        #Image Medium
        temp = temp[temp.find('medium') + 8:]
        image_medium = temp[:temp.find('</image>')]
        
        #Image Large
        temp = temp[temp.find('large') + 7:]
        image_large = temp[:temp.find('</image>')]
        
        #Image Extralarge
        temp = temp[temp.find('extralarge') + 12:]
        image_extralarge = temp[:temp.find('</image>')]

        # DirectoryItem erzeugen
        url = build_url({'mode': 'folder', 'foldername': 'Folder One'})
        li = xbmcgui.ListItem('Folder One', iconImage='DefaultFolder.png')
        li.setProperty('artistname', artistname)
        li.setProperty('imageurl_s', image_small)
        li.setProperty('imageurl_m', image_medium)
        li.setProperty('imageurl_l', image_large)
        li.setProperty('imageurl_xl', image_extralarge)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
        
    xbmcplugin.endOfDirectory(addon_handle)
    
if request == 'getTopAlbums':
    #Quelltext nach Albums splitten
    albums = Quelltext.split('</album><album>')

    # jeden match durchlaufen
    for entry in albums:
        temp = entry
        
        #AlbumName
        temp = temp[temp.find('<name>') + 6:]
        albumname = temp[:temp.find('</name>')]
        
        #Playcount
        temp = temp[temp.find('<playcount>') + 11:]
        playcount = temp[:temp.find('</playcount>')]
        
        #Image Small
        temp = temp[temp.find('small') + 7:]
        image_small = temp[:temp.find('</image>')]
        
        #Image Medium
        temp = temp[temp.find('medium') + 8:]
        image_medium = temp[:temp.find('</image>')]
        
        #Image Large
        temp = temp[temp.find('large') + 7:]
        image_large = temp[:temp.find('</image>')]
        
        #Image Extralarge
        temp = temp[temp.find('extralarge') + 12:]
        image_extralarge = temp[:temp.find('</image>')]
        
        # DirectoryItem erzeugen
        url = build_url({'mode': 'folder', 'foldername': 'Folder One'})
        li = xbmcgui.ListItem('Folder One', iconImage='DefaultFolder.png')
        li.setProperty('albumname', albumname)
        li.setProperty('playcount', playcount)
        li.setProperty('imageurl_s', image_small)
        li.setProperty('imageurl_m', image_medium)
        li.setProperty('imageurl_l', image_large)
        li.setProperty('imageurl_xl', image_extralarge)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)
    
if request == 'getTopTracks':
    #Quelltext nach Tracks splitten
    tracks = Quelltext.split('</track><track')

    # jeden match durchlaufen
    for entry in tracks:
        temp = entry
        
        #TrackName
        temp = temp[temp.find('<name>') + 6:]
        trackname = temp[:temp.find('</name>')]
        
        #Playcount
        temp = temp[temp.find('<playcount>') + 11:]
        playcount = temp[:temp.find('</playcount>')]
        
        #Listeners
        temp = temp[temp.find('<listeners>') + 11:]
        listeners = temp[:temp.find('</listeners>')]
        
        #Image Small
        temp = temp[temp.find('small') + 7:]
        image_small = temp[:temp.find('</image>')]
        
        #Image Medium
        temp = temp[temp.find('medium') + 8:]
        image_medium = temp[:temp.find('</image>')]
        
        #Image Large
        temp = temp[temp.find('large') + 7:]
        image_large = temp[:temp.find('</image>')]
        
        #Image Extralarge
        temp = temp[temp.find('extralarge') + 12:]
        image_extralarge = temp[:temp.find('</image>')]
        
        # DirectoryItem erzeugen
        url = build_url({'mode': 'folder', 'foldername': 'Folder One'})
        li = xbmcgui.ListItem('Folder One', iconImage='DefaultFolder.png')
        li.setProperty('trackname', trackname)
        li.setProperty('playcount', playcount)
        li.setProperty('listeners', listeners)
        li.setProperty('imageurl_s', image_small)
        li.setProperty('imageurl_m', image_medium)
        li.setProperty('imageurl_l', image_large)
        li.setProperty('imageurl_xl', image_extralarge)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
        
    xbmcplugin.endOfDirectory(addon_handle)

#f = open('d:\\test.txt', 'w+')
#    f.write(SimilarArtistName + '\n')
#    f.write(SimilarArtistExtraLargeImage + '\n\n')
#f.close()
    
# Error Codes from LastFM API
# 2 : Invalid service - This service does not exist
# 3 : Invalid Method - No method with that name in this package
# 4 : Authentication Failed - You do not have permissions to access the service
# 5 : Invalid format - This service doesn't exist in that format
# 6 : Invalid parameters - Your request is missing a required parameter
# 7 : Invalid resource specified
# 8 : Operation failed - Something else went wrong
# 9 : Invalid session key - Please re-authenticate
# 10 : Invalid API key - You must be granted a valid key by last.fm
# 11 : Service Offline - This service is temporarily offline. Try again later.
# 13 : Invalid method signature supplied
# 16 : There was a temporary error processing your request. Please try again
# 26 : Suspended API key - Access for your account has been suspended, please contact Last.fm
# 29 : Rate limit exceeded - Your IP has made too many requests in a short period

