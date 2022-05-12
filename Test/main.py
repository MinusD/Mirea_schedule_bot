import requests
import openpyxl
import pickle
import re
from bs4 import BeautifulSoup
import src.cfgs.system_config as scfg

if __name__ == '__main__':
    group_slug = "ИКБО-30-21"
    # book = openpyxl.load_workbook(
    #     f'../{scfg.DATA_DIR}{scfg.SCHEDULE_BASE_NAME}{1}.xlsx')  # открытие файла
    # sheet = book.active  # активный лист
    # num_cols = sheet.max_column  # количество столбцов
    # num_rows = sheet.max_row  # количество строк
    # data = []
    # last_group = 0
    # for i in range(6, num_cols):
    #     if last_group >= 4:
    #         last_group = -1
    #         continue
    #     tmp = []
    #     for j in range(2, 75):
    #         v = str(sheet.cell(column=i, row=j).value)
    #         if j == 2 and re.match(scfg.GROUP_PATTERN, v):
    #             last_group = 0
    #         tmp.append(v)
    #     if last_group != -1:
    #         data.append(tmp)
    #         last_group += 1
    # # print(data)
    # for a in data:
    #     # print(a)
    #     print(a[0])
    # with open('data.pickle', 'wb') as f:
    #     pickle.dump(data, f, fix_imports=True)
    # del data


    # print('dd')
    #
    # a = int(input())
    # cell = sheet.cell(row=2, column=(i + 1))
    #
    # if sheet.cell(row=2, column=(i + 1)).value == group_slug:
    #     print(i + 1)

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

# book = openpyxl.load_workbook("file.xlsx")  # открытие файла
# sheet = book.active  # активный лист
# num_cols = sheet.max_column  # количество столбцов
# num_rows = sheet.max_row  # количество строк
# for i in range(num_cols):
#     group_name_pattern = r''
#     cell = sheet.cell(row=2, column=i+1).value
#     print(cell)
#         # cell = sheet.cell(row=1, column=1).value
#         # print(cell)
#     # print(x.find('div', 'uk-link-heading').text.strip())
#     # if x.find(string='1 Курс'):
#     #     print(x)
#     # if x.find('a', 'uk-link-toggle')
#     # if ...:  # среди всех ссылок найти нужную
#     # f = open("file.xlsx", "wb")  # открываем файл для записи, в режиме wb
#     # resp = requests.get(...)  # запрос по ссылке
#     # f.write(resp.content)
