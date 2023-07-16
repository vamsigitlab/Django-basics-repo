from django.urls import path
from index_page_app import views

# Create your urls here

urlpatterns = [
    path('', views.index_page_view),
]