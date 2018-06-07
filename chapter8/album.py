def make_album(artist, title, tracks=''):
    album_details = {}
    album_details['artist'] = artist
    album_details['album_name'] = title
    if tracks:
        album_details['tracks'] = tracks
    
    return album_details

new_album = make_album('infinite', 'infinitize')
print(new_album)
new_album = make_album('twice', 'what is love')
print(new_album)
new_album = make_album('nct dream', 'my first and last', 3)
print(new_album)