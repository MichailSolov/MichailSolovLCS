from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote


def make_workspace():
    ur_req = "Программист"
    url = "https://www.avito.ru/tatarstan/rabota?q=" + quote(ur_req)
    req = urllib.request.urlopen(url)
    html = req.read()

    soup = BeautifulSoup(html, "html.parser")
    vacancies = soup.find_all('div', class_='snippet-horizontal')
    return vacancies


def main_page_parsing():
    results = []
    for i in make_workspace():
        results.append({
            'title': i.a.get('title'),
            'href': i.a.get('href'),
            'city': i.find('span', class_='item-address-georeferences-item__content').get_text(strip=True),
            'kind': i.find('div', class_='data').find('p').get_text(strip=True),
            'price': i.find('span', attrs={"itemprop": "offers"}).get_text(strip=True)
        })
        url_second = 'https://www.avito.ru' + results[len(results) - 1]['href']
        results[len(results) - 1]['info'] = second_page_parsing(url_second)

    return results


def make_workspace_for_second(url):
    req = urllib.request.urlopen(url)
    html = req.read()

    soup = BeautifulSoup(html, "html.parser")
    vacancies_info = soup.find_all('ul', class_='item-params-list')
    return vacancies_info


def second_page_parsing(url):
    results = []
    for i in make_workspace_for_second(url):
        info = i.find_all('li', class_='item-params-list-item')
        for j in info:
            results.append({
                j.get_text(strip=True)
            })
    return results


def get_results_file():

    with open('txt.txt', 'w', encoding="utf-8") as f:
        for i in main_page_parsing():
            f.write(f'title: {i["title"]}\nhref: {i["href"]}\ncity: {i["city"]}\n'
                    f'kind: {i["kind"]}\nprice: {i["price"]}\nother info: {i["info"]}\n\n\n')


if __name__ == '__main__':
    get_results_file()
    exit()

