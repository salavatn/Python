# Lib Faker

## Installation

```bash
pip install -r requirements.txt
```

## Demo run

```bash
python demo.py
```
```
{'firstname': 'Tyler', 'lastname': 'Scott', 'balance': 114638, 'birth_date': '1947-08-30', 'email': 'jennifer56@brown.net'}
```

## Usage

1. Import the library
    ```python
    from faker import Faker
    ```
2. Create an instance of the Faker class
    ```python
    fake = Faker('en_EN')
    ```
3. Use the instance to generate fake data
    ```python
    print(fake.name())
    ```
    ```
    'Tyler Scott'
    ```