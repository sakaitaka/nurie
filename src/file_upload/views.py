# coding: UTF-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from file_upload.edgedetected import my_Canny
import sys
from wsgiref.util import FileWrapper
import mimetypes
# ------------------------------------------------------------------
import random
import string
import os
import shutil


def num(request, str):
    context = {
        'num': str,
    }
    return render(request, 'file_upload/upload.html', context)


def randomname(n):
    randlst = [random.choice(string.ascii_letters + string.digits)
               for i in range(n)]
    return ''.join(randlst)


def download(request, fullpath):
    file_name = fullpath.split('/')[-1]
    path_to_file = fullpath
    content_type = mimetypes.guess_type(fullpath)
    with open(fullpath, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="%s"' % file_name
    os.remove(fullpath)
    return response

def file_upload(request):
    #sigma = 100
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #try:
            #    sigma = request.POST['sigma']
            #except:
            #    sigma = 100
            file_obj = request.FILES['file']
            file_obj.name = randomname(30)
            handle_uploaded_file(file_obj)
            output = my_Canny('media/documents/' + file_obj.name, 0.,
             0.05, 0.09, 2, 
             file_obj.name, 1)
            os.remove('media/documents/' + file_obj.name)
            return download(request, output)
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/upload.html', {'form': form})
#
#
# ------------------------------------------------------------------


def handle_uploaded_file(file_obj):
    file_path = 'media/documents/' + file_obj.name
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)
#
# ------------------------------------------------------------------


def success(request):
    str_out = "Success!<p />"
    str_out += "成功<p />"
    return HttpResponse(str_out)
# ------------------------------------------------------------------
