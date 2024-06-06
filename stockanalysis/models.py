from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    full_post_time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, default='')
    url = models.URLField(max_length=200)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    arrows = models.IntegerField(default=0)
    content = models.TextField()
    source_page = models.CharField(max_length=200)
    sentiment_feedback = models.TextField(default='')

    def __str__(self):
        return self.title
