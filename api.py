import requests
import tkinter as tk

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
    findPoke = fetch(input, "pokemon")
    findAbil = fetch(input, "ability")
    if findPoke == None:
        print("Did not find anything in Pokemon Database")
    else:
        print("Found search in Pokemon Database")
    if findAbil == None:
        print("Did not find anything in the Ability Database")
    else:
        print("Found search in Ability Database")

window = tk.Tk()
window.title("PokeAPI")
window.geometry("700x700")
window.resizable(True, True) ## window stuff

prompt = tk.Label(window, 
                  text="Press one of the below buttons to search for something Pokemon-related!!", 
                  font=("Arial", 14)) ## gives information on the application to user
prompt.pack(pady=10)
logLabel = tk.Label(window,
                    text=" ",
                    font=( "Arial", 14)) ## this tells the user if the search was successful or failed, as well as misc. errors
logLabel.pack(pady=12)
searchContinue = tk.Button(window, 
                         text="Search Abils / Mons", 
                         font=("Arial", 14), 
                         relief="raised", 
                         command=lambda:find(search.get())) ## button that the user presses to initiate the search
searchContinue.pack(pady=11)
search = tk.Entry(window,
                  font=("Arial", 14), 
                  width=40) ## where user types in the pokemon / ability they want to search for
search.pack(pady=10)
window.mainloop()


        
