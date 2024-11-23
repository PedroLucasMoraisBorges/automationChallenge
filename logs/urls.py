from django.urls import path
from .views import *

urlpatterns = [
    path('api/registerErrorLog', RegisterLog.as_view(), name='register_error_log'),
    path('logs', Logs.as_view(), name='logs')
]