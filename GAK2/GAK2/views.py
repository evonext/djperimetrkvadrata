from django.shortcuts import render


def index(request):
    return render(request, "GAK2/index.html")


def calculate(request):
    result = None
    square_side = None
    if request.method =='POST':
        if 'reset' in request.POST:
            result = None
            square_side = ''
        else:
            try:
                square_side = int(request.POST.get('square_side', ''))
                result = square_side * 4
            except(ValueError,TypeError):
                result = " Invalid input "

    return render(request, "GAK2/calculate.html", {'result' : result, 'square_side': square_side})
