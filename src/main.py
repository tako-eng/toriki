#coding: UTF-8
from urllib import request
from urllib import error
from bs4 import BeautifulSoup
from logging import getLogger
import re
import contextlib
from model.excel_writer import ExcelWriter
from tk_logger import initialize_logger
from model.toriki_menu import TorikiMenu
logger = getLogger(__name__)

base_url = "https://www.torikizoku.co.jp/"
file_name = "../menu.xlsx"


def root_scraping():
    url = base_url + 'menu/'
    html = request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    main_menu_box = soup.find("div", attrs={"class","img2col clearfix"})
    menu_list = main_menu_box.find_all("a", href=re.compile("/menu/+"))

    target_urls = [item.attrs['href'] for item in menu_list]

    all_menu = {}
    id = 1
    # set menu items
    for url in target_urls:
        category = url.split("/")[2]
        items = get_menu_from_one_category(url)
        menu_buffer = []

        for i in range(len(items)):
            toriki_menu = TorikiMenu(
                id=id,
                name=items[i]['name'],
                price=280,
                description=items[i]['description'],
                category=url.split("/")[2])
            menu_buffer.append(toriki_menu)
            id = id + 1
        all_menu[category] = menu_buffer

    # write all
    with ExcelWriter(file_name) as writer:
        writer.writeHeader(headers=(["ID", "カテゴリ", "名前", "価格", "説明"]))
        for k in all_menu:
            writer.write(all_menu[k])

    logger.debug("complete")



def get_menu_from_one_category(path="/"):

    if path == "/":
        return root_scraping()

    target_url = base_url + path
    html = request.urlopen(target_url)

    soup = BeautifulSoup(html, "html.parser")
    main_menu = soup.find("div", attrs={"class",re.compile("mlBox clearfix.?")})
    if not main_menu:
        return []
    menu = main_menu.find_all("li")
    menu_name_list = []
    for item in menu:
        name_element = item.find("h5")
        name = name_element.string
        if not name:
            continue
        description_element = item.find("p")
        if not description_element:
            description = ""
        else :
            description = description_element.string
        menu_name_list.append(({
            "name": name,
            "description": description
        }))
    return menu_name_list

if __name__ == "__main__":
    initialize_logger()
    root_scraping()
