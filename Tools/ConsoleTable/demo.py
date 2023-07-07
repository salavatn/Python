from rich.console import Console
from rich.table import Table


# Section 1: Product data list
smartphone = [
    {'title': 'Samsung Galaxy S21 FE', 'price': '699.99', 'rating': '4.5', 'OS': 'Android 11', 'RAM': '8GB', 'ROM': '128GB', 'Battery': '4500mAh', 'Display': '6.4"'},
    {'title': 'Samsung Galaxy A33 5G', 'price': '499.99', 'rating': '4.0', 'OS': 'Android 11', 'RAM': '6GB', 'ROM': '128GB', 'Battery': '5000mAh', 'Display': '6.6"'},
    {'title': 'Apple iPhone 13 Pro', 'price': '999.99', 'rating': '4.5', 'OS': 'iOS 15', 'RAM': '6GB', 'ROM': '128GB', 'Battery': '3000mAh', 'Display': '6.1"'},
    {'title': 'Samsung Galaxy A32', 'price': '399.99', 'rating': '4.0', 'OS': 'Android 11', 'RAM': '4GB', 'ROM': '64GB', 'Battery': '5000mAh', 'Display': '6.4"'},
    {'title': 'Xiaomi Redmi Note 8 Pro', 'price': '299.99', 'rating': '4.0', 'OS': 'Android 10', 'RAM': '6GB', 'ROM': '64GB', 'Battery': '4500mAh', 'Display': '6.53"'},
    {'title': 'Honor 10', 'price': '199.99', 'rating': '3.5', 'OS': 'Android 8.1', 'RAM': '4GB', 'ROM': '64GB', 'Battery': '3400mAh', 'Display': '5.84"'}
]


# Section 2: Create table
table   = Table(title='Smartphones', title_justify='center')


# Section 3: Add columns in table
columns = list(smartphone[0].keys())
for item in columns:
    table.add_column(item)


# Section 4: Add data in table
for item in smartphone:
    data = item.values()
    table.add_row(*data)


# Section 5: Instantiate console object and print table
console = Console()
console.print(table)

