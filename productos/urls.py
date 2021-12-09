from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

#definimos los paths en los que vamos a poder ingresar
urlpatterns = [
    path('',views.inicio,name='inicio'), #primer parametro como verlo en la url, funcion asociada y alias
    path('nosotros',views.nosotros,name='nosotros'),
    path('productos',views.productos,name='productos'),
    path('productos/crear',views.crear,name='crear'),
    path('productos/editar/<int:id>',views.editar,name='editar'),
    path('productos/eliminar/<int:id>',views.eliminar,name='eliminar'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)