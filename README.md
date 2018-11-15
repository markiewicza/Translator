# Property Translator

Narzędzie do tłumaczenia plików "properties".

## Jak zacząć

Instrukcje odnośnie instalacji projektu i konfiguracji środowiska.

### Wymagania wstępne

Po sklonowaniu folderu z projektem, należy stworzyć nowy interpreter oraz uruchomić środowisko wirtualne
za pomocą komendy:

```
.\venv\Scripts\activate
```

### Instalacja

Wszystkie pakiety potrzebne do uruchomienia projektu mogą zostać zainstalowane za pomocą pliku "requirements.txt",
przy użyciu następującej komendy:

```
pip install -r requirements.txt
```

## Opisy funkcji

### Zbieranie angielskich wyrażeń

Funkcja "gather_english_phrases_from_files" przechodzi przez folder zadany na wejściu i dla każdego pliku
zbiera wyrażenia oraz podstawia aliasy wewnątrz nich ("swap_aliases"). Wynik tej operacji jest zapisywany w zadanym pliku.

### Tworzenie słownika

Odbywa się ono po uruchomieniu metody "create_dictionary_from_file". Łączone są dwa pliki, do których ścieżki zadane są
wejściu i wynik zapisywany jest wewnątrz klasy "Translator" w formie "pd.DataFrame".

### Tłumaczenie plików

Funkcja "translate_files" przechodzi po zadanym folderze plików, zbiera wyrażenia i następnie każdy z nich próbuje
przetłumaczyć przy pomocy zapisanego słownika.

## Uruchamianie narzędzia

Objaśnienie używanych komend oraz plików.

### Komendy

Po przejściu do folderu z projektem, oraz uruchomieniu maszyny wirtualnej, można wyświetlić wszystkie dostępne komendy,
wpisując w terminalu:

```
python -m nc_project -h
```

Powinna wyświetlić się dokumentacja następujących komend:

* Operacja do wykonania

    ```
    --action ACTION, -a ACTION
    ```
    Dostępnymi operacjami są "only translate" oraz domyślnie cały proces (w pierwszej opcji nie ma zbierania angieslkich
    wyrażeń)
    
* Folder wejściowy

    ```
    --input_directory INPUT_DIRECTORY, -i INPUT_DIRECTORY
    ```
    Jest to argument, w którym można podać sciężkę do folder z danymi wejściowymi (domyślnie "translations")

* Pliki  do słownika

    Wejściowy (domyślnie "english_phrases.csv")
    ```
    --file_path_from_trans FILE_PATH_FROM_TRANS, -pf FILE_PATH_FROM_TRANS
    ```
    Wyjściowy (domyślnie "polish_phrases.csv")
    
    ```
    --file_path_to_trans FILE_PATH_TO_TRANS, -pt FILE_PATH_TO_TRANS
    ```
* Języki

    Wejściowy (domyślnie "ENG")
    ```
    --trans_from TRANS_FROM, -f TRANS_FROM
    ```
    Wyjściowy (domyślnie "PL")
    
    ```
    --trans_to TRANS_TO, -t TRANS_TO
    ```
    
Przykładowe uruchomienie narzędzia:

```
python -m translator -a "only translate" -i "C:\\moj_folder\\translations" -pf "C:\\inny_folder\\phrases.csv"
```

Wszystkie niewypełnione argumenty przyjmują wartości domyślne.

### Format plików

Zarówno plik wejściowy jak i wyjściowy do słownika mają format csv i powinny zawierać wszystkie dane w jednej kolumnie,
bezpośrednio pod sobą.

### Wykorzystane technologie

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)