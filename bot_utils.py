from serial_handler import ArduinoManager
from PIL import ImageGrab
import pygetwindow as gw
import config
import time
from random import uniform

class TargetManager:
    def __init__(self):
        self.last_target_change_time = 0  # When target was changed last time
        self.target_timeout = 20  # Seconds to wait before changing target
        # if target is still alive
        self.target_fullhp_timeout = uniform(2.5, 3) # Seconds to wait before changing target
        # if hp remains full
        self.current_target_stale = False  # Flag for tracking target state

    def is_alive_monster_in_target(self):
        """Check if monster is alive by comparing last left pixel color"""
        return self.get_pixel_color(*config.LEFT_HP_PIXEL_COORDINATES) == config.LEFT_HP_PIXEL_COLOR

    def is_target_hp_full(self):
        """Check if monster's hp is full comparing last right pixel color"""
        return self.get_pixel_color(*config.RIGHT_HP_PIXEL_COORDINATES) == config.RIGHT_HP_PIXEL_COLOR

    def get_pixel_color(self, x, y):
        """Get the color of the pixel at the specified coordinates"""
        screen = ImageGrab.grab()
        return screen.getpixel((x, y))

    def get_next_target(self):
        """Send to serial port byte representation for specified characters """
        arduino_manager.write_data(b'4')
        self.last_target_change_time = time.time()
        self.current_target_stale = False
        print('Attempting to get target...')

    def should_change_target(self):
        current_time = time.time()
        time_since_last_target_change = current_time - self.last_target_change_time

        hp_full_for_too_long = (self.is_target_hp_full() and
                                time_since_last_target_change >= self.target_fullhp_timeout)

        absolute_timeout_reached = time_since_last_target_change >= self.target_timeout

        self.current_target_stale = hp_full_for_too_long or absolute_timeout_reached

        return self.current_target_stale


running = False
target_manager = TargetManager()
arduino_manager = ArduinoManager()


def toggle_running_state():
    """Toggle the running state of the program
    
    This function changes the value of the global variable 'is_running' to
    its opposite. If 'running' currently True, it will be set to False,
    and vice versa. It allows the program to start and stop based on user input."""
    global running
    running = not running
    print(f'page down pressed, running = {running}')


def is_game_window_active():
    """Check if the target game windows is currently active"""
    active_window = gw.getActiveWindow()
    return active_window and config.TARGET_WINDOW_TITLE in active_window.title


def attack():
    """Send to serial port byte representation for specified characters """
    arduino_manager.write_data(b'3')
