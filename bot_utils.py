from PIL import ImageGrab
import serial
import time
import random
import keyboard
import pygetwindow as gw

ser = serial.Serial('COM6', 9600)
time.sleep(2)

random_delay1 = random.uniform(0.025, 0.036)
random_delay2 = random.uniform(1.5, 0.6)
target_window_title = "ТемнаяЭльфийка"  
hp_pixel_color = (134,31,20)
pixel_coordinates = (905,35)
def get_pixel_color(x,y):
    """Get the color of the pixel at the specified coordinates"""
    screen = ImageGrab.grab()
    return screen.getpixel((x,y))

running = True
def toggle_running():
    global running
    running = not running

keyboard.add_hotkey('page down',toggle_running)

def is_game_window_active():
    """Check if the target game windows is currently active"""
    active_window = gw.getActiveWindow()
    return active_window and target_window_title in active_window.title

def is_monster_alive():
    """Check if monster is alive by comparing pixel color"""
    return get_pixel_color(*pixel_coordinates) == hp_pixel_color

def attack():
    """Send to serial port attack commands"""
    ser.write(b'3') 
    ser.write(b'2') 

def get_next_target():
    ser.write(b'4')