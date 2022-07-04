from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('agents/', views.agents, name='agents'),
    path('properties/', views.properties, name='properties'),
    path('properties_detail/<str:pk>', views.property_detail, name='properties_detail'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog_detail/<str:pk>', views.blog_single, name='blog_single'),
    path('contact/', views.contactPage, name='contact'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('dislike/<str:pk>', views.dislike, name='dislike'),
]
