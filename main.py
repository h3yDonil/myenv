import time
from bot_utils import *

init_serial()

while True:
    if not is_running:
        time.sleep(0.1)
        continue 
    if is_game_window_active():
        if is_alive_monster_in_target():
            actions_delay(0.025,0.036)
            attack()
        else:
            get_next_target()