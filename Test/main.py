import datetime

import requests
import openpyxl
import pickle
import re
from bs4 import BeautifulSoup
import src.cfgs.system_config as scfg

if __name__ == '__main__':
    region = 'Татарстан'
    page = requests.get(scfg.CORONA_STAT_URL + '/country/russia')  # Получаем страницу
    soup = BeautifulSoup(page.text, "html.parser")  # Парсим её
    result = soup.findAll('div', {'class': 'c_search_row'})
    d = ''
    for x in result:
        tmp = x.find('span', 'small').find('a')
        if region.title() in tmp.getText().split(' '):
            rg = tmp.getText()
            d = tmp.get('href')
    print('URL:', scfg.CORONA_STAT_URL + d)
    page = requests.get(scfg.CORONA_STAT_URL + d)  # Получаем страницу
    soup = BeautifulSoup(page.text, "html.parser")  # Парсим её
    result = soup.find(string='Прогноз заражения на 10 дней').find_parent('div',
                                                                          {'class': 'border rounded mt-3 mb-3 p-3'})
    status = result.find('h6', 'text-muted').getText()[:-17]
    print(status)
    print(rg)

    # result = soup.find(string="Институт информационных технологий").find_parent("div").find_parent("div").findAll(
    #     'a', {'class': 'uk-link-toggle'})

    # course_pattern = r'([1-3]) курс'
    # for x in result:
    #     course = x.find('div', 'uk-link-heading').text.lower().strip()
    #     course_number = re.match(course_pattern, course)
    #     if course_number:
    #         course_number = course_number.group(1)
    #         f = open(f'{scfg.DATA_DIR}{scfg.SCHEDULE_BASE_NAME}{course_number}.xlsx', "wb")
    #         link = x.get('href')
    #         resp = requests.get(link)  # запрос по ссылке
    #         f.write(resp.content)  # Записываем контент в файл
    #         f.close()
    # self.last_schedule_file_update = time.time()
    # Debug('Update schedule files', key='UPD')
    # self._parse_schedule_file()

    # response = requests.get(
    #     'https://api.openweathermap.org/data/2.5/weather?q=moscow&appid=483841295963b30a56e7679ae38f99e1&units=metric'
    #     '&lang=ru')
    # info = response.json()
    # print(info)
    # temp = info["main"]["temp"]
    # print(temp)
    # now = datetime.datetime.now()
    # print(now.isocalendar())

    # a = [i for i in range(10)]
    # for i in range(len(a)):
    #     if i % 2 == 0:
    #         del a[i]
    # for i in range(len(a)):
    #     print(a[i])
    # s = '123\n321'
    # a = '123'
    # d = s.split('\n')
    # d.append('213')
    # print(' - '.join(d))
    # print(' - '.join(a.split('\n')))

    # data = ['Структуры и алгоритмы обработки данных',
    #         '4,8,12,16 н. Физика (1 п/г)\n4,8,12,16 н. Физика (2 п/г)',
    #         'кр. 12 н. Объектно-ориентированное программирование',
    #         'кр. 1,3 н. Ознакомительная практика']
    #
    # custom_week_pattern_1 = r'([\d\,]+) н. ([^\\]+)'
    # custom_week_pattern = r'кр. ([\d\,]+) н. ([^\\]+)'
    #
    # for a in data:
    #     s = re.search(custom_week_pattern, a)
    #     if s:
    #         d = s.group(1).split(',')
    #         print(d)
    #         print(s.group(2))
    #     else:
    #         s = re.search(custom_week_pattern_1, a)
    #         if s:
    #             d = s.group(1).split(',')
    #             print('есть', d)
    #             print(s.group(2))

    # print(re.search(custom_week_pattern, text1))
    # print(re.search(custom_week_pattern, text2))
    # print(re.search(custom_week_pattern, text3))
    # print(re.search(custom_week_pattern, text4))

    # group_slug = "ИКБО-30-21"
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
    pass

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
