
from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.conf import settings
# Create your views here. 

count=0
def savepdf(params:dict):
    c1=['A','B','C','D']
    template=get_template("template1.html") 
    html=template.render(params)
    result = BytesIO()
    count=0
    print(params)
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    try:
        with open(str(settings.BASE_DIR)+f'/static/'+c1[count]+'.pdf', 'wb+') as output:

            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), output)
    except Exception as e:
        print(e)
    
    count=count+1