import requests
import pandas as pd

# завдання 1
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі реального часу)
print("############ Task1 ############")
req = requests.get('http://api.open-notify.org/astros.json')
people = req.json()['people']
pd_people = pd.DataFrame(people)
print(pd_people)

# завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv, london)
# погода змінюється, як і місто. яке ви введете
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране
print("############ Task2 ############")
api_key = '47503e85fabbabc93cff28c52398ae97'
city_name = input('Enter city name: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
req = requests.get(url)
weather = req.json()
print(f'Temperature in {city_name.capitalize()} is {weather["main"]["temp"]} C')
print(f'Wind speed in {city_name.capitalize()} is {weather["wind"]["speed"]} m/s')