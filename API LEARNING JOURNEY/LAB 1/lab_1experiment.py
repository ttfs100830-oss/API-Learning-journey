import requests
url = "https://jsonplaceholder.typicode.com/users/999999"

response=requests.get(url)
print(response.status_code)