from django.urls import path
from .views import predict
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('', predict, name='analysis_predict'),
]  + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
