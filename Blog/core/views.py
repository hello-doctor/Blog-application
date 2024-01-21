from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile,Post

# Create your views here.
@login_required(login_url ='signin')
def index (request):
  all_posts=Post.objects.all()
  context={
    'all_posts':all_posts
  }
  return render(request, 'index.html',context)


def signup(request):


  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email taken')
        return redirect('signup')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username taken')
      else:
        user =User.objects.create_user(username=username,email=email,password=password)
        user.save()

        #log user and redirect to setings page
        #create a profile obj for the nwe user

        user_model = User.objects.get(username=username)
        new_profile =Profile.objects.create(user=user_model,id_user=user_model.id)
        new_profile.save()
        return redirect('signup')
    else:
      messages.info(request , 'Password not matching')
      return redirect('signup')

  else:
    return render(request,'signup.html')

def signin (request):
  if request.method == 'POST':
    username= request.POST['username']
    password= request.POST['password']

    user=auth.authenticate(username=username,password=password)

    if(user is not None):
      auth.login(request,user)
      return redirect('/')
    else:
      messages.info(request,'Credentials Invalid')
      return redirect('signin')





    pass
  else:
    return render(request,'signin.html')

@login_required(login_url ='signin')
def logout(request):
  auth.logout(request)
  return redirect ('signin')
  


@login_required(login_url ='signin')  
def upload(request):
  if request.method=='POST':
    mycontent=request.POST['content']
    user_id=request.user.id
    new_post=Post.objects.create(user=user_id,title="New user",body=mycontent)
    new_post.save()

  return redirect('index')