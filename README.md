# Проект Brendwall-app
Проект представляет собой 2 отдельных приложения (API и Фронтенд-часть). 
API предназначено для получения всех товаров из базы данных/добавления товара в базу.
Фронтенд реализован в виде SPA и позволяет отправлять запросы к API для добавления товаров и получать список всех товаров.

СУБД - SQLite. 


## Стек:
Backend-часть: Python + Django, DRF, SQLite3
Фронтенд-часть: JavaScript + React, Fetch API.

## Инструкция по запуску:
Клонировать репозиторий и перейти в него в командной строке:
  
```
git@github.com:VDronovVladislav/BW-app.git
```
Cоздать и активировать виртуальное окружение:
  
```
python -m venv venv
```

* Если у вас Linux/macOS

```
source venv/bin/activate

```

* Если у вас windows

```
source venv/Scripts/activate

```
Перейти в директорию backend-приложения и запустить его:
```
cd bwapp
python manage.py runserver
```
Перейти в директорию frontend-приложения и запустить его:
```
cd bw-frontend
npm start
```

Лиценция:
```
MIT License
```
