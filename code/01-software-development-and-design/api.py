# Utilizing fakestoreapi.com for API practice

import requests

response = requests.get("https://fakestoreapi.com/products")

print(response) #prints <Response[200]>
print(response.json()) #prints a large dictionary