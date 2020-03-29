import json

import requests
from bs4 import BeautifulSoup

import oauth2 as oauth

# client_id = 'zzue4ILaIkxP5Jub0bOdVFbKub2dsBOIc-DpG6kq6FzS1cZRL7UKeJVDWz1VySmq'
# client_secret = 'ZePqYCKRG3TwKjZfdPTCFQ-kaxDuM69tM4e-TmVhnKf2bppOxJO0vGqum5A93l3lNkajLsYWMst_hC5i8_z0Zg'
client_access_token = 'rnng65r8lN34SSMqUiOfxt_3zAo0b4HyTW_9ng1pel8xBnQkoiTAQ7ntD5kUSFcK'

# # Create your consumer with the proper key/secret.
# consumer = oauth.Consumer(key=client_id, secret=client_secret)
#
api_url = "https://api.genius.com"
#
# # Create our client.
# client = oauth.Client(consumer)
#
# # The OAuth Client request works just like httplib2 for the most part.
# resp, content = client.request(request_token_url, "GET")
# print(resp)
# print(content)

# params = {
#     'client_id': client_id,
#     'client_secret': client_secret,
# }

headers = {
    'Authorization': 'Bearer ' + client_access_token,
}

def get_song_lyrics(song_title, artist_name):
    params = {
        'q': '{} {}'.format(song_title, artist_name),
    }

    response = requests.get(api_url + '/search', headers=headers, params=params)
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


def scrape_song_url(song_url):
    page = requests.get(song_url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()

    return lyrics


if __name__ == '__main__':
    song_url = get_song_lyrics('humble', 'kendrick lamar')
    print(scrape_song_url(song_url))

