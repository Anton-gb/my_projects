import json
import re
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent


def install_driver(browser):
    """

    :param browser: браузер для которого необходимо скачать драйвер
    :return:
    """
    if browser == 'chrome':
        ChromeService(executable_path=ChromeDriverManager().install())
    elif browser == 'edge':
        EdgeService(executable_path=EdgeChromiumDriverManager().install())


def set_driver(browser):
    """
    Функция создает объект драйвера
    :param browser: браузер
    :return: объект вебдрайвера
    """
    if browser == 'chrome':
        service = Service(
            executable_path=r"C:\Users\aoioh\.wdm\drivers\chromedriver\win32\101.0.4951.41\chromedriver.exe"
        )
        ua = UserAgent()
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={ua}")
        driver = webdriver.Chrome(
            service=service,
            options=options
        )
    elif browser == 'edge':
        service = Service(
            executable_path=r"C:\Users\aoioh\.wdm\drivers\edgedriver\win64\101.0.1210.39\msedgedriver.exe"
        )
        driver = webdriver.Edge(
            service=service
        )
    else:
        return print('Неверное имя браузера')
    return driver


def site_requests(url):
    ua = UserAgent()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': f"{ua}"
    }
    s = requests.Session()
    response = s.get(url=url, headers=headers)
    with open('index2.html', 'w', encoding='utf-8') as file:
        file.write(response.text)


def get_page(url, driver):
    html_page = None
    try:
        driver.get(url=url)
        driver.maximize_window()
        time.sleep(5)

        html_page = driver.page_source

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    time.sleep(10)
    print(f"[...] Обрабатываем данные")
    soup = BeautifulSoup(html_page, 'lxml')
    html_pages = soup.find_all('li', class_='page-item')
    pages = []
    for i in html_pages:
        if i.text != '':
            pages.append(int(i.text))
    return max(pages)


def collect_html(url, driver, retry):
    """
    Функция открывает ссылку скролит ее до <footer>, а затем собирает html
    :param retry:
    :param url: ссылка
    :param driver: объект созданного драйвера
    :return: html разметка
    """
    if retry == 0:
        return 1
    try:
        driver.get(url=url)
        driver.maximize_window()
        time.sleep(5)

        i = 1080
        while True:
            driver.execute_script(f"window.scrollTo(0, {i})")
            time.sleep(2)
            i += 1080
            find_footer = driver.find_elements(By.TAG_NAME, 'footer')
            if find_footer:
                # with open('index.html', 'w', encoding='utf-8') as file:
                #     file.write(driver.page_source)
                # print('Данные успешно записанны в файл')
                # break
                print("Дно найдено!")
                return driver.page_source

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def collect_price(url, driver):
    try:
        driver.get(url=url)
        driver.maximize_window()
        time.sleep(5)
        return driver.page_source

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def parsing_html(url, driver):
    """
    Функция находит все ссылки на странице, и отбирает нужные

    :return: словарь вида Наименование: ссылка
    """
    # with open('index.html', 'r', encoding='utf-8') as file:
    #     s = file.read()
    retry = 3
    date = collect_html(url, driver, retry)
    dict_card = {}
    cards = []
    print(f"[...] Получаем данные с сайта")
    while True:
        soup = BeautifulSoup(date, 'lxml')
        cards = soup.find_all('a', class_='product-title__text', text=re.compile('Игровые наушники .+\s'))
        for card in cards:
            if card.get('href') is None:
                date = collect_html(url, driver, retry - 1)
                if date == 1:
                    raise 'Не удалось подключиться к сайту'
                dict_card = {}
                continue
            else:
                dict_card[card.text.strip()] = card.get('href')
        break

    print(len(cards))
    return dict_card, len(cards)


def parsing_price(data):
    """

    :return: цена товара
    """
    soup = BeautifulSoup(data, 'lxml')
    price = soup.find('span', class_="price__main-value")
    return price


def collect_json(page):
    result = []
    browser = 'chrome'
    for page in range(1, page + 1):
        url = f"https://www.mvideo.ru/naushniki-54/naushniki-3967/f/category=naushniki-polnorazmernye-1152/tolko-v-nalichii=da?page={page}"
        name_link, amount_card = parsing_html(url, set_driver(browser))
        for key, val in name_link.items():
            print(
                f"[INFO]\n"
                f"\tКарточек осталось: {amount_card}\n"
                f"\tОбрабатываемая ссылка: {val}"
            )
            price = None
            count = 1
            while price is None:
                time.sleep(30 + count ** 3)
                print(f"[-] Попытка сбора цены: {count}")
                html_p = collect_price(val, set_driver(browser))
                price = parsing_price(html_p)
                if count == 4:
                    print(f"[WARNING] С этого сайта не удалось получить цену: {val}")
                    break
                count += 1
            print(f"[+] Цена полученна: {price.text.strip()}")
            result.append(
                {
                    'title': key,
                    'link': val,
                    'price': price.text.strip()
                }
            )
            amount_card -= 1

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def main():
    # collect_json()
    url = 'https://www.mvideo.ru/komputernye-aksessuary-24/komputernye-naushniki-219/f/category=naushniki-igrovye-1115'
    # page = get_page(url, set_driver('chrome'))
    # collect_json(page)

    # print(parsing_html(url, set_driver('chrome')))

    site_requests('https://www.citilink.ru/catalog/naushniki-s-mikrofonom/')


if __name__ == '__main__':
    main()
