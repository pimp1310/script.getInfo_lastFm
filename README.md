# Last-FM Similar Artist Addon


List of possible script calls.
All calls can also be done by using a plugin path.

### ATTENTION

You need this file in your MQ7 Skin Folder (Easy Replace the old one)
```
https://github.com/pimp1310/dialogmusicinfo
```


Example of a Request in a Container :
```
$INFO[Listitem.Property(artistname)]
```


### LASTFM SIMILAR ARTISTS
```
<content>plugin://script.getInfo_LastFM?request=getSimilar&amp;&amp;artist=$INFO[ListItem.Artist]</content>
```
Properties:
   
- 'artistname'
- 'imageurl_s'
- 'imageurl_m'
- 'imageurl_l'
- 'imageurl_xl'
	
	


### LASTFM TOP ALBUMS ARTISTS
```
<content>plugin://script.getInfo_LastFM?request=getTopAlbums&amp;&amp;artist=$INFO[ListItem.Artist]</content>
```
Properties:

- 'albumname'
- 'playcount'
- 'imageurl_s'
- 'imageurl_m'
- 'imageurl_l'
- 'imageurl_xl'


### LASTFM TOP TRACKS ARTISTS
```
<content>plugin://script.getInfo_LastFM?request=getTopTracks&amp;&amp;artist=$INFO[ListItem.Artist]</content>
```
Properties:

- 'trackname'
- 'playcount'
- 'listeners'
- 'imageurl_s'
- 'imageurl_m'
- 'imageurl_l'
- 'imageurl_xl'


###Examples

[![Bildschirmfoto vom 2016-12-20 16-09-59.png](https://s28.postimg.org/fdpgcmcgt/Bildschirmfoto_vom_2016_12_20_16_09_59.png)](https://postimg.org/image/nvywgyizd/)

[![Bildschirmfoto vom 2016-12-20 16-10-07.png](https://s23.postimg.org/cblzgeadn/Bildschirmfoto_vom_2016_12_20_16_10_07.png)](https://postimg.org/image/rkbwu641z/)

[![Bildschirmfoto vom 2016-12-20 16-10-19.png](https://s30.postimg.org/b0olz64nl/Bildschirmfoto_vom_2016_12_20_16_10_19.png)](https://postimg.org/image/cfq6nw5ql/)




