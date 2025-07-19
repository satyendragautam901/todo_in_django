from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages  # ✅ import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def Test_view(request):
    return HttpResponse("This is a TODO application. Homepage coming soon!")

def register_view(request):
    if request.method == 'POST':  
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            
            user = User.objects.create(
                username=email,  # ✅ username is required (mandatory field in default User model)
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.set_password(password)  # ✅ Password hashing
            user.save()
            messages.success(request, "User registered successfully!")  # ✅ success message
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")  # ✅ error message

    return render(request, 'register.html')

# login view

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # First, try to get the user by email
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "No account with this email.")
            return render(request, 'login.html')

        # Authenticate using username (email is not used by default)
        user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('/')
        else:
            messages.error(request, "Invalid password.")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('/')

        