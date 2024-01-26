import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self, currency_code, exchange_rate):
        self.currency_code = currency_code
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount):
        return amount / self.exchange_rate


def get_usd_exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return float(data[0]['rate'])
    else:
        print(f"Ошибка: {response.status_code}")
        return None


def main():
    usd_exchange_rate = get_usd_exchange_rate()

    if usd_exchange_rate is not None:
        converter = CurrencyConverter("UAH", usd_exchange_rate)

        try:
            amount = float(input("Введіть кількість валюти: "))
            result = converter.convert_to_usd(amount)
            print(f"{amount} {converter.currency_code} = {result:.2f} USD")
        except ValueError:
            print("Будь ласка, введіть числове значення")


if __name__ == "__main__":
    main()
