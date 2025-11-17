import requests
import tkinter as tk

window = tk.Tk()
window.title("PokeAPI")
window.geometry("400x250")
window.resizable(False, False)
prompt = tk.Label(window, 
                  text="Press one of the below buttons to search for something Pokemon-related!!", 
                  font=("Arial", 14))
prompt.pack(pady=10)
logLabel = tk.Label(window,
                    text=" ",
                    font=( "Arial", 14)) ## this tells the user if the search was successful or failed, as well as misc. errors
logLabel.pack(pady=12)
searchContinue = tk.Button(window, 
                         text="Search Abils / Mons", 
                         font=("Arial", 14), 
                         relief="raised", 
                         command=lambda:find())
searchContinue.pack(pady=11)
search = tk.Entry(window,
                  font=("Arial", 14), 
                  width=40)

window.mainloop()


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
def find(input):
    findPoke = Search.Pokemon(input)
    findAbil = Search.Ability(input)
    if findPoke and findAbil == None:
        logLabel.config(text="Error! Could not find what you were looking for in neither database.")
        
class Search:
    def Pokemon(byName):
        if fetch(byName, "pokemon") == None:
            print("Couldnt find: Pokemon")
            return None
        else:
            return fetch(byName)
    def Ability(byName):
        if fetch(byName, "ability") == None:
            print("Couldnt find: Ability")
            return None
        else:
            return fetch(byName, "ability")