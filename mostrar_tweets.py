# Devuelve la cantidad de tweets que especifiquemos del usuario que introduzcamos.


#Importamos el paquete requests:
import requests
# Muestra el numero de tweets que indiquemos en el parametro count del usuario indicado, en este ejemplo 3 tweets del usuario lorimeyersband:
visar_tweets = requests.get("https://api.twitter.com/1/statuses/user_timeline.json", params={"screen_name":"lorimeyersband", "count":"3"})
# Condicionamos la impresion de la información si la petición ha sido correcta:
if visar_tweets.status_code == 200:
    print visar_tweets.text


#Parametros:
  # user_id: El ID de usuario del que se se desea obtener los resultados.
	# screen_name: El nombre de la pantalla del usuario del que se desea obtener los resultados.
	# count: Especifica el número de tweets para tratar de recuperar, hasta un máximo de 200.
