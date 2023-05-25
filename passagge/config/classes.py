from config.settings import logger, re, locale
from config.settings import Union, Dict, Any, List
from config.settings import Table, box, console
from config.settings import HTTPException, status



class Converting:
    '''Converting data for flexible search'''

    def __init__(self):
        pass
    

    def sensitive_off(self, keywords: str) -> re.Pattern:
        '''Converting keywords to insensitive search'''
        data = re.compile(keywords, re.IGNORECASE)
        logger.debug(f'Converter.sensitive_off: {data}')

        return data
    
    
    def price_range(self, price: str) -> Union[int, Dict[str, int]]:
        '''Converting 11400-25000 to {"$gte": 11400, "$lte": 25000}'''
        if '-' in price:
            minimum, maximum = price.split('-')
            range = {"$gte": int(minimum), "$lte": int(maximum)}
            logger.debug(f'Converter.price: {range}')
            return range
        
        elif 'RUB' in price:
            #Converting 21 430,00 RUB to 21430
            price = price.split(',')[0].replace(' ', '')
            price = int(price)
            logger.debug(f'Converter.price: {price}')
            return price
 
        else:           
            minimum = int(price)
            logger.debug(f'Converter.price: {minimum}')
            return minimum


    def price(self, price: int) -> str:
        '''Converting 11400 to 11 400,00 RUB'''
        locale.setlocale(locale.LC_ALL, 'ru_RU')
        price = locale.currency(price, grouping=True, symbol=True, international=True)
        logger.debug(f'Converter.price: {price}')
        return price
    

    def output_format(self, format: str) -> str:
        if format == 'json':
            logger.debug(f'Converter.output_format: {format}')
            return 'json'
        else:       
            logger.debug(f'Converter.output_format: {format}')
            return 'table'

class ClientMongoDB:
    '''MongoDB class for working with MongoDB'''
    def __init__(self, converter, collection):
        self.converter = converter
        self.collection = collection


    def get_filter(self, args) -> Union[Dict[str, Any], str, Union[int, str]]:
        '''Creating Search FILTER for MongoDB based on user arguments'''
        self.args = args

        # FILTER for MongoDB:
        filter = {}
        if args.title:    filter['title']   = self.converter.sensitive_off(args.title)
        if args.sku:      filter['sku']     = self.converter.sensitive_off(args.sku)        
        if args.color:    filter['color']   = self.converter.sensitive_off(args.color)
        if args.brand:    filter['brand']   = self.converter.sensitive_off(args.brand)
        if args.price:    filter['price']   = self.converter.price_range(args.price)
        if args.type:     filter['size_table_type']     = self.converter.sensitive_off(args.type)
        if args.category: filter['category']            = self.converter.sensitive_off(args.category)
        if args.country:  filter['manufacture_country'] = self.converter.sensitive_off(args.country)
       

        # OUTPUT format: json or table, count
        if args.output: output_format = args.output 
        if args.limit:  output_limit  = args.limit 
        if args.size:   output_size   = args.size

        logger.debug(f'MongoDB.get_filter: Filter={filter}')
        logger.debug(f'MongoDB.get_filter: Format={output_format}')
        logger.debug(f'MongoDB.get_filter: Limit={output_limit}')

        return filter, output_format, output_limit, output_size


    def get_limit(self, limit: Union[str, int]) -> Union[str, int]:
        if limit == 'all':
            logger.debug('MongoDB.get_limit: Limit=all')
            return 0
        else:
            limit = int(limit)
            logger.debug(f'MongoDB.get_limit: Limit={limit}')
            return limit


    def show_record(self, filter: dict, format: str) -> None:
        '''Get first record from collection by filter'''

        table   = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
        record  = self.collection.find_one(filter)

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
        table.add_row("ID",                         str(record['_id']))
        table.add_row("Title",                      str(record['title'].title()))
        table.add_row("SKU",                        str(record['sku']))
        table.add_row("Color",                      color)
        table.add_row("Brand",                      str(record['brand']))
        table.add_row("Gender",                     str(record['sex']))
        table.add_row("Material",                   str(record['material']).strip().title())
        table.add_row("Size Table Type",            str(record['size_table_type']))
        table.add_row("Root Category",              str(record['root_category']))
        table.add_row("Fashion Season ",            str(record['fashion_season']))
        table.add_row("Fashion Collection",         str(record['fashion_collection']))
        table.add_row("Fashion Collection Inner",   str(record['fashion_collection_inner']))
        table.add_row("Country ",                   str(record['manufacture_country']))
        table.add_row("Category",                   str(record['category']).title())
        table.add_row("Price",                      str(record['price']) + ' RUB' )
        table.add_row("Discount",                   str(record['discount_price']) + ' RUB')
        table.add_row("Sale",                       str(record['in_the_sale']))

        leftovers = record['leftovers']
        list_leftovers   = []

        for leftover in leftovers:
            data = f'♦ Size: {leftover["size"]},\tCount: {leftover["count"]},\tPrice: {leftover["price"]} RUB'
            list_leftovers.append(data)

        for leftover in list_leftovers:
            table.add_row("Leftovers", leftover)
        
        table.add_row("URL Link: ", f"https://ppassage.com/women/catalog/?search={record['sku']}&page=1")

        console.print(table)


    def show_all_records(self, filter: dict, format: str, limit: Union[str, int], size: Union[str, int]) -> None:
        '''Get all filtered records from MongoDB collection'''

        count           = self.get_limit(limit)
        mongodb_records = self.collection.find(filter).limit(count)
        table           = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
        
        if format == 'json':
            logger.debug('MongoDB.show_all_records: Format=JSON')
            for element in mongodb_records:
                logger.info(f'MongoDB.show_all_records: JSON:\t{element}\n')
            exit()
        
        logger.debug('MongoDB.show_all_records: Format=TABLE')

        table.add_column("ID",          style="dim", justify="center")
        table.add_column("Title",       style="dim", justify="left") #, width=20)
        table.add_column("SKU",         style="dim", justify="left")
        table.add_column("Color",       style="dim", justify="left")
        table.add_column("Brand",       style="dim", justify="left")
        table.add_column("Type",        style="dim", justify="left")
        table.add_column("Category",    style="dim", justify="left")
        table.add_column("Country ",    style="dim", justify="right") #, width=15)
        table.add_column("Price",       style="dim", justify="right")
        if self.args.size == 'show':
            table.add_column("Leftover",    style="dim", justify="right")


        for record in mongodb_records:
            id       = str(record['_id'])
            title    = str(record['title'].title())
            sku      = str(record['sku'])
            color    = str(record['color'])
            brand    = str(record['brand'])
            type     = str(record['size_table_type'])
            category = str(record['root_category'])
            country  = str(record['manufacture_country'].title())
            price    = self.converter.price(record['price']) 
            leftovers= record['leftovers']

           
            list_leftover = []
            for leftover in leftovers:
                l_size = leftover['size']
                l_count = leftover['count']
                l_price = self.converter.price(leftover['price']) 
                size = f'{l_price},  Size: {l_size},  Count: {l_count}'
                list_leftover.append(size)
            leftover_string = "\n".join(list_leftover)
            
            data = [id, title, sku, color, brand, type, category, country, price]
            if self.args.size == 'show':
                data.append(leftover_string)

            table.add_row(*data)    

        console.print(table)

class APImongodb:
    def __init__(self, converter, collection):
        self.converter = converter
        self.collection = collection

class MongodbFilters:
    '''Creating MongoDB filter based on Query from FastAPI'''

    def __init__(self, query: Dict[str, Any]):
        self.query = query


    def check_operator(self, key: str, value: str, operator: str) -> Dict[str, Any]:
        '''Check operator and create MongoDB filter'''
        log_header = 'MongodbFilters.check_operator:'
        logger.debug(f"{log_header} Operator={operator}")

        value = self.check_value(value)

        if   operator == 'IN':  filter_element = self.operator_in(key, value)
        elif operator == 'EQ':  filter_element = self.operator_eq(key, value)
        elif operator == 'GT':  filter_element = self.operator_gt(key, value)
        elif operator == 'LT':  filter_element = self.operator_lt(key, value)
        elif operator == 'BT':  filter_element = self.operator_bt(key, value)
        else:
            error_message = f"Operator {operator} not found. Possbile operators: IN, EQ, GT, LT, BT"
            logger.error(f"{log_header} {error_message}")
            raise HTTPException(status_code=404, detail=error_message)

        logger.debug(f"{log_header} Filter={filter_element}")

        return filter_element


    def check_value(self, value: str) -> Union[str, int]:
        '''Check value for multiple values'''
        log_header = 'MongodbFilters.check_value:'

        if "|" in value:
            value = list(value.split('|'))
        else:
            value = value.strip()
        
        logger.debug(f"{log_header} Value={value}")

        return value
        

    def operator_in(self, field:str, value_list: Union[List, str]) -> Dict[str, Any]:
        '''Filter for String - IN'''

        log_header = 'MongodbFilters.operator_in:'
        logger.debug(f"{log_header} Field={field}")
        logger.debug(f"{log_header} Values={value_list}")

        # Check if value is string (only one value)
        if isinstance(value_list, str):
            value_list = [value_list]
            logger.debug(f"{log_header} Values={value_list}")
        
        # Check if value is list (multiple values)
        count       = len(value_list)
        conditions  = []

        for i in range(count):
            value = value_list[i].strip()
            logger.debug(f"{log_header} Cycle: Value={value}")
            if value.isdigit():
                value = int(value)  
            else:
                value = re.compile(value, re.IGNORECASE)

            conditions.append({field: value})
            logger.debug(f"{log_header} Cycle: Condition-{i+1}={conditions[i]}")

    
        filter_element = {'$or': conditions}
        logger.debug(f"{log_header} Filter={filter_element}")

        return filter_element


    def operator_eq(self, field: str, value:str) -> Dict[str, Any]:
        '''Filter for String - Equal'''
        log_header = 'MongodbFilters.operator_eq:'

        if isinstance(value, list):
            erros_message = f"Operator EQ not support multiple values. Use OR operator"
            logger.error(f"{log_header} {erros_message}")
            raise HTTPException(status_code=404, detail=erros_message)
        
        value = value.strip()
        
        if value.isdigit():
            value = int(value)  
        else:
            value = re.compile(value, re.IGNORECASE)

        filter_element = {field: value}

        logger.debug(f"{log_header} Filter={filter_element}")

        return filter_element


    def operator_gt(self, field: str, value:str) -> Dict[str, Any]:
        '''Filter for Number - Greater Then'''

        log_header = 'MongodbFilters.operator_gt:'

        number = value.strip()

        if not number.isdigit():
            error_message = f"Waiting the numbers. But received {number}"
            logger.error(f"{log_header} {error_message}")
            raise HTTPException(status_code=404, detail=error_message)

        number = int(number)  
        filter_element = {field: {'$gt': number}}

        logger.debug(f"{log_header} Filter Greater Then={filter_element}")

        return filter_element
    

    def operator_lt(self, field: str, value: str) -> Dict[str, Any]:
        '''Filter for Number - Less Then'''

        log_header = 'MongodbFilters.operator_lt:'

        number = value.strip()

        if not number.isdigit():
            error_message = f"Waiting the numbers. But received {number}"
            logger.error(f"{log_header} {error_message}")
            raise HTTPException(status_code=404, detail=error_message)

        number = int(number)  
        filter_element = {field: {'$lt': number}}

        logger.debug(f"{log_header} Filter Less Then={filter_element}")

        return filter_element
       

    def operator_bt(self, field: str, value_list: list) -> Dict[str, Any]:
        log_header = 'MongodbFilters.operator_between:'

        count = len(value_list)
        num_1 = value_list[0].strip()
        num_2 = value_list[1].strip()


        # Check for 2 values
        if count != 2:
            error_message = f"Waiting for 2 values, but received {count}"
            logger.error(f"{log_header} {error_message}")
            raise HTTPException(status_code=404, detail=error_message)

        # Check for digits
        if not num_1.isdigit() or not num_2.isdigit():
            error_message = f"Waiting for 2 numbers, but received {num_1} and {num_2}"
            logger.error(f"{log_header} {error_message}")
            raise HTTPException(status_code=404, detail=error_message)


        num_1 = int(num_1)
        num_2 = int(num_2)


        if num_1 < num_2:
            query = {'$gte': num_1, '$lte': num_2}
            logger.debug(f"{log_header} Range={num_1}-{num_2}")
        else:
            query = {'$gte': num_2, '$lte': num_1}
            logger.debug(f"{log_header} Range={num_2}-{num_1}")

        conditions  = {}
        conditions[field] = query
        logger.debug(f"{log_header} Filter Between={conditions}")

        return conditions


    def get_filter(self) -> Dict[str, Any]:
        '''Get MongoDB filter based on Query from FastAPI'''

        log_header = 'MongodbFilters.get_filter:'
        logger.debug(f"{log_header} Query={self.query}")

        count_conditions = len(self.query['filters'])


        # Check for one condition
        if count_conditions == 1:
            logger.debug(f"{log_header} count conditions={count_conditions}")
            final_filter = {}  
            field    = self.query['filters'][0]['field']
            logger.debug(f"{log_header} Field={field}")
            value    = self.query['filters'][0]['value']
            logger.debug(f"{log_header} Value={value}")
            operator = self.query['filters'][0]['operator']
            logger.debug(f"{log_header} Operator={operator}")

            final_filter = self.check_operator(field, value, operator)
            logger.debug(f"{log_header} Final filter={final_filter}")
            return final_filter

        logger.debug(f"{log_header} count conditions={count_conditions}")
        mongodb_filter = {'$and': []}  # Initialize with an empty $and array
        logger.debug(f"{log_header} MongoDB Filter={mongodb_filter}")


        # Check for multiple conditions
        for i in range(count_conditions):
            field    = self.query['filters'][i]['field']
            logger.debug(f"{log_header} Field={field}")
            operator = self.query['filters'][i]['operator']
            logger.debug(f"{log_header} Operator={operator}")
            value    = self.query['filters'][i]['value']
            logger.debug(f"{log_header} Value={value}")
            

            filter_part = self.check_operator(field, value, operator)
            logger.debug(f"{log_header} Filter-{i+1}/{count_conditions}={filter_part}")

            
            mongodb_filter['$and'].append(filter_part)
        

        logger.debug(f"{log_header} Full Filter={mongodb_filter}\n")



        return mongodb_filter



