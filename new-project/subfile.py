from fastapi.templating import Jinja2Templates
import pdfkit
from PyPDF2 import PdfWriter
import datetime
import os


templates = Jinja2Templates(directory='../new-project/templates')

sales = {
    'ongoing_sales':[
        {'image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg','author':'ANDY WARHOL', 'painting':'FLOWERS (FELDMAN /SCHELLM...', 'price':'£6,000 - £10,000','size':'30.4 * 30.2 cm', 'medium':'Screen print, offset print on vellum'},
        {'image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg','author':'ANDY WARHOL', 'painting':'($9)', 'price':'$100,00 - $150,000','size':'81.3 * 101.6 cm', 'medium':'Color screenprint on Lenox Museum Board'},
        {'image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg','author':'ANDY WARHOL', 'painting':'Mick Jagger', 'price':'$30,000 - $50,000','size':'73.7 * 110.2 cm', 'medium':'Screenprint on Arches Aquarelle Paper'},
        ],
    'past_sales':[
         {'image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg','author':'ANDY WARHOL', 'painting':'Details of Renaissance Paintings (Paolo ...', 'price':'£20,480','size':'37.0 * 25.0 inch', 'medium':'Screen print in colour on Arches Aquarelle paper'},
         {'image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg','author':'ANDY WARHOL', 'painting':'THE BROOKLYN BRIDGE 1883 - 1983 (N...', 'price':'$2,176','size':'23.875 * 35.875 inch', 'medium':'Color screenprint, offset lithograph on smooth wove paper'}
    ]
}

action_lots = [{'image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg', 'author':'ANDY WARHOL','painting':'FLOWERS (FELDMAN /SCHELLMAN II.6)', 'price':'$38,400', 'low_estimate':'$10,000', 'square_inch':'73', 'size':'23.0 * 23.0 Inch','medium':'Color offset lithograph on paper'},

{'image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg', 'author':'ANDY WARHOL','painting':'THE BROOKLYN BRIDGE 1883 - 1983 (N...', 'price':'$2,176', 'low_estimate':'$800', 'square_inch':'3', 'size':'23.875 * 35.875 Inch','medium':'Color screenprint, offset lithograph on smooth wove...'}]

events = {
    'event':[ 

        {'heading':'GALLERY EXHIBITION', 'image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg', 'painting':'Andy Warhol: Beyond the Brand', 'location':'London, United Kingdom', 'date':'Jan 18, 2024 - May 06, 2024','description':'An exhibition dedicated to the life and work of Andy Warhol at 148 & 29 New Bond Street.', 'artist_images':[{'artist-image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg', 'artist-name':'Jean fautrirer', 'country':'France'}]},
              
        {'heading':'MUSEUM EXHIBITION', 'image':'', 'painting':'Collection2 Body---Body', 'location':'National Museum of Art Osaka, Osaka, Japan', 'date':'Feb 06, 2024 - May 06, 2024','description':'The body remains a subject and an issue that is indivisible from artistic expressions and acts i.e., the body of the artist, model, and viewer; physical representation; nudes; and portraits and self-portraits. Moreover, in contemporary society we are repeatedly faced with questions surrounding the body in terms of our relationship with others, and as a battlefield for power s...', 'artist_images':[
            
            {'artist-image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg', 'artist-name':'Andy Warhol', 'country':'United States'},
            {'artist-image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg', 'artist-name':'Pablo Piccaso', 'country':'Spain'},
            {'artist-image':'/Users/Pavan/arthur project/arthur-email-templates-analytics/new-project/assets/first.jpg', 'artist-name':'Jean fautrirer', 'country':'France'} ],}]}






def arthur_index():
    x = datetime.datetime.now()
    date = (x.strftime('%d'))
    month = (x.strftime('%b'))
    year = (x.strftime('%Y'))
    output = (templates.get_template('/arthur_landing.html').render( {'date':date, 'month':month, 'year':year, 'artwork':'5','action_lots':'3', 'event':'2','news':'3', 'artist':'1'}))
    pdfkit.from_string(output, 'output_index.pdf',)


def ongoing_sales():

    output=(templates.get_template('/sales_demo.html').render({
    'ongoing_sales': sales['ongoing_sales'],}))
    pdfkit.from_string(output, 'ongoing_sales.pdf',)


def past_sales():

    output=(templates.get_template('/past_sales.html').render({'past_sales':sales['past_sales']} ))
    pdfkit.from_string(output, 'past_sales.pdf',)

def action_lot():

    output=(templates.get_template('/action_lots.html').render({ 'action_lots':action_lots}))
    pdfkit.from_string(output, 'actions_lot.pdf',)


def events_page():

    a=events['event']
    for item in a[0:]:
        image= item['image']
        if image == '':
            image_description_letters= " ".join([ word[0] for word in item['painting'].split(" ")])
            string = image_description_letters
        else:
            string=''
        
    
  
    output=(templates.get_template('/events.html').render({'events':events['event'], 'painting_string':string}))
    pdfkit.from_string(output, 'events.pdf',)

def merge_pdf():

    merger = PdfWriter()

    for pdf in ["output_index.pdf", "ongoing_sales.pdf", "past_sales.pdf", 'actions_lot.pdf', ]:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()








