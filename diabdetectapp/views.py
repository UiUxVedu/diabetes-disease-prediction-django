from django.conf import settings
import os
import joblib
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm

# --------------------
# LOAD ML MODEL (SAFE WAY)
# --------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(
    settings.BASE_DIR,
    'diabdetectapp',
    'ml',
    'model.joblib'
)

model = joblib.load(model_path)

# --------------------
# HOME PAGE
# --------------------
def index(request):
    return render(request, 'index.html')

# --------------------
# LOGIN PAGE
# --------------------
def login_view(request):
    form = LoginForm(data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('medical_info')

    return render(request, 'login.html', {'form': form})

# --------------------
# REGISTER PAGE
# --------------------
def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )
        return redirect('login')

    return render(request, 'register.html', {'form': form})

# --------------------
# MEDICAL INFO + PREDICTION
# --------------------
def medical_info(request):
    if request.method == "POST":
        glucose = float(request.POST['glucose'])
        bp = float(request.POST['blood_pressure'])
        skin = float(request.POST['skinfold'])
        insulin = float(request.POST['insulin'])
        bmi = float(request.POST['bmi'])
        dpf = float(request.POST['dpf'])
        age = float(request.POST['age'])

        features = [[
            glucose,
            bp,
            skin,
            insulin,
            bmi,
            dpf,
            age
        ]]

        prediction = model.predict(features)[0]

        result = "Diabetes Detected" if prediction == 1 else "No Diabetes Detected"

        return render(request, 'prediction.html', {'result': result})

    return render(request, 'medical_info.html')
def help_page(request):
    return render(request, 'fillfor_help.html')
