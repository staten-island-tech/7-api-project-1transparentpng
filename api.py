import requests
import tkinter as tk
import platform
headers = {
    'User-Agent': f"OS: {platform.system()} {platform.release()} {platform.version()}"
}
print(headers)
def find():
    address = search.get().lower()
    print(f"Address Provided: {address}")
    response = requests.get(url=f"https://api.mcsrvstat.us/3/{address}", 
                            headers=headers)
    if response.status_code != 403:
        print("Error fetching data!")
        logLabel.config(text="An error occured: 403 Forbidden")
    else:
        print("Successfully got data")
        logLabel.config(text=f"Successfully got Data of {address.lower()}!")
    data = response.json()
    print(data)
    return {
        "online": data["online"],
        "ver": data["version"],
        "software": data["software"],
        "plyr": data["players"], ## this is a dict
        "plugins": data["plugins"], ## this is a dict
        "mods": data["mods"] ## this is a dict
        
    }


window = tk.Tk()
window.title("MC:J Server Status")
window.geometry("700x700")
window.resizable(True, True) ## window stuff

prompt = tk.Label(window, 
                  text="Java Server Address:", 
                  font=("Arial", 12))
prompt.pack(pady=2)
search = tk.Entry(window,
                  font=("Arial", 12), 
                  width=40) ## where user types in the server address they want to search for
search.pack(pady=1)
searchContinue = tk.Button(window, 
                         text="Search", 
                         font=("Arial", 14), 
                         relief="raised", 
                         command=lambda:find()) ## button that the user presses to initiate the search
searchContinue.pack(pady=2)
logLabel = tk.Label(window,
                    text="Test",
                    font=( "Arial", 12)) ## this tells the user if the search was successful or failed, as well as misc. errors
logLabel.pack(pady=2)
window.mainloop()


        
