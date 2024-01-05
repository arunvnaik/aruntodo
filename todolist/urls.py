
from django.urls import path
from todolist.views import  TaskListView, TaskDetailView,UserList, UserDetail

urlpatterns = [
    
    path('tasks/', TaskListView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
     path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:user_id>/', UserDetail.as_view(), name='user-detail'),
]
