### Description:
Создайте веб страницу, которая будет выводить иерархию сотрудников в
древовидной форме.
* Информация о каждом сотруднике должна храниться в базе данных и
содержать следующие данные:
  * ФИО;
  * Должность;
  * Дата приема на работу;
  * Размер заработной платы;
  * У каждого сотрудника есть 1 начальник;
* База данных должна содержать не менее 50 000 сотрудников и 5 уровней
иерархий.
* Не забудьте отобразить должность сотрудника

[Demo on Heroku](https://obscure-garden-24670.herokuapp.com/)

### Requrements:
* Python 3.9+
* Poetry
* GNU Make

### Setup:
```bash
make setup
```
### Run server:
```bash
make start
# Open http://0.0.0.0:8000/
```
### Seed your DB:
```bash
make seed
# You can choose number of records see /scripts/db_seed.py
```
