import asyncio
import aiohttp
from bs4 import BeautifulSoup
from re import compile
from fake_useragent import UserAgent as ua
import csv


async def fetch(session, url):
    async with session.get(url, headers={'User-Agent': ua().random}) as response:
        return await response.text()


def write_data(data: dict):
    with open('week-6/files/realitika.csv', 'w', newline='', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


async def parse_items_from_link(session, link):
    html = await fetch(session, link)
    soup = BeautifulSoup(html, 'html.parser')
    found_items = {
        'id': None,
        'title': None,
        'city': None,
        'location': None,
        'beds_number': 0,
        'bathrooms': 0,
        'price': 0.0,
        'living_area': 0.0,
        'land_area': 0.0,
        'parking_places': 0,
        'distance_from_sea': 0,
        'new_construction': False,
        'air_conditioning': False,
        'link': link,
        'mobile_phone': None,
        'last_update': None
    }

    add_key_value(found_items, 'id', 'Oglas Broj', soup)
    add_key_value(found_items, 'title', 'Vrsta', soup)
    add_key_value(found_items, 'city', 'Područje', soup)
    add_key_value(found_items, 'location', 'Adresa', soup)
    add_key_value(found_items, 'beds_number', 'Spavaćih Soba', soup)
    add_key_value(found_items, 'bathrooms', 'Kupatila', soup)
    add_key_value(found_items, 'price', 'Cijena', soup)
    add_key_value(found_items, 'living_area', 'Stambena Površina', soup)
    add_key_value(found_items, 'land_area', 'Zemljište', soup)
    add_key_value(found_items, 'parking_places', 'Parking Mjesta', soup)
    add_key_value(found_items, 'distance_from_sea', 'Od Mora (m)', soup)
    add_key_value(found_items, 'published_by', 'Oglasio', soup)
    add_key_value(found_items, 'mobile_phone', 'Mobitel', soup)
    add_key_value(found_items, 'last_update', 'Zadnja Promjena', soup)
    item = soup.find('strong', string='Novogradnja')
    if item:
        found_items['new_construction'] = True
    item = soup.find('strong', string='Klima Uređaj')
    if item:
        found_items['air_conditioning'] = True

    return found_items


async def parse_page(session, url):
    soup = BeautifulSoup(await fetch(session, url), 'html.parser')
    found_divs = soup.find_all('a', href=compile(r"https://www.realitica.com/hr/listing/\d+"))
    links = set()
    for elem in found_divs:
        links.add(elem['href'])

    tasks = [parse_items_from_link(session, link) for link in links]

    return await asyncio.gather(*tasks)


def add_key_value(found_items: dict, key_name: str, text: str, soup: BeautifulSoup):
    item = soup.find('strong', string=text)
    if not item:
        return

    item = item.find_next_sibling(string=True)
    if not item:
        return

    if text == 'Oglasio':
        item = item.find_next_sibling(name='a')
        if not item.get('href'):
            return
        found_items[key_name] = item.get('href').replace('/', '').strip()
        return

    value = item.replace(':', '').strip()
    if value.isdigit():
        found_items[key_name] = int(value)
        return
    try:
        temp = None
        if '€' in value:
            temp = value.replace('€', '').replace('.', '')
        elif 'm' in value:
            temp = value.replace('m', '').replace('.', '')
        float(temp)
        if temp:
            found_items[key_name] = float(temp)
        elif value:
            found_items[key_name] = float(temp)
    except:
        found_items[key_name] = value


async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            f'https://www.realitica.com/?cur_page={i}&for=Prodaja&pZpa=Istra&pState=hrvatska&type%5B%5D=&since-day=p-anytime&qob=p-default&lng=hr'
            for i in range(43)]

        tasks = [parse_page(session, url) for url in urls]
        res = await asyncio.gather(*tasks) # returns structure [[{}], [{}], .., [{}]]

    new_res_structure = []
    for nested_arr in res:
        for dict_elem in nested_arr:
            new_res_structure.append(dict_elem)
    new_res_structure.sort(key=lambda x: (x['price'], x['living_area']), reverse=True)
    write_data(new_res_structure)


if __name__ == '__main__':
    asyncio.run(main())
