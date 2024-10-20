
from django.urls import path
from . import views

urlpatterns = [
    path("list-create-tickets/", views.ApiListCreateTickets.as_view(),
         name="list-create-tickets"),
]
