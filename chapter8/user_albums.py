def make_album(artist, title):
    album_details = {}
    album_details['artist'] = artist
    album_details['album_name'] = title
    return album_details

active = True
while active:
    name = input('\nArtist\'s Name: ')
    title = input('Album Title: ')
    new_album = make_album(name, title)
    print(new_album)
    
    repeat = input('\nWould you like to make another album? y/n ')
    if repeat.lower() == 'n':
        active = False
        print('\nByeeeeeee')

