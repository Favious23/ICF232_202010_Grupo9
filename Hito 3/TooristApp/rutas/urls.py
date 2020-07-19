from django.conf.urls import url, re_path
from django.urls import path, include
from rutas import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name = "index"),
    url(r'rutas/', views.HomeRutasView.as_view(), name = "rutas"),
    url(r'ruta/create/$', views.RutaCreate.as_view(success_url='/rutas/'), name = "ruta_create"),
    url(r'ruta/(?P<pk>\d+)/update/$', views.RutaUpdate.as_view(success_url='/rutas/'), name = "ruta_update"),
    url(r'ruta/(?P<pk>\d+)/delete/$', views.RutaDelete.as_view(success_url='/rutas/'), name = "ruta_delete"),
    re_path(r'^ruta/(?P<codigo>rta[0-9]{3})/$', views.DetalleRutaView.as_view(), name = "detalle"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
