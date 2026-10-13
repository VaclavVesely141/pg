def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    jed = ["nula","jedna", "dva","tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset"]
    jed_plus = ["jedenact", "dvanact", "trinact", "ctrnact", "patnact", "sestnact", "sedmnact", "osmnact", "devatenact"]
    des = ["nula", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    

    cislo = int(cislo)
    
    if(cislo >= 0 and cislo < 11):
        return (jed[cislo])
    elif(cislo >= 11 and cislo < 20):
        return (jed_plus[cislo-11])
    elif(cislo >= 20 and cislo <100):
        jednotky = cislo % 10

        desitky = (cislo - jednotky)//10
        
        if(jednotky == 0):
            return (des[desitky])
        else:
            return (des[desitky]+" "+jed[jednotky])
    elif(cislo == 100):
        return("sto")

if __name__ == "__main__":
   
    while(True):
        cislo = input("Zadej číslo: ")
        text = cislo_text(cislo)
        print(text)