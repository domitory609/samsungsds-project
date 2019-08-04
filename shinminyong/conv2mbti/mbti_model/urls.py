from django.urls import path
from . import views

app_name = 'mbti_model'


urlpatterns=[
             path('',views.test,name='test'),
             path('result',views.result,name='result')
             ]