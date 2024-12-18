from django.urls import path

from api import views

urlpatterns=[
    
    path('signup/',views.UserCreateView.as_view()),
    
    path('todos/',views.TodoListCreateView.as_view()),
    
    path('todos/<int:pk>/',views.TodoRetrieveUpdateDeleteView.as_view()),
    
]