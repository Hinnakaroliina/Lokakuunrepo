try:
    with open("sana.txt", "r", encoding="utf-8") as tiedosto:
        sisalto = tiedosto.read()
    print(sisalto)
except FileNotFoundError:
    print("Tiedostoa sana.txt ei löytynyt!")
