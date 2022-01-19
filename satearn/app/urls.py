from django.urls import path, include
from . import views

app_name = 'app'
urlpatterns = [
    # ex: /app/
    path('', views.index, name='index'),
    # ex: /app/browse
    path('browse/', views.browse, name='browse'),
    # ex: /app/3/
    path('<int:bounty_id>/', views.bounty, name='bounty'),
    # ex: /app/create/
    path('create/', views.create, name='create'),
    # ex: /app/2/apply/
    path('<int:bounty_id>/apply/', views.apply, name='apply'),
    # ex: /app/unapply/2
    path('unapply/<int:application_id>', views.unapply, name='unapply'),
    # ex: /app/unapply_jobs/2
    path('unapply_jobs/<int:application_id>', views.unapply_jobs, name='unapply_jobs'),
    # ex: /app/my_bounties/
    path('my_bounties/', views.my_bounties, name='my_bounties'),
    # ex: /app/my_jobs/
    path('my_jobs/', views.my_jobs, name='my_jobs'),
    # ex: /app/select_applicant/32
    path('select_applicant/<int:application_id>', views.select_applicant, name='select_applicant'),
    # ex: app/90/delete
    path('<int:bounty_id>/delete/', views.delete_bounty, name='delete'),
    
    path('', include('django.contrib.auth.urls')),
]