import requests
import json

posts = requests.get("https://jsonplaceholder.typicode.com/posts/")

# con esta opción podemos ver qué contiene el request que hicimos
print(posts.text)

# aunque parece un diccionario de python, como verás, el tipo del objeto es un string, es decir, tenemos que parsearlo
print(type(posts.text))

dicposts = json.loads(posts.text)

print(dicposts)
print(type(dicposts))

lista_titulos = []
for dicpost in dicposts:
    post = dicpost
    numero_post = post["id"]
    lista_titulos = post["title"]
    print(str(numero_post) + " " + lista_titulos)
