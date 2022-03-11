import requests

results = requests.get('https://jsonplaceholder.typicode.com/users')

print(results.json())