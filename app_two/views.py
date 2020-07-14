from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User

# Create your views here.
def index(request):
  return HttpResponse('<h1>Welcome!</h1><p>Go to /users to see the list of user information!</p>')

def help(request):
  help_dict = { 'help_insert': 'HELP PAGE' }
  return render(request, 'app_two/help.html', context=help_dict)

def users(request):
  users_list = User.objects.order_by('first_name')
  users_dic = { 'users_list': users_list}
  return render(request, 'app_two/users.html', context=users_dic)
