from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [path('', views.churn_rate, name='churn_rate'),]