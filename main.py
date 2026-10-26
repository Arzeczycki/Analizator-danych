# Uruchamianie aplikacji
from interface import uruchom_menu


def main():
    """    Uruchamia menu glowne aplikacji    """
    uruchom_menu()

# def main():
#     print("Uruchamiam aplikację")
#warunek uruchamiania programu - określa czy dany plik został uruchomiony bezpośrednio, czy został zaimportowany jako moduł z innego pliku
#__name__ - zmienna automatycznie ustawiana przez Pythona dla każdego modułu
# "__main__" wartość oznaczająca moduł uruchoamiany jako główny program
if __name__ == "__main__":
    main()