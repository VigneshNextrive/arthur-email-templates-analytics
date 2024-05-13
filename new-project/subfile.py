from fastapi.templating import Jinja2Templates
import pdfkit
import PyPDF2
import datetime
import os


templates = Jinja2Templates(directory='../new-project/templates')


sales = {
    'ongoing_sales':[
        {'image':'../new-project/assets/first.jpg','author':'ANDY WARHOL', 'painting':'FLOWERS (FELDMAN /SCHELLM...', 'price':'£6,000 - £10,000','size':'30.4 * 30.2 cm', 'medium':'Screen print, offset print on vellum'},
        {'image':'../new-project/assets/first.jpg','author':'ANDY WARHOL', 'painting':'($9)', 'price':'$100,00 - $150,000','size':'81.3 * 101.6 cm', 'medium':'Color screenprint on Lenox Museum Board'},
        {'image':'../assets/first.jpg','author':'ANDY WARHOL', 'painting':'Mick Jagger', 'price':'$30,000 - $50,000','size':'73.7 * 110.2 cm', 'medium':'Screenprint on Arches Aquarelle Paper'},
        ],
    'past_sales':[
         {'image':'../new-project/assets/first.jpg','author':'ANDY WARHOL', 'painting':'Details of Renaissance Paintings (Paolo ...', 'price':'£20,480','size':'37.0 * 25.0 inch', 'medium':'Screen print in colour on Arches Aquarelle paper'},
         {'image':'../new-project/assets/first.jpg','author':'ANDY WARHOL', 'painting':'THE BROOKLYN BRIDGE 1883 - 1983 (N...', 'price':'$2,176','size':'23.875 * 35.875 inch', 'medium':'Color screenprint, offset lithograph on smooth wove paper'}
    ]
}

action_lots = [{'image':'../new-project/assets/first.jpg', 'author':'ANDY WARHOL','painting':'FLOWERS (FELDMAN /SCHELLMAN II.6)', 'price':'$38,400', 'low_estimate':'$10,000', 'square_inch':'73', 'size':'23.0 * 23.0 Inch','medium':'Color offset lithograph on paper'},

{'image':'../new-project/assets/first.jpg', 'author':'ANDY WARHOL','painting':'THE BROOKLYN BRIDGE 1883 - 1983 (N...', 'price':'$2,176', 'low_estimate':'$800', 'square_inch':'3', 'size':'23.875 * 35.875 Inch','medium':'Color screenprint, offset lithograph on smooth wove...'}]


def arthur_index():
    x = datetime.datetime.now()
    date = (x.strftime('%d'))
    month = (x.strftime('%b'))
    year = (x.strftime('%Y'))
    output = (templates.get_template('/arthur_landing.html').render( {'date':date, 'month':month, 'year':year, 'artwork':'5','action_lots':'3', 'event':'2','news':'3', 'artist':'1'}))

    pdfkit.from_string(output, 'output_index.pdf',)



def ongoing_sales():

    output = (templates.get_template('/sales_demo.html').render({
    'ongoing_image_1':sales['ongoing_sales'][0]['image'], 'first_author':sales['ongoing_sales'][0]['author'], 'first_painting':sales['ongoing_sales'][0]['painting'], 'first_price':sales['ongoing_sales'][0]['price'], 'first_size':sales ['ongoing_sales'][0]['size'], 'first_medium':sales['ongoing_sales'][0]['medium'],

    'ongoing_image_2':sales['ongoing_sales'][1]['image'], 'second_author':sales['ongoing_sales'][1]['author'], 'second_painting':sales['ongoing_sales'][1]['painting'], 'second_price':sales['ongoing_sales'][1]['price'], 'second_size':sales ['ongoing_sales'][1]['size'], 'second_medium':sales['ongoing_sales'][1]['medium'],


    'ongoing_image_3':sales['ongoing_sales'][2]['image'], 'third_author':sales['ongoing_sales'][2]['author'], 'third_painting':sales['ongoing_sales'][2]['painting'], 'third_price':sales['ongoing_sales'][2]['price'], 'third_size':sales ['ongoing_sales'][2]['size'], 'third_medium':sales['ongoing_sales'][2]['medium'],}))

    pdfkit.from_string(output, 'output1.pdf',)


def past_sales():

    output = (templates.get_template('/past_sales.html').render({
    'past_image_1':sales['past_sales'][0]['image'], 'first_author':sales['past_sales'][0]['author'], 'first_painting':sales['past_sales'][0]['painting'], 'first_price':sales['past_sales'][0]['price'], 'first_size':sales ['past_sales'][0]['size'], 'first_medium':sales['past_sales'][0]['medium'],

    'past_image_2':sales['past_sales'][1]['image'], 'second_author':sales['past_sales'][1]['author'], 'second_painting':sales['past_sales'][1]['painting'], 'second_price':sales['past_sales'][1]['price'], 'second_size':sales ['past_sales'][1]['size'], 'second_medium':sales['past_sales'][1]['medium'],} ))
   
    pdfkit.from_string(output, 'output2.pdf',)

def action_lot():

    output = (templates.get_template('/action_lots.html').render({ 
        'action_image_1':action_lots[0]['image'], 'first_author':action_lots[0]['author'], 'first_painting':action_lots[0]['painting'],'first_price':action_lots[0]['price'], 'first_low_estimate':action_lots[0]['low_estimate'], 'first_square_inch':action_lots[0]['square_inch'],'first_size':action_lots[0]['size'], 'first_medium':action_lots[0]['medium'],

    'action_image_2':action_lots[1]['image'], 'second_author':action_lots[1]['author'],'second_painting':action_lots[1]['painting'],'second_price':action_lots[1]['price'], 'second_low_estimate':action_lots[1]['low_estimate'], 'second_square_inch':action_lots[1]['square_inch'],'second_size':action_lots[1]['size'], 'second_medium':action_lots[1]['medium'] } ))

    pdfkit.from_string(output, 'output_3.pdf',)

def merge_pdf():
    merger = PyPDF2.PdfMerger()
    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merger.append(file)
    merger.write("Arthur_pdf_creation.pdf")








