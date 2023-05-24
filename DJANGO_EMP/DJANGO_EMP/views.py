from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from DJANGO_EMP.dao_emp import DaoEmp

# Create your views here.


def emplist(request):
    de = DaoEmp()
    list = de.selectList()
    return render( request,'emplist.html',{"list":list})

def empdetail(request):
    e_id = request.GET.get('e_id','')
    de= DaoEmp()
    vo = de.selectOne(e_id)
    return render( request,'emp_detail.html',{'vo':vo})

def empmod(request):
    e_id = request.GET.get('e_id','')
    de= DaoEmp()
    vo = de.selectOne(e_id)
    return render( request,'emp_mod.html',{'vo':vo})

def empmodact(request):
    e_id = request.POST.get('e_id','')
    e_name = request.POST.get('e_name','')
    sex = request.POST.get('sex','')
    addr = request.POST.get('addr','')
    de = DaoEmp()
    cnt = de.update(e_id, e_name, sex, addr)
    return render( request,'emp_mod_act.html',{'cnt':cnt})

def empadd(request):
    return render(request,'emp_add.html')

def empaddact(request):
    e_id = request.POST.get('e_id','')
    e_name = request.POST.get('e_name','')
    sex = request.POST.get('sex','')
    addr = request.POST.get('addr','')
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, sex, addr)
    return render( request,'emp_mod_act.html',{'cnt':cnt})

def empdelact(request):
    e_id = request.POST.get('e_id','')
    de = DaoEmp()
    cnt = de.delete(e_id)
    return render( request,'emp_del_act.html',{'cnt':cnt})