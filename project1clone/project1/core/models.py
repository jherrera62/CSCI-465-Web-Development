from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks_view_hide_completed = models.BooleanField()

    def change(self):
        print("this needs to change")
        print(self.tasks_view_hide_completed)
        self.tasks_view_hide_completed=not self.tasks_view_hide_completed
        print("HERE")
        print(self.tasks_view_hide_completed)
