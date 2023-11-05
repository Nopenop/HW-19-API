import tkinter as tk
import requests
import tools_config

#configuration for information within loop
route_info = tools_config.Path()
info = requests.get(route_info.route).json()
cpu = info["CPU"]
memory = info["memory"]
disk = info["disk"]
root = tk.Tk()
root.update()

# Create the main window
root.title("system monitor")

#refreshes the information on the buttoms
def refresh() -> None:
    route_info = tools_config.Path()
    info = requests.get(route_info.route).json()
    cpu = info["CPU"]
    memory = info["memory"]
    disk = info["disk"]
    cpu_info.config(text=f"CPU Usage %: {cpu}")
    disk_info.config(text=f"Memory Usage %: {memory}")
    mem_info.config(text=f"Disk Usage %: {disk}")

#labels are global to configure upon refresh call
global cpu_info
global disk_info
global mem_info

# Creates a label with cpu usage
cpu_info = tk.Label(root, text=f"CPU Usage %: {cpu}")
cpu_info.pack(padx=20, pady=20)
# Creates a label with disk usage
disk_info = tk.Label(root, text=f"Disk Usage %: {memory}")
disk_info.pack(padx=20, pady=20)
# Creates a label with memory usage
mem_info = tk.Label(root, text=f"Mem Usage %: {disk}")
mem_info.pack(padx=20, pady=20)

#creates button that call refresh function
refresh_button = tk.Button(root, text="Refresh", command = refresh)
refresh_button.pack(padx=20, pady=20)




# Starts tkinter main loop
root.mainloop()