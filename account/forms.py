from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput
from django.contrib.auth.models import Group

groups = Group.objects.all()


class RegistrationForm(forms.ModelForm):
    re_password = forms.CharField(max_length=128, label='تایید گذرواژه', widget=PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password', 're_password', 'first_name', 'last_name',  'groups']
        widgets = {
            'password': PasswordInput(),
            # 're_password': PasswordInput()
        }

    groups = forms.CharField(label='نوع کاربر', max_length=50,
                             widget=forms.Select(choices=zip(groups, groups),
                                                 attrs={
                                                     'class': 'rounded border border-gray-300 text-gray-800 w-full '
                                                              'mt-4 '
                                                              'mb-8 px-3 py-2 block',
                                                     'placeholder': 'تایید پسورد'}))

    def clean(self):

        # data from the form is fetched using super function
        super(RegistrationForm, self).clean()

        # extract the username and text field from the data
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        # conditions to be met for the username length
        if len(email) < 5:
            self._errors['email'] = self.error_class([
                'آدرس ایمیل درست نیست'])
        if len(password) < 8:
            self._errors['password'] = self.error_class([
                'کلمه عبور خالی است و یا کوتاه است!'])
        if password != re_password:
            self._errors['re_password'] = self.error_class([
                'کلمه عبور و تایید آن استباه است!'])

        # return any errors if found
        return self.cleaned_data
