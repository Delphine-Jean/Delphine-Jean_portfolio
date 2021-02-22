import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":10, "name":"delphine","views":27},
        {"likes":110, "name":"tim","views":2715},
        {"likes":4510, "name":"lisa","views":2017}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i),data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())