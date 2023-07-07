from config.settings import django_start
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database.models import Clients


app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/register', response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("templates/register.html", {"request": request})


@app.post('/register', response_class=HTMLResponse)
def register_page(request: Request):
    username = request.form['username']
    password = request.form['password']
    email    = request.form['email']

    data = {
        'username': username,
        'email':    email,
        'password': password
    }

    new_record = Clients(**data)
    new_record.save()

    all_data = Clients.objects.all()
    for record in all_data:
        user = record.username
        pswd = record.password
        mail = record.email

        print(f'User {user}/{pswd} and {mail}')
    
    return templates.TemplateResponse("templates/register.html", {"request": request})    



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)