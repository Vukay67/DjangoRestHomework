from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('politics', 'Политика'),
    ('economy', 'Экономика'),
    ('technology', 'Технологии'),
    ('sports', 'Спорт'),
    ('world', 'Мир'),
    ('society', 'Общество'),
    ('culture', 'Культура'),
    ('science', 'Наука'),
    ('health', 'Здоровье'),
    ('auto', 'Авто'),
    ('other', 'Другое'),
]

class News(models.Model):
    headline = models.CharField(max_length=15, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    categories = models.CharField(choices=CATEGORY_CHOICES, max_length=25, verbose_name="Kатегории")

    def __str__(self):
        return f"Заголовок - {self.headline} || Категория - {self.categories}"
    
class Vievs(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vievs")
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news")

    

    