import datetime
from django.db import models
from django.utils import timezone

kor_now = timezone.localtime()

'''
model.py: 모델 변경
$python manage.py makemigrations 통해 변경사항에 대한 마이그레이션 생성
$python manage.py migrate 통해 변경사항을 DB에 적용
'''

# 한국시간 필요한 경우:
# from django.utils import timezone
# now = timezone.localtime()

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= kor_now - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
