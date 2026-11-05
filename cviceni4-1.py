import sys
from cviceni4 import download_rates

def convert_amount(amount, currency):
    
    rates = download_rates()
    if currency not in rates:
        print(f"Currency {currency} not found in rates.")
        return 0.0
    rate = rates.get(currency)
    print(rate)
    return amount / rate
    

if __name__ == "__main__":
    sys.exit()

if len(sys.argv) < 3:
    print(f"Usage: python {sys.argv[0]} <amount> <currency>")
    sys.exit()

amount = int(sys.argv[1])
currency = sys.argv[2]
convert_amount(amount, currency)
