from django.contrib import messages
from django.shortcuts import render, redirect

from Application.forms import RegistrationForm
from Application.models import RegistrationModel

# Create your views here.
def home(request):
    return render(request,'main.html')


def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('otp_page')
        else:
            # messages.error(request, 'We Are Unable to send OTP to Your Mobile Number Please, Enter Valid Contact Number..!')
            return render(request, 'register.html', {'form': form})
    else:
        return render(request,'register.html', {'form':form})


def login(request):
    return render(request,'login.html')


def check_user(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    try:
        data = RegistrationModel.objects.get(email=user, password=password)
        if data.status == 'pending':
            messages.error(request,'Your Registration is still Pending..!')
            redirect('login')
        if data.status == 'closed':
            messages.error(request, 'Your Profile is Blocked..!')
            redirect('login')
        request.session['contact'] = data.contact
        request.session['name'] = data.name
        return redirect('profile')
    except RegistrationModel.DoesNotExist:
        messages.error(request,'Invalid User..!')
        redirect('login')


def otp_page(request):
    return render(request,'otp_page.html')


def check_otp(request):
    cno = request.POST.get('cno')
    otp = request.POST.get('otp')

    try:
        data = RegistrationModel.objects.get(contact=cno, otp=otp)
        data.status = 'approved'
        data.save()
        return redirect('profile')

    except RegistrationModel.DoesNotExist:
        messages.error(request, 'Invalid OTP..!')
        return redirect('otp_page')


def profile(request):
    return render(request,'profile.html')


def logout(request):
    del request.session['contact']
    del request.session['name']
    return redirect('home')


def about_us(request):
    return render(request,'about_us.html')