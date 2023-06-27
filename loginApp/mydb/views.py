from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from mydb.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid email or password'
            return render(request, 'login.html', {'error_message':error_message})
        
    else:
        return render(request, 'login.html')
    
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form':form})

@login_required
def dashboard_view(request):
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('Login')
    return render(request, 'index.html')