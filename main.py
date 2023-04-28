import requests

london = 'https://wttr.in/{city}'.format(city='London')
svo = 'https://wttr.in/svo'
cherepovec = 'https://wttr.in/{city}?MnqT'.format(city='Череповец')

payload = {'lang': 'ru'}

response_london = requests.get(london)
response_svo = requests.get(svo)
response_cherepovec = requests.get(cherepovec, params=payload)

print(response_london.text)
print(response_svo.text)
print(response_cherepovec.text)