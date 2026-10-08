
def vynasob_xty_prvek(seznam, cislo_prvku, nasobek):

    cislo_prvku -=1
    if(cislo_prvku <= len(seznam)-1 and cislo_prvku >=0):
       x = seznam[cislo_prvku]
       x *= nasobek
       seznam[cislo_prvku] = x;
       print(seznam);
    else:
        print("pocet prvku neexistuje");
    
def prumer_pole(seznam):
    if(len(seznam) != 0):
        print(sum(seznam) / len(seznam))
    else:
        print("pole je prazdne")

def formatuj_text(student):
    return f"Student {student('jmeno')}" 



if __name__ == "__main__":

    seznam = [1,2,3,4,5]
    vynasob_xty_prvek(seznam,6,10)
    prumer_pole(seznam)
    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek" : 21,
        "znamky" : [1,2,3,4,5]
    }
    print(formatuj_text(student))

    #vek = input("zadej svuj vek")
    #vek = int(vek)

    #if vek >= 21:
    #    print("muzes pit v USA")
    #else:
    #    print("dejh si colu")

    #print("za rok ti bude [vek + 1]")
