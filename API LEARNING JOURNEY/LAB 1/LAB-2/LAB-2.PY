import requests
url ="https://jsonplaceholder.typicode.com/users/999999" 
# response.raise_for_status()-This will raise an error if the request failed so the next lines never print
response = requests.get(url)
response.raise_for_status()
print(response.status_code)
print(response.json()["name"])