from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import UserRegistrationForm, ArticleAddingForm,ArticleUpdateForm
# Create your views here.
from django.contrib.auth.decorators import login_required


def article_list(request):
    article_list = Article.objects.all().order_by('-published')

    return render(request, 'articles.html', {'article_list':article_list})


def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():

            #create new user object, but we dont want to save that
            new_user = user_form.save(commit=False)

            #set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            return render(request, 'account/register_done.html', {'user_form':user_form})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form':user_form})




@login_required()
def article_form(request):
    article_form = ArticleAddingForm(request.POST)

    if request.method == "POST":
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article = article_form.save()
            return redirect('article_list')


    efrom django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import UserRegistrationForm, ArticleAddingForm,ArticleUpdateForm
# Create your views here.
from django.contrib.auth.decorators import login_required


def article_list(request):
    article_list = Article.objects.all().order_by('-published')

    return render(request, 'articles.html', {'article_list':article_list})


def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():

            #create new user object, but we dont want to save that
            new_user = user_form.save(commit=False)

            #set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            return render(request, 'account/register_done.html', {'user_form':user_form})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form':user_form})




@login_required()
def article_form(request):
    article_form = ArticleAddingForm(request.POST)

    if request.method == "POST":
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article = article_form.save()
            return redirect('article_list')


    else:
        article_form = ArticleAddingForm()

    return render(request, 'account/add_article.html', {'article_form':article_form})



@login_required()
def update_article(request,slug):
    article = get_object_or_404(Article, slug=slug)

    form = ArticleUpdateForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('article_list')

    return render(request, 'account/update.html', {'form':form})

@login_required()
def delete_article(request, slug):
    article=  get_object_or_404(Article,slug=slug)
    article.delete()
    return redirect('article_list')
