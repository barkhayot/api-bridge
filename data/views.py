from django.shortcuts import render, redirect
from .models import Data
from . recources import DataResource
from django.contrib import messages
from django.http import JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.forms.models import model_to_dict





# Create your views here.

from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        data_resource = DataResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        if not new_data.name.endswith('xlsx'):
            messages.info(request,'wrong format data')
            return redirect('loadData')

        imported_data = dataset.load(new_data.read(), format='xlsx')

        for data in imported_data[1:]:
            #Deliver.objects.all().filter(carnumber=carnumber).delete()
            value = Data(
                product_code = data[0],
                company = data[1],
                weight = data[2],
                product_name = data[3],
                purchase_price = data[4],
                sale_price = data[5],
                profit_rate = data[6],
                progress = data[7],
                event_price = data[8],
                eveent_sale = data[9],
                event_buy = data[10],
                ex_profit_rate = data[11],
                main_category = data[12],
                account = data[13],
                quantity = data[14],
                abc = data[15],
                situation = data[16],
                date_of_change = data[17],
                last_pur_date = data[18],
                last_sale_date = data[19]
            )
            value.save()
            return redirect('upload')
    return render(request, 'upload.html')


def get_api(request):
    data = list(Data.objects.values())
    #json_data = json.dumps(data)
    print(data)
    return JsonResponse(data, safe=False)

@csrf_exempt
def send_api(request):
    data = list(Data.objects.values())
    #print(data)

    r = requests.post('http://localhost:8000/api/recive', json=data)    
    myobj = {'message': 'has been sent'}
    
    
    print(r)
    return redirect('recive')
    #return JsonResponse(myobj, safe=False)

@csrf_exempt
def recieve(request):
    data = []
    if request.method == 'POST':
        data = json.loads(request.body)
        #print(data)
    return JsonResponse(data, safe=False)