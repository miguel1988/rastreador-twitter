#Obtener el id del usuario el cual ha mencionado la palabra buscada en un tweet

import requests
import json
busqueda = requests.get("http://search.twitter.com/search.json", params = {"q":"informatica", "lang":"es", "result_type":"popular",  "rpp":"1"})
idusuario = json.loads(busqueda.text)['results'][0]['from_user_id']
print idusuario



# Parametros: 
  # q: Consulta de búsqueda de un máximo de 1.000 caracteres, incluidos los operadores.
  # lang: Restringe tweets a la lengua.
	# result_type: Especifica qué tipo de resultados de búsqueda que prefiere recibir. Los valores válidos son: mixed, recent y popular.
	# rpp: El número de tweets a regresar por página, hasta un máximo de 100.
	# until: Devuelve los tweets generados antes de la fecha indicada. Fecha debe tener el formato AAAA-MM-DD.
