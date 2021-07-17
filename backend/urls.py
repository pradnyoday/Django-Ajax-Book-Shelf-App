
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('save/', views.save_data, name='save'),
    path('edit/', views.edit_data, name='edit'),
    path('delete/', views.delete_data, name='delete')
]
