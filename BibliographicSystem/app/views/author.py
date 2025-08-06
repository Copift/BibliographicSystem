from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from BibliographicSystem.app.forms.author import AuthorUpdateForm


class AuthorHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'author/author_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        context['author_degree_choices'] = Author.degree
        return context


@login_required
def update_author_profile(request):
    # Получаем автора, связанного с текущим пользователем
    author = request.user

    if request.method == 'POST':
        form = AuthorUpdateForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_home')  # Перенаправляем после успешного сохранения
    else:
        form = AuthorUpdateForm(instance=author)

    context = {
        'form': form,
        'author': author
    }
    return render(request, 'author/author_home.html', context)
from django.shortcuts import get_object_or_404
from BibliographicSystem.app.models.author import Author

def author_profile(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author/public_author.html', {'author': author})

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
import logging
logger = logging.getLogger(__name__) # Gets a logger named after the current module


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

