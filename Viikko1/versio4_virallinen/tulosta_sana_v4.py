import sys

tiedosto_nimi = "sana.txt"  # oletus

if len(sys.argv) > 1:
    tiedosto_nimi = sys.argv[1]

try:
    with open(tiedosto_nimi, "r", encoding="utf-8") as tiedosto:
        sisalto = tiedosto.read()
    print(sisalto)
except FileNotFoundError:
    print(f"Tiedostoa {tiedosto_nimi} ei löytynyt!")
