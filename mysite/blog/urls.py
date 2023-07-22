from django.urls import path
from . import views 

urlpatterns = [    
   # path('', views.testing, name='test'),
   path('', views.post_list, name='post_list'),
]


