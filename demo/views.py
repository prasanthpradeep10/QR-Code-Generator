from django.shortcuts import render
from qrcode import *

# Create your views here.
data = None


def Home(request):
    global data
    if request.method == 'POST':
        data = request.POST['data']

        img = make(data)
        img.save('demo/static/images/test.png')
    else:
        pass
    return render(request, 'home.html', {'data': data})
