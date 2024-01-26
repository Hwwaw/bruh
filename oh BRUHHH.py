import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
def get_temperature():
    url = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%BE%D0%BF%D0%B8%D0%B2%D0%BD%D0%B8%D1%86%D1%8C%D0%BA%D0%B8%D0%B9"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature_element = soup.find('span', class_='weatherDetails tr.temperature td')
        if temperature_element:
            temperature = temperature_element.text.strip()
            return temperature
        else:
            print("Не вдалося знайти температуру на сторінці.")
            return None
    else:
        print("Помилка при отриманні сторінки: {}".format(response.status_code))
        return None
def save_to_database(date_time, temperature):
    try:
        conn = sqlite3.connect('weather_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_time TEXT NOT NULL,
                temperature TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO weather_data (date_time, temperature) VALUES (?, ?)
        ''', (date_time, temperature))
        conn.commit()
        conn.close()
        print("Дані успішно внесено в базу даних.")
    except Exception as e:
        print("Помилка при внесенні даних до бази даних:", e)
current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
temperature_value = get_temperature()
if temperature_value is not None:
    save_to_database(current_date_time, temperature_value)
