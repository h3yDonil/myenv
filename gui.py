import tkinter as tk
from tkinter import ttk
import bot_utils
import keyboard
import bot


class BotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Radio station player")
        master.geometry('400x250')
        master.attributes('-topmost', True)

        # Title label
        self.panel_name = ttk.Label(master, text="Control panel")
        self.panel_name.pack(pady=10)

        # Start/stop button
        self.toggle_button = ttk.Button(master, text="Press to start",
                                        command=self.toggle_bot)
        self.toggle_button.pack()
        keyboard.add_hotkey('page down', self.toggle_bot)

        # Connection status label
        self.connection_status = ttk.Label(master)
        self.connection_status.pack()
        self.update_connection_status()

        # 'Check connection' button
        self.check_connection_button = ttk.Button(master, text='Check arduino connection',
                                                  command=bot_utils.arduino_manager.init_serial)
        self.check_connection_button.pack()

    def toggle_bot(self):
        bot_utils.toggle_running_state()
        self.update_toggle_button()

    def update_toggle_button(self):
        if bot_utils.running:
            self.toggle_button.configure(text="Bot working")
        else:
            self.toggle_button.configure(text="Bot paused")

    def update_connection_status(self):
        if bot_utils.arduino_manager.connected:
            self.connection_status.configure(
                text=f'Connection to {bot_utils.config.COM_PORT} established successfully')
        else:
            self.connection_status.configure(
                text=f'Failed to connect to {bot_utils.config.COM_PORT}')


if __name__ == '__main__':
    root = tk.Tk()
    gui = BotGUI(root)
    bot.start_bot_thread()
    root.mainloop()
