import requests
from bs4 import BeautifulSoup
import csv
import os
import time

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36', 'accept': '*/*'}
FILE = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition_area')


    cars=[]
    for item in items:
            cars.append({
            'title':item.find('h3', class_='proposition_name').get_text(strip=True),
            'equip': item.find('div', class_='proposition_equip').get_text(strip=True),
            'cena': item.find('span', class_='green').get_text(strip=True)
            })
    return cars


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Характеристики', 'Цена'])
        for item in items:
            writer.writerow([item['title'], item['equip'], item['cena']])


def parse():
    name = input('Введите марку автомобиля: ')
    if name == "Jeep":
        URL = 'https://auto.ria.com/newauto/marka-jeep/'
        html=get_html(URL)
        if html.status_code == 200:
            cars=[]
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name=="Volkswagen":
        URL = 'https://auto.ria.com/newauto/marka-volkswagen/'
        html=get_html(URL)
        if html.status_code == 200:
            cars=[]
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Skoda":
        URL = 'https://auto.ria.com/newauto/marka-skoda/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Renault":
        URL = 'https://auto.ria.com/newauto/marka-renault/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Mercedes":
        URL = 'https://auto.ria.com/newauto/marka-mercedes-benz/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Toyota":
        URL = 'https://auto.ria.com/newauto/marka-toyota/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Opel":
        URL = 'https://auto.ria.com/newauto/marka-opel/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Ford":
        URL = 'https://auto.ria.com/newauto/marka-ford/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "BMW":
        URL = 'https://auto.ria.com/newauto/marka-bmw/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Kia":
        URL = 'https://auto.ria.com/newauto/marka-kia/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Hyundai":
        URL = 'https://auto.ria.com/newauto/marka-hyundai/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Nissan":
        URL = 'https://auto.ria.com/newauto/marka-nissan/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Chevrolet":
        URL = 'https://auto.ria.com/newauto/marka-chevrolet/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Audi":
        URL = 'https://auto.ria.com/newauto/marka-audi/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Jaguar":
        URL = 'https://auto.ria.com/newauto/marka-jaguar/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Bentley":
        URL = 'https://auto.ria.com/newauto/marka-bentley/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Cadillac":
        URL = 'https://auto.ria.com/newauto/marka-cadillac/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    elif name == "Porsche":
        URL = 'https://auto.ria.com/newauto/marka-porsche/'
        html = get_html(URL)
        if html.status_code == 200:
            cars = []
            pages_count = get_pages_count(html.text)
            print('Я знал, что ты выберешь Porsche))')
            time.sleep(1)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} из {pages_count}...')
                time.sleep(1)
                html = get_html(URL, params={'page': page})
                cars.extend(get_content(html.text))

            save_file(cars, FILE)
            print(f'Получено {len(cars)} автомобилей')
            os.startfile(FILE)
        else:
            print('Error')
    else:
        print('Вы некорректно ввели данные о машине или произошла ошибка.')

parse()