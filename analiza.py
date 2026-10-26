# Statystyki opisowe
from termcolor import colored


def podstawowe_statystyki(df):
    if df is None or df.empty:
        print(colored("Najpierw wczytaj dane z pliku CSV","red"))
        return
    print(colored("\n ***** PODSTAWOWE STATYSTYKI *****","green"))
    print(colored("Średnia temperatura maksymalną: ", "green"),colored(f"{df['temp_max'].mean():.2f} ℃", "red"))
    print(colored("Średnia temperatura minimalną: ","green"),colored(f"{df['temp_min'].mean():.2f} ℃","yellow"))
    print(colored("Suma opadów: ","green"),colored(f"{df['opady'].sum():.2f} mm","blue"))

