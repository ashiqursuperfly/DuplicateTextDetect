from django.http import HttpResponse
from django.shortcuts import render
from home import dd


# Create your views here.


def index(request):
    return render(request, 'home/home.html')


def result(request):
    if request.method == 'POST':
        text1 = request.POST.get("text-1")
        text2 = request.POST.get("text-2")

        (res1, res2) = dd.longest_substring_mine(str(text1).strip(), str(text2).strip())
        context = {"result1": round(res1, 2), "result2": round(res2, 2)}
        return render(request, 'home/result.html', context=context)

    return render(request, 'home/home.html')
