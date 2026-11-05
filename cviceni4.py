import sys
import requests
import json


url = 'https://www.jcu.cz/cz/'
url1 = 'https://data.carnewschina.com/suggest?q='
url2 = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'


def get_model_names(prefix):
    try:
        responce = requests.get(url1 + prefix)
        if responce.status_code != 200:
            print("error: ", responce.status_code)
            return []
        data = json.loads(responce.content)
        model_names = [] 
        for model in data["models"]:
            model_names.append(model["name"])
        return model_names
        
        
    except Exception as e:
        print("error",e)
    #data["models"] -> model["name"]
    return []
def download_rates():
    try:
        responce = requests.get(url2)
        if responce.status_code != 200:
            print("error: ", responce.status_code)
            return []
        data = responce.content.decode("utf-8")
        lines = data.splitlines()
        rates = {}
        for line in lines[2:]:
            parts = line.split("|")
            if len(parts) >= 5:
                rate = float(parts[4].replace(",", ".")) / float(parts[2])
                currency_code = parts[3]
                rates[currency_code] = rate
        return rates
    except Exception as e:
        print("error", e)
    return {}


if __name__ == "__main__":
    # responce = requests.get(url)
    # if responce.status_code == 200:
    #     print(responce.content)
    # responce.json()
    #if len(sys.argv) < 2:
    #    sys.exit()

    #prefix = sys.argv[1]
    #models = get_model_names(prefix)
        #for model in models:
        #    print(model)
    # prefix = input("Enter prefix: ")
    # models = get_model_names(prefix)
    # for model in models:
    #     print(model)
    
    print(download_rates())