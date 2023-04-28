import requests

payload = {'lang': 'ru'}

cherepovec = 'https://wttr.in/{city}?MnqT'.format(city='Череповец')
response = requests.get(cherepovec, params=payload)

print(response.text)
