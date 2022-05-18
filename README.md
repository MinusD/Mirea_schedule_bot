# Mirea schedule bot

[//]: # (![MinusD]&#40;https://habrastorage.org/webt/4n/x6/kx/4nx6kxyw0pfm0pvtuhpyhsw0dpq.png&#41;)

## Возможности
Бот может показать расписания на сегодня, завтра, текущую неделю и тд. 
А так же может показать расписание преподавателей


## Подготовка среды
+ Python 3.10 или новее

```shell
pip install vk_api 

pip install openpyxl 

pip install requests 

pip install matplotlib 

pip install bs4 
```

Так же необходимо запустить файл ```preparation.py```. Он создаст необходимые файлы и таблицы в базе данных.

## Примечание
Бот писался как домашнее задания по Ознакомительной практике, 
поэтому функционал ограничен, команды работают только для первых трёх курсов ИИТ, 
а так же, могу быть баги, т.к. проводилось только alpha тестирование. 

Если нашли баг, 
[напишите администратору](https://vk.com/minusd).

Удобный сайт с расписание: [mbc-d.ru/schedule](https://mbc-d.ru/schedule)


### [License](./LICENSE)