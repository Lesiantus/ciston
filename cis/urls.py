from django.urls import path

from cis import views

app_name = 'cis'

urlpatterns = [
    path('list/', views.CombineListView.as_view(), name='list'),
]