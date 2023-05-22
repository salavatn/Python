from config.settings import logger, re, locale, Union, Dict, Any
from config.settings import Table, box, console
from config.settings import HTTPException, status



class Converting:
    '''Converting data for flexible search'''

    def __init__(self):
        pass
    

    def sensitive_off(self, keywords: str) -> re.Pattern:
        '''Converting keywords to insensitive search'''
        # if "|" in keywords:
        #     keywords = list(keywords.split('|')).strip()
        #     filter = {"$or": [{"color": "Red"}, {"color": "Blue"}]}
        #     logger.debug(f'Converter.sensitive_off: {keywords}')
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

        value = self.check_value(value)

        if   operator == 'OR':      filter_element = self.operator_or(key, value)
        elif operator == 'EQ':      filter_element = self.operator_eq(key, value)
        elif operator == 'GT':      filter_element = self.operator_gt(key, value)
        elif operator == 'LT':      filter_element = self.operator_lt(key, value)
        elif operator == 'BETWEEN': filter_element = self.operator_between(key, value)
        else:
            error_message = f"Operator {operator} not found. Possbile operators: OR, EQ, GT, LT, BETWEEN"
            logger.error(f"{log_header} {error_message}")
            raise HTTPException(status_code=404, detail=error_message)

        logger.debug(f"{log_header} Filter={filter_element}")

        return filter_element


    def check_value(self, value: str) -> Union[str, int]:
        '''Check value for multiple values'''
        log_header = 'MongodbFilters.check_value:'

        if "|" in value:
            value = list(value.split('|'))
        
        logger.debug(f"{log_header} Value={value}")

        return value
        
    def operator_or(self, title, value_list):
        logger.debug(f"MongodbFilters.operator_or: Title={title}")
        logger.debug(f"MongodbFilters.operator_or: Values={value_list}")

        count       = len(value_list)
        conditions  = []


        for i in range(count):
            value = value_list[i].strip()
            logger.debug(f"MongodbFilters.operator_or: Value={value}")
            if value.isdigit():
                value = int(value)  
            else:
                value = re.compile(value, re.IGNORECASE)

            conditions.append({title: value})
            logger.debug(f"MongodbFilters.operator_or: Condition-{i+1}={conditions[i]}")

    
        filter_element = {'$or': conditions}
        logger.debug(f"MongodbFilters.operator_or: Filter OR={filter_element}")

        return filter_element

    def operator_eq(self, title, value):
        if value.isdigit():
            value = int(value)  
        else:
            value = re.compile(value, re.IGNORECASE)

        filter_element = {title: value}
        logger.debug(f"MongodbFilters.operator_eq: Filter Equal={filter_element}")
        return filter_element

    def operator_gt(self, title, value):
        if value.isdigit():
            value = int(value)  
        filter_element = {title: {'$gt': value}}
        logger.debug(f"MongodbFilters.operator_gt: Filter Greater Then={filter_element}")
        return filter_element
    
    def operator_lt(self, title: str, value: str) -> Dict[str, Any]:
        '''Filter for Number - Less Then'''

        log_header = 'MongodbFilters.operator_lt:'

        number = value.strip()

        if not number.isdigit():
            error_message = f"Waiting the numbers. But received {number}"
            logger.error(f"{log_header} {error_message}")
            raise HTTPException(status_code=404, detail=error_message)

        number = int(number)  
        filter_element = {title: {'$lt': number}}
        
        logger.debug(f"{log_header} Filter Less Then={filter_element}")

        return filter_element
       

    def operator_between(self, title: str, value_list: list) -> Dict[str, Any]:
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
        conditions[title] = query
        logger.debug(f"{log_header} Filter Between={conditions}")

        return conditions


    def get_filter(self):
        logger.debug(f"MongodbFilters.get_filter: Query={self.query}")

        count_conditions = len(self.query['filters'])

        if count_conditions == 1:
            logger.debug(f"MongodbFilters.get_filter: count conditions={count_conditions}")

            final_filter = {}  

            key      = self.query['filters'][0]['title']
            value    = self.query['filters'][0]['value']
            operator = self.query['filters'][0]['operator']

            final_filter = self.check_operator(key, value, operator)

            logger.debug(f"MongodbFilters.get_filter: Final filter={final_filter}")
            return final_filter


        logger.debug(f"MongodbFilters.get_filter: count conditions={count_conditions}")
        mongodb_filter = {'$and': []}  # Initialize with an empty $and array
        logger.debug(f"MongodbFilters.get_filter: MongoDB Filter={mongodb_filter}")

        for i in range(count_conditions):
            title    = self.query['filters'][i]['title']
            operator = self.query['filters'][i]['operator']
            value    = self.query['filters'][i]['value']

            logger.debug(f"webapp.get_mongodb_filter: Title={title}")
            logger.debug(f"webapp.get_mongodb_filter: Operator={operator}")
            logger.debug(f"webapp.get_mongodb_filter: Value={value}")

            # MongoDB Filter OR
            if operator == 'OR':
                logger.debug(f"webapp.get_mongodb_filter: Operator={operator}")
                filter = {'$or': [{title: value}]}
                mongodb_filter['$and'].append(filter)
                logger.debug(f"webapp.get_mongodb_filter: Filter={mongodb_filter}\n")

            # MongoDB Filter EQ (equals)
            elif operator == 'EQ':
                logger.debug(f"webapp.get_mongodb_filter: Operator={operator}")
                filter = {title: value}
                mongodb_filter['$and'].append(filter)
                logger.debug(f"webapp.get_mongodb_filter: Filter={mongodb_filter}\n")

        return mongodb_filter



