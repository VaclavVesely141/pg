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
    def load_json_data(cls, json_data):
        osoby = []
        for data in json_data:
            osoba = cls(data["jmeno"], data["telefon"], data["email"])
            osoby.append(osoba)
        return osoby

if __name__ == "__main__":
    #o = Osoba("Jan Novák", "123456789", "jan@novak.cz")
    #o.jmeno = "petypety"  #kontorla ze obsahuje jenom string
    #o.telefon = "77777777" #kontrola ze obsahuje jenom cislo
    #o.email = "michal@mazgal.cz" #kontrola ze obsahuje jen cisla, pismena, zavinac a tecku
    #o.vypsat_info()
    osoby = []
    print(osoby)