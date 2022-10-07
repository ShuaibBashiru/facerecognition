from django.shortcuts import render, HttpResponse


def index():
    print("good")


def error_404(request, exception):
    data = {'name': "404"}
    return render(request, "views/Page404.html", data)


def error_500(request, *args, **argv):
    return render(request, "views/Page404.html", status=500)

def error_400(request, *args, **argv):
    return render(request, "views/Page404.html", status=400)

def error_403(request, *args, **argv):
    return render(request, "views/Page404.html", status=403)

    