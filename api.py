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
    response = requests.get(url=f"https://api.mcsrvstat.us/3/{address.lower()}", 
                            headers=headers)
    if response.status_code == 403:
        print("Error fetching data! 403")
        logLabel.config(text="An error occured: 403 Forbidden")
    else:
        print("Successfully got data")
        logLabel.config(text=f"Successfully got Data of {address.lower()}!")
    data = response.json()
    print(data)
    if data["online"] == True:
        isOnline.config(text="Online: YES")
        serverVersion.config(text=f"Server Version: {data["version"]}")
        serverSoftware.config(text=f"Server Software: {data["software"]}")
        return {
            "ip": data["ip"],
            "online": data["online"],
            "ver": data["version"],
            "software": data["software"], 
            "maxplyrs": data["players"]["max"],
            "onlineplyrs": data["players"]["online"], ## for dict lists, do data['players']['list'][1]['name']   
        }
    else:
        return {
            "online": data["online"]
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
serverPlayers = tk.Label(window,
                         text="Players: ? / ?",
                         font=("Arial", 10))
serverPlayers.pack(pady=1)
window.mainloop()


        
