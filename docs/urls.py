from django.urls import path
from .views import *

urlpatterns = [
    path('', DocsView.as_view(), name='docs'),
    path('api/registerDocAccepted', RegisterDocAccepted.as_view(), name='register_doc_accepted'),
    path('api/registerDenied', RegisterDocDenied.as_view(), name='register_doc_denied',)
]