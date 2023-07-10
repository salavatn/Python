# Internet Market

## Project Structure
```python
PASSAGE/
├── config/                 
│   ├── __init__.py
│   ├── classes.py          # Config classes
│   ├── logging.conf        # Logging configuration
│   ├── settings.py         # Settings
│   ├── schema.py           # Pydantic models
│   └── .env                # Environment variables
│
├── mongodb/                
│   ├── __init__.py
│   ├── client.py           # MongoDB client
│   └── connection.py       # MongoDB connection
│
├── testsing/
│   ├── __init__.py
│   └── requests.http       # HTTP requests
│
├── venv/
│
├── __init__.py
├── README.md
├── requirements.txt
└── webapp.py               # FastAPI application
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
