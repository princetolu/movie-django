from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
# Create your views here.

class Index(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['posts']= Post.objects.all()
        return context


class Card(TemplateView):
    template_name='profile.html'

class Profile(ListView):
    template_name='profile.html'
    # context_object_name='post_list'

class Detailed(DetailView):
    model = Post
    template_name='details.html'
    