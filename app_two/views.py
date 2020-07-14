from django.shortcuts import render
# from django.http import HttpResponse
# from app_two.models import User
from app_two.forms import NewUserForm

# Create your views here.
def index(request):
  return render(request, 'app_two/index.html')
  # return HttpResponse('<h1>Welcome!</h1><p>Go to /users to see the list of user information!</p>')

def help(request):
  help_dict = { 'help_insert': 'HELP PAGE' }
  return render(request, 'app_two/help.html', context=help_dict)

def users(request):
  form = NewUserForm()

  if request.method == 'POST':
    form = NewUserForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      return index(request)
    else:
      print('Error form invalid!')

  return render(request, 'app_two/users.html', {'form': form})

  # users_list = User.objects.order_by('first_name')
  # users_dic = { 'users_list': users_list}
  # return render(request, 'app_two/users.html', context=users_dic)
