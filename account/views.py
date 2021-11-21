from django.shortcuts import render, redirect

from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User, Group


def user_list(request):
    users = Profile.objects.all()
    
    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        # print(form)
        if form.is_valid():
            print('in valid form')
            instance = form.save(commit=False)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            groups = request.POST.get('groups')
            group = Group.objects.get(name=groups)
            print('group:', group)
            # # gender = request.POST.get('gender')
            username = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username,email=email, password=password, first_name=first_name, last_name=last_name)
            user.groups.set(group)
            user.save()
            Profile.objects.create(user=user)
            return redirect('account:user_list')


    context = {
        'users': users,
        'form': form,
    }

    return render(request, 'account/user_list.html', context=context)


def user_profile(request):
    pass