import bottle
import requests
import json

@bottle.route('/')
def home_page():
    return bottle.template('index')

@bottle.route('/resultado', method='POST')
def pagina_rasultante():
    palabrabuscada = bottle.request.forms.get("palabrabuscada")
	busqueda = requests.get("http://search.twitter.com/search.json", params={"q":palabrabuscada, "lang":"es", "result_type":"recent", "rpp":"1"})
	palabra_buscada= json.loads(busqueda.text)['query']
	comentario = json.loads(busqueda.text)['results'][0]['text']
	imagen_usuario = json.loads(busqueda.text)['results'][0]['profile_image_url']
	delusuario = json.loads(busqueda.text)['results'][0]['from_user']
	creado_en = json.loads(busqueda.text)['results'][0]['created_at']
	return bottle.template('resultado', rastreando=palabra_buscada, texto=comentario, autor=delusuario, imagen=imagen_usuario, fecha=creado_en)

bottle.debug(True)
bottle.run(host="localhost", port=8080)
