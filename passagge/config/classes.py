from config.settings import logger, re, locale, Union, Dict, Any
from config.settings import Table, box, console

class Converting:
    '''Converting data for flexible search'''

    def __init__(self):
        pass
    

    def sensitive_off(self, keywords: str) -> re.Pattern:
        '''Converting keywords to insensitive search'''
        data = re.compile(keywords, re.IGNORECASE)
        logger.debug(f'Converter.sensitive_off: {data}')
        return data
    
    '''    
    def check_size(self, value: str):
        if isinstance(value, str):
            value = self.sensitive_off(value)
            return value
        elif isinstance(value, int):
            return value
    '''
    
    
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


class MongoDB:
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
        # Get first record from collection by filter

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
        table.add_column("Category",    style="dim", justify="center")
        table.add_column("Country ",    style="dim", justify="right") #, width=15)
        table.add_column("Price",       style="dim", justify="center")
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

