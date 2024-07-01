from django.db import models

class Schedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Dashboard(models.Model):
    user = models.CharField(max_length=100)  # 이름을 입력하는 텍스트 필드로 변경
    progress = models.IntegerField()
    description = models.TextField()  # 설명 필드 추가
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.progress}%'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)  # 이름을 입력하는 텍스트 필드로 변경
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
