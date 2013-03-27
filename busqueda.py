# Para hacer una busqueda de una palabra en concreta en los tweets nos valdremos de:

#Importamos el paquete requests:
import requests
#Buscamos la palabra informatica en tweets escritos con lengua española que sea el mas popular hasta el 24 de marzo 
busqueda = requests.get("http://search.twitter.com/search.json", params = {"q":"informatica", "lang":"es", "result_type":"popular", "until":"2013-03-24", "rpp":"1"})
# Condicionamos la impresion de la información si la petición ha sido correcta:
if busqueda.status_code == 200:
    print busqueda.text

# Parametros: 
  # q: Consulta de búsqueda de un máximo de 1.000 caracteres, incluidos los operadores.
	# lang: Restringe tweets a la lengua.
	# result_type: Especifica qué tipo de resultados de búsqueda que prefiere recibir. Los valores válidos son: mixed, recent y popular.
	# rpp: El número de tweets a regresar por página, hasta un máximo de 100.
	# until: Devuelve los tweets generados antes de la fecha indicada. Fecha debe tener el formato AAAA-MM-DD.
