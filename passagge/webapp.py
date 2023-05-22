from mongodb.connection import collection
from config.settings import FastAPI, CORSMiddleware
from config.settings import uvicorn
from config.settings import Dict
from config.settings import logger
from config.classes  import Converting, MongodbFilters
from config.schema   import Filter
import json


converting = Converting()


data = {"title":"Internet Market", "description":"Get products from MongoDB", "version":"22.05.23"}
app  = FastAPI(**data)

data = {"allow_origins": ["*"], "allow_credentials":True, "allow_methods": ["*"], "allow_headers": ["*"]}
app.add_middleware(CORSMiddleware, **data)


@app.post("/api/data")
async def get_data(query: Filter) -> Dict:
    '''Get data from MongoDB'''
    log_header      = 'WebApp[/api/data]:'
    query           = json.loads(query.json())
    logger.debug(f"{log_header} Query={query}")

    query_limit     = query['limit']
    logger.debug(f"{log_header} Limit={query_limit}")

    mongodb_filters = MongodbFilters(query)
    filter          = mongodb_filters.get_filter()
    logger.debug(f"{log_header} Filter={filter}")

    exclude_id = {"_id": 0}
    result_cursor = collection.find(filter, exclude_id).limit(query_limit)

    results = []
    output  = {'RESULT': results}
    for record in result_cursor:
        results.append(record)
        logger.debug(f"{log_header} Result: {record}\n")

    if results == []:
        return {"Error": "No results found"}
    logger.debug(f"{log_header} Result Type: {type(output)}\n")
    return output  



if __name__ == '__main__':
    uvicorn.run(app='webapp:app', host="127.0.0.1", port=8000,reload=True)

