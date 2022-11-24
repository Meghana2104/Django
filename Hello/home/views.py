from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {'variable1':'Python',
    'variable2':'Django'}
    return render(request,'index.html',context)
def about(request):
    return HttpResponse('<h1>This is about page.</h1>')
def contact(request):
    return HttpResponse('<h1>This is contact page.</h1>')
