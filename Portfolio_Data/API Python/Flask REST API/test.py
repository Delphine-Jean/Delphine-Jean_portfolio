import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1" , {"likes":10, "name":"delphine","views":27})
print(response.json())
input()

response = requests.get(BASE + "video/6")
print(response.json())