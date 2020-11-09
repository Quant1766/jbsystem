from django.urls import path, include
from jbssys import views
urlpatterns = [
    path('master/',views.master_table_view, name="master_table_view"),
    path('', views.index, name="views"),
]