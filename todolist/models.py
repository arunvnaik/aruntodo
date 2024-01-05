from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

    
    

class Task(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title


# Task.objects.filter(created_by=None).update(created_by=some_default_user_id)
#  def get_creator_name(self):
        # return self.created_by.name if self.created_by else None