
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from computerService.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('khubancomputer',home),
    path('khuban/proje',project_view),
    path('khuban/about',Abouts),
    path('khuban/service',service),
    path('khuban/emp',Employe),
    path('khuban/succses',sucsess),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #not both
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


