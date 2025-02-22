# CurrencyConverter

This python script asks for an amount, the currency you want to convert from and to and then uses the current exchange rate via an API key to convert "x" currency into "y" currency of your choice.

Notes

You'll need an API key in order to test and run this script. The easiest way is to go to https://www.exchangerate-api.com/ and you'll get a personal API key in less than 5 minutes, all it needs is your email.

## How to Use  

### 1. Clone the Repository  
Open a terminal and run:  

```sh
git clone https://github.com/frankierong101/CurrencyConverter.git
cd CurrencyConverter
```

### 2. Run this below and paste "EXCHANGE_RATE_API_KEY=YOUR_API_KEY_HERE" into the contents of the .env file
```sh
echo > .env
notepad .env
```

### 3. Run:
```sh
python currencyConverter.py
```
