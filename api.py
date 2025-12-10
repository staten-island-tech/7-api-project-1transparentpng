import requests
import tkinter as tk
import platform
headers = {
    'User-Agent': f"OS: {platform.system()} {platform.release()} {platform.version()}"
}
print(headers)
def find():
    address = search.get().lower()
    print(f">> >{address}<")
    if address == "":
        print("No Address Specified!")
        logLabel.config(text="You did not specify a server address!")
        return
    elif "." not in address:
        print("Invalid address detected!")
        logLabel.config(text="The specified server address is invalid!")
        return
    print(f"Address Provided: {address}")
    response = requests.get(url=f"https://api.mcsrvstat.us/3/{address.lower()}", headers=headers)
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
    else:
        isOnline.config(text="Online: NO")
        serverVersion.config(text=f"Server Version: N/A")
        serverSoftware.config(text=f"Server Software: N/A")
        serverPlayers.config(text="Players: ? / ?")
window = tk.Tk()
window.title("MC:J Server Status")
window.geometry("600x400")
window.resizable(False, False) ## window stuff

prompt = tk.Label(window, 
                  text="Java Server Address:", 
                  font=("Bahnschrift", 16))
prompt.pack(pady=2)
search = tk.Entry(window,
                  font=("Bahnschrift", 14), 
                  width=40) ## where user types in the server address they want to search for
search.pack(pady=1)
searchContinue = tk.Button(window, 
                         text="Search", 
                         font=("Bahnschrift", 14), 
                         relief="raised", 
                         command=lambda:find()) ## button that the user presses to initiate the search
searchContinue.pack(pady=2)
logLabel = tk.Label(window,
                    text="Enter a java server address to see information about a server!",
                    font=( "Bahnschrift", 12)) ## this tells the user if the search was successful or failed, as well as misc. errors
logLabel.pack(pady=10)
isOnline = tk.Label(window,
                    text="Online: N/A",
                    font=("Bahnschrift", 12)) ## set to N/A as default, will change after a sucessful search
isOnline.pack(pady=1)
serverVersion = tk.Label(window,
                         text="Server Version: N/A",
                         font=("Bahnschrift", 12))
serverVersion.pack(pady=1)
serverSoftware = tk.Label(window,
                          text="Server Software: N/A",
                          font=("Bahnschrift", 12))
serverSoftware.pack(pady=1)
serverPlayers = tk.Label(window,
                         text="Players: ? / ?",
                         font=("Bahnschrift", 12),
                         width=60)
serverPlayers.pack(pady=1)
window.mainloop()


        
