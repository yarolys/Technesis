# Тестовая задача для Technesis

Телеграм-бот для сбора данных с сайтов и расчета средних цен на товары.

## Возможности

- Загрузка Excel-файлов с данными для парсинга сайтов
- Хранение информации о сайтах в базе данных PostgreSQL


## Требования

- Python 3.12+
- Токен Telegram бота ([@BotFather](https://t.me/BotFather))

## Установка

1. Клонируйте репозиторий
2. Установите необходимые пакеты:
```bash
pip install poetry
poetry install
poetry shell
```

3. Создайте файл `.env` (подробнее в .env example):


## Использование

1. Запустите бота:
```bash
python run.py
```

2. В Telegram отправьте команду `/start`

3. Загрузите Excel-файл, используя кнопку "Загрузить файл". Excel-файл должен содержать следующие столбцы:
   - `title`: Название сайта/магазина
   - `url`: URL страницы товара
   - `xpath`: XPath для элемента с ценой



## Структура проекта

```
├── alembic.ini
├── docker-compose.yaml
├── dockerfile
├── logs
│   └── log.log
├── pgdata
├── poetry.lock
├── pyproject.toml
├── README.md
├── run.py
└── src
    ├── config.py
    ├── database
    │   ├── connection.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── env.py
    │   │   ├── __pycache__
    │   │   │   └── env.cpython-312.pyc
    │   │   ├── README
    │   │   ├── script.py.mako
    │   │   └── versions
    │   │       ├── 54984f944968_add_column_for_currency.py
    │   │       ├── 8b81d3a4ec26_create_table.py
    │   │       └── __pycache__
    │   │           ├── 54984f944968_add_column_for_currency.cpython-312.pyc
    │   │           └── 8b81d3a4ec26_create_table.cpython-312.pyc
    │   ├── models
    │   │   ├── __pycache__
    │   │   │   ├── example_database_module.cpython-312.pyc
    │   │   │   └── website.cpython-312.pyc
    │   │   └── website.py
    │   └── __pycache__
    │       ├── connection.cpython-312.pyc
    │       └── __init__.cpython-312.pyc
    ├── handlers
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-312.pyc
    │   │   └── start.cpython-312.pyc
    │   ├── start.py
    │   └── user_panel
    │       ├── __pycache__
    │       │   └── user_panel.cpython-312.pyc
    │       └── user_panel.py
    ├── __pycache__
    │   └── config.cpython-312.pyc
    ├── schemas.py
    └── utils
        ├── filter.py
        └── keyboard
            ├── admin.py
            ├── __pycache__
            │   └── user.cpython-312.pyc
            └── user.py
```

## Зависимости

(В pyproject.toml)


## Формат Excel-файла

Excel-файл должен содержать следующие обязательные столбцы:
- `title`: Название магазина или сайта
- `url`: Полный URL страницы с товаром
- `xpath`: Путь XPath к элементу, содержащему цену

Пример содержимого файла:
| title | url | xpath |
|-------|-----|-------|
| Книга | https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html | //p[@class="price_color"]/text() |

ну и т.п.