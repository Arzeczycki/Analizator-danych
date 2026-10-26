"""Interface konsolowy aplikacji """

from termcolor import colored

from analiza import podstawowe_statystyki
from baza import zapisz_do_bazy
from dane import wczytaj_dane, wyswietl_dane
from wykresy import generuj_wykres


def wyswietl_menu():
    print("\n\nRESEARCH DATA ANALYZER")
    print("1. Wczytaj dane z pliku CSV")
    print("2. Wyświetl dane")
    print("3. Analizuj dane")
    print("4. Generuj i zapisz wykres")
    print("5. Zapisz dane do bazy")
    print("0. Wyjście z programu")
    print(colored("-"*40, "blue"))

def uruchom_menu():

    dane = None

    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ").strip()
        if wybor == "0":
            print(colored("Zakończono działanie programu", "magenta"))
            break
        elif wybor == "1":
            print(colored("wybrano opcję 1", "green"))
            nowe_dane = wczytaj_dane()
            if nowe_dane is not None:
                dane = nowe_dane
        elif wybor == "2":
            print(colored("wybrano opcję 2", "green"))
            wyswietl_dane(dane)
        elif wybor == "3":
            print(colored("wybrano opcję 3", "green"))
            podstawowe_statystyki(dane)
        elif wybor == "4":
            print(colored("wybrano opcję 4", "green"))
            generuj_wykres(dane)

        elif wybor == "5":
            print(colored("wybrano opcję 5", "green"))
            zapisz_do_bazy(dane)
        else:
            print(colored("Nieprawidłowy wybór. Wybierz z listy.","red"))