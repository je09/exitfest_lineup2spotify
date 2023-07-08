import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import logging

clientId = ''
clientSectret = ''
scope = 'playlist-modify-public,playlist-modify,playlist-read-private,playlist-read-collaborative,playlist-modify-private'
playlist_url = ''
playlist_uri = ''

logger = logging.getLogger('examples.add_tracks_to_playlist')
logging.basicConfig(level='DEBUG')


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=clientId,
        client_secret=clientSectret,
        redirect_uri='http://localhost:8888/callback')
)
def read_json(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(''.join(file.readlines()))


def main():
    lineup = read_json('lineup.json')
    print(sp.me())
    for event in lineup:
        artist = event['artist']
        results = sp.search(q='artist:' + artist, type="artist", limit=1)
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            artist_uri = artist['uri']
            artist_genres = artist['genres']

            print(artist_genres)
            track_res = sp.artist_top_tracks(artist_uri)
            if len(track_res['tracks']) > 0:
                sp.playlist_add_items(playlist_url, [i['uri'] for i in track_res['tracks'][:2]])


main()
