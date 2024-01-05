# 
# todolist/serializers.py
from rest_framework import serializers
from todolist.models import  User,Task



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age']


class TaskSerializer(serializers.ModelSerializer):
   
     class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed']


