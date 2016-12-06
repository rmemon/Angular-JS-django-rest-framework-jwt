import os

from django.contrib import auth
from django.contrib.auth import logout
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from standard_django import settings


def logout_view(request):
    logout(request)
    auth.logout(request)
    return HttpResponseRedirect("/admin/")


@csrf_exempt
def index(request):
    return render(request, "index.html",)


class AngularTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        # print(item)
        print(item)
        template_dir_path = settings.TEMPLATES[0]["DIRS"][0]
        final_path = os.path.join(template_dir_path, item + ".html")
        try:
            html = open(final_path)
            return HttpResponse(html)
        except:
            raise Http404