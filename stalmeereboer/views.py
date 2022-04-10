from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Hengst, Sale, PostImage, About, Merrie, Veulen, Paard, NieuwsImage, Nieuws


def home(request):
    return render(request, 'stalmeereboer/home.html')


def about(request):
    context = {'abouts': About.objects.all()}
    return render(request, 'stalmeereboer/about.html', context)


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
    fields = ['hengst_image', 'title', 'stokmaat', 'kleur', 'content', 'father_name', 'mother_name',
              'fatherfather_name', 'fathermother_name', 'motherfather_name', 'mothermother_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HengstUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Hengst
    fields = ['hengst_image', 'title', 'stokmaat', 'kleur', 'content', 'father_name', 'mother_name',
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


def sale_view(request):
    sales = Sale.objects.all()

    sale_paginator = Paginator(sales, 2)

    page_num = request.GET.get('page')

    page = sale_paginator.get_page(page_num)
    context = {
        'count': sale_paginator.count,
        'page': page

    }
    return render(request, 'stalmeereboer/verkoop.html', context)


def detail_view(request, id):
    sale = get_object_or_404(Sale, id=id)
    photos = PostImage.objects.filter(sale=sale)
    return render(request, 'stalmeereboer/verkoop_detail.html', {
        'sale': sale,
        'photos': photos
    })


class AboutListView(ListView):
    model = About
    template_name = 'stalmeereboer/about.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'abouts'


class AboutDetailView(DetailView):
    model = About


class AboutCreateView(LoginRequiredMixin, CreateView):
    model = About
    fields = ['about_image', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AboutUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = About
    fields = ['title', 'about_image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AboutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = About
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def veulens(request):
    context = {'veulens': Veulen.objects.all()}
    return render(request, 'stalmeereboer/veulens.html', context)


class VeulenListView(ListView):
    model = Veulen
    template_name = 'stalmeereboer/veulens.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'veulens'
    paginate_by = 2


class VeulenDetailView(DetailView):
    model = Veulen


class VeulenCreateView(LoginRequiredMixin, CreateView):
    model = Veulen
    fields = ['veulen_image', 'title', 'kleur', 'content', 'father_name', 'mother_name',
              'fatherfather_name', 'fathermother_name', 'motherfather_name', 'mothermother_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VeulenUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Veulen
    fields = ['veulen_image', 'title', 'kleur', 'content', 'father_name', 'mother_name',
              'fatherfather_name', 'fathermother_name', 'motherfather_name', 'mothermother_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class VeulenDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Veulen
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def merries(request):
    context = {'merries': Merrie.objects.all()}
    return render(request, 'stalmeereboer/merries.html', context)


class MerrieListView(ListView):
    model = Merrie
    template_name = 'stalmeereboer/merries.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'merries'
    paginate_by = 2


class MerrieDetailView(DetailView):
    model = Merrie


class MerrieCreateView(LoginRequiredMixin, CreateView):
    model = Merrie
    fields = ['merrie_image', 'title', 'stokmaat', 'kleur', 'content', 'father_name', 'mother_name',
              'fatherfather_name', 'fathermother_name', 'motherfather_name', 'mothermother_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MerrieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Merrie
    fields = ['merrie_image', 'title', 'stokmaat', 'kleur', 'content', 'father_name', 'mother_name',
              'fatherfather_name', 'fathermother_name', 'motherfather_name', 'mothermother_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class MerrieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Merrie
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def paarden(request):
    context = {'paarden': Paard.objects.all()}
    return render(request, 'stalmeereboer/veulens.html', context)


class PaardListView(ListView):
    model = Paard
    template_name = 'stalmeereboer/paarden.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'paarden'
    paginate_by = 2


class PaardDetailView(DetailView):
    model = Paard


class PaardCreateView(LoginRequiredMixin, CreateView):
    model = Paard
    fields = ['paard_image', 'title', 'kleur', 'geslacht', 'geboortedatum', 'content', 'stokmaat', 'father_name',
              'mother_name', 'fatherfather_name', 'fathermother_name', 'motherfather_name', 'mothermother_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PaardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Paard
    fields = ['paard_image', 'title', 'kleur', 'geslacht', 'geboortedatum', 'content', 'stokmaat', 'father_name',
              'mother_name', 'fatherfather_name', 'fathermother_name', 'motherfather_name', 'mothermother_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PaardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Paard
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def nieuws_view(request):
    nieuwss = Nieuws.objects.all().order_by('-date_posted')

    nieuws_paginator = Paginator(nieuwss, 2)

    page_num = request.GET.get('page')

    page = nieuws_paginator.get_page(page_num)
    context = {
        'count': nieuws_paginator.count,
        'page': page

    }
    return render(request, 'stalmeereboer/nieuws.html', context)


def nieuwsdetail_view(request, id):
    nieuws = get_object_or_404(Nieuws, id=id)
    photos1 = NieuwsImage.objects.filter(nieuws=nieuws)
    return render(request, 'stalmeereboer/nieuws_detail.html', {
        'nieuws': nieuws,
        'photos1': photos1
    })
