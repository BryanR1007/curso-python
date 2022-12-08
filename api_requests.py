import requests

#URL de la api. ejemplo breaking bad
response = requests.get(
    'https://www.breakingbadapi.com/api/characters/', 
    params={'category': 'Better+call+saul'},
    headers={'Accept': 'aplication/json'}
) 
requests.post('url', data={'key': 'value'})

print(response.status_code)
#print(response.json())
walter = response.json()[0]
print(walter['name'])
print(walter['birthday'])

print(response.headers)

