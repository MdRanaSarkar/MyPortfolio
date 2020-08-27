from django.urls import path
from RanaProtfolio.views import Home,Specialized,services_individual,WorkingProtfolio_individual
urlpatterns=[
path('',Home,name='home'),
path('specialization/',Specialized,name='Specialized'),
path('services/<int:id>/',services_individual,name='services_individual'),
path('protfolio/<int:id>/',WorkingProtfolio_individual,name='protfolio_individual')
]