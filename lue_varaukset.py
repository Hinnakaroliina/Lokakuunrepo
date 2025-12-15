def main():
    tiedosto = "varaukset.txt"

    # Luetaan tiedosto
    with open(tiedosto, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Pilkotaan tiedot listaksi
    osat = varaus.split('|')

    varaus_id = osat[0]
    varaaja = osat[1]
    paivamaara = osat[2]
    aloitusaika = osat[3]
    tuntimaara = int(osat[4])
    tuntihinta = float(osat[5])
    maksettu = "Kyllä" if osat[6] == "True" else "Ei"
    kohde = osat[7]
    puhelin = osat[8]
    sahkoposti = osat[9]

    # Muotoillaan päivämäärä (YYYY-MM-DD -> DD.MM.YYYY)
    pvm_osat = paivamaara.split('-')
    paivamaara_muotoiltu = f"{pvm_osat[2]}.{pvm_osat[1]}.{pvm_osat[0]}"

    # Lasketaan kokonaishinta
    kokonaishinta = tuntimaara * tuntihinta

    # Tulostetaan tiedot
    print(f"Varausnumero: {varaus_id}")
    print(f"Varaaja: {varaaja}")
    print(f"Päivämäärä: {paivamaara_muotoiltu}")
    print(f"Aloitusaika: {aloitusaika}")
    print(f"Tuntimäärä: {tuntimaara}")
    print(f"Tuntihinta: {tuntihinta} €")
    print(f"Kokonaishinta: {kokonaishinta} €")
    print(f"Maksettu: {maksettu}")
    print(f"Kohde: {kohde}")
    print(f"Puhelin: {puhelin}")
    print(f"Sähköposti: {sahkoposti}")

if __name__ == "__main__":
    main()
    