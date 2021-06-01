from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
   path('dregister/',views.dregisterfunction,name='dregister'),
    path('dlogin/',views.dloginfunction,name='dlogin'),
    path('designerhome/',views.designerhomefunction,name='designerhome'),
    path('deleteimage/<int:sid>',views.deleteimagefunction,name='deleteimage'),
    path('orders/',views.ordersfunction,name='orders'),
    path('logout/',views.logoutfunction,name='logout'),
    path('graph/', views.graphs, name='graph')

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

