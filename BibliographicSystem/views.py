from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import logging
logger = logging.getLogger(__name__) # Gets a logger named after the current module

def test():
    return [x for x in range(10)]
def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    logger.warning(request.method)
    if request.method == 'POST':
        logger.info(f"Login attempt with method: {request.method}")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            logger.info(f"Attempting to authenticate user: {username}")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                logger.info(f"User {username} logged in successfully")
                next_url = request.POST.get('next', '') or 'author_home'
                return redirect(next_url)

            else:
                logger.warning(f"Failed login attempt for user: {username}")
        else:
            logger.warning(f"Invalid form submission. Errors: {form.errors}")
            # Добавляем ошибки формы в контекст

    return render(request, 'login.html', {'form': form})

def index(request):
    context = {
        'test': ['test1','test2'],
    }
    return render(request, 'index.html', context)