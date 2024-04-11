from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import AddressForm, PenggunaForm, ContentForm
from .models import Pengguna

def set_data_entry(request):
    list_pengguna = Pengguna.objects.all().order_by('-id')
    form = AddressForm()
    context = {'form': form, 'list_pengguna': list_pengguna}
    return render(request, 'data_entry/input_data_1.html', context)

def set_pengguna(request):
    list_pengguna = Pengguna.objects.all().order_by('-id')
    form = PenggunaForm()
    
    if request.method == "POST":
        form = PenggunaForm(request.POST)
        if form.is_valid():
            form.save()
            list_pengguna = Pengguna.objects.all().order_by('-id')
            context = {
                'form': form,
                'list_pengguna': list_pengguna
            }
            return render(request, 'data_entry/input_data_1.html', context)
    
    context = {'form': form, 'list_pengguna': list_pengguna}
    return render(request, 'data_entry/input_data_1.html', context)

def view_pengguna(request, id):
    try:
        pengguna = Pengguna.objects.get(pk=id)
        return render(request, 'data_entry/pengguna_detail.html', {'user_id': pengguna.id})
    except Pengguna.DoesNotExist:
        return JsonResponse({'error': 'user not found'}, status=404)

def get_pengguna_detail_api(request, user_id):
    try:
        pengguna = Pengguna.objects.get(pk=user_id)
        data = {
            'email': pengguna.email,
            'address_1': pengguna.address_1,
            'address_2': pengguna.address_2,
            'city': pengguna.city,
            'state': pengguna.state,
            'zip_code': pengguna.zip_code,
            'tanggal_join': pengguna.tanggal_join.strftime('%Y-%m-%d'),
        }
        return JsonResponse(data)
    except Pengguna.DoesNotExist:
        return JsonResponse({'error': 'user not found'}, status=404)

def set_content(request):
    form = ContentForm()
    
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': form}
            return render(request, 'data_entry/content.html', context)
    
    context = {'form': form}
    return render(request, 'data_entry/content.html', context)
