import os

from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView

from lesson_6.forms import MyForm, FormFromModel
from django.shortcuts import render

# def my_form(request):
#
#     return HttpResponse(MyForm().as_p())

def my_form(request):

    print(request.FILES)
    form = MyForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        print(form.cleaned_data)
        file_path = os.path.join(settings.MEDIA_ROOT,
                                 form.cleaned_data['profile_picture'].name)
        with open(file_path, 'wb+') as local_file:
            for chunk in form.cleaned_data['profile_picture']:
                local_file.write(chunk)
    else:
        print(form.errors)

    return render(request, 'form_page.html', context={'form': form})


class MyFormView(FormView):

    form_class = MyForm
    template_name = "form_page.html"

    def get(self, request, *args, **kwargs):
        print(request.GET)
        return super().get(request, *args, **kwargs)


class ModelFormView(FormView):
    form_class = FormFromModel
    template_name = "model_from_page.html"
    success_url = reverse_lazy("modelform")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)