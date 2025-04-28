# Talos
Mój osobisty prywatny assysten AI

## TODO
[ ] Dodać uniwersalny tekst/setup dla każdego agenta i assystenta ze strukturą wiadomości itp.
[ ] Dodać sprawdzanie czy json jest odpoweiedni i posiada wszystkie potrzebne dane, ewentualnie urzyć try - co bedzie chyba najlepszym rozwiązaniem

## JSON
To jest wiadomości
```json
{
    "succes": true,
    "message": ["Wiadomość", "Nastepny wiesz"],
    "source_id": 1,
    "destination_id": 2
}
```

To wiadomość do system/app
```json
{
    "succes": true,
    "message": ["coś tam"],
    "action_type": "nazwa akcji",
    "action_details": {
        ...
    },
    "source_id": 1,
    "destination_id": 2
}
```

To jest wiadomośc od systemu:
```json
{
    "succes": true,
    "message": ["Wszystkie inforamacje w polu 'data'"],
    "data": ...,
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