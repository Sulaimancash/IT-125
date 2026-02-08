import random
import time

class RussianRouletteGame:
    def __init__(self, player1: str, player2: str, turn_time: int = 5):
        self.players = [player1, player2]
        self.current_player = 0

        self.chambers = [0, 0, 0, 0, 0, 1]
        random.shuffle(self.chambers)

        self.current_index = 0
        self.turn_time = turn_time
        self.last_turn_time = time.time()
        self.is_active = True

    def get_current_player(self):
        return self.players[self.current_player]

    def _time_over(self):
        return time.time() - self.last_turn_time > self.turn_time

    def shoot(self):
        if not self.is_active:
            return "game_over"

        if self._time_over():
            self.is_active = False
            return "time_over"

        if self.current_index >= len(self.chambers):
            self.is_active = False
            return "no_bullets"

        bullet = self.chambers[self.current_index]
        self.current_index += 1

        if bullet == 1:
            self.is_active = False
            return "boom"

        self.current_player = 1 - self.current_player
        self.last_turn_time = time.time()
        return "click"
