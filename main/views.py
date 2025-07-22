from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages  # ✅ import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # used to protect function based view
from main.models import * # import model for create todos
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required(login_url='/login')
def home_view(request):
    user = request.user # this for logged in user credentials
    tasks = Task.objects.filter(user=user).order_by('-id')  # filter data based on logged in user
    return render(request, 'home.html', {'tasks': tasks})

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
            return redirect("/login")
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

@login_required(login_url='/login')  # ✅ Correct usage of login_required
def create_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed') == 'on'  # ✅ Checkbox handling
        user = request.user

        try:
            Task.objects.create(
                title=title,
                description=description,
                is_completed=is_completed,
                user=user
            )
            messages.success(request, "Your todo was created successfully.")
            return redirect('/')
        except Exception as e:
            messages.error(request, "Error while creating your todo. Please try again.")
    
    return render(request, 'create_todo.html')

@login_required(login_url='/login')
def update_todo(request, id):
    todo = get_object_or_404(Task,id = id)
    if(request.method == "POST"):
        if(todo is None):
            messages.error(request,f"No todo with this id {id}")
            return redirect("/")
        
        todo.title  = request.POST.get('title')
        todo.description =  request.POST.get('description')
        todo.is_completed =  request.POST.get('is_completed') == 'on'  # ✅ Checkbox handling
        todo.user = request.user
        
        try:
            todo.save()
            messages.success(request,"Successfully updated blog")
            return redirect("/")

        except:
            messages.error(request,"Error during updating todo")

    return render(request, 'update_todo.html', {"todo": todo})


@login_required(login_url='/login')
def delete_todo(request, id):
    todo = get_object_or_404(Task, id=id)

    if request.method == "POST":
        todo.delete()
        messages.success(request, "Todo deleted successfully.")
        return redirect("/")
    
    messages.error(request, "Invalid request.")
    return redirect("/")
    