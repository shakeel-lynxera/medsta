from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from authModule.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate

from authModule.models import ForgetPasswordOTP, UserOTP
from users.models import Profile
from django.contrib.auth import login as auth_login

# Create your views here.

def login(request):
    if request.method == "POST":
        try:
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.data["password"]
                user = authenticate(username=email, password=password)
                if user is None:
                    context = {"form": form, "error": "Invalid email or password"}
                    return render(request, "clients/auth/login.html", context)
                auth_login(request, user)
                return redirect("/")
        except Exception as e:
            print(e)
            context = {"form": form, "server_error": str(e)}
            return render(request, "clients/auth/login.html", context)

    else:
        form = LoginForm()
    return render(request, "clients/auth/login.html", {"form": form})


def registration(request):
    if request.method == "POST":
        try:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                if User.objects.filter(email=form.data["email"], is_active=True).exists():
                    return HttpResponse("Email already exists")

                password = form.data["password"]
                confirm_password = form.data["confirm_password"]
                if not password == confirm_password:
                    context = {"form": form, "error": "password does not match!"}
                    return render(request, "clients/auth/registration.html", context)

                user, cr = User.objects.get_or_create(email=form.data["email"],
                                                username=form.data["email"],
                                                is_active=False)
                user.set_password(password)
                user.save()
                Profile.objects.get_or_create(user=user, defaults= {
                    "full_name": form.data["full_name"],
                    "gender": form.data["gender"]
                })
                UserOTP.objects.update_or_create(user=user)
                return render(request, "clients/auth/registration-otp-verification.html")
            context = {"form": form, "error": form.errors.as_text()}
            return render(request, "clients/auth/registration.html", context)
        except Exception as e:
            print(str(e))
            context = {"form": form, "server_error": str(e)}
            return render(request, "clients/auth/login.html", context)

    else:
        return render(request, "clients/auth/registration.html")


def registration_otp_verification(request):
    if request.method == "GET":
        return render(request, "clients/auth/login.html")

    try:
        otp = request.POST.get("otp", "")
        otp_object = UserOTP.objects.filter(otp=otp).first()
        if otp_object is None:
            context = {"error": "Invalid OTP"}
            return render(request, "clients/auth/registration-otp-verification.html", context)
        else:
            otp_object.user.is_active = True
            otp_object.user.save()
            otp_object.delete()
            context = {"user": otp_object.user}
            auth_login(request, otp_object.user)
            return render(request, "clients/dashboard/dashboard.html", context=context)
    except Exception as e:
        context = {"server_error": str(e)}
        return render(request, "clients/auth/registration-otp-verification.html", context)


def forget_password(request):
    if request.method == "GET":
        return render(request, "clients/auth/forget-password.html")
    email = request.POST.get("email", "")
    if not User.objects.filter(email=email).exists():
        context = {"error": "Email does not exists"}
        return render(request, "clients/auth/forget-password.html", context)
    try:
        user = User.objects.get(email=email)
        ForgetPasswordOTP.objects.update_or_create(user=user)
        return render(request, "clients/auth/forget-password-otp.html")
    except Exception as e:
        print(e)
        context = {"server_error": str(e)}
        return render(request, "clients/auth/forget-password.html", context)


def verify_forget_password_otp(request):
    if request.method == "GET":
        return render(request, "clients/auth/login.html")
    
    otp = request.POST.get("otp", "")
    if ForgetPasswordOTP.objects.filter(otp=otp).exists():
        ForgetPasswordOTP.objects.filter(otp=otp).update(is_verified=True)
        email = ForgetPasswordOTP.objects.filter(otp=otp).first().user.email
        context = {"email": email}
        return render(request, "clients/auth/reset-password.html", context)
    context = {"error": "Invalid OTP"}
    return render(request, "clients/auth/forget-password-otp.html", context)


def reset_password(request):
    if request.method == "GET":
        return render(request, "clients/auth/login.html")
    try:
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not password == confirm_password:
            context = {"error": "Password does not match"}
            return render(request, "clients/auth/reset-password.html", context)

        if not ForgetPasswordOTP.objects.filter(user__email=email, is_verified=True).exists():
            context = {"error": "OTP is not verified."}
            return render(request, "clients/auth/reset-password.html", context)
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return render(request, "clients/auth/login.html")
    except Exception as e:
        print(e)
        context = {"server_error": str(e)}
        return render(request, "clients/auth/reset-password.html", context)
