from django.urls import path
from . import views 

urlpatterns = [    
   # path('', views.testing, name='test'),
   path('', views.post_list, name='post_list'),
   path('post/<int:pk>/', views.post_detail, name='post_inhoud'),
   path('post/nieuw/', views.post_nieuw, name='post_nieuw'),
]


