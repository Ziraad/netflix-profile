from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group

groups = Group.objects.all()
class ProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['first_name', 'last_name', 'email', 'groups']

    first_name = forms.CharField(label='نام', max_length=50,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'rounded border border-gray-300 w-full text-gray-800 mt-4 '
                                                  'mb-8 px-3 py-2 block',
                                         'placeholder':'نام'}))

    last_name = forms.CharField(label='نام خانوادگی', max_length=50,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'rounded border border-gray-300 w-full text-gray-800 mt-4 '
                                                 'mb-8 px-3 py-2 block',
                                                 'placeholder':'نام خانوادگی'}))
    email = forms.CharField(label='ایمیل', max_length=50,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'rounded border border-gray-300 text-gray-800 w-full mt-4 '
                                             'mb-8 px-3 py-2 block',
                                             'placeholder':'ایمیل'}))
    
    password = forms.CharField(label='ایمیل', max_length=50,
                            widget=forms.PasswordInput(
                                attrs={
                                    'class': 'rounded border border-gray-300 text-gray-800 w-full mt-4 '
                                             'mb-8 px-3 py-2 block',
                                             'placeholder':'پسورد'}))

    re_password = forms.CharField(label='ایمیل', max_length=50,
                            widget=forms.PasswordInput(
                                attrs={
                                    'class': 'rounded border border-gray-300 text-gray-800 w-full mt-4 '
                                             'mb-8 px-3 py-2 block',
                                             'placeholder':'تایید پسورد'}))

    groups = forms.CharField(label='ایمیل', max_length=50,
                            widget=forms.Select(choices=zip(groups,groups),
                                attrs={
                                    'class': 'rounded border border-gray-300 text-gray-800 w-full mt-4 '
                                             'mb-8 px-3 py-2 block',
                                             'placeholder':'تایید پسورد'}))                                           
