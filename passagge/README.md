# Report every 2 hours:

## Part-01
* Формирование структуры проекта
* Анализ JSON файла и выбор в качестве Database - MongoDB 
* Регистрация и изучение работы с MongoDB (first time)
* Загрузил в MongoDB содержимое data.json:
```log
2023-05-18 00:03:07:03S - root - INFO - Connected successfully to MongoDB!
2023-05-18 00:03:07:03S - root - INFO - Count of documents in collection: 20625
```

* Изучение фильтров в MongoDB:
   - Сформировать фильтр по двум параметрам   `filter = {"title": "юбка", "price": 37500}`
   - Получить первую запись по фильтру `documents = collection.find_one(filter)`


* Анализ JSON + [Боевые данные](https://ppassage.com/product/iubka-acne-studios-fn-wn-skir000099-oranzhevyi/):

```python
{
    '_id': ObjectId('6465404fe4a9c7ea27f62220'), 
    'title': 'юбка', 
    'sku': 'FN-WN-SKIR000099', 
    'color': 'DUSTYORANGE/персиковый', 
    'brand': 'Acne Studios', 
    'sex': 'Ж', 
    'material': ' 100% полиэстер', 
    'size_table_type': 'Одежда Ж Германия', 
    'root_category': 'Одежда без маркировки', 
    'fashion_season': '2019-2', 
    'fashion_collection': 'Acne Studios Donna FW 2019', 
    'fashion_collection_inner': 'Acne Studios Womens RTW Main', 
    'manufacture_country': 'КИТАЙ', 
    'category': 'юбка', 
    'price': 11990, 
    'discount_price': 8990, 
    'in_the_sale': True, 
    'leftovers': [
        {
            'size': '36', 'count': 1, 'price': 8990
        }, 
        {
            'size': '38', 'count': 1, 'price': 8990
        }
]}
```

* На веб-сайте имеются фильтры:
  - Все `{title}`
  - Все `{title}` + `{brand}`
  - Все товары `{brand}`

* Похожие товары:
  - `{title}` + `{brand}`





## Part-02
1) Cформировал `Client.py`, получаем первый результат:
```sh
2023-05-18 11:21:04:21S - root - INFO - Connected successfully to MongoDB!
                                                                    
  Title                      Value                                  
 ────────────────────────────────────────────────────────────────── 
  ID                         6465404fe4a9c7ea27f62225               
  Title                      Юбка                                   
  SKU                        A-04-4001-000-1                        
  Color                      BLACK/черный                           
  Brand                      Anine Bing                             
  Gender                     Ж                                      
  Material                   100% Шёлк                              
  Size Table Type            Буквы Ж                                
  Root Category              Одежда без маркировки                  
  Fashion Season             2022-1                                 
  Fashion Collection         Anine Bing Donna SS 2022               
  Fashion Collection Inner   Anine Bing Womens RTW Precollection    
  Country                    КИТАЙ                                  
  Category                   Юбка                                   
  Price                      37500 RUB                              
  Discount                   23630 RUB                              
  Sale                       True                                   
  Leftovers                  ♦ Size: L, Count: 0, Price: 23630 RUB  
  Leftovers                  ♦ Size: M, Count: 0, Price: 23630 RUB  
  Leftovers                  ♦ Size: S, Count: 0, Price: 23630 RUB  
```

* Знакомство с задание - какие фильтры по полям необходимо использовать






## Part-03

* Добавил поиск данных по фильтрам
```
   1) Поискпоназванию   =  title    DONE
   2) Артикул           =  sku      DONE
   3) Цвет              =  color    DONE
   4) Бренд             =  brand    DONE
   5) Размер            =  size     DONE
   6) Диапазонцен       =  price    DONE
```

* Возможность отображать данные в **JSON** и **Табличном** виде

**Примеры:**

* Отображение в табличном виде [by default]
```sh
(venv) salavat@Linux passagge % python client.py --brand 'GaBBana' --color "красный" --price 25000-26000
```
```output                                                                                             
  Title                      Value                                                           
 ────────────────────────────────────────────────────────────────────────────
  ID                         6465404fe4a9c7ea27f615d9                                        
  Title                      Трусы                                                           
  SKU                        O2B23T-FSA4T                                                    
  Color                      Красный леопард                                                 
  Brand                      Dolce&Gabbana                                                   
  Gender                     Ж                                                               
  Material                   96% Шелк, 4% Эластан                                            
  Size Table Type            Белье Ж                                                         
  Root Category              Одежда без маркировки                                           
  Fashion Season             2023-1                                                          
  Fashion Collection         Dolce&Gabbana UW Donna SS 2023                                  
  Fashion Collection Inner   Dolce&Gabbana Womens UW Precollection                           
  Country                    ИТАЛИЯ                                                          
  Category                   Трусы                                                           
  Price                      25290 RUB                                                       
  Discount                   25290 RUB                                                       
  Sale                       False                                                           
  Leftovers                  ♦ Size: 1,      Count: 1,       Price: 25290 RUB                
  Leftovers                  ♦ Size: 2,      Count: 2,       Price: 25290 RUB                
  URL Link:                  https://ppassage.com/women/catalog/?search=O2B23T-FSA4T&page=1  
```

--- 
* Отображение в JSON формате
```sh
python client.py --brand 'GaBBana' --color "красный" --price 25000-26000 --format json
```

```output
2023-05-18 15:45:37:45S - root - INFO - {'_id': ObjectId('6465404fe4a9c7ea27f615d9'), 'title': 'трусы', 'sku': 'O2B23T-FSA4T', 'color': 'HSYJN/красный леопард', 'brand': 'Dolce&Gabbana', 'sex': 'Ж', 'material': '96% шелк, 4% эластан', 'size_table_type': 'Белье Ж', 'root_category': 'Одежда без маркировки', 'fashion_season': '2023-1', 'fashion_collection': 'Dolce&Gabbana UW Donna SS 2023', 'fashion_collection_inner': 'Dolce&Gabbana Womens UW Precollection', 'manufacture_country': 'ИТАЛИЯ', 'category': 'трусы', 'price': 25290, 'discount_price': 25290, 'in_the_sale': False, 'leftovers': [{'size': '1', 'count': 1, 'price': 25290}, {'size': '2', 'count': 2, 'price': 25290}]}
```



## Part-04

* Добавил фильтр по категорию ("root_category": "Косметика")
* Сформирована таблица для отображения множества записей по фильтру

```
(venv) salavat@Linux passagge % python client.py --sku 47268                       

2023-05-18 17:27:21:27S - root - INFO - Connected successfully to MongoDB!
2023-05-18 17:27:21:27S - root - INFO - Output format: table
2023-05-18 17:27:21:27S - root - INFO - Filter: {'sku': re.compile('47268', re.IGNORECASE)}
                                                                                                                                                                     
  Title     SKU            Color             Brand   Size Table Type   Root Category          Country      Category   Price   Leftovers                              
 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  Ботинки   47268-A        01-black/черный   Bronx   Обувь Ж Россия    Обувь без маркировки   ПОРТУГАЛИЯ   ботинки    18330   Size: 42,  Count: 0,  Price: 8630 RUB  
  Ботинки   47268-A-01     01/черный         Bronx   Обувь Ж Россия    Обувь без маркировки   ПОРТУГАЛИЯ   ботинки    19360   Size: 36,  Count: 1,  Price: 8070 RUB  
                                                                                                                              Size: 39,  Count: 2,  Price: 8070 RUB  
  Ботинки   47268-A-3104   3104/белый        Bronx   Обувь Ж Россия    Обувь без маркировки   ПОРТУГАЛИЯ   ботинки    20710   Size: 36,  Count: 0,  Price: 8630 RUB  
                                                                                                                              Size: 37,  Count: 1,  Price: 8630 RUB  
                                                                                                                              Size: 38,  Count: 1,  Price: 8630 RUB  
                                                                                                                              Size: 39,  Count: 2,  Price: 8630 RUB  
                                                                                                                              Size: 40,  Count: 1,  Price: 8630 RUB  
```                                                                                                           

* Разбор задач (ТЗ)



## Part-05

* Разбор и анализ задач (ТЗ)

python client.py --sku "GY6IET-FUFJR"
python client.py --sku "GH590A-FUFJR" 

```
(venv) salavat@Linux passagge % python client.py --sku "GH590A-FUFJR"
2023-05-18 18:07:48:07S - root - INFO - Connected successfully to MongoDB!
2023-05-18 18:07:48:07S - root - INFO - Output format: table
2023-05-18 18:07:48:07S - root - INFO - Filter: {'sku': re.compile('GH590A-FUFJR', re.IGNORECASE)}
2023-05-18 18:07:48:07S - root - INFO - Output format: table
2023-05-18 18:07:48:07S - root - INFO - Color: W0800/белый
                                                                                               
  Title                      Value                                                             
 ───────────────────────────────────────────────────────────────────────────────────────────── 
  ID                         6465404fe4a9c7ea27f5ec13                                          
  Title                      Кепка                                                             
  SKU                        GH590A-FUFJR-1                                                    
  Color                      Белый                                                             
  Brand                      Dolce&Gabbana                                                     
  Gender                     М                                                                 
  Material                   97% Хлопок, 3% Эластан                                            
  Size Table Type            Головные уборы                                                    
  Root Category              Одежда аксессуары                                                 
  Fashion Season             2022-1                                                            
  Fashion Collection         Dolce&Gabbana Accessori Uomo SS 2022                              
  Fashion Collection Inner   Dolce&Gabbana Mens Accessories Precollection                      
  Country                    ИТАЛИЯ                                                            
  Category                   Кепка                                                             
  Price                      31610 RUB                                                         
  Discount                   18730 RUB                                                         
  Sale                       True                                                              
  Leftovers                  ♦ Size: 57,     Count: 0,       Price: 18730 RUB                  
  Leftovers                  ♦ Size: 58,     Count: 0,       Price: 18730 RUB                  
  Leftovers                  ♦ Size: 59,     Count: 0,       Price: 18730 RUB                  
  Leftovers                  ♦ Size: 60,     Count: 0,       Price: 18730 RUB                  
  URL Link:                  https://ppassage.com/women/catalog/?search=GH590A-FUFJR-1&page=1  
                                                                                               
                                                                                                                                                                           
  Title   SKU              Color               Brand           Size Table Type   Root Category       Country    Category   Price   Leftovers                               
 ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  Кепка   GH590A-FUFJR-1   W0800/белый         Dolce&Gabbana   Головные уборы    Одежда аксессуары   ИТАЛИЯ     кепка      31610   Size: 57,  Count: 0,  Price: 18730 RUB  
                                                                                                                                   Size: 58,  Count: 0,  Price: 18730 RUB  
                                                                                                                                   Size: 59,  Count: 0,  Price: 18730 RUB  
                                                                                                                                   Size: 60,  Count: 0,  Price: 18730 RUB  
  Кепка   GH590A-FUFJR-R   B0665/темно-синий   Dolce&Gabbana   Головные уборы    Одежда аксессуары   ИТАЛИЯ     кепка      26750   Size: 58,  Count: 1,  Price: 26750 RUB  
                                                                                                                                   Size: 59,  Count: 0,  Price: 26750 RUB  
                                                                                                                                   Size: 60,  Count: 0,  Price: 26750 RUB  
  Кепка   GH590A-FUFJR-R   N0000/черный        Dolce&Gabbana   Головные уборы    Одежда аксессуары   ИТАЛИЯ     кепка      26750   Size: 58,  Count: 0,  Price: 26750 RUB  
                                                                                                                                   Size: 59,  Count: 0,  Price: 26750 RUB  
                                                                                                                                   Size: 60,  Count: 0,  Price: 26750 RUB  
                                                                                                            
```                                                                                                            