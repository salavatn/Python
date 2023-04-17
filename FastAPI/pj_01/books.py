from fastapi import FastAPI, HTTPException
from faker import Faker
from datetime import datetime
from mangum import Mangum
import random



fake = Faker()

cities = ['Michaelburgh', 'Christopherville', 'Stephaniechester', 'East Robert', 'East Valerie', 
          'Lake Jamesfurt', 'Markbury', 'West Alejandro', 'Russellfort', 'Masonport', 
          'Lake Anthony', 'Lake Davidville', 'Port Cheyenne', 'Michaelside', 'New Lori', 
          'Dustinville', 'Peterchester', 'Christopherborough', 'North Melissaburgh']

'''
search = "city"
params = dir(fake)
for element in params:
    if search in element:
        print(element)
'''

app = FastAPI(
    title="Password Generator API", 
    version="version 1.0.45", 
    description="This API provide random passwords",
    terms_of_service="https://example.com/terms/", 
    contact={"email": "salavat@nigmatullin.net"},
    license_info={"name": "MIT License", "url": "https://example.com/license"},
    )

handler = Mangum(app)


@app.get("/home")
async def home_page():
    firstname = fake.first_name()
    lastname = fake.last_name()
    email = fake.email()
    data = {"user": f"{firstname} {lastname}",
            "email": f"{email}"}
    return data


@app.get("/pswd")
async def get_password():
    password = fake.password()
    data = {"password": f"{password}"}
    return data


@app.get("/time")
async def get_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"current_time": f"{current_time}"}
    return data


@app.get("/city/rand")
async def get_random_city():
    city = random.choice(cities)
    number = cities.index(city)
    data = {"city": city, "city_id": number}
    return data



@app.get("/city/{city_id}")
async def get_city_by_id(city_id: int):
    
    if city_id < 0 or city_id > len(cities):
        raise HTTPException(status_code=404, detail=f"City not found! Index {city_id} is out of range!")
    
    else:
        data = {"city": f"{cities[city_id]}"}
        return data




@app.get("/city")
async def get_city_name():
    data = {"city": f"{cities}"}
    return data


@app.post("/city")
async def add_city(city: str):
    cities.append(city)
    city_index = cities.index(city)
    data = {"city": cities[city_index], "city_id": city_index} 
    return data


