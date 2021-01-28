from django.shortcuts import render
from django.http import HttpResponse
    
def main(request):
        # Show Hello World HTML to home page
    html = '''
    <!doctype html>
    <html>
    <title> My Blog </title>
    <meta charset='utf-8'>
    </head>
    <body>
    這是HTML版本的Hello World!
    </body>
    </html>
    '''
    return HttpResponse(html)
# Create your views here.
