from analiza import podstawowe_statystyki

import pandas as pd


def test_podstawowe_statystyki(capsys):
    df = pd.DataFrame({
        "temp_max": [20, 24],
        "temp_min": [10, 12],
        "opady": [2, 4]
    })
    podstawowe_statystyki(df)
    # capsys - przechwytuje tekst, ktory funkcja wypisuje za pomoca print()
    # capsys.readouterr().out() pobiera przechwycony tekst 
    wynik = capsys.readouterr().out
    # assert - sprawdza czy tekst zawiera oczekiwane wartości
    assert "Średnia temperatura maksymalna: 22.00 ℃" in wynik
    assert "Średnia temperatura minimalna: 11.00 ℃" in wynik
    assert "Suma opadów: 6.00 mm" in wynik

def test_brak_danych(capsys):
    podstawowe_statystyki(None)
    wynik = capsys.readouterr().out
    assert "Najpierw wczytaj dane z pliku CSV" in wynik

def test_pusty_df(capsys):
    df = pd.DataFrame ({})
    podstawowe_statystyki(df)
    wynik = capsys.readouterr().out
    assert "Najpierw wczytaj dane z pliku CSV" in wynik