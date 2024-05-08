### This program is a CLI program that allows you to convert an amount of dollars to euros.
import requests
from datetime import datetime
import sys

url = "https://api.exchangerate-api.com/v4/latest/EUR"
codes = "https://v6.exchangerate-api.com/v6/codes"

def main(args):
    response = requests.get(url)
    ### Load in data from url
    data = response.json()
    original_value = int(args[1])
    print(data['time_last_updated'])
    human_readable_date = datetime.fromtimestamp((data['time_last_updated'])).strftime('%d-%m-%Y')

    conversion_rate = data['rates']['THB']
    new_value = original_value * conversion_rate
    print(original_value , "Euros is worth" , new_value ,  "Thai Baht on" , human_readable_date)

if __name__ == '__main__':
    main(sys.argv)
