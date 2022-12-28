from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_show),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('<int:id>', views.edit_data, name='edit'),
]