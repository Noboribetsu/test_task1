## Description:
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

Стек
* Django/Django-boostrap4/Django REST framework
* PostgreSQL

[Demo on Heroku](https://obscure-garden-24670.herokuapp.com/)

### API:

[Api](https://obscure-garden-24670.herokuapp.com/api/employees/)

/api/employees/

Allow: GET, POST, HEAD, OPTIONS

/api/employees/id

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS


#### Usage:
```bash
curl -H 'Accept: application/json; indent=4' https://obscure-garden-24670.herokuapp.com/api/employees/
{
    "count": 7500,
    "next": "https://obscure-garden-24670.herokuapp.com/api/employees/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "fullname": "Darlene Hawkins",
            "position": "Insurance account manager",
            "salary": "76349.05",
            "employment_date": "2022-01-30",
            "supervisor": null,
            "subordinates": [
                1288,
                1369
            ]
        },
        {
            "id": 2,
            "fullname": "Traci Shaffer",
            "position": "Lighting technician, broadcasting/film/video",
            "salary": "80085.74",
            "employment_date": "2020-08-24",
            "supervisor": null,
            "subordinates": []
        },
.......
}
```
```bash
curl -H 'Accept: application/json; indent=4' https://obscure-garden-24670.herokuapp.com/api/employees/2
{
    "id": 2,
    "fullname": "Traci Shaffer",
    "position": "Lighting technician, broadcasting/film/video",
    "salary": "80085.74",
    "employment_date": "2020-08-24",
    "supervisor": null,
    "subordinates": []
}
```

### Requrements:
* Python 3.10+
* Poetry
* GNU Make

### Setup:
```bash
make setup
```
### Fullfill .env:
See .env.example

### Run server:
```bash
make start
# Open http://0.0.0.0:8000/
```
### Seed your DB:
```bash
make seed
# You can choose number of records see employees/scripts/db_seed.py
```
