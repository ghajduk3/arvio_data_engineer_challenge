from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .services.extract_download import extract_and_download
from .services.CertificatesDbService import getCertificateById
from . import models

def index(request):
    return render(request,'search_form.html')

def get_certificate(request):
    try:
        data = getCertificateById(request.GET['property_id'])
    except ValueError as e:
        return HttpResponseBadRequest(e)
    return render(request,'display_form.html',{'data':data})

def insert_data_db(request):
    extract_and_download()
    return HttpResponse("Database is recreated")


# Create your views here.
