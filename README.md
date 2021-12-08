# weather - osługa biblioteki zewnętrznej

Zapoznaj się z dokumentacją biblioteki requests:
https://requests.readthedocs.io/en/master/
oraz zbiorem dostępnych api dla sczytywania pogody.

Napisz program weather.py, który sprawdzi, czy danego dnia będzie padać. Przykładowe API
https://rapidapi.com/collection/top-weather-apis
program powinien być wykonany jako:
python weather.py <<klucz api>> <<data w formacie YYYY-MM-DD>>
lub
python weather.py <<klucz api>>

Jeśli data nie jest podana, przyjmij dzień następny. Lokalizacja, dla której sprawdzasz pogodę, może być wpisana na stałe w kodzie.
Rozwiązanie powinno zawierać zarówno plik weather.py, jak i requirements.txt

Uwaga: program nie powinien mieć nigdy wpisanego klucza API do kodu, powinien go pobierać z sys.argv.

Możliwe odpowiedzi programu (standardowe wyjście) to:

Będzie padać
Nie będzie padać
Nie wiem

Aby uniknąć zużywania quoty w programie, zapamiętuj w pliku tekstowym rezultat dla już sprawdzonych dni.
Jeśli wynik jest już znany, zwróć odpowiedź na podstawie pliku txt, nie pytaj ponownie AP o ten sam dzień.
