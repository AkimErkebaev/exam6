from django.db import models

# Create your models here.
status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Guest(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, default="NoName", verbose_name="Автор")
    email = models.EmailField(max_length=50, null=False, blank=False, default="NoEmail", verbose_name="Мэйл")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=50, choices=status_choices, default=status_choices[0][0],
                              verbose_name="Статус")

    def __str__(self):
        return f"{self.id}. {self.text}: {self.status} {self.author} {self.email}"

    class Meta:
        db_table = "guests"
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
