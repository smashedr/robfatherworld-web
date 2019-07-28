import logging
import requests
import requests_cache

requests_cache.install_cache('twitch_cache', expire_after=120)
logger = logging.getLogger('app')


def filter_streams(client_id, search_terms):
    all_streams = get_streams(client_id)
    streams = []
    for s in all_streams:
        if not s['type'] == 'live':
            break

        search_list = search_terms.split(' ')
        for idx, term in enumerate(search_list, 1):
            if term.lower() not in s['title'].lower():
                break

            if idx == len(search_list):
                streams.append(s)
    return streams


def get_streams(client_id, game_id='1229'):
    url = 'https://api.twitch.tv/helix/streams'
    params = {'first': 100, 'game_id': game_id}
    headers = {'Client-ID': client_id}
    all_streams = []
    while True:
        r = requests.get(url, params=params, headers=headers, timeout=5)
        if not r.ok:
            logger.error(r.content)
            r.raise_for_status()

        j = r.json()
        for x in j['data']:
            all_streams.append(x)

        if 'pagination' in j and 'cursor' in j['pagination'] and j['pagination']['cursor']:
            params['after'] = j['pagination']['cursor']
        else:
            break
    return all_streams
