# simple currency conversion using api 

import requests

# First create a api key from exchange rates api
API_KEY = '2907aa5###############43'  
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def convert_currency(base_currency, target_currency, amount):
    try:
        # get the exchange rate
        response = requests.get(BASE_URL + base_currency.upper())
        data = response.json()

        # check for responce
        if data['result'] != 'success':
            print("Error fetching data:", data.get('error-type', 'Unknown error'))
            return

        #  Extract exchange rate and calculate conversion
        rates = data['conversion_rates']
        if target_currency.upper() not in rates:
            print("Invalid target currency code.")
            return

        rate = rates[target_currency.upper()]
        converted_amount = amount * rate

       
        print(f"{amount} {base_currency.upper()} = {converted_amount:.2f} {target_currency.upper()}")

    except Exception as e:
        print("Error:", str(e))

# Take user input
base = input("Enter base currency code (e.g., USD): ")
target = input("Enter target currency code (e.g., INR): ")
try:
    amount = float(input("Enter amount to convert: "))
    convert_currency(base, target, amount)
except ValueError:
    print("Invalid amount entered.")
