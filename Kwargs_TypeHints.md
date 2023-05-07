# Kwargs and Type Hints

## Define a function №1. Simple Example - Junior Level.

```python
def car(model, car, engine_capacity, year, used, price):
    print(f'Model:      {model}')
    print(f'Car:        {car}')
    print(f'Engine:     {engine_capacity}')
    print(f'Year:       {year}')
    print(f'Used:       {used}')
    print(f'Price:      {price}')

car('BMW', 'X5', 3.0, 2021, True, 1000000)
```
**Result:**
```
Model:      BMW
Car:        X5
Engine:     3.0
Year:       2021
Used:       True
Price:      1000000
```


## Define a function №2.1. Using **kwargs:
```python
def car(**kwargs):
    print(f'Model:      {kwargs["model"]}')
    print(f'Car:        {kwargs["car"]}')
    print(f'Engine:     {kwargs["engine_capacity"]}')
    print(f'Year:       {kwargs["year"]}')
    print(f'Used:       {kwargs["used"]}')
    print(f'Price:      {kwargs["price"]}')

car(model='Audi', car='A6', engine_capacity=2.0, year=2020, used=False, price=2000000)
```

**Result:**
```
Model:      Audi
Car:        A6
Engine:     2.0
Year:       2020
Used:       False
Price:      2000000
```


## Define a function №2.2. Using **kwargs and dictionary:
```python
def car(**kwargs):
    print(f'Model:      {kwargs["model"]}')
    print(f'Car:        {kwargs["car"]}')
    print(f'Engine:     {kwargs["engine_capacity"]}')
    print(f'Year:       {kwargs["year"]}')
    print(f'Used:       {kwargs["used"]}')
    print(f'Price:      {kwargs["price"]}')

mazda = {'model': 'Mazda', 'car': 'CX-5', 'engine_capacity': 2.5, 'year': 2019, 'used': True, 'price': 1500000}

car(**mazda)
```

**Result:**
```
Model:      Mazda
Car:        CX-5
Engine:     2.5
Year:       2019
Used:       True
Price:      1500000
```

## Define a function №3. Using **kwargs and Type Hint:
```python
def car(**kwargs: dict) -> str:
    model   = kwargs['model']
    car     = kwargs['car']
    engine  = kwargs['engine']
    year    = kwargs['year']
    price   = kwargs['price']

    msg = f"You bought a car {model} {car} {engine}, {year} year -- ${price}!"
    
    return msg

ford = {'model': 'Ford', 'car': 'Focus', 'engine': 1.6, 'year': 2022, 'price': 15000}

result = car(**ford)

print(result)
```

**Result:**
```
You bought a car Ford Focus 1.6, 2022 year -- $15000!
```



## Define a function №4. Using **kwargs and Type Hint in function.
```python
def car(**kwargs: dict) -> dict:
    model:str    = kwargs['model']
    car:str      = kwargs['car']
    engine:float = kwargs['engine']
    year:int     = kwargs['year']
    price:int    = kwargs['price']
    
    return {'model': model, 'car': car, 'engine': engine, 'year': year, 'price': price}

hummer = {'model': 'Hummer', 'car': 'H2', 'engine': 6.2, 'year': 2021, 'price': 100000}

result = car(**hummer)
print(result)
```
**Result:**
```log
{'model': 'Hummer', 'car': 'H2', 'engine': 6.2, 'year': 2021, 'price': 100000}
```

from typing import Any, List


## Define a function №5. Using **kwargs and Type Hinting
```python
from typing import Any, List

def car(**kwargs: Any) -> List[str]:
    model:str    = kwargs['model']
    car:str      = kwargs['car']
    color:str    = kwargs['color']

    return [model, car, color]
    
  
hummer = {'model': 'Hummer', 'car': 'H2', 'color': 'yellow'}

result = car(**hummer)
print(result)
```

**Result:**
```log
['Hummer', 'H2', 'yellow']
```


## Define a function №6. 
```python
from typing import Any, List, Dict, Union


def car(**kwargs: Dict[str, Union[str, int, float]]) -> List[Any]:
    model:str    = kwargs['model']
    car:str      = kwargs['car']
    engine:float = kwargs['engine']
    year:int     = kwargs['year']

    return [model, car, engine, year]
    

hummer = {'model': 'Hummer', 'car': 'H2', 'engine': 6.2, 'year': 2007}

result = car(**hummer)
print(result)
```

**Result:**
```log
['Hummer', 'H2', 6.2, 2007]
```
