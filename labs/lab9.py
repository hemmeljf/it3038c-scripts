import requests

url = 'http://localhost:3000'
response = requests.get(url)

if response.status_code == 200:
	data = response.json()
	for item in data:
		name = item['name']
		color = item['color']
		print(f"{name} is {color}.")
else:
	print(f"Data not found")