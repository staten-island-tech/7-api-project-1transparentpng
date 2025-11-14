import requests
import tkinter as tk

window = tk.Tk()
window.title = "PokeAPI"
window.geometry("400x250")
window.resizable(False, False)
prompt = tk.Label(window, text="Press one of the below buttons to search for a specific thing in regards to Pokemon.", font=("Arial", 14))
prompt.pack(pady=10)
reverse_button = tk.Button(window, text="Search for a Pokemon", font=("Arial", 14), command=searchMon())

def fetch(poke, searchfor):
    if searchfor.lower() == "pokemon":
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    elif searchfor.lower() == "ability":
        response = requests.get(f"https://pokeapi.co/api/v2/ability/{poke.lower()}")
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
    if fetch(byName) == None:
        print("Sorry, I couldnt find the Pokemon Specified. Did you enter the name correctly?")
    else:
        pokemon = fetch(byName)
        for key, value in pokemon.items():
            print(f"{key.title()}: {value}")
def searchAbility(byName):
    if fetch(byName, "ability") == None:
        print("Sorry, I couldnt find the Ability Specified. Did you enter the name correctly?")
    else:
        abil = fetch(byName, "ability")
        for key, value in abil.items():
            print(f"{key.title()}: {value}")