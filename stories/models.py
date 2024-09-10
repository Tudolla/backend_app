from django.db import models

class Story(models.Model):
    TYPE_CHOICES = [
        ('cuoi', 'Truyện cười'),
        ('ngungon', 'Truyện ngụ ngôn'),
        ('khoahoc', 'Truyện khoa học'),
        ('tamlinh', 'Truyện tâm linh'),

    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.IntegerField(default=0)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'stories'


    def __str__(self):
        return self.title