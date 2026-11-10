print("====api====")
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data)
print("===handaling api=====")
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    for user in data:
        print(user["name"])

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:
    print("API Error:", error)