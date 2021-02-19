from .tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame
from typing import Callable, List, Optional
from copy import deepcopy

class TicTacToeGame(AbstractTicTacToeGame):

    def __init__(self, game_id: str, first_player_id: str, second_player_id: str) -> None:
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__winner_id = ""
        self.__turns: List[TicTacToeTurn] = []

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if 0 <= turn.x_coordinate <= 2 and 0 <= turn.y_coordinate <= 2 and self.get_game_info().field[turn.x_coordinate][turn.y_coordinate] == " " and self.__winner_id == "":
            if turn.player_id == self.__first_player_id:
                if len(self.__turns) % 2 == 0:
                    return True
            elif turn.player_id == self.__second_player_id:
                if len(self.__turns) % 2 == 1:
                    return True
        return False

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn) == True:
            if turn.player_id == self.__first_player_id:
                self.get_game_info().field[turn.x_coordinate][turn.y_coordinate] = "X"
            elif turn.player_id == self.__second_player_id:
                self.get_game_info().field[turn.x_coordinate][turn.y_coordinate] = "O"
            self.__turns.append(turn)
            self.check_winner(turn, self.__first_player_id)
            self.check_draw()
        return self.get_game_info()

    def check_winner(self, turn: TicTacToeTurn, player_id: str) -> None:
        for i in self.get_game_info().field:
            if self.get_game_info().field[turn.x_coordinate][turn.y_coordinate] == i[0] == i[1] == i[2] != " ":
                self.__winner_id = player_id
        for j in range(0, 3):
            if self.get_game_info().field[turn.x_coordinate][turn.y_coordinate] == self.get_game_info().field[0][j] == self.get_game_info().field[1][j] == self.get_game_info().field[2][j] != " ":
                self.__winner_id = player_id
        if self.get_game_info().field[turn.x_coordinate][turn.y_coordinate] == self.get_game_info().field[0][0] == self.get_game_info().field[1][1] == self.get_game_info().field[2][2] != " ":
            self.__winner_id = player_id
        if self.get_game_info().field[turn.x_coordinate][turn.y_coordinate] == self.get_game_info().field[0][2] == self.get_game_info().field[1][1] == self.get_game_info().field[2][0] != " ":
            self.__winner_id = player_id

    def check_draw(self) -> None:
        draw = True
        for row in self.get_game_info().field:
            if "O" not in row or "X" not in row:
                draw = False
        for j in range(0, 3):
            row = []
            row.append(self.get_game_info().field[0][j])
            row.append(self.get_game_info().field[1][j])
            row.append(self.get_game_info().field[2][j])
            if "O" not in row or "X" not in row:
                draw = False
        row = []
        row.append(self.get_game_info().field[0][0])
        row.append(self.get_game_info().field[1][1])
        row.append(self.get_game_info().field[2][2])
        if "O" not in row or "X" not in row:
            draw = False
        row = []
        row.append(self.get_game_info().field[0][2])
        row.append(self.get_game_info().field[1][1])
        row.append(self.get_game_info().field[2][0])
        if "O" not in row or "X" not in row:
            draw = False
        if draw == True:
            self.__winner_id = "draw"

    def get_game_info(self) -> TicTacToeGameInfo:
        result = TicTacToeGameInfo(
            game_id=self.__game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=deepcopy(self.__turns),
            first_player_id=self.__first_player_id,
            second_player_id=self.__second_player_id,
            winner_id=self.__winner_id
        )
        for turn in self.__turns:
            if turn.player_id == self.__first_player_id:
                ch = "X"
            else:
                ch = "O"
            result.field[turn.x_coordinate][turn.y_coordinate] = ch
        return result
