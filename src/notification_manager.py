import tkinter as tk
from tkinter import messagebox

def show_notification(title, message):
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    messagebox.showinfo(title, message)
    root.destroy()

def show_error(title, message):
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    messagebox.showerror(title, message)
    root.destroy()
