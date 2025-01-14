from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Areas, Blog_tag, Blogs, Panorama, Properties, Image, Property_type, Region, SavedProperties, User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm




# none login required views:
def index(request):
    properties = Properties.objects.all()
    types = Property_type.objects.all()
    regions = Region.objects.all()
    region_list_count = list()
    agents = User.objects.all()
    blogs = Blogs.objects.all()

    for region in regions:
        region_properties = Properties.objects.filter(Region__id = region.id).count()
        region_list_count.append(region_properties)

    context = {'properties':properties, 'types':types, 'regions':regions, 'regions_count':region_list_count, 'agents':agents, 'blogs':blogs}
    return render(request, 'base/index.html', context)


def agents(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    agents = User.objects.all()
    context = {'agents' : agents}
    return render(request, 'base/agents.html', context)


def properties(request):
    keyword = request.GET.get('keyword') if request.GET.get('keyword') != None else ''
    type = request.GET.get('type') if request.GET.get('type') != None else ''
    region = request.GET.get('location') if request.GET.get('location') != None else ''
    price_limit = request.GET.get('price') if request.GET.get('price') != None else 0

    if keyword == "" and type == "" and region == "" and price_limit == "":
        properties = Properties.objects.all()
    elif type == "" or price_limit == "":
        properties = Properties.objects.filter(Q(title__contains=keyword) & Q(Region__city__contains=region))
    else:
        properties = Properties.objects.filter(Q(tags__name=type)&Q(title__contains=keyword)&Q(Region__city__contains=region))

    types = Property_type.objects.all()
    context = {'properties' : properties, 'types':types, 'price_limit':int(price_limit)}
    return render(request, 'base/properties.html', context)


def property_detail(request, pk):
    property = Properties.objects.get(id = pk)
    saved_properties = SavedProperties.objects.all()
    properties_id = list()

    for p in saved_properties:
        properties_id.append(p.property.id)

    if request.method == "POST":
        savedproperties=SavedProperties.objects.create(property=property, user=request.user)
        return redirect('properties_detail', pk=pk)


    areas = property.areas_set.all()
    images = property.properties.all()
    panoramas = property.info.all()

    context = {"saved_properties":saved_properties, 'properties_id':properties_id,'property':property, 'images':images, 'areas':areas, 'panoramas':panoramas}
    return render(request, 'base/properties_detail.html', context)

def blogs(request):
    blogs = Blogs.objects.all()
    context = {'blogs':blogs}
    return render(request, 'base/blog.html', context)


def blog_single(request, pk):
    blogs = Blogs.objects.all()
    blog = Blogs.objects.get(id = pk)
    tags = Blog_tag.objects.all()
    context = {'blog':blog, 'tags':tags, 'blogs':blogs}
    return render(request, 'base/blog_single.html', context)


def contactPage(request):
    return render(request, 'base/contact.html')

#--------------------login required views-----------------------------#

def loginPage(request):
    page='login'
     
    if request.user.is_authenticated:
        if request.user.is_superuser:
            pass
            #return redirect("superuser panel")
        else:
            return redirect("userPanel")



    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'this username does not exist')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                pass
                #return redirect('superuser panel')
            else:
                return redirect('userPanel')
        else:
            messages.error(request, 'username or password does not match')

    context = {"page":page}
    return render(request, 'base/auth.html', context)



def signupPage(request):
    
    form = MyUserCreationForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            #return redirect("userpanel")
        else:
            messages.error(request, 'form is not valid. please fill it again.')
    
    context = {'form':form}

    return render(request, 'base/auth.html', context)


def dislike(request, pk):

    user = request.user
    property = Properties.objects.get(id = pk)
    saved_properties = SavedProperties.objects.get(property=property, user = user )

    if request.method == "POST":
        saved_properties.delete()
        return redirect('properties_detail', pk=pk)
