from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from .models import Case
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages
from .forms import EditForm, EditCaseInfoForm




# Create your views here.

def home(request):
    return render(request, 'orphan/home.html',)

def response(request):
    return render(request, 'orphan/response.html',)

def donate(request, pk):
    obj = Case.objects.get(id=pk)
    form = EditCaseInfoForm()
    if request.method == 'POST':
        form = EditCaseInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, ' details updated successfully.')
            return redirect('response')

    context = {'form': form}
    return render(request, 'orphan/donate.html', context)


def orphanage(request):
    if request.method == 'POST':
        name = request.POST['orphanage']
        date = request.POST['date']
        children = request.POST['children']
        phone_no = request.POST['phonenumber']
        email = request.POST['email']
        address = request.POST['address']
        situation = request.POST['situation']
        
        Case_info = Case.objects.create(name=name, date=date, children=children, phone_number=phone_no, email=email, address=address,  situation=situation)
        Case_info.save()

        return redirect('home')
    
    
    return render(request, 'orphan/orphanage.html')

def panel(request):
    mydata = Case.objects.all().values()
    context = {'mymembers': mydata}
    return render(request, 'orphan/panel.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.save()
            

            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'orphan/register.html', {'form': form})

def login_donor(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("panel")
            else:
                messages.error(request, "user does not exist or wrong password")

    form = AuthenticationForm()

    return render(request, 'orphan/login_donor.html', context={"login_form": form})




