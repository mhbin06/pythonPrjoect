from django import forms
from .models import Schedule, Dashboard, Post

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'description', 'date']

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['user', 'progress', 'description']  # 설명 필드 추가

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']  # 이름을 입력하는 텍스트 필드로 변경
