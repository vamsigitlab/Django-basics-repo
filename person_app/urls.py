from django.urls import path
from person_app import views

# Create your urls here

urlpatterns = [
    path('index/', views.indexView),
    path('detail/<int:person_id>/', views.person_detail_view),
]