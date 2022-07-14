'''
Make a request to the Wikipedia API using the given search parameters.
Returns a parsed dict of the JSON response.


Please note that if RATE_LIMIT = True then this function will wait for making the next request by RATE_LIMIT_MIN_WAIT time after last call made.
'''


import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from decimal import Decimal


API_URL = 'http://en.wikipedia.org/w/api.php'
RATE_LIMIT = True
RATE_LIMIT_MIN_WAIT = timedelta(milliseconds=50)
RATE_LIMIT_LAST_CALL = None
USER_AGENT = 'wikipedia'

def _wiki_request(params):
    global RATE_LIMIT_LAST_CALL
    global USER_AGENT

    params['format'] = 'json'
    if not 'action' in params:
        params['action'] = 'query'

    headers = { 'User-Agent': USER_AGENT }

    if RATE_LIMIT and RATE_LIMIT_LAST_CALL and RATE_LIMIT_LAST_CALL + RATE_LIMIT_MIN_WAIT > datetime.now():
        wait_time = (RATE_LIMIT_LAST_CALL + RATE_LIMIT_MIN_WAIT) - datetime.now()
        time.sleep(int(wait_time.total_seconds()))

    r = requests.get(API_URL, params=params, headers=headers)

    if RATE_LIMIT: RATE_LIMIT_LAST_CALL = datetime.now()
    return r.json()