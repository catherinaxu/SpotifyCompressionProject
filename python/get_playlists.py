import sys
import spotipy
import spotipy.util as util
from typing import List, Tuple

class PlaylistRetriever:

    @staticmethod
    def _add_tracks(tracks_items, track_list: List[Tuple[str, str]]):
        for i, item in enumerate(tracks_items):
            track = item['track']
            track_list.append((track['artists'][0]['name'], track['name']))

    @staticmethod
    def get_playlists(user_id: str):
        scope = 'playlist-read-private'
        client_id = 'c4566167b7814ab1b22916d17a77063e'
        client_secret = '9e100161059247f7877c66636fae3f74'
        redirect_uri = 'http://localhost/'

        token = util.prompt_for_user_token(user_id, scope, client_id, client_secret, redirect_uri)

        if token:
            sp = spotipy.Spotify(auth=token)
            playlists = sp.user_playlists(user_id)
            tracks_by_playlist = []
            for playlist in playlists['items']:
                track_list = []
                if playlist['owner']['id'] == user_id:
                    results = sp.playlist(playlist['id'],
                                          fields="tracks,next")
                    tracks = results['tracks']
                    PlaylistRetriever._add_tracks(tracks['items'], track_list)
                    while tracks['next']:
                        tracks = sp.next(tracks)
                        PlaylistRetriever._add_tracks(tracks['items'], track_list)
                    tracks_by_playlist.append((playlist['name'], track_list))
        else:
            print("Can't get token for", user_id)
            return None

        return tracks_by_playlist

if __name__ == '__main__':
    print(PlaylistRetriever.get_playlists('129599297'))