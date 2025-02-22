# CurrencyConverter

This Python script allows you to convert currencies using real-time exchange rates. It prompts the user for:
- The amount to convert.
- The currency to convert from.
- The currency to convert to.
  
## Prerequisites

1. **Python**: Ensure python is installed on your device, otherwise to install, head to https://www.python.org/

2. **API key**: You'll need an API key. The easiest way is to go to https://www.exchangerate-api.com/. Sign up with your email and you'll get a personal API key in less than 5 minutes

## How to Use  

### 1. Clone the Repository  
Open a terminal and run:  

```sh
git clone https://github.com/frankierong101/CurrencyConverter.git
cd CurrencyConverter
```

### 2. Run this below and paste "EXCHANGE_RATE_API_KEY=YOUR_API_KEY_HERE" into the contents of the .env file:
```sh
echo EXCHANGE_RATE_API_KEY=YOUR_API_KEY_HERE > .env
notepad .env
```
## 2.5 Run this below if you want to double check or change your inserted API key from step 2:
```sh
notepad .env
```
"CTRL + S" to save before heading to the next step

### 3. Run:
```sh
python currencyConverter.py
```
