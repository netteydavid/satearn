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
    # ex: /app/2/apply/
    path('<int:bounty_id>/apply/', views.apply, name='apply'),
    # ex: /app/6/unapply/2
    path('<int:bounty_id>/unapply/<int:application_id>', views.unapply, name='unapply'),
    # ex: /app/my_bounties/
    path('my_bounties/', views.my_bounties, name='my_bounties'),
    # ex: /app/my_jobs/
    path('my_jobs/', views.my_jobs, name='my_jobs'),
    
    path('', include('django.contrib.auth.urls')),
]