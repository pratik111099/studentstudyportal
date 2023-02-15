from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#   Notes Model !!!!!!!!!!!!!!!!!!!!!!
class Notes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    decriptions=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='notes'
        verbose_name_plural ='notes'



#   Homework Model !!!!!!!!!!!!!!!!!!!!!!
class Homework(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    descriptions=models.TextField()
    due=models.DateTimeField()
    is_finish=models.BooleanField(default=False)

    def __str__(self):
        return self.title
        