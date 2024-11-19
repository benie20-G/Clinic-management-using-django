from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Get the user instance but don't save yet
            user.password = make_password(form.cleaned_data['password'])  # Hash password
            user.save()  # Save the user with the hashed password
            return redirect('login')  # Redirect to login page after signup
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    # Set user session
                    request.session['user_id'] = user.id
                    request.session['email'] = user.email
                    return redirect('index')  # Redirect to homepage
                else:
                    error_message = "Invalid password."
            except User.DoesNotExist:
                error_message = "User does not exist."

            return render(request, 'accounts/login.html', {'form': form, 'error_message': error_message})

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    return redirect('login')