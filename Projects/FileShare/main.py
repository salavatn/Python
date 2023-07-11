from fastapi import FastAPI


app = FastAPI()


@app.post('/upload')
async def upload_file():
    pass

@app.get('/download/{file_id}')
async def download_file(file_id: int):
    pass

