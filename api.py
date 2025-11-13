import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }


def searchMon(byName):
    if getPoke(byName) == None:
        print("Sorry, I couldnt find the Pokemon Specified. Did you enter the name correctly?")
    else:
        pokemon = getPoke(byName)
        for key, value in pokemon.items:
            print({key.title()}) ## continue here


searchMon("Ditto")