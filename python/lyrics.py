import json
import requests

from bs4 import BeautifulSoup


class LyricGetter:
    def __init__(self):
        self.client_access_token = 'rnng65r8lN34SSMqUiOfxt_3zAo0b4HyTW_9ng1pel8xBnQkoiTAQ7ntD5kUSFcK'

    def get_song_url(self, song_title, artist_name):
        headers = {'Authorization': 'Bearer ' + self.client_access_token}
        params = {'q': '{} {}'.format(song_title, artist_name)}

        response = requests.get('https://api.genius.com/search', headers=headers, params=params)
        results = json.loads(response.content)['response']['hits']
        results = [result for result in results if artist_name in result['result']['primary_artist']['name'].lower()]
        if len(results) == 0:
            print('error for {} - {}'.format(song_title, artist_name))
            return
        # print(results[0])

        sorted_results = sorted(results, key=lambda result: result['result']['stats'].get('pageviews', 0), reverse=True)
        # print(sorted_results[0])

        if results[0] != sorted_results[0]:
            print('most page views was not top result for {} - {}'.format(song_title, artist_name))
        # print(results[0])
        song_url = results[0]['result']['url']
        return song_url

    def scrape_process_lyrics(self, song_url):
        page = requests.get(song_url)
        html = BeautifulSoup(page.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()

        return lyrics


def main():
    lyric_getter = LyricGetter()
    song_url = lyric_getter.get_song_url('humble', 'kendrick lamar')
    print(lyric_getter.scrape_process_lyrics(song_url))


if __name__ == '__main__':
    main()
