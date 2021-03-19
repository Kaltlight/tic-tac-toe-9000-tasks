from flask import Flask, request
from game_app import TicTacToeApp
from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn

from dataclasses import dataclass
from dataclasses_json import dataclass_json

app = Flask(__name__)
game = TicTacToeApp()

@app.route('/start_game', methods=["GET"])
def start_game():
    first_player_id = request.args["first_player_id"]
    second_player_id = request.args["second_player_id"]
    return game.start_game(first_player_id, second_player_id).to_json()

@app.route('/get_game_by_id', methods=["GET"])
def get_game_by_id():
    game_id = request.args["game_id"]
    return game.get_game_by_id(game_id).to_json()

@app.route('/do_turn', methods=["GET"])
def do_turn():
    player_id = request.args["player_id"]
    x = request.args["x"]
    y = request.args["y"]
    game_id = request.args["game_id"]
    return game.do_turn(TicTacToeTurn(player_id, int(x), int(y)), game_id).to_json()
