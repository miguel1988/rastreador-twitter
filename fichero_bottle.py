import bottle
import requests
import json

busqueda = requests.get("http://search.twitter.com/search.json", params = {"q":"programar", "lang":"es", "result_type":"recent", "rpp":"1"})
palabra_buscada= json.loads(busqueda.text)['query']
comentario = json.loads(busqueda.text)['results'][0]['text']
imagen_usuario = json.loads(busqueda.text)['results'][0]['profile_image_url']
delusuario = json.loads(busqueda.text)['results'][0]['from_user']
creado_en = json.loads(busqueda.text)['results'][0]['created_at']



@bottle.route('/resultado')
def pagina_rasultante():
    return bottle.template("resultado", rastreando=palabra_buscada, texto=comentario, autor=delusuario, imagen=imagen_usuario, fecha=creado_en)



bottle.run(host="localhost", port=8080)
