import requests
import tkinter as tk
import platform
headers = {
    'User-Agent': f"OS: {platform.system()} {platform.release()} {platform.version()}"
}
pluginList = []
print(headers)
def find():
    pluginList = [] ## clears the plugin list
    address = search.get().lower()
    print(f">> >{address}<")
    if address == "":
        print("No Address Specified!")
        logLabel.config(text="You did not specify a server address!")
        return
    elif address. ## continue here
    print(f"Address Provided: {address}")
    response = requests.get(url=f"https://api.mcsrvstat.us/3/{address.lower()}", 
                            headers=headers)
    print(response.status_code)
    if response.status_code == 403:
        print("Error fetching data! 403")
        logLabel.config(text="An error occured: 403 Forbidden")
    elif response.status_code == 200:
        print("Successfully got data")
        logLabel.config(text=f"Successfully got Data of {address.lower()}!")
    elif response.status_code == 404:
        print(f"Could not find {address}, 404")
        logLabel.config(text=f"Could not find the specified Server Address. Did you type it correctly?")
    else:
        print(f"An Error Occured: {response.status_code}")
        logLabel.config(text=f"An error occured: {response.status_code}")
    data = response.json()
    print(data)
    if data["online"] == True:
        isOnline.config(text="Online: YES")
        serverVersion.config(text=f"Server Version: {data["version"]}")
        serverSoftware.config(text=f"Server Software: {data["software"]}")
        serverPlayers.config(text=f"Players: {data["players"]["online"]} / {data["players"]["max"]}")       
        for i in data["plugins"]:
            pluginList.append(i["name"]) 
            print(f"found plugin {i["name"]}, appending to list")
        serverPlugins.config(text=f"Installed Plugins: {pluginList}")
    else:
        isOnline.config(text="Online: NO")
        serverVersion.config(text=f"Server Version: N/A")
        serverSoftware.config(text=f"Server Software: N/A")
        serverPlayers.config(text="Players: ? / ?")
        serverPlugins.config(text=f"Installed Plugins: N/A")

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
logLabel.pack(pady=10)
isOnline = tk.Label(window,
                    text="Online: N/A",
                    font=("Arial", 10)) ## set to N/A as default, will change after a sucessful search
isOnline.pack(pady=1)
serverVersion = tk.Label(window,
                         text="Server Version: N/A",
                         font=("Arial", 10))
serverVersion.pack(pady=1)
serverSoftware = tk.Label(window,
                          text="Server Software: N/A",
                          font=("Arial", 10))
serverSoftware.pack(pady=1)
serverPlugins = tk.Label(window,
                         text="Installed Plugins: N/A",
                         font=("Arial", 10),
                         wraplength=400)
serverPlugins.pack(pady=1)
serverPlayers = tk.Label(window,
                         text="Players: ? / ?",
                         font=("Arial", 10),
                         width=60)
serverPlayers.pack(pady=1)
window.mainloop()


        
