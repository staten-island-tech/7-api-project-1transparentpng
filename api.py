import requests
import tkinter as tk

def fetch(address):
    response = requests.get(f"https://api.mcsrvstat.us/3/{address.lower()}")
    if response.status_code != 403:
        print("Error fetching data!")
        return 403
    
    data = response.json()
    return {
        "online": data["online"],
        "ver": data["version"],
        "software": data["software"],
        "plyr": data["players"], ## this is a dict
        "plugins": data["plugins"] ## this is a dict
        
    }
def find(input):
    server = fetch(input)
    if server == 403:
        print("ERROR: 403 forbidden")
        logLabel.config(text="An unexpected error occured whilst processing: 403 Forbidden")
    elif server =

window = tk.Tk()
window.title("MC:J Server Status")
window.geometry("700x700")
window.resizable(True, True) ## window stuff

prompt = tk.Label(window, 
                  text="Java Server Address:", 
                  font=("Arial", 12))
prompt.pack(pady=3)
logLabel = tk.Label(window,
                    text=" ",
                    font=( "Arial", 14)) ## this tells the user if the search was successful or failed, as well as misc. errors
logLabel.pack(pady=1)
search = tk.Entry(window,
                  font=("Arial", 12), 
                  width=40) ## where user types in the server address they want to search for
search.pack(pady=1)
searchContinue = tk.Button(window, 
                         text="Search", 
                         font=("Arial", 14), 
                         relief="raised", 
                         command=lambda:find(search.get())) ## button that the user presses to initiate the search
searchContinue.pack(pady=1)
window.mainloop()


        
