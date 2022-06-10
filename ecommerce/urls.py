
from django.contrib import admin
from django.urls import include,path
from django.apps import apps

#for images
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(apps.get_app_config('oscar').urls[0])),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
