from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserForm(UserCreationForm):
    # CHOICE_GENDER = (
    #     ('man', '남자'),
    #     ('woman', '여자')
    # )
    email = forms.EmailField(label='이메일')
    nickname = forms.CharField(max_length=30, label='이름')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    # gender = forms.CharField(label='성별', widget=forms.Select(choices=CHOICE_GENDER))

    class Meta:  # SignupForm에 대한 기술서
        model = User
        fields = ("email", "nickname", "password1", "password2")  # 작성한 필드만큼 화면에 보여짐

    def __init__(self, *args, **kwargs):
        # SignupForm 을 재정의하여 모든 template class 속성을 'form-control' 로 지정
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# class LoginForm(AuthenticationForm):
class LoginForm(forms.ModelForm):
    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'email',
    #             'required': 'True',
    #         }
    #     )
    # )
    # password = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Password',
    #             'required': 'True',
    #         }
    #     )
    # )
    email = forms.EmailField(label='이메일')
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ("email", "password")
        # fields = ['email', 'password']
        # widgets = {
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }
        # labels = {
        #     'email': '이메일',
        #     'password': '비밀번호',
        # }
    def __init__(self, *args, **kwargs):
        # SignupForm 을 재정의하여 모든 template class 속성을 'form-control' 로 지정
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'