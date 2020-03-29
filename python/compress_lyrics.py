import argparse
import gzip
import json
import re
import requests
import zlib

from bs4 import BeautifulSoup
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import List, Tuple


class LyricCompressor:
    def __init__(self, cache_path: str):
        self.cache_path = Path(cache_path)

        self.client_access_token = 'rnng65r8lN34SSMqUiOfxt_3zAo0b4HyTW_9ng1pel8xBnQkoiTAQ7ntD5kUSFcK'
        self._load_cache()

    def _load_cache(self):
        self.cache = {}
        if not self.cache_path.exists():
            return
        with self.cache_path.open(mode='r') as f:
            for line in f.readlines():
                title, artist, reduction_str = line.split('\t')
                self.cache[(title, artist)] = float(reduction_str)

    def _save_cache(self):
        with self.cache_path.open(mode='w') as f:
            for (title, artist), reduction in self.cache.items():
                f.write('{}\t{}\t{:.3f}\n'.format(title, artist, reduction))

    def analyze_songs(self, songs: List[Tuple[str, str]]):
        songs_to_process = [song for song in set(songs) if song not in self.cache]
        all_song_lyrics = deque()

        with ThreadPoolExecutor(max_workers=100) as e:
            for title, artist in songs_to_process:
                e.submit(self.store_song_lyrics, all_song_lyrics, title, artist)

        for title, artist, lyrics in all_song_lyrics:
            self.cache[(title, artist)] = self.compress_lyrics(lyrics)

        self._save_cache()

        for title, artist in songs:
            print('{}\t{}\t{:.3f}'.format(title, artist, self.cache[(title, artist)]))

    def store_song_lyrics(self, all_song_lyrics, title: str, artist: str):
        song_lyrics = self.get_song_lyrics(title, artist)
        all_song_lyrics.append((title, artist, song_lyrics))

    def get_song_lyrics(self, title: str, artist: str):
        song_url = self._get_song_url(title, artist)
        lyrics = self._scrape_lyrics(song_url)
        return lyrics

    def _get_song_url(self, title: str, artist: str):
        headers = {'Authorization': 'Bearer ' + self.client_access_token}
        params = {'q': '{} {}'.format(title, artist)}

        response = requests.get('https://api.genius.com/search', headers=headers, params=params)
        results = json.loads(response.content)['response']['hits']
        results = [result for result in results if artist in result['result']['primary_artist']['name'].lower()]
        if len(results) == 0:
            print('error for {} - {}'.format(title, artist))
            return
        # print(results[0])

        sorted_results = sorted(results, key=lambda result: result['result']['stats'].get('pageviews', 0), reverse=True)
        # print(sorted_results[0])

        if results[0] != sorted_results[0]:
            print('most page views was not top result for {} - {}'.format(title, artist))
        # print(results[0])
        song_url = results[0]['result']['url']
        return song_url

    def _scrape_lyrics(self, song_url: str):
        page = requests.get(song_url)
        html = BeautifulSoup(page.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()
        return lyrics

    def compress_lyrics(self, lyrics: str):
        # Preprocessing
        lyrics = lyrics.strip()
        lyrics = lyrics.replace('\n\n', '\n')
        lyrics = re.sub(r'\[.*\]\n', '', lyrics)
        lyrics = lyrics.replace(r'\[.*\]', '')
        # print(lyrics)

        # Compression
        compressed_lyrics = gzip.compress(lyrics.encode(), compresslevel=1)
        # compressed_lyrics = zlib.compress(lyrics.encode(), level=1)
        # compressed_lyrics = self._compress(lyrics)

        # print(compressed_lyrics)
        # print(len(compressed_lyrics))
        return 1 - len(compressed_lyrics) / len(lyrics)

    def _compress(self, uncompressed: str):
        """Compress a string to a list of output symbols."""

        # Build the dictionary.
        dict_size = 256
        dictionary = {chr(i): i for i in range(dict_size)}

        w = ""
        result = []
        for c in uncompressed:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                # Add wc to the dictionary.
                dictionary[wc] = dict_size
                dict_size += 1
                w = c

        # Output the code for w.
        if w:
            result.append(dictionary[w])
        return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--song')
    parser.add_argument('-a', '--artist')
    parser.add_argument('-c', '--cache')
    args = parser.parse_args()

    if args.song and args.artist:
        lyric_getter = LyricCompressor()
        lyrics = lyric_getter.get_song_lyrics(args.song, args.artist)
        reduction = lyric_getter.compress_lyrics(lyrics)
        print('size_reduction={}'.format(reduction))
    elif args.cache:
        lyric_getter = LyricCompressor(args.cache)
        lyric_getter.analyze_songs([
            ('humble', 'kendrick lamar'),
            ('timber', 'pitbull'),
            ('moves like jagger', 'maroon 5'),
            ('cheap thrills', 'sia'),
        ])
    else:
        print('error')


if __name__ == '__main__':
    main()
