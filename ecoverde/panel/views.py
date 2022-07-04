from django.http import HttpResponse
from django.shortcuts import render
from base.models import Properties, SavedProperties
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def userPanel(request):

    properties = Properties.objects.all()
    saved_properties_queryset = SavedProperties.objects.all()
    saved_properties = 0


    for object in saved_properties_queryset:
        if object.user == request.user:
            saved_properties+=1

    context = {"properties":properties, "saved_properties":saved_properties}
    return render(request, 'panel/user_dash.html', context)


@login_required(login_url='login')
def Compare(request):
    properties = Properties.objects.all()


    compare_property1 = None
    compare_property2 = None  

    if request.method == "POST":
        propertyId1 = request.POST.get('p1')
        propertyId2 = request.POST.get('p2') 

        try:
            compare_property1 = Properties.objects.get(id = propertyId1)
            compare_property2 = Properties.objects.get(id = propertyId2)
        except:
            messages.error(request, "No Property Found")

    context = {"properties":properties, "compare_property1":compare_property1, "compare_property2":compare_property2}
    return render(request, 'panel/user_dash.html', context)


@login_required(login_url='login')
def saves(request):
    all_properties = SavedProperties.objects.all()
    saved_properties = list()
    
    for property in all_properties:
        if property.user == request.user:
            saved_properties.append(property.property)

    context = {"properties":saved_properties}
    return render(request, 'panel/saves.html', context)