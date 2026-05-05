from django.http import HttpResponse,HttpRequest

# Create your views here.
# Home-page greeting
def greeting(request:HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from our first view!")

# Greeting with  username
def greeting_username(request:HttpRequest,name:str) -> HttpResponse:
    return HttpResponse(f'<h1>Hello , {name}!</h1>')

def greeting_default(request:HttpRequest) -> HttpResponse:
    return HttpResponse(f'<h1>Hello , Vladislav!</h1>')