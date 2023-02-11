# Objects (Объекты)
Объект - этой контейнер состоящий из:
1. Данных (Attributes) и состояний
2. Поведения (Method)

По содержимому можно определить тип данных

## Пример 1 - list
**Attributes:** - значения в списке
```python
mylist = ["BMW","Kia", "Audi", "Ford"]
print(type(mylist))   # <class 'list'>
```

**Methods:** Возможные поведения для списка
```python
mylist.count()
mylist.append()
mylist.sort()
mylist.pop()
mylist.index()
mylist.remove()
mylist.insert()
mylist.extend()
mylist.copy()
mylist.clear()
```

**Examples:**
```python
print(mylist)               # ['BMW', 'Kia', 'Audi', 'Ford']
print(mylist.count("BMW"))  # 1
print(mylist.index("BMW"))  # 0

newlist = mylist.copy()     # ['BMW', 'Kia', 'Audi', 'Ford']

mylist.append("Nissan")     # ['BMW', 'Kia', 'Audi', 'Ford', 'Nissan']
mylist.sort()               # ['Audi', 'BMW', 'Ford', 'Kia', 'Nissan']
mylist.pop()                # ['Audi', 'BMW', 'Ford', 'Kia']
mylist.remove("BMW")        # ['Audi', 'Ford', 'Kia']
mylist.insert(0, "Dodge")   # ['Dodge', 'Audi', 'Ford', 'Kia']
mylist.extend(mylist)       # ['Dodge', 'Audi', 'Ford', 'Kia', 'Dodge', 'Audi', 'Ford', 'Kia']
mylist.extend(mylist)       # []
```


## Пример 2 - int
**Attributes:** - значение целое число
```python
mynumber = 1999
print(type(mynumber)) # <class 'int'>
```

**Methods:** Возможные поведения для целых чисел
```python
mynumber.to_bytes()
mynumber.conjugate()
mynumber.as_integer_ratio()
mynumber.bit_count()
mynumber.bit_length()
mynumber.from_bytes()
```

# Class
```python
class Person:
  name = 'Jared'
  age = 30

print(Person.name)
print(Person.age)
```
name и age - являются Attribute, при обращении к классу:
Class.attribute