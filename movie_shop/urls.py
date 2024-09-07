from django.urls import path
from .views import homepage,product_detail,registration,sing_in,log_out

urlpatterns = [
    path('',homepage,name='home'),
    path('detail/<int:id>',product_detail,name='detail'),
    path('reg/',registration,name='reg'),
    path('login/',sing_in,name='login'),
    path('logout/',log_out,name='logout'),
    ]