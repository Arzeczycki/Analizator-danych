# Wczytywanie danych z pliku CSV
from pathlib import Path

import pandas as pd
from termcolor import colored


def wczytaj_dane():
    """
    Pozwala wybrac plik CSV z danymi z katalogu data, i wczytuje do DataFrame
    Retuns:
        pandas.DataFrame | None: Wczytane dane lub None, jesli nie wybrano pliku lub wystapil blad
    """
    folder = Path("data")
    # metoda glob - służy do wyszukiwania plików pasujących do określonego wzorca
    pliki = sorted(folder.glob("*.csv"))
    
    if not pliki:
        print(colored(f"Brak plików w folderze {folder}", "red"))
        return None
    
    print(colored("\nDostępne pliki CSV: ","blue"))
    if len(pliki) <= 10:
            for i, plik in enumerate(pliki, start=1):
                print(colored(f"{i}. {plik.name}", "green"))
    
    else:    
    
        for i, plik in enumerate(pliki[:5], start=1):
            print(colored(f"{i}. {plik.name}", "green"))
        print(colored("...","light_green"))
        print(f"{len(pliki)}. {pliki[-1].name}")    
    
    print(colored("-"*40,"blue"))
    print(colored("0. Powrót do menu głównego","green"))
    # pętla while obsługująca wybór pliku do analizy
    while True:
    
        wybor = input(colored("Wybierz numer pliku: ", "blue"))
        if wybor == "0":
            return None
        if not wybor.isdigit():
            print(colored(f"Podaj poprawny numer od 1 do {len(pliki)}\n","red"))
            continue
        numer = int(wybor)
        if numer > len(pliki):
            print(colored("Nie ma pliku o takim numerze\n", "red"))
            continue
        wybrany_plik = pliki[numer - 1]
        try:
            df = pd.read_csv(wybrany_plik)
        except pd.errors.ParserError:
            print(colored(f"Bląd wczytania pliku {wybrany_plik}","red"))
            return None
        
        print(colored(f"Wczytano plik {wybrany_plik.name}", "green"))
        print(colored(f"Liczba wierszy: {len(df)}", "green"))
        return df

def wyswietl_dane(df):
    """
    Wyswietla podglad danych oraz podstawowe informacje o zbiorze 
    Args:
        df (pandas.DataFrame | None): Dane do wyswietlenia
    """
    if df is None:
        print(colored("\nNie wczytano danych", "red"))
        return
    print(colored("\n******** PODGLĄ DANYCH**********", "green"))
    print(colored("Pierwsze 10 wierszy", "green"))
    print(colored(df.head(10).to_string(index=False), "green"))
    print(colored("\nInformacje o zbiorze:", "green"))
    print(colored(f"Liczba rekordów: {df.shape[0]}", "green"))
    print(colored(f"Liczba kolumn: {df.shape[1]}", "green"))
    print(colored(f"Kolumny: {', '.join(df.columns)}", "green"))