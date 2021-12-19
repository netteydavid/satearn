from django.urls import path, include
from . import views

app_name = 'app'
urlpatterns = [
    # ex: /app/
    path('', views.index, name='index'),
    # ex: /app/3/
    path('<int:bounty_id>/', views.bounty, name='bounty'),
    # ex: /app/3/invoice
    path('<int:bounty_id>/invoice/', views.invoice, name='invoice'),
    # ex: /app/create/
    path('create/', views.create, name='create'),
    
    path('', include('django.contrib.auth.urls')),
]