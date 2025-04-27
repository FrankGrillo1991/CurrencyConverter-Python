import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"

    try:
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            print("Error fetching data:", data['error'])
            return
        
        rates = data['rates']

        if to_currency.upper() not in rates:
            print("Currency not found.")
            return

        converted_amount = amount * rates[to_currency.upper()]
        print(f"{amount:.2f} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")
    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    amount = float(input("Enter the amount: "))
    from_currency = input("From currency (e.g., USD): ")
    to_currency = input("To currency (e.g, EUR): ")

    convert_currency(amount, from_currency, to_currency)
