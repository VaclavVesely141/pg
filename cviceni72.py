import json
class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self,jmeno,telefon,email):
        self.__jmeno = jmeno
        self.__telefon = telefon
        self.__email = email

    def vypsat_info(self):
                print(f"Jméno: {self.__jmeno}, Telefon: {self.__telefon}, Email: {self.__email}")

    @property
    def jmeno(self):
        return self.__jmeno

    @jmeno.setter
    def jmeno(self, hodnota):
        if hodnota.isalpha():
            self.__jmeno = hodnota
        else:
            raise InvalidData("Jméno musí obsahovat pouze písmena.")
        
    @property
    def telefon(self):
        return self.__telefon
    @telefon.setter
    def telefon(self, hodnota):
        if hodnota.isdigit():
            self.__telefon = hodnota
        else:
            raise InvalidData("Telefon musí obsahovat pouze čísla.")
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, hodnota):
        if "@" in hodnota and "." in hodnota:
            self.__email = hodnota
        else:
            raise InvalidData("Email musí obsahovat zavináč a tečku.")

    @classmethod
    def json_data(cls, data):
        if not isinstance(data, list):
            raise InvalidData("Data musí být seznam.")
        if "jmeno" not in data or "telefon" not in data or "email" not in data:
            raise InvalidData("Data musí obsahovat jméno, telefon a email.")
        return [cls(item["jmeno"], item["telefon"], item["email"]) for item in data]

if __name__ == "__main__":
    #o = Osoba("Jan Novák", "123456789", "jan@novak.cz")
    #o.jmeno = "petypety"  #kontorla ze obsahuje jenom string
    #o.telefon = "77777777" #kontrola ze obsahuje jenom cislo
    #o.email = "michal@mazgal.cz" #kontrola ze obsahuje jen cisla, pismena, zavinac a tecku
    #o.vypsat_info()
    osoby = []
    with open("osoby.json", "r") as f:
        data = json.loads(f.read())
        for record in data:
            osoby.append(Osoba(Osoba.json_data(record)))
        print(osoby)
    