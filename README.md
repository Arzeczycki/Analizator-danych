# **RESEARCH DATA ANALYZER**

Aplikacja konsolowa napisana w języku Python przeznaczona do wczytywania danych pogodowych z pliku CSV oraz analizę tych danych wraz z tworzeniem wykresu i zapisem do bazy danych

Projekt powstał w ramach szkolenia
**"Projektowanie i programowanie aplikacji w Pythonie...**


## Spis treści
1. [Funkcjonalność](#1-funkcjonalności)
2. [Wykorzystane technologie](#2-wykorzystane-technologie)
3. [Struktura projektu](#3-struktura-projektu)
4. [Instalacja](#4-instalacja)
5. [Uruchomienie aplikacji](#5-uruchomienie-aplikacji)
6. [Analiza danych](#6-analiza-danych)
7. [Testowanie](#7-testowanie)
8. [Kontrola jakości kodu](#8-kontrola-jakosci-kodu)
9. [Automatyzacja CI](#9-automatyzacja-ci)
10. [Dystrybucja pakietu](#10-dystrybucja-pakietu)
11. [Zastosowanie](#11-zastosowanie)

## 1. Funkcjonalności

Aplikacja umożliwia:
- Pobieranie danych z pliku CSV
- Wyświetlanie podglądu danych
- Analiza danych z wczytanego pliku
- Generowanie wykresu temperatury maksymalnej w zależności od daty i miasta
- Zapis danych do bazy danych SQLite
- Obsługę programu przez interaktywne menu konsolowe

## 2. Wykorzystane technologie
![Static Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=%233776AB&labelColor=%23ffffff) - język programowania

`pandas` - przetwarzanie i analiza danych
`matplotlib` - wizualiacja danych
`SQLite3`- przechowywanie danych w relacyjnej bazie danych
`termcolor` - kolorowanie tekstów w konsoli
`Pytest` - testy jednostkowe
`Ruff` - kontrola jakości kodu
`Git` i `GitHub` - kontrola wersji i przechowywanie repozytorium
`GitHub Actions` - automatyczne uruchoamianie testów i kontroli jakości kodu

## 3. Struktura projektu
TBA

## 4. Instalacja
Do uruchomienia aplikacji potrzebny jest Python w wersji 3.12+ oraz biblioteki wymienione w `requirements.txt`

W powershell uruchomić środowisko wewnętrzne, a następnie je aktywować oraz pobrać wymagane moduły z pliku requirements.txt
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 5. Uruchomienie aplikacji
W katalogu głównym projektu wykonujemy:
```bash
python main.py
```
Po uruchomieniu pojawia się menu:
```text
    RESEARCH DATA ANALYZER
    1. Wczytaj dane z pliku CSV
    2. Wyświetl dane
    3. Analizuj dane
    4. Generuj i zapisz wykres
    5. Zapisz dane do bazy
    0. Wyjście z programu
```
Aby rozpocząć pracę należy umieścić pliki CSV w katalogu `\data`

## 8. Kontrola jakości kodu

Sprawdzenie kodu:
```bash
python -m ruff check .
```
Automatyczne poprawienie obsługiwanych problemów:
```bash
python -m ruff check . --fix
```

## 10. Dystrybucja pakietu

Utworzenie pliku toml.
Insalacja pakietu build
```bash
python -m pip install build
```
Zbudowanie paczki
```bash
python -m build
```
Projekt jest dostępny dla użytkownika w postaci pakietu instalacyjnego .whl. Wykorzystując **GitHub Releases**

Po pobraniu pliku .whl należy zainstalowac poleceniem
```bash
python -m pip install research_data_analyzer-1.0.0-py3-none-any.whl
```
Instalacja wymaga zgodnej wersji Pythona, oraz przygotowanego środowiska wirtualnego.

## 11. Zastosowanie
Aplikacja może być punktem wyjścia do przetwarzania danych wykozrystanych w pracy naukowej lub dydaktycznej.

Przykładowe zastosowania obejmują analizę danych pomiarowych, przgotowanie prostych zestawień statystycznych, wizualizację wyników oraz archiwizowanie danych w bazie danych.

Projekt ma **charakter edukacyjny** i może być rozwijany o kolejne funkcjonalności.