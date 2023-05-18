from mongodb.connection import client, collection
from typing import List, Dict, Union, Optional
from settings import Table, console, box
from settings import logger
from settings import args
import re



def flexible_search(keywords: str) -> str:
    data = re.compile(keywords, re.IGNORECASE)
    return data

def price_range(start_finish: str) -> Union[int, Dict[str, int]]:
    if '-' not in start_finish:
        logger.info(f'Price: {start_finish}')
        return int(start_finish)

    start, finish = start_finish.split('-')
    # logger.info(f'Price range: {start} - {finish}')

    if finish is None:
        logger.info(f'Price: {start}')
        return int(start)
    
    logger.info(f'Price: {start} - {finish}')
    range = {"$gte": int(start), "$lte": int(finish)}
    return range

def get_filter():
    filter = {}

    if args.title:    filter['title'] = flexible_search(args.title)
    if args.color:    filter['color'] = flexible_search(args.color)
    if args.size:     filter['leftovers.size'] = flexible_search(args.size)
    if args.price:    filter['price'] = price_range(args.price)
    if args.brand:    filter['brand'] = flexible_search(args.brand)
    if args.sku:      filter['sku'] = flexible_search(args.sku)
    if args.category: filter['root_category'] = flexible_search(args.category)
    if args.format:    
        if args.format == 'json':
            logger.info('Output format: json')
        else:       
            logger.info('Output format: table')


    logger.info(f'Filter: {filter}')
    return filter, args.format

def get_first(filter: dict, format: str) -> None:
    '''Get first record from collection by filter'''

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



def get_all(filter: dict, format: str) -> None:
    '''Get all records from collection by filter'''

    table   = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
    records = collection.find(filter)

    if format == 'json':
        logger.debug('Output format: json')
        for element in records:
            logger.info(element)
        exit()
    
    # Two columns with default justification (centered)
    logger.debug('Output format: table')

    '''
    records_keys = records[0].keys()
    list_records_keys = list(records_keys)
    logger.debug(f'Records keys: {list_records_keys}')
    for element in list_records_keys:
        table.add_column(element, style="dim") #, width=24)
    '''

    # table.add_column("ID", style="dim")
    table.add_column("Title", style="dim")
    table.add_column("SKU", style="dim")
    table.add_column("Color", style="dim")
    table.add_column("Brand", style="dim")
    # table.add_column("Gender", style="dim")
    # table.add_column("Material", style="dim")
    table.add_column("Size Table Type", style="dim")
    table.add_column("Root Category", style="dim")
    # table.add_column("Fashion Season ", style="dim")
    # table.add_column("Fashion Collection", style="dim")
    # table.add_column("Fashion Collection Inner", style="dim")
    table.add_column("Country ", style="dim")
    table.add_column("Category", style="dim")
    table.add_column("Price", style="dim")
    # table.add_column("Discount", style="dim")
    # table.add_column("Sale", style="dim")
    table.add_column("Leftovers", style="dim")
    # table.add_column("URL Link: ", style="dim")



    for record in records:
        # id = str(record['_id'])
        title = str(record['title'].title())
        sku = str(record['sku'])
        color = str(record['color'])
        brand = str(record['brand'])

        size_table_type = str(record['size_table_type'])
        root_category = str(record['root_category'])
        manufacture_country = str(record['manufacture_country'])
        category = str(record['category'])
        price = str(record['price'])
        leftovers = record['leftovers']

        list_leftover = []
        for leftover in leftovers:
            data = f'Size: {leftover["size"]},  Count: {leftover["count"]},  Price: {leftover["price"]} RUB'
            list_leftover.append(data)
        logger.debug(f'Leftovers: {list_leftover}')

            # list_leftover = '\n'.join(list_leftover)
        # list_leftover = [str(i) for i in list_leftover]
        leftover_string = "\n".join(list_leftover)


        # values = record.values()

        # logger.debug(f'Record values: {values}')

        # values = list(values)
        # logger.debug(f'Record values: {values}')

        table.add_row(title, sku, color, brand, size_table_type, root_category, manufacture_country, category, price, leftover_string)    


        # # table.add_row("ID", record['_id'])
        # table.add_row("Title", record['title'].title())
        # table.add_row("SKU", record['sku'])
        # table.add_row("Color", record['color'])
        # table.add_row("Brand", record['brand'])

    console.print(table)


    # table.add_column("Title", style="dim", width=24)
    # table.add_column("Value")




    # # Color, get second element from list
    # color = str(record['color'])
    # logger.info(f'Color: {color}')
    # if '/' in color:
    #     color = color.split('/')[1].strip().capitalize()
    #     logger.debug(f'Color: {color}')
    # else:
    #     color = None
    #     logger.debug(f'Color: {color}')


    # # Add a row for each info type
    # table.add_row("ID",     str(record['_id']))
    # table.add_row("Title",  str(record['title'].title()))
    # table.add_row("SKU",    str(record['sku']))
    # table.add_row("Color",  color)
    # table.add_row("Brand",  str(record['brand']))
    # table.add_row("Gender", str(record['sex']))
    # table.add_row("Material",           str(record['material']).strip().title())
    # table.add_row("Size Table Type",    str(record['size_table_type']))
    # table.add_row("Root Category",      str(record['root_category']))
    # table.add_row("Fashion Season ",    str(record['fashion_season']))
    # table.add_row("Fashion Collection",         str(record['fashion_collection']))
    # table.add_row("Fashion Collection Inner",   str(record['fashion_collection_inner']))
    # table.add_row("Country ",   str(record['manufacture_country']))
    # table.add_row("Category",   str(record['category']).title())
    # table.add_row("Price",      str(record['price']) + ' RUB' )
    # table.add_row("Discount",   str(record['discount_price']) + ' RUB')
    # table.add_row("Sale",       str(record['in_the_sale']))
    # leftovers = record['leftovers']
    # list_LO   = []



filter, format_output = get_filter()
get_first(filter, format_output)
get_all(filter, format_output)


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



