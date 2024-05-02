from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/assets",StaticFiles(directory="assets"), name="assets")


@app.get('/')
def send_data():
    return { 'name':'pavan kumar'} 


