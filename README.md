# Last-FM Similar Artist Addon
Aufrufe des Plugins:


<content>plugin://script.getInfo_LastFM?request=getSimilar&amp;&amp;artist=$INFO[ListItem.Artist]</content>
Properties:
    -artistname
    -imageurl_s
    -imageurl_m
    -imageurl_l
    -imageurl_xl

<content>plugin://script.getInfo_LastFM?request=getTopAlbums&amp;&amp;artist=$INFO[ListItem.Artist]</content>
Properties:
    -albumname
    -playcount
    -imageurl_s
    -imageurl_m
    -imageurl_l
    -imageurl_xl

<content>plugin://script.getInfo_LastFM?request=getTopTracks&amp;&amp;artist=$INFO[ListItem.Artist]</content>
    -trackname
    -playcount
    -listeners
    -imageurl_s
    -imageurl_m
    -imageurl_l
    -imageurl_xl





