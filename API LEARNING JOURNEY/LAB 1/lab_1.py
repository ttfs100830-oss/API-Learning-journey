import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response= requests.get(url)
print(response.status_code)
print(response.text)

data=response.json()
print(data["name"])
print(data["username"]) 
print(data["address"])
print(data["address"]["city"])
print(data["address"]["street"])
print(data["address"]["geo"]["lat"])
print(data["address"]["geo"]["lng"])