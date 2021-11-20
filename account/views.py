from django.shortcuts import render

from .models import Profile


def user_list(request):
    users = Profile.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'account/user_list.html', context=context)
