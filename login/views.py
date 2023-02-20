from django.shortcuts import render
import mysql.connector as  sql

# Create your views here.

em = ''
pwd = ''
def loginaction(request):
    global em,pwd

    if request.method=="POST":
        m=sql.connect(host='localhost',user='root',passwd='',database='crm1')
        cursor=m.cursor()
        d=request.POST
        
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        
        if t==():
            return render(request,'error.html')
        else:
            if em == 'admin@gmail.com':

                return render(request,'admin_welcome.html', {'credintials':t})
            else:
                return render(request,'welcome.html')

    return render(request,'login_page.html')