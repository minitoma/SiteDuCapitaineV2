from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views

urlpatterns = [
            re_path('projets/', views.projet_list, name='projet_list'),
            ]
###urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
