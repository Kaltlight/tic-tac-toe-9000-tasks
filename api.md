# API

There I will suggest how api could work in my opinion.

1. GET: ```/start_game?first_player_id=Petya&second_player_id=Vasya```
    Starts new game, requires parameters ```first_player_id``` and ```second_player_id```. Created game is added to the dictionary of games with unique uuid.

    Responce:
    ```json
    {
        "game_id": "4ef414ed-1cad-44ea-b0f4-df097c728543",
        "field": [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        "sequence_of_turns": [],
        "first_player_id": "Petya",
        "second_player_id": "Vasya",
        "winner_id": ""
    }
    ```

2. GET: ```/get_game_by_id?game_id=4ef414ed-1cad-44ea-b0f4-df097c728543&user_id=someone```
    Returns game information, requires parameter ```game_id```.

    Responce:
    ```json
    {
        "game_id": "4ef414ed-1cad-44ea-b0f4-df097c728543",
        "field": [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        "sequence_of_turns": [],
        "first_player_id": "Petya",
        "second_player_id": "Vasya",
        "winner_id": ""
    }
    ```

3. GET: ```/do_turn?turn=Petya,0,0&game_id=4ef414ed-1cad-44ea-b0f4-df097c728543```
    Makes turn in the game, requires parameters ```turn``` and ```game_id```. ```turn``` should be written as ```player_id,x,y```, where ```player_id``` is id of the player, ```x```, ```y``` are coordinates of the turn.

    Responce:
    ```json
    {
        "game_id": "4ef414ed-1cad-44ea-b0f4-df097c728543",
        "field": [
            ["X", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ],
        "sequence_of_turns": [["Petya", 0, 0]],
        "first_player_id": "Petya",
        "second_player_id": "Vasya",
        "winner_id": ""
    }
    ```
