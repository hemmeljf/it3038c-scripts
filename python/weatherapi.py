import json
import request

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=45828,us&appid=702944da871f8af97a2997bf8789b95f
')
data=r.json()
print(data)