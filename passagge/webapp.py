from config.settings import FastAPI, CORSMiddleware, Query
from config.settings import uvicorn
from config.settings import logger
from config.classes import Converting, MongodbFilters
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



@app.post("/api/data")
async def get_data(query: Filter):

    query = json.loads(query.json())
    query_limit  = query['limit']
    mongodb_filters = MongodbFilters(query)


    logger.debug(f"webapp[/api/data]: Query={query}")
    logger.debug(f"webapp[/api/data]: Limit={query_limit}")


    filter = mongodb_filters.get_filter()
    logger.debug(f"WebApp[/api/data]: Filter={filter}")

    projection = {"_id": 0}  # Exclude the _id field
    result_cursor = collection.find(filter, projection).limit(query_limit)

    results = []
    for doc in result_cursor:
        results.append(doc)

    if results == []:
        return {"Error": "No results found"}
    
    logger.debug(f'WebApp[/api/data]: Result: {results}\n')

    return results  





# filter = {'$or': [{'title': 'Юбка'}, {'title': 'джинсы'}]}
# result  = collection.find_one(filter)
# print(f'Result: {result}\n')





example = {
  "filters": [
    {
      "title": "title",
      "operator": "OR",
      "value": "бабочка | джинсы"
    }
  ]
}

'''
title    = filter['title']
operator = filter['operator']
value    = filter['value']

# MongoDB Filter OR
if operator == 'OR':
    list_values = value.split('|').strip()
    count = len(list_values) 
    conditions = []

    for i in range(count):
        conditions.append({title: list_values[i]})

    filter = {'$or': conditions}

'''

# MongoDB Filter BETWEEN





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

