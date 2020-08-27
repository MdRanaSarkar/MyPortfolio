from  django.urls import path
from EasyCSELearnApp.views import Main
urlpatterns=[
path('home/',Main,name='main')
]