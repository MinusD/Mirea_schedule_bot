import requests
import openpyxl
from bs4 import BeautifulSoup

# page = requests.get("https://www.mirea.ru/schedule/")
#
# soup = BeautifulSoup(page.text, "html.parser")
# # print(soup)
# # print(soup.find('div'))
# # result = soup.find(string="Институт информационных технологий").find_parent("div").find_parent("div").findAll('a')
# result = soup.find(string="Институт информационных технологий").find_parent("div").find_parent("div").findAll('a', {
#     'class': 'uk-link-toggle'})
# # print(result)
# for x in result:
#     if x.find('div', 'uk-link-heading').text.strip() == '1 курс':
#         f = open("file.xlsx", "wb")
#         link = x.get('href')
#         resp = requests.get(link)  # запрос по ссылке
#         f.write(resp.content)

book = openpyxl.load_workbook("file.xlsx")  # открытие файла
sheet = book.active  # активный лист
num_cols = sheet.max_column  # количество столбцов
num_rows = sheet.max_row  # количество строк
for i in range(num_cols):
    group_name_pattern = r''
    cell = sheet.cell(row=2, column=i+1).value
    print(cell)
        # cell = sheet.cell(row=1, column=1).value
        # print(cell)
    # print(x.find('div', 'uk-link-heading').text.strip())
    # if x.find(string='1 Курс'):
    #     print(x)
    # if x.find('a', 'uk-link-toggle')
    # if ...:  # среди всех ссылок найти нужную
    # f = open("file.xlsx", "wb")  # открываем файл для записи, в режиме wb
    # resp = requests.get(...)  # запрос по ссылке
    # f.write(resp.content)
