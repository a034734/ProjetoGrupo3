from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Game



def index(response):
    return HttpResponse(" <h1> Home </h1>")

def home(response):
    return render(response,'main/homepage.html')

def find(response):
    return render(response,'main/find.html')

def play(response):
    return render(response,'main/play.html')

def about(response):
    return render(response,'main/about.html')

def scoreboard(response):
    return render(response,'main/scoreboard.html')

def user_games(request):
    context = {
        'games': Game.objects.all()
    }
    return render(request,'main/user_games.html', context)

class GameListView(ListView):
    model = Game
    template_name = 'main/user_games.html'
    context_object_name = 'games'
    ordering = ['-data']
    paginate_by = 3

class GameDetailView(DetailView):
    model = Game

class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['title', 'img1', 'img2']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GameUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Game
    fields = ['title', 'img1', 'img2']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        game = self.get_object()
        if self.request.user == game.user:
            return True
        return False

class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    success_url = '/user_games'

    def test_func(self):
        game = self.get_object()
        if self.request.user == game.user:
            return True
        return False

def jogo1(response):
    return render(response,'main/jogo_ofc1.html')

def jogo2(response):
    return render(response,'main/jogo_ofc2.html')

def jogo3(response):
    return render(response,'main/jogo_ofc3.html')



# Create your views here.
