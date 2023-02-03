from django.urls import path
from .import views


app_name = 'school'

urlpatterns = [
    path('', views.index, name='crud'),
    path('save/', views.saveAction, name='save'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.deleteAction, name='delete')
]