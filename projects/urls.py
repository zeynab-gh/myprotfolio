from django.urls import path,include
from  .import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    
    path('', views.project_list, name= 'project_list' ),
    path('navbar/', views.navbar, name= 'navbar' ),
    path('heder/', views.heder, name= 'heder' ),
    path('about/', views.about, name= 'about' ),
    path('contact/', views.contact, name= 'contact' ),
    path('python/', views.python, name= 'python'),
    path('category/category/django/', views.django, name= 'django'),
    path('product/<int:pk>',views.product, name= 'product' ),
    path('category/<str:cat>',views.category, name= 'category' ),
    path('login/', views.login_user, name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
    
    
]