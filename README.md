<div align=center>

   # Project *`api_currency_conversion`*

   ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
   ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  
</div>

## Description:
The application allows you to receive the current dollar to ruble exchange rate and also store the last 10 queries.
The pause between requests is 10 seconds.

## Installation:
1. Clone the repository:
```bash
git clone git@github.com:bannybaks/api_currency_conversion.git
```
2. Go to the project directory:
```bash
cd api_currency_conversion
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage:
1. Launch the application with the command:
```bash
python manage.py runserver
```
2. In the browser address bar (as an example of use), enter:
```html
http://127.0.0.1:8000/api/get-current-usd/
```
<div align=center>

#### Structure of a response to a request like `GET /api/get-current-usd/`:

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
     // Other entries...
   ]
}

```
