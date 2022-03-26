from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def get_equation(request):
    equation = request.GET['input']
    response = {"input": equation, "answer": "", "flag": False, "error": ""}
    while True:
        if "|" in equation:
            try:
                fst = equation.index("|") + 1
            except Exception as error:
                response["flag"] = True
                response["error"] = error.args[0]
                break
            tmp = equation[fst:]
            try:
                snd = tmp.index("|")
            except Exception as error:
                response["flag"] = True
                response["error"] = error.args[0]
                break
            tmp = tmp[:snd]
            try:
                value = abs(eval(tmp))
            except Exception as error:
                response["flag"] = True
                response["error"] = error.args[0]
                break
            equation = equation.replace("|" + tmp + "|", str(value))
        else:
            break
    try:
        response["answer"] = eval(equation)
    except Exception as error:
        response["flag"] = True
        response["error"] = error.args[0]
    return render(request, 'index.html', context=response)
