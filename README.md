## weather - osługa biblioteki zewnętrznej, optymalizacja kodu

Zoptymalizuj kod dla zadania: "Zadanie - obsługa biblioteki zewnętrznej"
 
Utwórz klasę WeatherForecast, która w konstruktorze będzie pobierać jeden parametr: klucz API.
 
Obiekt klasy WeatherForecast - wf będzie odpowiadał na następujące wywołania:
 

**wf[date]** da odpowiedź na temat pogody dla podanej daty (według specyfikacji z poprzedniego zadania)

**wf.items()** zwróci generator tupli w formacie (data, pogoda) dla już zcache’owanych rezultatów przy wywołaniu

**wf** to iterator zwracający wszystkie daty, dla których znana jest pogoda
 
Użyj tak stworzonej klasy do implementacji programu z poprzedniego zadania.
