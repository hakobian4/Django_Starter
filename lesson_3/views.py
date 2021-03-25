from django.http import HttpResponse, FileResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static

from django.views import View

from django.template import loader

class MyView(View):


    def get(self, request):
        if request.GET.get('type') == "file":
            return FileResponse(open(static('images/001.jpg'), "rb+"))
        elif request.GET.get('type') == "json":
            return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
        elif request.GET.get('type') == "redirect":
            return HttpResponseRedirect("http://127.0.0.1:8000/admin")
        else:
            return HttpResponseNotAllowed("You shall not pass!!!")

    def post(self, request):
        print(request.POST)
        return HttpResponse("This is POST")


def main(request):
    # return HttpResponse("<button>Some button</button>")
    test_template = loader.render_to_string("templates_example.html",
                                            context={"str": "Test string 4545",
                                                     "int": 12,
                                                     "books": [
                                                         {'title': '1984',
                                                          'author': {
                                                              'name': 'George',
                                                              'age': 45}},
                                                         {'title': 'Timequake',
                                                          'author': {
                                                              'name': 'Kurt',
                                                              'age': 75}},
                                                         {'title': 'Alice',
                                                          'author': {
                                                              'name': 'Lewis',
                                                              'age': 33}},
                                                     ]
                                                     })

    return HttpResponse(test_template)


def text(request):
    return HttpResponse("This is text from backend to user interface")


def file(request):
    # with open() as file:
    #     work with file

    print(static('images/001.jpg'))
    return FileResponse(open(static('images/001.jpg'), "rb+"))


def redirect(request):
    return HttpResponseRedirect("http://www.google.com")


def not_allowed(request):
    return HttpResponseNotAllowed("You shall not pass!!!")


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
