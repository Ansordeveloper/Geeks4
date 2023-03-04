from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    create = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("-create",)

