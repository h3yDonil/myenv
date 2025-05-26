import time
from random import uniform
import bot_utils
from bot_utils import (is_game_window_active,
                       target_manager,
                       attack, )
import threading


def run_bot():
    while True:
        if not bot_utils.running:
            time.sleep(0.2)
            continue

        if is_game_window_active():
            if target_manager.is_alive_monster_in_target():
                time.sleep(uniform(0.025, 0.036))
                attack()
                time.sleep(uniform(0.32, 0.55))
                print('attacking')
            else:
                target_manager.get_next_target()
                time.sleep(uniform(0.05, 0.1))


def start_bot_thread():
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()


if __name__ == '__main__':
    run_bot()
