from pprint import pprint
import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
heroes = response.json()
# pprint(data)
heroes_dict = {}
for hero in heroes:
    if hero["name"] in ["Hulk", "Captain America", "Thanos"]:
        heroes_dict[hero["name"]] = hero

max_intelligence = -1
smart_hero = ""
for hero_name, hero_data in heroes_dict.items():
    intelligence = int(hero_data["powerstats"]["intelligence"])
    if intelligence > max_intelligence:
        max_intelligence = intelligence
        smart_hero= hero_name
print("Самый умный герой:", smart_hero)

