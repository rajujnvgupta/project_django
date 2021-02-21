from django.contrib.auth.models import AbstractUser,AbstractBaseUser, BaseUserManager
# from annoying.fields import AutoOneToOneField
from django.db import models
from django.utils.html import escape, mark_safe

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class State(models.Model):

    state = models.CharField(max_length=100)
    def __str__(self):
        return self.state

DEFAULT = 'img/user.jpeg'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile_pic')
    college = models.CharField(max_length=255,null=True, blank=True)
    city  =  models.CharField(max_length=255,null=True , blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='states' ,null=True, blank=True)
    mobileNo = models.CharField(max_length=255,null=True, blank=True, unique=True)
    profile = models.ImageField(upload_to='profile_picture', default=DEFAULT, null=True,  blank=True)

    def __str__(self):
        return '%s %s %s' % (self.college ,self.mobileNo ,self.city)
'''
    def set_image_to_default(self):
        self.profile.delete(save=False)
        self.profile = DEFAULT
        self.save()
'''
class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)
        
class Quiz(models.Model):  
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    quizetime = models.DateTimeField(help_text='yyyy-mm-dd hh:mm:ss as 2019-04-10 18:00:00')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name
        #return '%s %s' % (self.name ,self.quizetime)
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject , related_name='interested_students')
    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username

class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')


