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





Отчет каждые 2 часа:
1) Добавил поиск данных по фильтрам
   1) • Поискпоназванию   =  title    DONE
   2) • Артикул           =  sku      DONE
   3) • Цвет              =  color    DONE
   4) • Бренд             =  brand    DONE
   5) • Размер            =  size     DONE
   6) • Диапазонцен       =  price    DONE
2) Возможность отображать данные в JSON и Табличном виде
3) Примеры:

```sh
(venv) salavat@Linux passagge % python client.py --brand 'GaBBana' --color "красный" --price 25000-26000
```
```output                                                                                             
  Title                      Value                                                           
 ─────────────────────────────────────────────────────────────────────────────────────────── 
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

```sh
python client.py --brand 'GaBBana' --color "красный" --price 25000-26000 --format json
```

```output
2023-05-18 15:45:37:45S - root - INFO - {'_id': ObjectId('6465404fe4a9c7ea27f615d9'), 'title': 'трусы', 'sku': 'O2B23T-FSA4T', 'color': 'HSYJN/красный леопард', 'brand': 'Dolce&Gabbana', 'sex': 'Ж', 'material': '96% шелк, 4% эластан', 'size_table_type': 'Белье Ж', 'root_category': 'Одежда без маркировки', 'fashion_season': '2023-1', 'fashion_collection': 'Dolce&Gabbana UW Donna SS 2023', 'fashion_collection_inner': 'Dolce&Gabbana Womens UW Precollection', 'manufacture_country': 'ИТАЛИЯ', 'category': 'трусы', 'price': 25290, 'discount_price': 25290, 'in_the_sale': False, 'leftovers': [{'size': '1', 'count': 1, 'price': 25290}, {'size': '2', 'count': 2, 'price': 25290}]}
```
