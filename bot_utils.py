import serial
import time
from PIL import ImageGrab
import pygetwindow as gw
import config

# Initialize the serial connection and pause execution
# for 2 second to allow the serial connection to establish properly

ser = serial.Serial(config.COM_PORT, config.BAUD_RATE)
time.sleep(2)

running = False


def toggle_running_state():
    """Toggle the running state of the program
    
    This function changes the value of the global variable 'is_running' to
    its opposite. If 'running' currently True, it will be set to False,
    and vice versa. It allows the program to start and stop based on user input."""
    global running
    running = not running
    print(f'page down pressed, running = {running}')


def get_pixel_color(x, y):
    """Get the color of the pixel at the specified coordinates"""
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))


def is_game_window_active():
    """Check if the target game windows is currently active"""
    active_window = gw.getActiveWindow()
    return active_window and config.TARGET_WINDOW_TITLE in active_window.title


def is_alive_monster_in_target():
    """Check if monster is alive by comparing pixel color"""
    return get_pixel_color(*config.PIXEL_COORDINATES) == config.HP_PIXEL_COLOR


def attack():
    """Send to serial port byte representation for specified characters """
    ser.write(b'3')


def get_next_target():
    """Send to serial port byte representation for specified characters """
    ser.write(b'4')
