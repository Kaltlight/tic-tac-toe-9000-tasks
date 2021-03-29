from flask import Flask, request
from game_app import TicTacToeApp
from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn

from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Start:
    first_player_id: str
    second_player_id: str

@dataclass_json
@dataclass
class Turn:
    player_id: str
    x: int
    y: int
    game_id: str = ""

app = Flask(__name__)
game = TicTacToeApp()

@app.route('/start_game', methods=["POST"])
def start_game():
    start = Start.from_dict(request.json)
    first_player_id = start.first_player_id
    second_player_id = start.second_player_id
    return game.start_game(first_player_id, second_player_id).to_json()

@app.route('/get_game_by_id', methods=["GET"])
def get_game_by_id():
    game_id = request.args["game_id"]
    return game.get_game_by_id(game_id).to_json()

@app.route('/do_turn', methods=["POST"])
def do_turn():
    turn = Turn.from_dict(request.json)
    player_id = turn.player_id
    x = turn.x
    y = turn.y
    game_id = turn.game_id
    return game.do_turn(TicTacToeTurn(player_id, int(x), int(y)), game_id).to_json()
