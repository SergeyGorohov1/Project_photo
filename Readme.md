# Проект: Слайдер-галерея
Данный проект реализует одностраничный сайт с адаптивной вёрсткой на Bootstrap 5
и слайдером изображений на Slick Slider. Фотографии для слайдера загружаются через
админ панель Django, с использованием django-filer. В админке реализован понятный интерфейс,
в том числе, удобная сортировка записей с помощью django-admin-sortable2. При клике на изображение
открывается галерея с возможностью пролистывания фотографий.

## Стэк технологий
* Python 3.12
* Django 5.2
* MySQL
* Bootstrap 5
* Slick Slider
* django-filer
* django-admin-sortable2

## Установка и настройка
* Склонируйте репозиторий
```bash
git clone git@github.com:SergeyGorohov1/Project_photo.git .
```
* Создайте и активируйте виртуальное окружения 
```bash
python -m venv .venv
source .venv/bin/activate      # для Linux/macOS
.venv\Scripts\activate         # для Windows
```
* Установите необходимые зависимости
```bash
pip install -r req.pip
```
* Создайте и заполните файл с переменными окружения (.env) в корне проекта, на основе шаблона переменных окружения .env.template
* Примените миграции
```bash
python manage.py migrate
```
* При необходимости, создайте суперпользователя
```bash
python manage.py createsuperuser
```
* Запустите сервер
```bash
python manage.py runserver
```
Приложение будет доступно по адресу http://127.0.0.1:8000/