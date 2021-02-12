'''
создать партию
сделать ход
получить информацию о партии
зарегистрироваться
'''
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict

from .tic_tac_toe_game import TicTacToeGame
from .tic_tac_toe_common_lib import TicTacToeGameInfo, UserInfo, TicTacToeTurn

class AbstractTicTacToeApp(ABC):
    @abstractmethod
    def __init__(self):
        self._games: Dict[str, TicTacToeGame] = {}
        self._passwords: Dict[str, str] = {}

    @abstractmethod
    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        """создаём игру, кладём в словарик (или другую вашу любимую коллекцию) с играми"""

    @abstractmethod
    def get_game_by_id(self, game_id: str, user_id: str) -> TicTacToeGameInfo:
        """получаем игру, отдавать нужно только если юзер с таким user_id реально в неё играет,
        но проверку секретного ключа пользователя нужно делать в обработчиках запросов,
        а не здесь, но здесь мы реализуем методы, которые в этом помогут"""

    @abstractmethod
    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        pass

    @abstractmethod
    def add_user(self) -> UserInfo:
        """регистрация"""
    
    @abstractmethod
    def is_autentified(self, user: UserInfo) -> bool:
        """проверка авторизации""" 

# https://colab.research.google.com/drive/192uqXymmzi5J-YxUOj-ldSNePP5dHdWZ
