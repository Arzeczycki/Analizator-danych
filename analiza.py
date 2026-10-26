# Statystyki opisowe
from termcolor import colored


def podstawowe_statystyki(df):
    """
    Oblicza i wyświetla podstawowe statystyki danych pogodowych
    
    Args: 
        df(pandas.DataFrame | None)
        Dane zawierające temperatury, wilgotność i opady
    Returns:
        None: Funkcja wyświetla wyniki w konsoli
    """
    if df is None or df.empty:
        print(colored("Najpierw wczytaj dane z pliku CSV","red"))
        return
    print(colored("\n ***** PODSTAWOWE STATYSTYKI *****","green"))
    print(colored("Średnia temperatura maksymalna:", "green"),colored(f"{df['temp_max'].mean():.2f} ℃", "red"))
    print(colored("Średnia temperatura minimalna:","green"),colored(f"{df['temp_min'].mean():.2f} ℃","yellow"))
    print(colored("Suma opadów:","green"),colored(f"{df['opady'].sum():.2f} mm","blue"))

# print(podstawowe_statystyki.__doc__)
# print(help(podstawowe_statystyki))