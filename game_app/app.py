from typing import Dict
import uuid

from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn


class TicTacToeApp:
    def __init__(self):
        self._games: Dict[str, TicTacToeGame] = {}

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        gid = str(uuid.uuid4())
        game = TicTacToeGame(gid, first_player_id, second_player_id)
        self._games[gid] = game
        return game.get_game_info()

    def get_game_by_id(self, game_id: str) -> TicTacToeGameInfo:
        return self._games[game_id].get_game_info()

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        self._games[game_id].do_turn(turn)
        return self._games[game_id].get_game_info()
