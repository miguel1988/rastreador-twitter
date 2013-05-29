# -*- coding: utf-8 -*-

import bottle
import requests
import json
from requests_oauthlib import OAuth1
from urlparse import parse_qs

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "vdGeYgxaveRGQ33yyTIQA"
CONSUMER_SECRET = "jVt1tXBFSmzPhrjoKJYGp3I1khAANy6p2VLdWR6oQtI"
TOKENS = {}

def get_request_token():
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
    )
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["request_token"] = credentials.get('oauth_token')[0]
    TOKENS["request_token_secret"] = credentials.get('oauth_token_secret')[0]

def get_access_token(TOKENS):
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["request_token"],
                   resource_owner_secret=TOKENS["request_token_secret"],
                   verifier=TOKENS["verifier"],
    )

    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["access_token"] = credentials.get('oauth_token')[0]
    TOKENS["access_token_secret"] = credentials.get('oauth_token_secret')[0]


@bottle.get('/')
def index():
    get_request_token()
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    return bottle.template('index.tpl', authorize_url=authorize_url)

@bottle.get('/busqueda')
def get_verifier():
    TOKENS["verifier"] = bottle.request.query.oauth_verifier
    get_access_token(TOKENS)
    return bottle.template('busqueda.tpl')


@bottle.route('/resultado', method='POST')
def pagina_rasultante():
    def get_verifier():
        TOKENS["verifier"] = bottle.request.query.oauth_verifier
        get_access_token(TOKENS)
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])

    palabrabuscada = bottle.request.forms.get("palabrabuscada")
    busqueda = requests.get("http://search.twitter.com/search.json", params={"q":palabrabuscada, "lang":"es", "result_type":"recent", "rpp":"1"})
    palabra_buscada= json.loads(busqueda.text)['query']
    comentario = json.loads(busqueda.text)['results'][0]['text']
    imagen_usuario = json.loads(busqueda.text)['results'][0]['profile_image_url']
    delusuario = json.loads(busqueda.text)['results'][0]['from_user']
    creado_en = json.loads(busqueda.text)['results'][0]['created_at']
    num_usuario = json.loads(busqueda.text)['results'][0]['from_user_id']

    url = 'https://api.twitter.com/1/friendships/create.json'
    
    r = requests.post(url=url,
                      data={"user_id":num_usuario},
                      auth=oauth)

    return bottle.template('resultado', rastreando=palabra_buscada, texto=comentario, autor=delusuario, imagen=imagen_usuario, fecha=creado_en)


import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
    'app-root/runtime/repo/wsgi/views/')) 

application=bottle.default_app()
