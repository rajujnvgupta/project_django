from django.shortcuts import redirect, render
from django.views.generic import TemplateView, UpdateView
from classroom.models import Profile , User
from django.urls import reverse, reverse_lazy





class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        else:
            return redirect('students:quiz_list')
    return render(request, 'classroom/home.html')

def mainhome(request):
	return render(request, 'classroom/mainhome.html')


#@method_decorator([login_required, teacher_required], name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = fields  = ('college', 'city', 'state', 'mobileNo', 'profile',)
    context_object_name = 'profile_object'
    template_name = 'registration/update_profile_form.html'

    def get_context_data(self, **kwargs):
        #layout = User.objects.filter(username=user.username)
        #layout.user.username = Profile()
        #layout.user.username.profile = 'profile_picture/user.jpeg'
        #layout.user.save()
        #kwargs['profile_update'] = self.get_object().user.profile_pic.filter(user=user)
        #p = User.objects.get(id=pk)
        #p.create(profile = 'profile_picture/user.jpeg')
        return super().get_context_data(**kwargs)

    #def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing quizzes that belongs
        to the logged in user.
        '''
        #return self.request.user.profile_pic.filter(pk=pk)

    def get_success_url(self):
	    if self.request.user.is_teacher:
	    	return reverse('teachers:quiz_change')
	    else:
	    	return reverse('students:quiz_list')