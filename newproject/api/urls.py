from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view-items'),
    path('item/<int:pk>/', views.get_item, name='retrieve-item'),
    path('update/<int:pk>/', views.update_item, name='update-item'),
    path('item/<int:pk>/delete/', views.delete_item, name='delete-item'),
    path('signup/', views.signup, name='signup'),
]