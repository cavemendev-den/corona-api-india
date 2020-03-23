import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd
URL = "https://www.mohfw.gov.in/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
def get_head_info():
    head_info = soup.findAll('div', attrs = {'class':'iblock'})
    main_info  = {}
    for item in head_info:
        title = item.find('div',attrs={'class':'info_label'}).text
        count = item.find('div',attrs={'class':'iblock_text'}).find('span').text
        title = title.replace("*","Active COVID 2019 cases")
        main_info.update({title:count})
    return main_info
def get_statewise_info():
    state_table = soup.findAll('table')[1]
    table_headings = state_table.findAll('th')
    titles = []
    for heading in table_headings:
        title = heading.find("strong").text
        titles.append(title)
    table_body = soup.findAll("tbody")[1]
    rows = table_body.findAll("tr")
    to_be_dataframe = []
    for row in rows:
        row_record = []
        for td in row:
            if isinstance(td,bs4.element.Tag):
                td_text = td.text.replace("\n","").replace("    ","").replace(" *","")
                row_record.append(td_text)
        if len(row_record) < 6:
            row_record = [int(to_be_dataframe[-1][0])+1] + row_record
        to_be_dataframe.append(row_record)

    df = pd.DataFrame(to_be_dataframe)
    df.columns = ["id"] + titles[1:]
    print()
    return df


get_statewise_info()
