from random import uniform

import bot_utils
from bot_utils import (is_game_window_active,
                       is_alive_monster_in_target,
                       get_next_target,
                       attack, time)


def main():
    while True:
        if not bot_utils.running:
            print('not running')
            time.sleep(0.2)
            continue
        if is_game_window_active():
            if is_alive_monster_in_target():
                time.sleep(uniform(0.025, 0.036))
                attack()
            else:
                get_next_target()
                time.sleep(uniform(0.05, 0.1))

if __name__ == '__main__':
    main()
