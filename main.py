from tic_tac_toe_game import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn

print("Enter first player's name: ")
first = input()
print("Enter second player's name: ")
second = input()
game = TicTacToeGame("game", first, second)
print(first + " vs " + second + "\n")
while game.get_game_info().winner_id == "":
    print(first + "'s turn\n")
    print("", game.get_game_info().field[0], "\n", game.get_game_info().field[1], "\n", game.get_game_info().field[2], "\n")
    print("Enter coordinates:")
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    game.do_turn(TicTacToeTurn(first, x, y))
    if game.get_game_info().winner_id != "":
        break
    print(second + "'s turn\n")
    print("", game.get_game_info().field[0], "\n", game.get_game_info().field[1], "\n", game.get_game_info().field[2], "\n")
    print("Enter coordinates:")
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    game.do_turn(TicTacToeTurn(second, x, y))
print("", game.get_game_info().field[0], "\n", game.get_game_info().field[1], "\n", game.get_game_info().field[2], "\n")
print(game.get_game_info().winner_id + " wins!")
