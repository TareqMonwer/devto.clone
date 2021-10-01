from django_quill.fields import QuillField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


class Article(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    title = models.CharField(max_length=255)
    content = QuillField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    tags = models.CharField("Add comma seperated tags", max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_at', ]
    
    def tags_list(self):
        return self.tags.split(',')
    
    def get_absolute_url(self):
        return reverse_lazy('articles:detail', args=[self.pk])

