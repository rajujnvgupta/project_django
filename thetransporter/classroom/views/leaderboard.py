from django.shortcuts import render
from classroom.models import User ,Subject, Quiz, Question, Answer, Student, TakenQuiz, StudentAnswer, Profile, State
from django.db.models import Avg, Count

def board(request):
    t = TakenQuiz.objects.annotate(Count('quiz' , distict=True))
    print(t)
    print("asddfasdf")
    t = TakenQuiz.objects.filter(quiz__name ='quiz2', quiz__subject__name='webTech').order_by('score').reverse()
    print(t)
    quiz_name = 'quiz2'
    return render(request, 'classroom/leader_board/leader_board.html' , { 't':t,
    	'quiz_name':quiz_name
    	 })
