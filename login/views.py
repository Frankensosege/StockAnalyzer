from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .forms import UserForm, LoginForm

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        # print(user)

        if user is not None:
            # redirect the user to the home page
            login(request, user)
            # print(user.nickname)

            redirect_to = reverse('login:welcome', kwargs={'nickname':user.nickname})
            return HttpResponseRedirect(redirect_to)
        else:
            # display an error message
            error = 'Invalid credentials. Please try again.'

        return redirect('login:welcome')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            sign = form.save(commit=False)
            email = form.cleaned_data.get('email')
            nickname = form.cleaned_data.get('nickname')
            raw_password = form.cleaned_data.get('password1')
            sign.save()
            user = authenticate(email=email, password=raw_password)
            # print(username)
            if user is not None:
                # redirect the user to the home page
                login(request, user)

                # redirect_to = reverse('login:welcome', kwargs={'nickname':nickname})
                # return HttpResponseRedirect(redirect_to)
                return render(request, 'welcome.html', {'name': nickname})
            else:
                # display an error message
                error = 'Invalid credentials. Please try again.'

            return redirect('login:welcome')
    else:
        form = UserForm()
    # context = {'form':form}
    # return render(request, 'common/signup.html', context)
    return render(request, 'signup.html', {'form':form})

def welcome(request, nickname):
    # error = None
    return render(request, 'welcome.html', {'name': nickname})

def userLogout(request):
    logout(request)
    return redirect('login:login')

def cancel(request):
    return redirect('login:login')