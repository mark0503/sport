from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .forms import CreationForm
from django.urls import reverse_lazy
from .models import Anketa, UserProfile
from .forms import AnketaForm, CommentForm, UpdateProfile, ApealForm, AnketaFilterForm
from django.contrib.auth.decorators import login_required
from .filters import PersonFilter
from django.core.paginator import Paginator 


def index(request):
    return render(request, 'index.html')

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def list_class(request):
    filter_list = Anketa.objects.all().order_by('-pub_date')
    form = AnketaFilterForm(request.GET)
    
    search_query = request.GET.get('search', '')
    if search_query:
        filter_list = filter_list.filter(title__icontains=search_query)
    else:
        filter_list = Anketa.objects.all().order_by('-pub_date')
    if form.is_valid():
        if form.cleaned_data['min_price']:
            filter_list = filter_list.filter(price__gte=form.cleaned_data['min_price'])

        if form.cleaned_data['max_price']:
            filter_list = filter_list.filter(price__lte=form.cleaned_data['max_price'])

        if form.cleaned_data['min_age']:
            filter_list = filter_list.filter(age__gte=form.cleaned_data['min_age'])

        if form.cleaned_data['max_age']:
            filter_list = filter_list.filter(age__lte=form.cleaned_data['max_age'])

        if form.cleaned_data['types']:
            filter_list = filter_list.filter(types=form.cleaned_data['types'])

        if form.cleaned_data['sity']:
            filter_list = filter_list.filter(sity=form.cleaned_data['sity'])
    paginator = Paginator(filter_list, 4)
    page_number = request.GET.get('page', 1) 
    page = paginator.get_page(page_number)
    return render(request, 'list.html', {'page': page, 'form': form})


@login_required(redirect_field_name='login')
def new_post(request):
    if request.method == 'POST':
        form = AnketaForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('list')
        return render(request, 'new.html', {'form': form})
    form = AnketaForm()
    return render(request, 'new.html', {'form': form})


def post_view(request, pk):
    form = CommentForm(request.POST or None)
    post = get_object_or_404(Anketa, pk=pk)
    comments = post.comments.all()
    return render(request, 'list_detail.html', {'post': post, 'form': form, 'comments': comments})


@login_required
def add_comment(request, username, post_id):
    post = get_object_or_404(Anketa, id=post_id, author__username=username)
    form = CommentForm(request.POST or None)
    context = {'form': form, 'post': post}
    if not form.is_valid():
        return render(request, 'comments.html', context)
    form.instance.author = request.user
    comment = form.save(commit=False)
    comment.anketa = post
    comment.save()
    return redirect('post_view', pk=post_id)


@login_required
def add_apeal(request, username, post_id):
    post = get_object_or_404(Anketa, id=post_id, author__username=username)
    form = ApealForm(request.POST or None)
    context = {'form': form, 'post': post}
    if not form.is_valid():
        return render(request, 'apeal.html', context)
    form.instance.author = request.user
    comment = form.save(commit=False)
    comment.anketa = post
    comment.save()
    return redirect('post_view', pk=post_id)


def profile(request, username):
    author = get_object_or_404(UserProfile, username=username)
    author_posts = author.posts.all()
    context = {'username': author,
               'author_posts': author_posts,
               }
    return render(request, 'profile.html', context)

@login_required
def post_edit(request, username, post_id):
    profile = get_object_or_404(UserProfile, username=username)
    post = get_object_or_404(Anketa, author=profile, pk=post_id)
    if request.user.id is not post.author.id:
        return redirect('post_view', pk=post_id)
    form = AnketaForm(request.POST or None, files=request.FILES or None,
                    instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("post_view",
                            pk=post_id)
    return render(
        request, 'new.html', {'form': form, 'post': post},
    )

def post_delete(request, post_id):
    post = get_object_or_404(Anketa, pk=pk)
    if request.user.id is not post.author.id:
        return redirect('post_view', pk=post_id)
    u = Anketa.objects.get(pk=post_id).delete()
    return redirect('list')


def delete_profile(request, username):
    u = UserProfile.objects.get(username=username)
    if request.user.id is not u.id:
        return redirect('index')
    u = UserProfile.objects.get(username=username).delete()
    return redirect('list')


def update_profile(request, username):
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect('profile', username=username)
        return render(request, 'update_profile.html', {'form': form})
    form = UpdateProfile()
    return render(request, 'update_profile.html', {'form': form})
