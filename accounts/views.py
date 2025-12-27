from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import EmailLoginForm
# from .forms import EmailRegisterForm
from .forms import RegisterForm



def loginForm(request):
    return render(request, "accounts/login.html", {})




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            return redirect('login')  # or any page you want
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})





# def login_view(request):
#     if request.method == "POST":
#         form = EmailLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data["email"]
#             password = form.cleaned_data["password"]
#
#             try:
#                 user_obj = User.objects.get(email=email)
#                 user = authenticate(
#                     request,
#                     username=user_obj.username,
#                     password=password
#                 )
#             except User.DoesNotExist:
#                 user = None
#
#             if user is not None:
#                 login(request, user)
#                 return redirect("home")  # change as needed
#             else:
#                 form.add_error(None, "Invalid email or password")
#     else:
#         form = EmailLoginForm()
#
#     return render(request, "login.html", {"form": form})



# def register_view(request):
#     if request.method == "POST":
#         form = EmailRegisterForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data["email"]
#             password = form.cleaned_data["password"]
#
#             if User.objects.filter(email=email).exists():
#                 form.add_error("email", "User already exists")
#             else:
#                 User.objects.create_user(
#                     username=email,   # admin login uses username
#                     email=email,
#                     password=password
#                 )
#                 return redirect("login")
#     else:
#         form = EmailRegisterForm()
#
#     return render(request, "app/register.html", {"form": form})

