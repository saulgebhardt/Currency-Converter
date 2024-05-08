### This program is a CLI program that allows you to convert an amount of dollars to euros.
import requests
from datetime import date
import sys

url = "https://api.exchangerate-api.com/v4/latest/EUR"
codes = "https://v6.exchangerate-api.com/v6/codes"

def main(args):
    response = requests.get(url)
    response_codes = requests.get(codes)
    ### Load in data from url
    data = response.json()
    currency_codes = response_codes.json()
    print(currency_codes)
    original_value = int(args[1])
    conversion_rate = data['rates']['THB']
    new_value = original_value * conversion_rate
    print(original_value , " Euros is worth " , new_value ,  " Thai Baht on " , data['date'])

if __name__ == '__main__':
    main(sys.argv)
