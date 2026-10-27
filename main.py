# Uruchamianie aplikacji
import logging

from interface import uruchom_menu
from logowanie import konfiguruj_logowanie


def main():
    """    Uruchamia menu glowne aplikacji    """
    konfiguruj_logowanie()
    logging.info("Uruchomiono aplikację")

    uruchom_menu()
    logging.info("Zakończono działanie aplikacji")

# def main():
#     print("Uruchamiam aplikację")
#warunek uruchamiania programu - określa czy dany plik został uruchomiony bezpośrednio, czy został zaimportowany jako moduł z innego pliku
#__name__ - zmienna automatycznie ustawiana przez Pythona dla każdego modułu
# "__main__" wartość oznaczająca moduł uruchoamiany jako główny program
if __name__ == "__main__":
    main()