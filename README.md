# Last-FM Similar Artist Addon


List of possible script calls.
All calls can also be done by using a plugin path.


Example:
```
$INFO[Listitem.Property(artistname)]
```


### LASTFM SIMILAR ARTISTS

<content>plugin://script.getInfo_LastFM?request=getSimilar&amp;&amp;artist=$INFO[ListItem.Artist]</content>

Properties:
    -artistname
    -imageurl_s
    -imageurl_m
    -imageurl_l
    -imageurl_xl
	
	


### LASTFM TOP ALBUMS ARTISTS

<content>plugin://script.getInfo_LastFM?request=getTopAlbums&amp;&amp;artist=$INFO[ListItem.Artist]</content>

Properties:
    -albumname
    -playcount
    -imageurl_s
    -imageurl_m
    -imageurl_l
    -imageurl_xl


### LASTFM TOP TRACKS ARTISTS

<content>plugin://script.getInfo_LastFM?request=getTopTracks&amp;&amp;artist=$INFO[ListItem.Artist]</content>
    -trackname
    -playcount
    -listeners
    -imageurl_s
    -imageurl_m
    -imageurl_l
    -imageurl_xl





