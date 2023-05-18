Отчет каждые 2 часа:
1) Формирование структуры проекта
2) Анализ JSON файла и выбор в качестве Database - MongoDB 
3) Регистрация и изучение работы с MongoDB (first time)
4) Загрузил в MongoDB содержимое data.json:
```log
2023-05-18 00:03:07:03S - root - INFO - Connected successfully to MongoDB!
2023-05-18 00:03:07:03S - root - INFO - Count of documents in collection: 20625
```
5) Изучение на MongoDB фильтры:
   - Получить первую запись по фильтру `documents = collection.find_one(filter)`
   - Получить запись по двум параметрам   `filter = {"title": "юбка", "price": 37500}`

6) Анализ JSON + [Боевыми данными](https://ppassage.com/product/iubka-acne-studios-fn-wn-skir000099-oranzhevyi/)

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

Имеются фильтры:
- Все {title}
- Все {title} + {brand}
- Все товары {brand}

Похожие товары:
- {title} + {brand}





Отчет каждые 2 часа:
1) Cформировал Client.py, по фильтру выдает первый результат:
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

2) Знакомство с задание - какие фильтры по полям необходимо использовать