import requests
import json



x=1

while x <= 100:
    posts = requests.get("https://jsonplaceholder.typicode.com/posts/"+str(x))
    dicposts = json.loads(posts.text)
    titulo_post =  dicposts["title"]
    print(str(x) + " " + titulo_post)
    x += 1
