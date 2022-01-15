from django.urls import path
from .views import CalcViewSet

urlpatterns = [
    path('senddata', CalcViewSet.as_view({
        'post': 'set_data',
    })),
]
