#This program parses information from Spotify API based on URI

import json, urllib2

def artist():
    
    # Get artist info
    artistid = idlist[2]
    url = ('https://api.spotify.com/v1/artists/' + artistid)
    raw_json = json.load(urllib2.urlopen(url))
    
    # find info in json and print it out
    artist = raw_json['name']
    genre  = raw_json['genres'][0]
    link   = raw_json['external_urls']['spotify']

    print(artist + ' on Spotify. Genre: ' + genre + '. Link: ' + link)



def album():
    
    # get album info
    albumid = idlist[2]
    url = ('https://api.spotify.com/v1/albums/' + albumid)
    raw_json = json.load(urllib2.urlopen(url))

    # find info in json and print it out
    album  = raw_json['name']
    artist = raw_json['artists'][0]['name']
    label  = raw_json['label']
    link   = raw_json['external_urls']['spotify']

    print(album + ' by ' + artist + ', an album on Spotify. Link: ' + link)

def track():

    # append trackid to API URL and fetch data from API
    trackid = idlist[2]
    url = ('https://api.spotify.com/v1/tracks/' + trackid)
    raw_json = json.load(urllib2.urlopen(url))

    # format some pretty output
    track  = raw_json['name']
    artist = raw_json['artists'][0]['name']
    link   = raw_json['external_urls']['spotify']

    print('Spotify: ' + track + ' by ' + artist + '. Link: ' + link)
            
def main():

    # determine whether we're dealing with an artist, album, or track URI
    if idlist[1] == str('artist'):
        artist()
    elif idlist[1] == str('album'):
        album()
    elif idlist[1] == str('track'):
        track()

# get URI and extract only the track ID
idstring = raw_input('Enter Spotify URI: ')
idlist = idstring.split(":")
    
main()
