from config.settings import FastAPI, CORSMiddleware, Query
from config.settings import uvicorn
from config.classes import Converting
from config.schema import Product, Filter
from mongodb.connection import collection
import json

converting = Converting()

app = FastAPI(
    title="Internet Market",
    description="Get products from MongoDB",
    version="20.05.23")


# Configuring CORS:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


def get_query(query):
    filter = {}
    limit = 10

    if query.title:     filter['title'] = converting.sensitive_off(query.title)
    if query.sku:       filter['sku']   = converting.sensitive_off(query.sku)
    if query.color:     filter['color'] = converting.sensitive_off(query.color)
    if query.brand:     filter['brand'] = converting.sensitive_off(query.brand)
    if query.price:     filter['price'] = converting.price_range(query.price)
    if query.type:      filter['size_table_type'] = converting.sensitive_off(query.type)
    if query.category:  filter['category'] = converting.sensitive_off(query.category)
    if query.country:   filter['manufacture_country'] = converting.sensitive_off(query.country)
    if query.limit:     limit = query.limit
    


    return filter, limit


@app.post("/api/items/")
async def search_items(query: Product):
    filter = get_query(query)[0]
    limit  = get_query(query)[1]

    print(f"Filter: {filter}")
    print(f"Limit:  {limit}\n")

    projection = {"_id": 0}  # Exclude the _id field

    result_cursor = collection.find(filter, projection).limit(limit)

    print(f"Result cursor: {result_cursor}\n")

    results = []
    for doc in result_cursor:
        results.append(doc)

    if results == []:
        return {"Error": "No results found"}
    
    print(f'Result: {results}\n')

    return results  


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        app='webapp:app', 
        host="192.168.1.33",
        port=8000,
        reload=True,
        # debug=True,
        # workers=1
        )

