import tkinter as tk
from tkinter import ttk, font
import bot_utils
import keyboard

class BotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Radio station player")
        master.geometry('800x500')
        
        # Title label
        self.label = ttk.Label(master, text="Control panel")
        self.label.pack(pady=10)

        # Start/stop button
        self.toggle_button = ttk.Button(master, text="Press to start", 
                                        command=self.toggle_bot)
        self.toggle_button.pack()
        keyboard.add_hotkey('page down', self.toggle_bot)

    def toggle_bot(self):
        bot_utils.toggle_running_state()
        self.update_button_text()

    def update_button_text(self):
        if bot_utils.running:
            self.toggle_button.configure(text="running")
        else:
            self.toggle_button.configure(text="paused")

            
if __name__ == '__main__':
    root = tk.Tk()
    gui = BotGUI(root)
    root.mainloop()
