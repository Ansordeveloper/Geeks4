from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
    # my_list = [1, 2, 3, 4]
    # body = "<h1>Hello</h1>"
    body = """"
    <!DOCTYPE html>
        <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>

            <h1>My First Heading</h1>
            <p>My first paragraph.</p>
    
        </body>
        </html>
    """
    headers = {"name":"ansor"}
    return HttpResponse(body, headers=headers, status=200)

def get_index(request):
    
    # print (request.__dict__)
    if request.method == "GET":
        return HttpResponse("Главная страница")
    else :
        return HttpResponse("Не тот метод запроса")

def get_contacts(request):
    return HttpResponse("Hi")

def get_about(reguest):
    return HttpResponse("Good")