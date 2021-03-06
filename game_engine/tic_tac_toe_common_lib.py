from abc import ABC, abstractmethod, abstractproperty
from typing import List, Callable
from dataclasses import dataclass


@dataclass
class TicTacToeTurn:
    player_id: str
    x_coordinate: int
    y_coordinate: int


@dataclass
class TicTacToeGameInfo:
    game_id: str
    field: List[List[str]]
    sequence_of_turns: List[TicTacToeTurn]
    first_player_id: str
    second_player_id: str
    winner_id: str


@dataclass
class UserInfo:
    user_id: str
    secret_key: str


class AbstractTicTacToeGame(ABC):
    @abstractmethod
    def __init__(self, game_id: str, first_player_id: str, second_player_id: str) -> None:
        """пока просто раскладываем по полям"""

    @abstractmethod
    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        """подумайте, когда использовать"""

    @abstractmethod
    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        """сначала проверяем корректность, для проверки используйте is_turn_correct,
        а возвращаем TicTacToeGameInfo"""

    @abstractproperty
    def get_game_info(self) -> TicTacToeGameInfo:
        """обычный геттер"""

# https://colab.research.google.com/drive/1EU8d5N4BupCAcoauf2coB_tZWaSYXWGv#scrollTo=amlz9_ZA8am4
# https://github.com/DarkSquirrelComes/tic-tac-toe-9000-tasks/blob/main/game_engine_test.py