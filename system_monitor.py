import tkinter as tk
import requests

def button_press():
    print("hello world")

info = requests.get("http://127.0.0.1:8000").json()
cpu = info["CPU"]
memory = info["memory"]
disk = info["disk"]
# Create the main window
root = tk.Tk()
root.title("system monitor")

# Create a label with the "Hello, World!" message
cpu_info = tk.Label(root, text=f"CPU Usage %: {cpu}")
cpu_info.pack(padx=20, pady=20)

disk_info = tk.Label(root, text=f"Disk Usage %: {memory}")
disk_info.pack(padx=20, pady=20)

mem_info = tk.Label(root, text=f"Mem Usage %: {disk}")
mem_info.pack(padx=20, pady=20)


refresh_button = tk.Button(root, text="Refresh", command = button_press)
refresh_button.pack(padx=20, pady=20)




# Start the tkinter main loop
root.mainloop()