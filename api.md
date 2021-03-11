# API

There I will suggest how api could work in my opinion.

1. ```/start_game?first_player_id=...&second_player_id=...```
    Starts new game, requires parameters ```first_player_id``` and ```second_player_id```. Created game is added to the dictionary of games with unique uuid.

2. ```/get_game_by_id?game_id=...&user_id=...```
    Returns game information, requires parameter ```game_id```.

3. ```/do_turn?turn=...&game_id=...```
    Makes turn in the game, requires parameters ```turn``` and ```game_id```. ```turn``` should be written as ```x,y,player_id```, where ```x```, ```y``` are coordinates of the turn, ```player_id``` is id of the player.
