import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url)
    response.raise_for_status()

    print("Status code:", response.status_code)
    print("User:", response.json()["name"])

except requests.exceptions.HTTPError:
    print("The request failed because the HTTP response indicates an error.")

#another type of exception handling
'''import requests

url = "https://jsonplaceholder.typicode.com/users/999999"

try:
    response = requests.get(url)
    response.raise_for_status()

    print("Status code:", response.status_code)
    print("User:", response.json()["name"])

except requests.exceptions.ConnectionError:
    print("The request failed because the server could not be reached.")'''


#for multiple types of exceptions, we can use multiple except blocks
'''import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

except requests.exceptions.ConnectionError:
    print("Could not connect to the server.")

except requests.exceptions.Timeout:
    print("The request took too long.")

except requests.exceptions.HTTPError:
    print("The server returned an HTTP error.")'''
