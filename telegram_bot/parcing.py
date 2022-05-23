import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def collect_date():
    url = 'https://www.mvideo.ru/naushniki-54/naushniki-3967/f/category=naushniki-polnorazmernye-1152/tolko-v-nalichii=da'
    s = requests.Session()
    r = requests.get(url=url, headers=headers)
    print(r.text)
    # with open('index.html', 'w', encoding='utf-8') as file:
    #     file.write(r.text)
    soup = BeautifulSoup()

def main():
    collect_date()


if __name__ == '__main__':
    main()

