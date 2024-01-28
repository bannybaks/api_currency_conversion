<div align=center>

  # Проект *`api_currency_conversion`*

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  
</div>

## Описание:
Приложение позволяет получать актуальный курс доллара к рублю и также хранить 10 последних запросов.
Пауза между запросами составляет 10 секунд.

## Установка:
1. Склонируйте репозиторий:
```bash
git clone git@github.com:bannybaks/api_currency_conversion.git
```
2. Перейдите в дирректорию проекта:
```bash
cd api_currency_conversion
```
3. Установите зависимости:
```bash
pip install -r requiremments.txt
```

## Использование:
1. Запустите приложение командой:
```bash
python manage.py runserver
```
2. В адресной строке браузера (как пример использования) введите:
```html
http://127.0.0.1:8000/api/get-current-usd/
```
<div align=center>

#### Структура ответа на запрос вида `GET /api/get-current-usd/`:

</div>

```json
{
  "exchange_rate": 89.907903,
  "latest_requests": [
    {
      "date": "2024-01-27",
      "time": "18:07:33",
      "exchange_rate": 89.907903
    },
    {
      "date": "2024-01-27",
      "time": "18:17:45",
      "exchange_rate": 89.912345
    },
    // Другие записи...
  ]
}

```





