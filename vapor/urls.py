from django.urls import path
from vapor import views

urlpatterns=[
    path('',views.feed,name='feed'),
    path('submit/',views.submit,name='submit'),
    path('report/<int:id>/', views.report, name='report'),
]