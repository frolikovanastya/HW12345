import requests

heroes = ['Hulk', 'Captain America', 'Thanos']

max_intelligence = 0
smartest_hero = ''

for hero in heroes:
    response = requests.get(f'https://akabab.github.io/superhero-api/api/id/{hero}.json')
    data = response.json()
    intelligence = int(data['powerstats']['intelligence'])
    if intelligence > max_intelligence:
        max_intelligence = intelligence
        smartest_hero = hero

print(f'The smartest superhero is {smartest_hero} with intelligence of {max_intelligence}')