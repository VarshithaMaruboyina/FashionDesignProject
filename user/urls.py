from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
path('uregister/',views.uregisterfunction,name='uregister'),
    path('ulogin/',views.uloginfunction,name='ulogin'),
    path('userhome/',views.userhomefunction,name='userhome'),
    path('partywear/',views.partywearfunction,name='partywear'),
    path('traditional/',views.traditionalfunction,name='traditional'),
    path('dlogout/',views.dlogoutfunction,name='dlogout'),
    path('designers/',views.designersfunction,name='designers'),
    path('view/<int:iid>',views.viewfunction,name='view'),
    path('cart/',views.cartfunction,name='cart'),
    path('cartdelete/<int:cid>',views.cartdeletefunction,name='cartdelete'),
    path('payment/',views.paymentfunction,name='payment'),
    
    

]
