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
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        try:
            data = RegistrationModel.objects.get(email=user, password=password)
            print(data.status)
            if data.status == 'pending':
                messages.error(request,'Your Registration is still Pending..!')
                redirect('login')
            if data.status == 'closed':
                messages.error(request, 'Your Profile is Blocked..!')
                redirect('login')
            if data.status == 'approved':
                return render(request,'profile.html')
        except RegistrationModel.DoesNotExist:
            messages.error(request,'Invalid Credentials..!')
            redirect('login')

    return render(request,'login.html')


def otp_page(request):
    return render(request,'otp_page.html')


def check_otp(request):
    cno = request.POST.get('cno')
    otp = request.POST.get('otp')

    try:
        data = RegistrationModel.objects.get(contact=cno, otp=otp)
        data.status = 'approved'
        data.save()
        return render(request,'profile.html')
    except RegistrationModel.DoesNotExist:
        messages.error(request, 'Invalid OTP..!')
        return redirect('otp_page')
