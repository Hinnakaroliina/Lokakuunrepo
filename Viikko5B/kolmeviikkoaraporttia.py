from datetime import datetime, date

def muunna_tiedot(kulutusTuotanto: list) -> list:
    """Muuttaa jokaisen annetun tietorivin tietotyypit oikein"""
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(kulutusTuotanto[0]))
    muutettu_tietorivi.append(int(kulutusTuotanto[1]))
    muutettu_tietorivi.append(int(kulutusTuotanto[2]))
    muutettu_tietorivi.append(int(kulutusTuotanto[3]))
    muutettu_tietorivi.append(int(kulutusTuotanto[4]))
    muutettu_tietorivi.append(int(kulutusTuotanto[5]))
    muutettu_tietorivi.append(int(kulutusTuotanto[6]))
    return muutettu_tietorivi

def lue_data(tiedoston_nimi: str) -> list:
    """Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä"""
    kulutusTuotantoTiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f) #Ensimmäinen rivi jää pois
        for kulutusTuotantoTieto in f:
            kulutusTuotantoTieto = kulutusTuotantoTieto.strip()
            kulutusTuotantoTietoSarakkeet = kulutusTuotantoTieto.split(';')
            kulutusTuotantoTiedot.append(muunna_tiedot(kulutusTuotantoTietoSarakkeet))
    return kulutusTuotantoTiedot

def paivantiedot(paiva: str, lukemat: list) -> list:
    pv = int(paiva.split('.')[0])
    kk = int(paiva.split('.')[1])
    vuosi = int(paiva.split('.')[2])

    kulutus1vaihe = 0
    kulutus2vaihe = 0
    kulutus3vaihe = 0
    tuotanto1vaihe = 0
    tuotanto2vaihe = 0
    tuotanto3vaihe = 0

    for lukema in lukemat:
        if lukema[0].date() == date(vuosi, kk, pv):
            kulutus1vaihe += (lukema[1])
            kulutus2vaihe += (lukema[2])
            kulutus3vaihe += (lukema[3])
            tuotanto1vaihe += (lukema[4])
            tuotanto2vaihe += (lukema[5])
            tuotanto3vaihe += (lukema[6])

    # muunnetaan kWh 
    return [
        kulutus1vaihe/1000,
        kulutus2vaihe/1000,
        kulutus3vaihe/1000,
        tuotanto1vaihe/1000,
        tuotanto2vaihe/1000,
        tuotanto3vaihe/1000,
    ]

def fmt(num: float) -> str:
    """Muotoillaan desimaalit ja vaihdetaan piste pilkuksi."""
    return f"{num:.2f}".replace('.', ',')

def viikonpaiva_str(pvkkvvvv: str) -> str:
    """Tässä taiotaan päivät"""
    dt = datetime.strptime(pvkkvvvv, "%d.%m.%Y")
    paivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
    return paivat[dt.weekday()]

def tulosta_rivi(viikonpaiva: str, paiva_str: str, arvot: list) -> None:
    """Tulostaa yhden rivin (päivä + pvm + 6 lukemaa) samalla asettelulla kuin tehtiin maanantai."""

    print(
        f"{viikonpaiva:<11} {paiva_str:<12} "
        f"{fmt(arvot[0])}  {fmt(arvot[1]):<6}  {fmt(arvot[2]):<6}           "
        f"{fmt(arvot[3]):<6}  {fmt(arvot[4]):<6}  {fmt(arvot[5]):<6}"
    )

def kasittele_viikko(csv_tiedosto: str, viikon_numero: int, f) -> None:
    lukemat = lue_data(csv_tiedosto)

    f.write(f"Viikon {viikon_numero} sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n")
    f.write("Päivä         Pvm         Kulutus [kWh]                 Tuotanto [kWh]\n")
    f.write("             (pv.kk.vvvv)  v1      v2      v3            v1     v2     v3\n")
    f.write("---------------------------------------------------------------------------\n")

    # Öö korvataan aiempi lista
    paivat = viikon_paivat(lukemat)  # Poimitaankin päivämäärät CSV:stä

    for pvm in paivat:
        arvot = paivantiedot(pvm, lukemat)
        viikonpaiva = viikonpaiva_str(pvm)

        f.write(
            f"{viikonpaiva:<11} {pvm:<12} "
            f"{fmt(arvot[0])}  {fmt(arvot[1]):<6}  {fmt(arvot[2]):<6}           "
            f"{fmt(arvot[3]):<6}  {fmt(arvot[4]):<6}  {fmt(arvot[5]):<6}\n"
        )

    f.write("\n\n")

def viikon_paivat(lukemat: list) -> list:
    """Toivottavasti palauttaa viikkojen päivämäärät CSVstä"""
    paivat = sorted({lukema[0].date() for lukema in lukemat})
    return [p.strftime("%d.%m.%Y") for p in paivat]

    for pvm in paivat:
        arvot = paivantiedot(pvm, lukemat)
        viikonpaiva = viikonpaiva_str(pvm)

        f.write(
            f"{viikonpaiva:<11} {pvm:<12} "
            f"{fmt(arvot[0])}  {fmt(arvot[1]):<6}  {fmt(arvot[2]):<6}           "
            f"{fmt(arvot[3]):<6}  {fmt(arvot[4]):<6}  {fmt(arvot[5]):<6}\n"
        )

    f.write("\n\n")


def main():
    viikot = [
        ("viikko41.csv", 41),
        ("viikko42.csv", 42),
        ("viikko43.csv", 43),
    ]

    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        for csv_tiedosto, viikon_numero in viikot:
            kasittele_viikko(csv_tiedosto, viikon_numero, f)


if __name__ == "__main__":
    main()