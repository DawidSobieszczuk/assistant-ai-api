# Talos
Mój osobisty prywatny assysten AI

## JSON
To jest wiadomości
```json
{
    "succes": true,
    "messeges": ["Wiadomość", "Nastepny wiesz"],
    "source_id": 1,
    "destination_id": 2
}
```

To wiadomość do system/app
```json
{
    "succes": true,
    "messege": ["coś tam"],
    "action_type": "nazwa akcji",
    "action_details": {
        ...
    },
    "source_id": 1,
    "destination_id": 2
}
```

To jest błąd
```json
{
    "succes": false,
    "error_message": "Oj nie. Coś poszło nie tak :(",
    "error_details": {
        ...
    },
    "source_id": 1,
    "destination_id": 2
}
```