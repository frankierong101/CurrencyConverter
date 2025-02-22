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

### 2. Run this below and replace "YOUR_API_KEY_HERE" with your own API key obtained in prerequisites step 2 above:
```sh
echo EXCHANGE_RATE_API_KEY=YOUR_API_KEY_HERE > .env

```
### 2.5 Run this below if you want to double check or change your inserted API key from step 2:
```sh
notepad .env
```
"CTRL + S" to save before heading to the next step

### 3. Run:
```sh
pip install requests python-dotenv
python currencyConverter.py
```

---
---
# EXTRA: Supported Currencies

This project supports the following currencies:

- **AED** - United Arab Emirates Dirham
- **AFN** - Afghan Afghani
- **ALL** - Albanian Lek
- **AMD** - Armenian Dram
- **ANG** - Netherlands Antillean Guilder
- **AOA** - Angolan Kwanza
- **ARS** - Argentine Peso
- **AUD** - Australian Dollar
- **AWG** - Aruban Florin
- **AZN** - Azerbaijani Manat
- **BAM** - Bosnia and Herzegovina Mark
- **BBD** - Barbadian Dollar
- **BDT** - Bangladeshi Taka
- **BGN** - Bulgarian Lev
- **BHD** - Bahraini Dinar
- **BIF** - Burundian Franc
- **BMD** - Bermudian Dollar
- **BND** - Brunei Dollar
- **BOB** - Bolivian Boliviano
- **BRL** - Brazilian Real
- **BSD** - Bahamian Dollar
- **BTN** - Bhutanese Ngultrum
- **BWP** - Botswana Pula
- **BYN** - Belarusian Ruble
- **BZD** - Belize Dollar
- **CAD** - Canadian Dollar
- **CDF** - Congolese Franc
- **CHF** - Swiss Franc
- **CLP** - Chilean Peso
- **CNY** - Chinese Yuan
- **COP** - Colombian Peso
- **CRC** - Costa Rican Colón
- **CUP** - Cuban Peso
- **CVE** - Cape Verdean Escudo
- **CZK** - Czech Koruna
- **DJF** - Djiboutian Franc
- **DKK** - Danish Krone
- **DOP** - Dominican Peso
- **DZD** - Algerian Dinar
- **EGP** - Egyptian Pound
- **ERN** - Eritrean Nakfa
- **ETB** - Ethiopian Birr
- **EUR** - Euro
- **FJD** - Fijian Dollar
- **FKP** - Falkland Islands Pound
- **FOK** - Faroese Króna
- **GBP** - British Pound Sterling
- **GEL** - Georgian Lari
- **GGP** - Guernsey Pound
- **GHS** - Ghanaian Cedi
- **GIP** - Gibraltar Pound
- **GMD** - Gambian Dalasi
- **GNF** - Guinean Franc
- **GTQ** - Guatemalan Quetzal
- **GYD** - Guyanese Dollar
- **HKD** - Hong Kong Dollar
- **HNL** - Honduran Lempira
- **HRK** - Croatian Kuna
- **HTG** - Haitian Gourde
- **HUF** - Hungarian Forint
- **IDR** - Indonesian Rupiah
- **ILS** - Israeli New Shekel
- **IMP** - Isle of Man Pound
- **INR** - Indian Rupee
- **IQD** - Iraqi Dinar
- **IRR** - Iranian Rial
- **ISK** - Icelandic Króna
- **JEP** - Jersey Pound
- **JMD** - Jamaican Dollar
- **JOD** - Jordanian Dinar
- **JPY** - Japanese Yen
- **KES** - Kenyan Shilling
- **KGS** - Kyrgyzstani Som
- **KHR** - Cambodian Riel
- **KID** - Kiribati Dollar
- **KMF** - Comorian Franc
- **KRW** - South Korean Won
- **KWD** - Kuwaiti Dinar
- **KYD** - Cayman Islands Dollar
- **KZT** - Kazakhstani Tenge
- **LAK** - Lao Kip
- **LBP** - Lebanese Pound
- **LKR** - Sri Lankan Rupee
- **LRD** - Liberian Dollar
- **LSL** - Lesotho Loti
- **LYD** - Libyan Dinar
- **MAD** - Moroccan Dirham
- **MDL** - Moldovan Leu
- **MGA** - Malagasy Ariary
- **MKD** - Macedonian Denar
- **MMK** - Myanmar Kyat
- **MNT** - Mongolian Tögrög
- **MOP** - Macanese Pataca
- **MRU** - Mauritanian Ouguiya
- **MUR** - Mauritian Rupee
- **MVR** - Maldivian Rufiyaa
- **MWK** - Malawian Kwacha
- **MXN** - Mexican Peso
- **MYR** - Malaysian Ringgit
- **MZN** - Mozambican Metical
- **NAD** - Namibian Dollar
- **NGN** - Nigerian Naira
- **NIO** - Nicaraguan Córdoba
- **NOK** - Norwegian Krone
- **NPR** - Nepalese Rupee
- **NZD** - New Zealand Dollar
- **OMR** - Omani Rial
- **PAB** - Panamanian Balboa
- **PEN** - Peruvian Sol
- **PGK** - Papua New Guinean Kina
- **PHP** - Philippine Peso
- **PKR** - Pakistani Rupee
- **PLN** - Polish Złoty
- **PYG** - Paraguayan Guaraní
- **QAR** - Qatari Riyal
- **RON** - Romanian Leu
- **RSD** - Serbian Dinar
- **RUB** - Russian Ruble
- **RWF** - Rwandan Franc
- **SAR** - Saudi Riyal
- **SBD** - Solomon Islands Dollar
- **SCR** - Seychellois Rupee
- **SDG** - Sudanese Pound
- **SEK** - Swedish Krona
- **SGD** - Singapore Dollar
- **SHP** - Saint Helena Pound
- **SLE** - Sierra Leonean Leone
- **SLL** - Sierra Leonean Leone (old)
- **SOS** - Somali Shilling
- **SRD** - Surinamese Dollar
- **SSP** - South Sudanese Pound
- **STN** - São Tomé and Príncipe Dobra
- **SYP** - Syrian Pound
- **SZL** - Swazi Lilangeni
- **THB** - Thai Baht
- **TJS** - Tajikistani Somoni
- **TMT** - Turkmenistani Manat
- **TND** - Tunisian Dinar
- **TOP** - Tongan Paʻanga
- **TRY** - Turkish Lira
- **TTD** - Trinidad and Tobago Dollar
- **TVD** - Tuvaluan Dollar
- **TWD** - New Taiwan Dollar
- **TZS** - Tanzanian Shilling
- **UAH** - Ukrainian Hryvnia
- **UGX** - Ugandan Shilling
- **USD** - United States Dollar
- **UYU** - Uruguayan Peso
- **UZS** - Uzbekistani Som
- **VES** - Venezuelan Bolívar Soberano
- **VND** - Vietnamese Đồng
- **VUV** - Vanuatu Vatu
- **WST** - Samoan Tala
- **XAF** - Central African CFA Franc
- **XCD** - East Caribbean Dollar
- **XDR** - Special Drawing Rights
- **XOF** - West African CFA Franc
- **XPF** - CFP Franc
- **YER** - Yemeni Rial
- **ZAR** - South African Rand
- **ZMW** - Zambian Kwacha
- **ZWL** - Zimbabwean Dollar
