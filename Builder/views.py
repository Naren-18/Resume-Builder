
count=0

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from tablib import Dataset
import pandas as pd
import os

# os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.conf import settings
from django.template import Context
from io import BytesIO 
import jinja2
# Create your views here. 
from weasyprint import HTML, CSS
import tempfile
from django.template.loader import render_to_string

k=1
@csrf_exempt
def savepdf(request,path ,data={}):
    global k
    
    # return 'Null'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="home_page.pdf"'
    response['Content-Transfer-Encoding']='binary'
    html_string=render_to_string(
        'template2.html',{'expenses':[],'total':0}
    ) 
    html=HTML(string=html_string)
    result=html.write_pdf()
    filename="%s_Resume.pdf"%(data['roll'])
    
    try:
        with open(str(settings.BASE_DIR)+f'/static/{filename}.pdf','wb+') as output:
            pdf=pisa.pisaDocument(BytesIO(html.encode("UTF-8")),output)
    except Exception as e:
        print(e)
    return response

# @csrf_exempt
# def savepdf(template_path,data={}):
#     template_loader = jinja2.FileSystemLoader(settings.BASE_DIR)
#     template_env = jinja2.Environment(loader=template_loader)
#     template=template_env.get_template(template_path)
#     html=template.render({"context":data})
#     result=BytesIO()
#     filename="%s_Resume.pdf"%(data['roll'])

#     try:
#         with open(str(settings.BASE_DIR)+f'/static/{filename}.pdf','wb+') as output:
#             pdf=pisa.pisaDocument(BytesIO(html.encode("UTF-8")),output)
#     except Exception as e:
#         print(e)
@csrf_exempt
def index(request):
    return render(request,'index.html')
    # pdf = render_to_pdf('template2.html', params)
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        t=2
        dataset = Dataset()
        path=request.POST.get('path')
        if(os.path.isabs(path)):
            pass
        
        else:
            msg="Invalid Path"
            context={
                'msg':msg
            }
            return render(request,'upload.html')
        
        new_persons = request.FILES['myfile']
        df=pd.read_csv(new_persons)
        
        temp1=request.POST.get("temp1")
        temp2=request.POST.get("temp2")
        temp3=request.POST.get("temp3")
        temp4=request.POST.get("temp4")
        temp5=request.POST.get("temp5")
        # print(temp1,"\n",temp2,"\n",temp3,"\n",temp4,"\n",temp5,"\n",)
        # imported_data = dataset.load(new_persons.read(),format='xlsx')
        list1=[]
        # count=0
        k=1
        for i in range(0,df.shape[0]):
            dict1={}
            temp=[]
            company=[]
            projects=[]

            projects_name=list(df['projects_name'][i].split(','))
            project_desc=list(df['projects_description'][i].split('$'))
            # print(project_desc)
            for j in range(0,len(project_desc)):
                temp={'n':projects_name[j],'d':project_desc[j]}
                projects.append(temp)

            _10th=list(df['10th'][i].split(','))
            intermediate=list(df['intermediate'][i].split(','))
            graduation=list(df['graduation'][i].split(','))

            company_nam=list(df['company_name'][i].split(','))
            company_duration=list(df['company_duration'][i].split(','))
            company_title=list(df['company_title'][i].split(','))
            company_city=list(df['company_city'][i].split(','))


            skills=list(df['skills'][i].split(','))
            hobbies=list(df['hobbies'][i].split(','))
            company1={
            "n":company_nam[0],
            'c':company_city[0],
            't':company_title[0],
            'y':company_duration[0],
            }
            company2={
                "n":company_nam[1],
                'c':company_city[1],
                't':company_title[1],
                'y':company_duration[1],
            }
            company=[company1,company2]
            # for j in range(0,len(company_city)):
            #     temp={'n':company_nam[j],'d':company_duration[j],'t':company_title[j],'c':company_city[j]}
            #     company.append(temp)
            school1=[_10th[0],intermediate[0],graduation[0]]
            school2=[_10th[1],intermediate[1],graduation[1]]
            school3=[_10th[2],intermediate[2],graduation[2]]

            school1={
            't':"School",
            "n":_10th[0],
            'a':_10th[1],
            'g':_10th[2],
            }
            school2={
                't':"Intermediate",
                "n":intermediate[0],
                'a':intermediate[1],
                'g':intermediate[2],
            }
            school3={
                't':"B.Tech",
                "n":graduation[0],
                'a':graduation[1],
                'g':graduation[2],
            }
            school=[school3,school2,school1]
            dict1={
                'T':t,
                'roll':df['roll_No'][i],
                'Name':df['name'][i],
                'Role':df['current_role'][i],
                'Mob':df['phone_no'][i],
                'Email':df['email'][i],
                'Address':df['Address'][i],
                'Projects':projects,
                "school1":school1,
                "school2":school2,
                "school3":school3,
                "school":school,

                'company':company,
                'Skills':skills,
                'Hobbies':hobbies
            }
            # savepdf(request,path,dict1)
            # k=k+1
            image = dict1['roll']
            html_string=render_to_string(
                'resumes/template2.html',{'data1':dict1, 'image': image}
            ) 
            filename="%s_Resume.pdf"%(dict1['roll'])
            try: 
                with open(path+f'/{filename}.pdf','wb+') as output:
                
                    HTML(string=html_string,base_url=request.build_absolute_uri()).write_pdf(output,stylesheets=[CSS('./static/css/temp2.css')])

            except Exception as e:
                print(e)
                k=k+1
            list1.append(dict1) 
        context={
            'list1':list1
        }
        
        # if(temp1=="True"):
        #     return render(request,'form.html')
        # elif(temp2=="True"):
        #     return render(request,'upload.html')
        # else:
        #     return render(request,'upload.html')
    return render(request,'upload.html')
@csrf_exempt
def form(request):
    if(request.method=='POST'):  
        t=1
        name=request.POST.get("name") 
        role=request.POST.get("role")
        email=request.POST.get("email")
        mob=request.POST.get("mob")
        Address=request.POST.get("Address")
        Experience=request.POST.get("Experience")
        sn1=request.POST.get("1school")
        sa1=request.POST.get("1add")
        sg1=request.POST.get("1gpa")
        sn2=request.POST.get("2school")
        sa2=request.POST.get("2add")
        sg2=request.POST.get("2gpa")
        sn3=request.POST.get("3school")
        sa3=request.POST.get("3add")
        sg3=request.POST.get("3gpa")
        cn1=request.POST.get("1company")
        ct1=request.POST.get("1title")
        cy1=request.POST.get("1years")
        cc1=request.POST.get("1city")
        cn2=request.POST.get("2company")
        ct2=request.POST.get("2title")
        cy2=request.POST.get("2years")
        cc2=request.POST.get("1city")
        h=request.POST.get("hobbies")
        s=request.POST.get("skills")
        hobbies=list(h.split(","))
        skills=list(s.split(","))
        temp1=request.POST.get("temp1")
        temp2=request.POST.get("temp2")
        temp3=request.POST.get("temp3")
        temp4=request.POST.get("temp4")
        temp5=request.POST.get("temp5")
        print(s)
        print(skills)
        school1={
            "n":sn1,
            'a':sa1,
            'g':sg1,
        }
        school2={
            "n":sn2,
            'a':sa2,
            'g':sg2,
        }
        school3={
            "n":sn3,
            'a':sa3,
            'g':sg3,
        }
        company1={
            "n":cn1,
            'c':cc1,
            't':ct1,
            'y':cy1,
        }
        company2={
            "n":cn2,
            'c':cc2,
            't':ct2,
            'y':cy2,
        }
        school=[school1,school2,school3]
        company=[company1,company2]
        list1=[]
        dict1={
            "T":t,
            "Name":name,
            "Role":role,
            "Email":email,
            "Mob":mob,
            "Address":Address,
            "Experience":Experience,
            "school":school,
            "company":company,

            "Hobbies":hobbies,
            "Skills":skills,
        }
        list1=[dict1]
        # list2.append(dict1)
            # print(df['10th'][i])
            # print("AAAAAAAAAAAAAAAA")
        context={
            'list1':list1
        }
        print(context)
        print(temp1,"\n",temp2,"\n",temp3,"\n",temp4,"\n",temp5,"\n",)
        if(temp1=="True"):

            return render(request,"resumes/template1.html",{"context":context})
        elif(temp2=="True"):
            return render(request,"resumes/template2.html",{"context":context})
        else:
            return render(request,'form.html')
    return render(request,'form.html')


