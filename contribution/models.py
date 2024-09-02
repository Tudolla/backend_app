from django.db import models

from django.utils import timezone

class TextPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=False)
    user = models.ForeignKey('user_auth.User', on_delete=models.CASCADE, related_name='text_posts')

    class Meta:
        db_table = 'text_post'

    def __str__(self):
        return self.title


class PollPost(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=False)
    user = models.ForeignKey('user_auth.User', on_delete=models.CASCADE, related_name='poll_posts')

    class Meta:
        db_table = 'poll_post'

    def __str__(self):
        return self.title

class Choice(models.Model):
    poll = models.ForeignKey(PollPost, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'choice'

    def __str__(self):
        return self.choice_text