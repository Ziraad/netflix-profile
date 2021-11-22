from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from market.models import Customer
from .models import Profile
from .forms import RegistrationForm
from django.contrib.auth.models import User, Group


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        print('username: ', username)
        password = request.POST.get('password')
        print('password: ', password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('login user')
            # Successful login
            login(request, user)
            redirect_url = next_url if next_url else reverse('account:user_list')
            return HttpResponseRedirect(redirect_url)
        else:
            print('user not found')
            # undefined user or wrong password
            context = {
                'username': username,
                'error': 'کاربری با این مشخصات یافت نشد!'
            }
    else:
        context = {
        }
    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:user_list'))


def user_list(request):
    users = Profile.objects.all()
    
    if request.method == 'GET':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            groups = request.POST.get('groups')
            group = Group.objects.get(name=groups)
            username = request.POST.get('email')
            password = request.POST.get('password')
            # try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                            last_name=last_name, is_staff=True)
            print('user created')
            user.groups.add(group)
            user.save()
            print('user save')
            Profile.objects.create(user=user)
            Customer.objects.create(user=user)
            print('success register')
            return render(request, "account/user_list.html", {'users': users, 'form': form})
            # except Exception as e:
            #     print('error in registration', str(e))
        # else:
        #
        #     # Redirect back to the same page if the data
        #     # was invalid
        #     return render(request, "account/user_list.html", {'users': users, 'form': form})

    context = {
        'users': users,
        'form': form,
    }

    return render(request, 'account/user_list.html', context=context)


@login_required
def user_profile(request, pk):
    print('pk: ', pk)
    user = get_object_or_404(Profile, user_id=pk)
    user_presented = Customer.objects.filter(order__presenter=user)
    print(user)

    context = {
        'user': user,
        'user_presented': user_presented,
    }

    return render(request, 'account/profile.html', context=context)



