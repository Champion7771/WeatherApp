import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

city = input('Enter city name: ')

url = f"http://api.weatherapi.com/v1/current.json?key=ff7c0f4861904fcba5b105815251304&q={city}"

r = requests.get(url)

# print(r.text)
# print(type(r.text))

wDict = json.loads(r.text)
print(wDict['location']['country'])
print(wDict['location']['name'])
# print(wDict['current']['temp_c'],"°C")
# print(wDict['current']['condition']['text'])
temp = wDict['current']['temp_c']
speak.speak(f"Current Temperature of {city} is {temp} °Celcius")