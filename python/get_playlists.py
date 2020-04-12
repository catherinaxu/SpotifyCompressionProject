import sys
import spotipy
import spotipy.util as util

def add_tracks(tracks, track_list):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        track_list.append((track['artists'][0]['name'], track['name']))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username,
                                       scope='playlist-read-private',
                                       client_id='c4566167b7814ab1b22916d17a77063e',
                                       client_secret='9e100161059247f7877c66636fae3f74',
                                       redirect_uri='http://localhost/')
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        tracks_by_playlist = []
        for playlist in playlists['items']:
            track_list = []
            if playlist['owner']['id'] == username:
                results = sp.playlist(playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                add_tracks(tracks, track_list)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    add_tracks(tracks, track_list)
                tracks_by_playlist.append(track_list)
    else:
        print("Can't get token for", username)

    print(tracks_by_playlist)