# Obtener información de un usuario determinado, especificado el ID o el nombre de usuario.


#Importamos el paquete requests:
import requests
# Solicitamos información acerca del usuario con nombre lorimeyersband:
informacion_usuario = requests.get("https://api.twitter.com/1/users/show.json", params={"screen_name":"lorimeyersband"})
# Condicionamos la impresion de la información si la petición ha sido correcta:
if informacion_usuario.status_code == 200:
    print informacion_usuario.text


#Parametros:
  # user_id: El ID de usuario del que se desea obtener los resultados.
	# screen_name: El nombre de la pantalla del usuario para el que retornen los resultados.
