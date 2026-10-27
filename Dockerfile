# cykl pracy: Dockerfile -(docker build)-> obraz dockera -(Docker run)-> Kontener
FROM python:3.12

WORKDIR /app

# kopiuj z "." z katalogu głównego do "." katalogu głównego
# Kopiuje plik z kontekstu budowania do katalogu roboczego
# Piersza kropka oznacz źródło, duga kropka oznacza miejsce docelowe
#COPY nie wybiera automatycznie potrzebnych plików, stąd stosowanie .dockerignore
COPY . .

# . - na końcu oznacza wykorzystanie z katalogu głównego projektu plik pyproject.toml
# Podczas budowania obrazu instaluje nasza aplicację i jej zależności. Kropka na końcu oznacza bieżący katalog, w którym znajduje się pyproject.toml
# --no-cache-dir - nie zapisuje pamięci podręcznej pobranych pakietów pip
RUN pip install --no-cache-dir .

# określenie polecenia uruchomieniowego
CMD  ["research-analyzer"]