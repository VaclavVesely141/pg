def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    jed = ["","jedna", "dva","tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset"]
    des = ["nula", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    return (des[str(cislo[0])]+jed[str(cislo[1])])

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)