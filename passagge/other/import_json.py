import json


with open('data.json' , 'r') as file:
    data = json.load(file)


# result = data[10]

leftovers_list = []

for item in data:
    leftovers = item['leftovers']
    print(leftovers)

    exit()
    for key in leftovers:
        # if key exists in leftovers - ignore
        if key in leftovers:
            continue
        leftovers_list.append(key)

print(leftovers_list)

# list_keys = list(result.keys())

set_values = set()
for  item in data:
    category_value = item['title']
    set_values.add(category_value)


# print(set_values)



# print(list_keys)

list_keys = [
    'title', 
    'sku', 
    'color', 
    'brand', 
    'sex', 
    'material', 
    'size_table_type', 
    'root_category', 
    'fashion_season', 
    'fashion_collection', 
    'fashion_collection_inner', 
    'manufacture_country', 
    'category', 
    'price', 
    'discount_price', 
    'in_the_sale', 
    'leftovers'
    ]
