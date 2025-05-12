# Assistant AI | API
Mój osobisty prywatny assysten AI | API

## JSON
To jest wiadomości
```json
{
    "success": true,
    "message": ["Wiadomość", "Nastepny wiesz"],
    "source_id": 1,
    "destination_id": 2,
    "timestamp": "28.04.2025 18:36"
}
```

To wiadomość do system/app
```json
{
    "success": true,
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
    "success": true,
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
    "success": false,
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
- [ ] (29.04.2025) Obsługa błedów i logowanie błedów do pliku, myśle zrobić to w classie app, a wcześniej wyrzucać błedy typu brak takie id w bazie danych
- [ ] (29.04.2025) Dokumentacja do bazy danych, zastanawiam się nad formą i odrazu można by ją przekazać assystentowi od bazy danych
