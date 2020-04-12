import statistics
from compress_lyrics import LyricCompressor
from get_playlists import PlaylistRetriever

if __name__ == '__main__':
    all_playlists = PlaylistRetriever.get_playlists('129599297')

    for i, playlist in enumerate(all_playlists):
        reductions = []
        for artist, title in playlist[1]:
            lyrics = LyricCompressor.get_song_lyrics(title, artist)
            reduction = LyricCompressor.compress_lyrics(lyrics)
            reductions.append(reduction)
        print('{}: Mean Reduction{}%'.format(playlist[0], statistics.mean(reductions)))

