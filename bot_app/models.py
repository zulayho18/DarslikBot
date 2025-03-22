from django.db import models

class BotUser(models.Model):
    chat_id = models.CharField(max_length=100, verbose_name="Chat ID", unique=True)
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name="Username", unique=True)
    full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ism familya")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name if self.full_name else f"User {self.chat_id}"  # Agar ism bo'lmasa, chat ID qaytaradi
