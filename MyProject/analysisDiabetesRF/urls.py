from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('predict/', views.predict_diabetes, name='predict_diabetes'),
    path('statistics/', views.stats_view, name='statistics'),
] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))