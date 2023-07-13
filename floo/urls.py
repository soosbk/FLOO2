from django.contrib import admin
from account import views
from main import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('', views.main, name='main'),  
    path('FLOO/', include('community.urls')),
    path('mbti/', include('mbti.urls')),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
