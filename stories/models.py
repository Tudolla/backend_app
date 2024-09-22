from django.db import models
from django.conf import settings

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
    

class MemberActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    click_timestamp = models.DateTimeField(auto_now_add=True) # auto_now = True thì sẽ khởi tạo nhiều lần
    start_reading = models.DateTimeField(null=True, blank=True)
    end_reading= models.DateTimeField(null=True, blank=True)
    duration=models.DurationField(null=True, blank=True)

    class Meta:
        db_table = 'story_user_tracking'


    def save(self, *args, **kwargs):
        if self.start_reading and self.end_reading:
            self.duration = self.end_reading - self.start_reading
        super(MemberActivity, self).save(*args, **kwargs)

    
    @property
    def formatted_duration(self):
        if self.duration:
            total_seconds = int(self.duration.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f'{hours:02}:{minutes:02}:{seconds:02}'
        return "No duration"

