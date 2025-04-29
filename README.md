# Talos
Mój osobisty prywatny assysten AI

## JSON
To jest wiadomości
```json
{
    "succes": true,
    "message": ["Wiadomość", "Nastepny wiesz"],
    "source_id": 1,
    "destination_id": 2,
    "timestamp": "28.04.2025 18:36"
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
    "destination_id": 2,
    "timestamp": "28.04.2025 18:36"
}
```

To jest wiadomośc od systemu:
```json
{
    "succes": true,
    "message": ["Wszystkie inforamacje w polu 'data'"],
    "data": ...,
    "source_id": 1,
    "destination_id": 2,
    "timestamp": "28.04.2025 18:36"
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
    "destination_id": 2,
    "timestamp": "28.04.2025 18:36"
}
```

## TODO
- [ ] (28.04.2025) Dodać uniwersalny tekst/setup dla każdego agenta i assystenta ze strukturą wiadomości itp.
- [ ] (28.04.2025) Dodać sprawdzanie czy json jest odpoweiedni i posiada wszystkie potrzebne dane, ewentualnie urzyć try - co bedzie chyba najlepszym rozwiązaniem
- [ ] (28.04.2025) I tak samo jak wyrzej dla danych z bazy danych
- [ ] (29.04.2025) Logowanie błedów do pliku