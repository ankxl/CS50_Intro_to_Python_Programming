import requests
import sys
import random
import json

def main():
    n = check_arguments()
    rate = check_rate()
    price = rate*n
    print(f"${rate*n:,.4f}")


def check_arguments():
    if (len(sys.argv) < 2) or (len(sys.argv) > 2):
        sys.exit("Missing command-line argument")
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

def check_rate():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        ds = response.json()
        rate = ds["bpi"]["USD"]["rate"]
        return float(rate.replace(",","").replace("$",""))
    except requests.RequestException:
        pass
    except ValueError:
        rate = 0



main()

