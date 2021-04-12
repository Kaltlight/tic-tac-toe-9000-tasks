# API

How does API work?

### POST: ```/start_game```
**request:**
```json
{
    "first_playerd_id": "Petya",
    "second_player_id": "Vasya"
}
```

**responce:**
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


### GET: ```/get_game_by_id?game_id=4ef414ed-1cad-44ea-b0f4-df097c728543```
**responce:**
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


### POST: ```/do_turn```
**request:**
```json
{
    "player_id": "Petya",
    "x": 0,
    "y": 0,
    "game_id": "4ef414ed-1cad-44ea-b0f4-df097c728543"
}
```

**responce:**
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
