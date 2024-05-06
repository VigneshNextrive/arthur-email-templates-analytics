from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app= FastAPI()
#Templates configurations
templates= Jinja2Templates(directory='templates')

#Staticfiles congigurations
app.mount('/static', StaticFiles(directory='assets'), name='static')

@app.get ('/')
def read_data (request:Request):

    data = {
    'sales': {
        'ongoing_sales': [
            {'image': '/src/assets/first.jpg', 'painting': 'Soleil Jaune', 'price': '£820,000', 'name': 'MAX ERNST'},
            {'image': '/src/images/second.jpg', 'painting': 'Marilyn (F. & S. II.25)', 'price': '$250,000', 'name': 'ANDY WARHOL'}
        ],
        'past_sales': [
            {'image': '/src/assets/third.jpg', 'painting': 'Muhammad Ali', 'price': '£180,000 - £250,000', 'name': 'ANDY WARHOL'},
            {'image': '//src/assets/third.jpg', 'painting': 'Queen Beatrix, from: Reigning Queens', 'price': '£30,000 - £50,000', 'name': 'ANDY WARHOL'}
        ]
    },
    'events': {
        'events_near_me': [
            {'image': '/static/images/fifth.jpg', 'painting': 'Roni Horn', 'date': 'Apr 04, 2024 - Jun 28, 2024', 'location': 'Hauser & Wirth, New York City, United States'},
            {'image': '/static/images/sixth.jpg', 'painting': 'Verena Loewensberg: Kind of Blue', 'date': 'Feb 21, 2024 - Apr 27, 2024', 'location': 'Hauser & Wirth, New York City, United States'}
        ],

        'upcoming_events':[
            {'image':'/static/images/seventh.jpg', 'painting':'Mark Rothko', 'date':'Oct 18, 2023 - Apr 04, 2024', 'location':'Palm Springs Art Museum, Palm Springs, CA'},
            {'image':'/static/images/eigth.jpg', 'painting':'Raymond Saunders: Post No Bills', 'date':'Feb 22, 2024 - Apr 06, 2024', 'location':'David Zwirner, New York City'},

        ]
    },
    'news': {
        'top_news': [
            {'image':'/static/images/nine.jpg', 'news': 'Collector Francesco Pellizzi’s Rare Basquiats Head to Auction for the First Time', 'source': 'Observer', 'location': 'Alexandra Tremayne-Pengelly'},
            {'image':'/static/images/tenth.jpg', 'news': 'Nicole Eisenman’s First Major Survey Comes to the Museum of Contemporary Art Chicago', 'source': 'Hyperallergic', 'location': 'Museum of Contemporary Art Chicago'}
            ]
        }
    }

    return templates.TemplateResponse('mock_design.html', { 'request':Request, 'data':data})

