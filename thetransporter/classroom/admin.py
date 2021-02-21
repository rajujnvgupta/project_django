from django.contrib import admin
from .forms import User
from .models import User ,Subject, Quiz, Question, Answer, Student, TakenQuiz, StudentAnswer, Profile, State

class ProfileAdmin(admin.ModelAdmin):
	list_displaly = ('user', 'college', 'city', 'state', 'mobileNo', 'profile')
admin.site.register(Profile, ProfileAdmin)

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)
admin.site.register(State)
