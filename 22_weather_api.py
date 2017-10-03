import requests

city = input('Please enter your city: ')
temp = input('Temperature in C or F: ').lower()


package = {
    'APPID': "2647af5e60e858b815b30696368b470a",
    'q': city
}

r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

data = r.json()

if temp == 'c':
    temp = round(int(data['main']['temp']) - 273.15)
elif temp == 'f':
    temp = round(int(data['main']['temp']) * (9/5) - 459.67)

print('Temperature: {}'.format(temp))
print('Wind direction: {} degrees'.format(data['wind']['deg']))
print('Current condition: {}'.format(data['weather'][0]['description']))
