from mongodb.connection import collection
from typing import List, Dict, Union, Optional, Any, Tuple, Callable, TypeVar, Generic, Deque, Type, Set, cast, no_type_check, AnyStr
from config.settings import Table, console, box
from config.settings import logger
from config.settings import args
import locale
import re


class Converting:
    def __init__(self):
        pass

    def price(self, price: int) -> str:
        locale.setlocale(locale.LC_ALL, 'ru_RU')
        price = locale.currency(price, grouping=True, symbol=True, international=True)
        return price
    
    def sensitive_off(self, keywords: str) -> str:
        logger.debug(f'Keywords: {keywords}')
        data = re.compile(keywords, re.IGNORECASE)
        return data
    
    def cutting(self, data: str) -> str:
        if len(data) > 15:
            data = data[:15] + '...'
        return data
    
    def price_range(self, start_finish: str) -> Union[int, Dict[str, int]]:
        if '-' not in start_finish:
            logger.debug(f'Price: {start_finish}')
            return int(start_finish)

        start, finish = start_finish.split('-')

        if finish is None:
            logger.debug(f'Price: {start}')
            return int(start)
        
        logger.debug(f'Price: {start} - {finish}')
        range = {"$gte": int(start), "$lte": int(finish)}
        return range
    
    def output_format(self, format: str) -> str:
        if format == 'json':
            return 'json'
        else:       
            return 'table'


converter = Converting()



def format(data: str) -> str:
    return data.title()


def get_filter() -> Union[Dict[str, Any], str, Union[int, str]]:
    '''Creating Search FILTER for MongoDB based on user arguments'''

    # FILTER for MongoDB:
    filter = {}
    if args.title:    filter['title']   = converter.sensitive_off(args.title)
    if args.sku:      filter['sku']     = converter.sensitive_off(args.sku)
    if args.color:    filter['color']   = converter.sensitive_off(args.color)
    if args.brand:    filter['brand']   = converter.sensitive_off(args.brand)
    if args.type:     filter['size_table_type'] = converter.sensitive_off(args.type)
    if args.category: filter['category']= converter.sensitive_off(args.category)
    if args.country:  filter['manufacture_country'] = converter.sensitive_off(args.country)
    if args.price:    filter['price']   = converter.price_range(args.price)
    '''if args.size:     filter['leftovers.size']  = converter.sensitive_off(args.size)'''

    # OUTPUT format: json or table, count
    
    if args.output:   output_format     = args.output   # converter.output_format(args.output)
    if args.limit:    output_limit      = args.limit    # converter.output_format(args.format)

    logger.debug(f'Filter: {filter}')
    logger.info(f'FORMAT: {output_format}, LIMIT: {output_limit}')

    return filter, output_format, output_limit


def get_first(filter: dict, format: str) -> None:
    # Get first record from collection by filter

    table   = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
    record  = collection.find_one(filter)

    if format == 'json':
        logger.debug('Output format: json')
        logger.info(record)
        exit()
    
    # Two columns with default justification (centered)
    logger.info('Output format: table')
    table.add_column("Title", style="dim", width=24)
    table.add_column("Value")


    # Color, get second element from list
    color = str(record['color'])
    logger.info(f'Color: {color}')
    if '/' in color:
        color = color.split('/')[1].strip().capitalize()
        logger.debug(f'Color: {color}')
    else:
        color = None
        logger.debug(f'Color: {color}')


    # Add a row for each info type
    table.add_row("ID",     str(record['_id']))
    table.add_row("Title",  str(record['title'].title()))
    table.add_row("SKU",    str(record['sku']))
    table.add_row("Color",  color)
    table.add_row("Brand",  str(record['brand']))
    table.add_row("Gender", str(record['sex']))
    table.add_row("Material",           str(record['material']).strip().title())
    table.add_row("Size Table Type",    str(record['size_table_type']))
    table.add_row("Root Category",      str(record['root_category']))
    table.add_row("Fashion Season ",    str(record['fashion_season']))
    table.add_row("Fashion Collection",         str(record['fashion_collection']))
    table.add_row("Fashion Collection Inner",   str(record['fashion_collection_inner']))
    table.add_row("Country ",   str(record['manufacture_country']))
    table.add_row("Category",   str(record['category']).title())
    table.add_row("Price",      str(record['price']) + ' RUB' )
    table.add_row("Discount",   str(record['discount_price']) + ' RUB')
    table.add_row("Sale",       str(record['in_the_sale']))
    leftovers = record['leftovers']
    list_LO   = []

    for leftover in leftovers:
        data = f'♦ Size: {leftover["size"]},\tCount: {leftover["count"]},\tPrice: {leftover["price"]} RUB'
        list_LO.append(data)

    for leftover in list_LO:
        table.add_row("Leftovers", leftover)
    
    table.add_row("URL Link: ", f"https://ppassage.com/women/catalog/?search={record['sku']}&page=1")

    console.print(table)




def get_all(filter: dict, format: str, limit: Union[str, int]) -> None:
    '''Get all filtered records from MongoDB collection'''

    if limit == 'all':
        mongodb_records = collection.find(filter)
    else:
        limit = int(limit)
        mongodb_records = collection.find(filter).limit(limit)

    table   = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
    

    if format == 'json':
        logger.debug('Output format: json')
        for element in mongodb_records:
            logger.info(element)
        exit()
    
    logger.debug('Output format: table')

    table.add_column("ID",          style="dim", justify="center")
    table.add_column("Title",       style="dim", justify="left") #, width=20)
    table.add_column("SKU",         style="dim", justify="left")
    table.add_column("Color",       style="dim", justify="left")
    table.add_column("Brand",       style="dim", justify="right")
    table.add_column("Type",        style="dim", justify="left")
    table.add_column("Category",    style="dim", justify="center")
    table.add_column("Country ",    style="dim", justify="right") #, width=15)
    table.add_column("Price",       style="dim", justify="right")


    for record in mongodb_records:
        id      = str(record['_id'])
        title   = str(record['title'].title())
        sku     = str(record['sku'])
        color   = str(record['color'])
        brand   = str(record['brand'])
        type    = str(record['size_table_type'])
        category = str(record['root_category'])
        country = str(record['manufacture_country'])
        price   = converter.price(record['price']) 
        # str(record['price'])
        # leftovers = record['leftovers']

        '''
        # list_leftover = []
        # for leftover in leftovers:
        #     data = f'Size: {leftover["size"]},  Count: {leftover["count"]},  Price: {leftover["price"]} RUB'
        #     list_leftover.append(data)
        # logger.debug(f'Leftovers: {list_leftover}')
        # leftover_string = "\n".join(list_leftover)
        '''

        data = [id, title, sku, color, brand, type, category, country, price]
        table.add_row(*data)    

    console.print(table)






# get_first(filter, format_output)



if __name__ == '__main__':
    logger.info('Start mongodb_client.py')
    
    filter, output_format, output_limit = get_filter()
    if output_limit == 'one':
        get_first(filter, output_format)
    else:
        get_all(filter, output_format, output_limit)


'''
## Example data:
• Поискпоназванию   =  title    DONE
• Артикул           =  sku      DONE
• Цвет              =  color    DONE
• Бренд             =  brand    DONE
• Размер            =  size     DONE
• Диапазонцен       =  price    DONE


  Title                      Юбка                                                                
  SKU                        FN-WN-SKIR000099                                                    
  Color                      Персиковый                                                          
  Brand                      Acne Studios                                                        
  Gender                     Ж                                                                   
  Material                   100% Полиэстер                                                      
  Fashion Season             2019-2                                                              
  Fashion Collection         Acne Studios Donna FW 2019                                          
  Fashion Collection Inner   Acne Studios Womens RTW Main                                        
  Country                    КИТАЙ                                                               
  Category                   Юбка                                                                
  Price                      11990 RUB                                                           
  Discount                   8990 RUB                                                            
  Sale                       True                                                                
  Leftovers                  ♦ Size: 36, Count: 1, Price: 8990 RUB                               
  Leftovers                  ♦ Size: 38, Count: 1, Price: 8990 RUB                               
  URL Link:                  https://ppassage.com/women/catalog/?search=FN-WN-SKIR000099&page=1  

'''



