from django.contrib.auth.models import User
from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название места')
    description = models.CharField(max_length=500, verbose_name='Описание места')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
