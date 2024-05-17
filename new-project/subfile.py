from fastapi.templating import Jinja2Templates
import pdfkit
from PyPDF2 import PdfWriter
import datetime

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
    pdfkit.from_string(output, 'output_index.pdf',options={'zoom':'1.15'})


def ongoing_sales():

    output = (templates.get_template('/sales_demo.html').render({'ongoing_sales': sales['ongoing_sales'],}))
    pdfkit.from_string(output, 'ongoing_sales.pdf',options={'zoom':'1.4'})


def past_sales():

    output = (templates.get_template('/past_sales.html').render({'past_sales':sales['past_sales']} ))
    option = {'zoom': '1.2',}   
    pdfkit.from_string(output, 'past_sales.pdf', options = option)


def action_lot():
    output = (templates.get_template('/action_lots.html').render({ 'action_lots':action_lots}))
    pdfkit.from_string(output, 'action_lots.pdf', options = {'zoom':'1.1'} )


def events_page():
    for i,event in enumerate(events['event']):
        image = event['image']
        if image =='' or image == None:
            image_description_letters = " ".join([ word[0] for word in event['painting'].split(" ")])
            string = image_description_letters
        else:
            string = ''
        output=(templates.get_template('/events.html').render({ 'event':event, 'painting_string':string}))
        if i == 0:
            events_pdf = pdfkit.from_string(output, f'events_{i}.pdf', options={'zoom':'1.5'})
        else:
            events_pdf = pdfkit.from_string(output, f'events_{i}.pdf', options={'zoom':'1.0'})

    merge = PdfWriter()
    for pdf in ['events_0.pdf','events_1.pdf']:
        merge.append(pdf)
    merge.write('events.pdf')
    merge.close()


def merge_pdf():
    
    merger = PdfWriter()
    for pdf in ["output_index.pdf", "ongoing_sales.pdf", "past_sales.pdf", 'action_lots.pdf', 'events.pdf']:
        merger.append(pdf)
    merger.write("merged-pdf.pdf")
    merger.close()
