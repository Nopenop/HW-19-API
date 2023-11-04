import tkinter as tk
import remote_api

def button_test():
    print("Button worked")

# Create the main window
root = tk.Tk()
root.title("system monitor")

# Create a label with the "Hello, World!" message
cpu_info = tk.Label(root, text=f"CPU Usage %: {remote_api.test()}")
cpu_info.pack(padx=20, pady=20)

disk_info = tk.Label(root, text=f"Disk Usage %: {remote_api.test()}")
disk_info.pack(padx=20, pady=20)

mem_info = tk.Label(root, text=f"Mem Usage %: {remote_api.test()}")
mem_info.pack(padx=20, pady=20)


refresh_button = tk.Button(root, text="Refresh", command = button_test)
refresh_button.pack(padx=20, pady=20)




# Start the tkinter main loop
root.mainloop()