
import requests
import json
from colorama import Fore, Back, Style
from secrets import riot_api

def get_champion_list(address):
    text = requests.get(address).text
    return text

address = "https://na1.api.riotgames.com/lol/platform/v3/champion-rotations"
champion_address = "http://ddragon.leagueoflegends.com/cdn/10.9.1/data/en_US/champion.json"
response = requests.get(address, headers = riot_api).text
free_rotation_data = json.loads(response)

champion_file = get_champion_list(champion_address)
champion_list = json.loads(champion_file)['data']
free_rotation_ids = free_rotation_data['freeChampionIds']
free_rotation = dict()

# print(champion_list)
for champ in champion_list:
    if int(champion_list[champ]['key']) in free_rotation_ids:
        free_rotation.setdefault(champ, champion_list[champ])

def print_champ(champion):
    print(Fore.RED + "-"*30 + Style.RESET_ALL)
    print(champion_list[champion]['id'] + ", " + champion_list[champion]['title'])
    print(Fore.RED + "-"*30 + Style.RESET_ALL)
    print("Attack: " + str(champion_list[champion]['info']['attack']))
    print("Defense: " + str(champion_list[champion]['info']['defense']))
    print("Magic: " + str(champion_list[champion]['info']['magic']))
    print("Difficulty: " + str(champion_list[champion]['info']['difficulty']))
    print("Classes: ", end = "")
    for i in range(len(champion_list[champion]['tags'])):
        print(champion_list[champion]['tags'][i], end = " ")
    print("\nHitpoints: " + Fore.RED + str(champion_list[champion]['stats']['hp']) + Style.RESET_ALL + "\t\t\t" + "Mana: " + Fore.BLUE + str(champion_list[champion]['stats']['mp']) + Style.RESET_ALL + "\t" + "Movement Speed: " + Fore.WHITE + str(champion_list[champion]['stats']['movespeed']) + Style.RESET_ALL)
    print("Hitpoints per level: " + Fore.RED + str(champion_list[champion]['stats']['hpperlevel']) + Style.RESET_ALL + "\t" + "Mana per level: " + Fore.BLUE + str(champion_list[champion]['stats']['mpperlevel']) + Style.RESET_ALL)
    print("Health Regeneration: " + Fore.GREEN + str(champion_list[champion]['stats']['hpregen']) + Style.RESET_ALL + "\t\t\t" + "Mana Regeneration: " + Fore.CYAN + str(champion_list[champion]['stats']['mpregen']) + Style.RESET_ALL)
    print("Health Regeneration per level: " + Fore.GREEN + str(champion_list[champion]['stats']['hpregenperlevel']) + Style.RESET_ALL + "\t" + "Mana Regeneration per level: " + Fore.CYAN + str(champion_list[champion]['stats']['mpregenperlevel']) + Style.RESET_ALL)
    print("Armor: " + Fore.YELLOW + str(champion_list[champion]['stats']['armor']) + Style.RESET_ALL + "\t\t" + "Armor per level: " + Fore.YELLOW + str(champion_list[champion]['stats']['armorperlevel']) + Style.RESET_ALL)
    print("Magic Resist: " + Fore.MAGENTA + str(champion_list[champion]['stats']['spellblock']) + Style.RESET_ALL + "\t" + "Magic Resist per level: " + Fore.MAGENTA + str(champion_list[champion]['stats']['spellblockperlevel']) + Style.RESET_ALL)
    print("Crit Chance: " + Fore.YELLOW + str(champion_list[champion]['stats']['crit']) + Style.RESET_ALL + "\t\t" + "Crit Chance per level: " + Fore.YELLOW + str(champion_list[champion]['stats']['critperlevel']) + Style.RESET_ALL)
    print("Attack Damage: " + Fore.RED + str(champion_list[champion]['stats']['attackdamage']) + Style.RESET_ALL + "\t" + "Attack Damage per level: " + Fore.RED + str(champion_list[champion]['stats']['attackdamageperlevel']) + Style.RESET_ALL)
    print("Attack Speed: " + Fore.GREEN + str(champion_list[champion]['stats']['attackspeed']) + Style.RESET_ALL + "\t" + "Attack Speed per level: " + Fore.GREEN + str(champion_list[champion]['stats']['attackspeedperlevel']) + Style.RESET_ALL)

# print(free_rotation)

for i in free_rotation:
    print_champ(i)

# print_champ("Aatrox")