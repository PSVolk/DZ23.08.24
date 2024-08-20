import json

countries_capitals = {}

def add_country_capital(country, capital):
    """Добавление данных о стране и столице"""
    countries_capitals[country] = capital
    print(f"Добавлена страна '{country}' с столицей '{capital}'.")

def remove_country_capital(country):
    """Удаление данных о стране и столице"""
    if country in countries_capitals:
        capital = countries_capitals.pop(country)
        print(f"Удалена страна '{country}' со столицей '{capital}'.")
    else:
        print(f"Страна '{country}' не найдена.")

def find_capital(country):
    """Поиск столицы по названию страны"""
    if country in countries_capitals:
        capital = countries_capitals[country]
        print(f"Столица страны '{country}' - '{capital}'.")
    else:
        print(f"Страна '{country}' не найдена.")

def update_capital(country, new_capital):
    """Обновление данных о столице"""
    if country in countries_capitals:
        countries_capitals[country] = new_capital
        print(f"Столица страны '{country}' обновлена на '{new_capital}'.")
    else:
        print(f"Страна '{country}' не найдена.")

def save_data():
    """Сохранение данных в файл"""
    with open("countries_capitals.json", "w") as file:
        json.dump(countries_capitals, file)
    print("Данные успешно сохранены.")

def load_data():
    """Загрузка данных из файла"""
    try:
        with open("countries_capitals.json", "r") as file:
            global countries_capitals
            countries_capitals = json.load(file)
        print("Данные успешно загружены.")
    except FileNotFoundError:
        print("Файл с данными не найден.")


add_country_capital("Россия", "Москва")
add_country_capital("Германия", "Берлин")
add_country_capital("Франция", "Париж")

find_capital("Россия")
find_capital("Италия")

update_capital("Россия", "Санкт-Петербург")

remove_country_capital("Германия")

save_data()
load_data()
