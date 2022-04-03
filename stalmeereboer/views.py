from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Hengst



def home(request):
    return render(request, 'stalmeereboer/home.html')


def about(request):
    return render(request, 'stalmeereboer/about.html')


def ponies(request):
    return render(request, 'stalmeereboer/ponies.html')


def news(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'stalmeereboer/news.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'stalmeereboer/news.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['header_image', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'header_image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def contact(request):

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_subject = request.POST['message-subject']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # send an email
        send_mail(
            message_name + " " + message_subject + " " + message_email,
            message,
            message_email,
            ['stalmeereboer@gmail.com'],
        )

        return render(request, 'stalmeereboer/contact.html', {'message_name': message_name})

    else:
        return render(request, 'stalmeereboer/contact.html')


def hengsten(request):
    context = {'hengsten': Hengst.objects.all()}
    return render(request, 'stalmeereboer/hengsten.html', context)


class HengstListView(ListView):
    model = Hengst
    template_name = 'stalmeereboer/hengsten.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'hengsten'
    paginate_by = 1


class HengstDetailView(DetailView):
    model = Hengst


class HengstCreateView(LoginRequiredMixin, CreateView):
    model = Hengst
    fields = ['hengst_image', 'title', 'stokmaat', 'content', 'father_name', 'mother_name',
              'fatherfather_name', 'fathermother_name', 'motherfather_name', 'mothermother_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HengstUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Hengst
    fields = ['hengst_image', 'title', 'content', 'father_name', 'mother_name',
              'fatherfather_name', 'fathermother_name', 'motherfather_name', 'mothermother_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class HengstDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Hengst
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



