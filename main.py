### This program is a CLI program that allows you to convert values from once currency to another, using https://www.exchangerate-api.com
import requests
from datetime import datetime
from codes import codes

def main():
    print("Please type a currency you want to convert from via the official 3 character code, "   
          "available here https://www.exchangerate-api.com/docs/supported-currencies")
    currency = input('--> ')
    print('Loading', end='', flush=True)
    currency = currency.upper()
    url = "https://api.exchangerate-api.com/v4/latest/" + currency
    print('\r \r', end='', flush=True)
    response = requests.get(url)
    data = response.json()
    print("Please choose a value")
    while True: 
        value = input('--> ')
        try:
            original_value = int(value)
            break
        except ValueError:
            print("This is not an integer. Please select a valid integer.")
    print("Select new currency")
    new_currency = input('--> ')
    human_readable_date = datetime.fromtimestamp((data['time_last_updated'])).strftime('%d-%m-%Y')

    conversion_rate = data['rates'][new_currency]
    new_value = original_value * conversion_rate
    print(original_value , currency, "is worth", new_value , codes[new_currency], "on" , human_readable_date)

if __name__ == '__main__':
    main()
