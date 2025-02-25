import time
from bot_utils import *

while True:
    if not running:
        time.sleep(0.1)
        continue 
    if is_game_window_active():
        if is_monster_alive:
            time.sleep(random_delay1) #25ms
            attack()
            time.sleep(random_delay1) #25ms
        else:
            time.sleep(random_delay1) #25ms
            get_next_target()