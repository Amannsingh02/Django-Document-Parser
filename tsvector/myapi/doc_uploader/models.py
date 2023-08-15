# models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVectorField
class TextFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    filename = models.CharField(max_length=255, null=True)
    content = models.TextField()
    tsvector_content = SearchVectorField(null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"TextFile {self.id}"
