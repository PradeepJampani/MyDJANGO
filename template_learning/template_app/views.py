from django.shortcuts import render

# Create your views here.

def index(request):
    temp_dic={'name':'KrishnaChaitanyaBogavalli','Roll':'1210101428'}
    return render(request,'index.html',context=temp_dic)

def other(request):
    return render(request,'other.html')

def relative(request):
    return render(request,'relative_url.html')
