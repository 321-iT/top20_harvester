#!/usr/bin/env python3

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from pygments import highlight, lexers, formatters

import sys
import json
import os


def call(api, endpoint):
    response = api.get('https://api.intra.42.fr/v2/' + endpoint)
    raw_json = response.content
    return raw_json

def init_api():
    client_id = os.environ['API42_ID']
    client_secret = os.environ['API42_SECRET']

    client = BackendApplicationClient(client_id=client_id)
    api = OAuth2Session(client=client)
    token = api.fetch_token(token_url='https://api.intra.42.fr/oauth/token', client_id=client_id, client_secret=client_secret)

    return(api)