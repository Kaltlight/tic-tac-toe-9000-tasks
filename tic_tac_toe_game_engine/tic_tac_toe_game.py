from tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame
from copy import deepcopy

class TicTacToeGame(AbstractTicTacToeGame):

    def __init__(self, game_id: str, first_player_id: str, second_player_id: str) -> None:
        self.game = TicTacToeGameInfo(game_id = game_id, field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], sequence_of_turns = [], first_player_id = first_player_id, second_player_id = second_player_id, winner_id = "")
        return None

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if 0 <= turn.x_coordinate <= 2 and 0 <= turn.y_coordinate <= 2 and self.game.field[turn.x_coordinate][turn.y_coordinate] == " " and self.game.winner_id == "":
            if turn.player_id == self.game.first_player_id:
                if len(self.game.sequence_of_turns) % 2 == 0:
                    return True
            elif turn.player_id == self.game.second_player_id:
                if len(self.game.sequence_of_turns) % 2 == 1:
                    return True
        return False

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn) == True:
            if turn.player_id == self.game.first_player_id:
                self.game.field[turn.x_coordinate][turn.y_coordinate] = "X"
                self.check_winner(turn, self.game.first_player_id)
                self.check_draw()
            elif turn.player_id == self.game.second_player_id:
                self.game.field[turn.x_coordinate][turn.y_coordinate] = "O"
                self.check_winner(turn, self.game.second_player_id)
                self.check_draw()
            self.game.sequence_of_turns.append(turn)
        return deepcopy(self.game)

    def check_winner(self, turn: TicTacToeTurn, player_id: str) -> None:
        for i in self.game.field:
            if self.game.field[turn.x_coordinate][turn.y_coordinate] == i[0] == i[1] == i[2]:
                self.game.winner_id = player_id
        for j in range(0, 3):
            if self.game.field[turn.x_coordinate][turn.y_coordinate] == self.game.field[0][j] == self.game.field[1][j] == self.game.field[2][j]:
                self.game.winner_id = player_id
        if self.game.field[turn.x_coordinate][turn.y_coordinate] == self.game.field[0][0] == self.game.field[1][1] == self.game.field[2][2]:
            self.game.winner_id = player_id
        if self.game.field[turn.x_coordinate][turn.y_coordinate] == self.game.field[0][2] == self.game.field[1][1] == self.game.field[2][0]:
            self.game.winner_id = player_id

    def check_draw(self) -> None:
        draw = True
        for row in self.game.field:
            if "O" not in row or "X" not in row:
                draw = False
        for j in range(0, 3):
            row = []
            row.append(self.game.field[0][j])
            row.append(self.game.field[1][j])
            row.append(self.game.field[2][j])
            if "O" not in row or "X" not in row:
                draw = False
        row = []
        row.append(self.game.field[0][0])
        row.append(self.game.field[1][1])
        row.append(self.game.field[2][2])
        if "O" not in row or "X" not in row:
            draw = False
        row = []
        row.append(self.game.field[0][2])
        row.append(self.game.field[1][1])
        row.append(self.game.field[2][0])
        if "O" not in row or "X" not in row:
            draw = False
        if draw == True:
            self.game.winner_id = "draw"

    def get_game_info(self) -> TicTacToeGameInfo:
        return deepcopy(self.game)
