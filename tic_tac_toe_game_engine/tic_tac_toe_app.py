from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict

from tic_tac_toe_game import TicTacToeGame
from tic_tac_toe_common_lib import TicTacToeGameInfo, TicTacToeTurn, UserInfo
from tic_tac_toe_app_abstract import AbstractTicTacToeApp

import random
import uuid

class TicTacToeApp(AbstractTicTacToeApp):
    def __init__(self):
        self._games: Dict[str, TicTacToeGame] = {}
        self._passwords: Dict[str, str] = {}

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        gid = str(random.randint(1, 9999))
        game = TicTacToeGame(gid, first_player_id, second_player_id)
        self._games[gid] = game
        return game.get_game_info()

    def get_game_by_id(self, game_id: str, user_id: str) -> TicTacToeGameInfo:
        return self._games[game_id].get_game_info()

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        self._games[game_id].do_turn(turn)
        return self._games[game_id].get_game_info()

    def add_user(self) -> UserInfo:
        name = str(uuid.uuid4())
        password = str(uuid.uuid4())
        self._passwords[name] = password
        return UserInfo(name, password)

    def is_autentified(self, user: UserInfo) -> bool:
        return self._passwords[user.user_id] == user.secret_key
