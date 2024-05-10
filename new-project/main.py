from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import pdfkit
import datetime

app= FastAPI()
#Templates configurations
templates= Jinja2Templates(directory='../new-project/templates')

#Staticfiles congigurations
# app.mount('/src', StaticFiles(directory='assets'), name='src')

def arthur_landing ():

    x= datetime.datetime.now()
    date=(x.strftime('%d'))
    month=(x.strftime('%b'))
    year=(x.strftime('%Y'))

    output=(templates.get_template('/arthur_landing.html').render( {'request': Request,'date':date, 'month':month, 'year':year} ))
    pdfkit.from_string(output, 'output1.pdf',)

arthur_landing()              


def Sales_page():
    output=(templates.get_template('/sales_demo.html').render( {'request': Request,} ))
    pdfkit.from_string(output, 'output.pdf',)

Sales_page()
    


   




