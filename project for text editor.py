import tkinter as tk
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Python Files", "*.py"),
                                                   ("Text Files", "*.txt"),
                                                   ("All Files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write("Hello, world!")

root = tk.Tk()
root.title("Save File Example")

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

root.mainloop()