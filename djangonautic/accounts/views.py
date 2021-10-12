from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(req):
  if req.method == 'POST':
    form = UserCreationForm(req.POST)
    
    if form.is_valid():
      user = form.save()
      login(req, user)
      print('SAVED')
      return redirect('articles:list')
  else:
    form = UserCreationForm()
  return render(req, 'accounts/signup.html', {'form': form})

def login_view(req):
  if req.method == 'POST':
    form = AuthenticationForm(data=req.POST)
    
    if form.is_valid():
      user = form.get_user()
      login(req, user)
      if 'next' in req.POST:
        return redirect(req.POST.get('next'))
      return redirect('articles:list')

  else:
    form = AuthenticationForm()
  return render(req, 'accounts/login.html', {'form': form, 'req': req})

def logout_view(req):
  if req.method == 'POST':
    logout(req)
    return redirect('articles:list')