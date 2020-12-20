from django.urls import path
from . import views
urlpatterns = [

    path('register/',views.registerView,name='register'),
    path('login/',views.loginView,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logoutView,name='logout'),
    path('product/',views.product,name='product'),
    path('v1/',views.view1),
    path('v2/',views.view2),
    path('v3/',views.view3),

]