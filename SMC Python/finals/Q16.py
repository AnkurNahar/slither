import tkinter as tk
from tkinter import messagebox

def show_song():
    song = entry.get().strip()
    if song:
        messagebox.showinfo("Your Song", f"{song}, {song}, {song}")
    else:
        messagebox.showwarning("Input Error", "Please enter your favorite song!")

root = tk.Tk()
root.title("Favorite Song App")
root.geometry("400x200")

label = tk.Label(root, text="Enter your favorite song:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Three", command=show_song, font=("Arial", 14), bg="lightblue")
button.pack(pady=10)

root.mainloop()