from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from BibliographicSystem.app.forms.author import AuthorUpdateForm


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