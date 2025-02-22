import requests
import os
from dotenv import load_dotenv

#Loads .env file
load_dotenv()

#Getting API key from env file
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
if not API_KEY:
    print("Error: API key not found. Please create a .env file with your API key.")
    exit(1)

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

def get_exchange_rates():
    try:
        # Make a request to the API
        response = requests.get(BASE_URL)
        response.raise_for_status()  #Raises error
        data = response.json()  #Converts response to JSON format

        if data["result"] == "success":
            return data["conversion_rates"]  #Returns the exchange rates
        else:
            print("Failed to fetch exchange rates. Error:", data.get("error-type", "Unknown error"))
            return None
    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return None

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates()
    if rates:
        #Converting
        from_rate = rates.get(from_currency)
        to_rate = rates.get(to_currency)

        if from_rate is None or to_rate is None:
            #Prints available currencies
            print(f"Error: Currency not found. Available currencies: {', '.join(rates.keys())}")
            return None

        converted_amount = (amount / from_rate) * to_rate
        return converted_amount
    else:
        return None

#User input
amount = float(input("Enter the amount: "))
from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., EUR): ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency)

if converted_amount:
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print("Conversion failed.")