
# Internet Market

## Project Structure
```
PASSAGE/
├── config/
│   ├── __init__.py
│   ├── classes.py
│   ├── logging.conf
│   ├── settings.py
│   ├── schema.py
│   └── .env
│
├── mongodb/
│   ├── __init__.py
│   ├── client.py
│   └── connection.py
│
├── testsing/
│   ├── __init__.py
│   └── requests.http
│
├── venv/
│
├── __init__.py
├── README.md
├── requirements.txt
└── webapp.py
```

## Libraries and frameworks
- [FastAPI](https://fastapi.tiangolo.com/)
-  Rich
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Argparse](https://docs.python.org/3/library/argparse.html)
- [Logging](https://docs.python.org/3/library/logging.html)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Uvicorn](https://www.uvicorn.org/)
- [HTTPX](https://www.python-httpx.org/)

## Usage
```bash
$ python3 webapp.py --help
usage: webapp.py [-h] [--title TITLE] [--sku SKU] [--color COLOR] [--brand BRAND] [--type TYPE] [--category CATEGORY] [--country COUNTRY] [--price PRICE] [--size {show,hide}] [--output {json,table}] [--limit {one,all}]

